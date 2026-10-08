#!/usr/bin/env python3
"""Audit controls and a declared random-eigenbasis benchmark.

No inference that local Hamiltonian eigenbases are Haar-distributed. The new
Haar and variance formulas use the original full symmetry decomposition.
Run with one BLAS thread. Mathematical asymptotic proofs are not replaced by tests.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from pathlib import Path
import sys
import numpy as np
from scipy.linalg import eigh
ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT/'prior'), str(ROOT/'prior/prior'), str(ROOT/'prior/prior/prior')]
from check_memory import qschur, project_schur, embed1, X, source_hamiltonian, time_average, total_E
from check_bulk import coefficients
from bulk_tools import criterion, kernel_vector, multiplier, shape, threshold
from fast_grid import fast
TOL = 2e-10

def schur_blocks(L:int,q:float,O:np.ndarray):
    groups={}
    for (_,h),B in qschur(L,q).items():
        groups.setdefault(h,[]).append(B)
    out=[]
    for h in sorted(groups):
        basis=groups[h]; d=h+1; m=len(basis)
        B=np.column_stack(basis)
        A=(B.conj().T@O@B).reshape(m,d,m,d).transpose(1,0,3,2)
        S=np.einsum('ambm->ab',A)
        C=A-np.einsum('ab,mn->ambn',S/m,np.eye(m))
        out.append((h,d,m,B,A,S,C))
    return out

def random_basis(m:int,rng,complex_:bool):
    z=rng.normal(size=(m,m))
    if complex_:z=z+1j*rng.normal(size=(m,m))
    U,R=np.linalg.qr(z)
    phase=np.diag(R); phase=phase/np.where(abs(phase)>0,abs(phase),1)
    return U*phase[None,:]

def haar_expected_excess(blocks,dim,real=False):
    value=0.
    for h,d,m,B,A,S,C in blocks:
        norm=float(np.vdot(C,C).real)
        if real:
            assert np.max(abs(C.imag))<TOL
            swap=float(np.einsum('ambn,anbm->',C.real,C.real))
            value+=(norm+swap)/(m+2)
        else:value+=norm/(m+1)
    return value/dim

def exact_vector_design(m,real=False):
    # Exact fourth-moment designs for a single Haar column. Full orthogonal
    # bases are not asserted; linearity gives m times the column mean.
    p_basis=2/(m+2) if real else 1/(m+1)
    phases=(1.,-1.) if real else (1.,-1.,1j,-1j)
    for j in range(m):
        yield np.eye(m,dtype=complex)[:,j], p_basis/m
    for labels in itertools.product(phases,repeat=m):
        yield np.asarray(labels,complex)/math.sqrt(m),(1-p_basis)/len(phases)**m

def counted_paths(n,r,u,q,theta,R):
    paths={(r,u,0):1.}
    for _ in range(n):
        new={}
        for (rr,uu,k),v in paths.items():
            a,b,c,d=coefficients(rr,uu,q)
            for dr,du,dk,w in [(-1,0,0,a),(0,-1,1,b),(0,1,1,c),(1,0,0,d)]:
                if rr+dr>=0 and uu+du>=0 and w:
                    key=(rr+dr,uu+du,k+dk)
                    new[key]=new.get(key,0.)+v*w
        paths=new
    base=lambda rr:(rr+1)*q**(-rr)
    total=sum(v*math.exp(theta*k)*base(rr) for (rr,uu,k),v in paths.items())
    tail=sum(v*math.exp(theta*abs(uu-u))*base(rr) for (rr,uu,k),v in paths.items() if k>R)
    rhs=kernel_vector(n,q,size=n+r+30,upper_tilt=theta)[r]
    tail_rhs=math.exp(-theta*R)*kernel_vector(n,q,size=n+r+30,upper_tilt=2*theta)[r]
    return total,rhs,tail,tail_rhs

def run():
    rng=np.random.default_rng(20261007)
    report={'scope':'review of complete symmetry memory; random symmetry-block eigenbasis benchmark explicitly nonlocal; no new local-Hamiltonian saturation claim'}
    # 1. Exact time-average/excess decomposition for actual small source H.
    local=[]
    for L,q,site in [(4,1.,1),(6,2.6,2),(8,2.6,3)]:
        dim=2**L;O=embed1(X,site,L);P,_=project_schur(O,L,q)
        M=float(np.vdot(P,P).real)/dim
        for lam in [0.,1.]:
            H=source_hamiltonian(L,q,lam)
            ev,U=eigh(H);Q=U.conj().T@O@U;R=U.conj().T@(O-P)@U
            same=abs(ev[:,None]-ev[None,:])<1e-9
            plateau=float(np.sum(abs(Q[same])**2))/dim
            excess=float(np.sum(abs(R[same])**2))/dim
            err=abs(plateau-M-excess)
            assert err<TOL and excess>=0
            assert np.linalg.norm(H@P-P@H)<2e-8
            assert abs(M-fast(L,site+1,q))<TOL
            local.append(dict(L=L,q=q,site=site+1,lam=lam,M=M,plateau=plateau,excess=excess,identity_error=err))
    report['time_average_decomposition']={'passed':True,'cases':local,'degeneracies_included':True}

    # 2. Simple spectra and randomly rotated multiplicity eigenvectors.
    checks=[];tables=[]
    for L in [4,6,8]:
        dim=2**L;O=embed1(X,L//2-1,L);q=2.6
        blocks=schur_blocks(L,q,O)
        M=sum(np.vdot(S,S).real/m for _,d,m,B,A,S,C in blocks)/dim
        exC=haar_expected_excess(blocks,dim)
        exR=haar_expected_excess(blocks,dim,True)
        dimsum=sum(d for _,d,m,*_ in blocks)
        assert dimsum==((L+2)**2//4)
        assert 0<=exC<=dimsum/dim+TOL and 0<=exR<=2*dimsum/dim+TOL
        tables.append(dict(L=L,q=q,M=float(M),complex_ensemble_mean=float(M+exC),real_ensemble_mean=float(M+exR),complex_excess_bound=dimsum/dim,real_excess_bound=2*dimsum/dim))
        for real in [False,True]:
            H=np.zeros((dim,dim),complex);formula=0.;varformula=0.;offset=0
            for h,d,m,B,A,S,C in blocks:
                V=random_basis(m,rng,not real)
                spectrum=np.arange(offset,offset+m,dtype=float);offset+=m+2
                hsmall=(V*spectrum[None,:])@V.conj().T
                H+=B@np.kron(hsmall,np.eye(d))@B.conj().T
                diag=np.einsum('mk,ambn,nk->kab',V.conj(),A,V)
                formula+=float(np.vdot(diag,diag).real)
                residual=diag-S[None,:,:]/m
                varformula+=float(np.vdot(residual,residual).real)
            exact,_=time_average(H,O)
            assert abs(exact-formula/dim)<TOL
            assert abs(formula/dim-M-varformula/dim)<TOL
            assert np.linalg.norm(H@total_E(L,q)-total_E(L,q)@H)<1e-7
            checks.append(dict(L=L,real_eigenbasis=real,plateau=exact,block_variance_excess=varformula/dim,error=abs(exact-formula/dim)))
    # H=0 leaves all memory, illustrating the no-universal-saturation scope.
    assert abs(time_average(np.zeros_like(O),O)[0]-1)<TOL
    report['multiplicity_block_identity']={'passed':True,'direct_spectral_cases':checks,'exact_ensemble_predictions':tables,'zero_H_plateau':1.0}

    # 3. Haar moments: deterministic exact moment designs, no Monte Carlo
    # used to validate the expectation formula.
    moments=[]
    for m in [1,2,3,4]:
        for real in [False,True]:
            for _ in range(3):
                A=rng.normal(size=(m,m))
                if not real:A=A+1j*rng.normal(size=(m,m))
                actual=sum(w*abs(v.conj()@A@v)**2 for v,w in exact_vector_design(m,real))
                if real:
                    target=(np.trace(A)**2+np.sum(A*A)+np.trace(A@A))/(m*(m+2))
                else:target=(abs(np.trace(A))**2+np.vdot(A,A).real)/(m*(m+1))
                assert abs(actual-target)<TOL
                moments.append(dict(m=m,real=real,error=float(abs(actual-target))))
    report['Haar_fourth_moment_designs']={'passed':True,'cases':moments,'sampling_error':False}

    # 4. Both strictly subcritical tilts and all paths with their actual
    # number of vertical steps. This extends, rather than replaces, the old
    # suite's one-tilt displacement controls.
    paths=[]
    for q in [2.1,2.2,2.6,4.]:
        b=criterion(q);theta=-math.log(b)/4
        assert 0<math.exp(2*theta)*b<1
        for n,r,u in [(6,0,0),(8,2,3),(10,4,8)]:
            for R in [0,2,5]:
                a,c,t,v=counted_paths(n,r,u,q,theta,R)
                assert a<=c+TOL and t<=v+TOL
                paths.append(dict(q=q,n=n,r=r,u=u,R=R,count_moment=a,majorant=c,tail=t,tail_bound=v,twice_tilted_criterion=math.exp(2*theta)*b))
    report['two_tilt_uniformity_control']={'passed':True,'cases':paths,'no_asymptotic_fit':True}

    # 5. Analytic uniform excess bound relative to the already-derived bulk
    # asymptotic, with finite M computed using the unchanged exact recurrence.
    scale=[]
    for L in [20,40,80,160]:
        M=fast(L,L//2,2.6);bound=((L+2)**2//4)/2**L
        scale.append(dict(L=L,M=M,complex_excess_bound=bound,real_excess_bound=2*bound,real_relative_bound=2*bound/M))
    assert abs(multiplier(2.6)*shape(.5)-9.55570977050275)<1e-10
    assert abs(criterion(threshold())-1)<1e-12
    report['conditional_scaling']={'passed':True,'values':scale,'does_not_model_finite_range_H':True}
    report['groups_passed']=5
    return report

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'review_report.json')
    args=ap.parse_args();report=run();args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'groups_passed':report['groups_passed'],'output':str(args.output)}))
