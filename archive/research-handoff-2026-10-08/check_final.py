#!/usr/bin/env python3
"""Finite operational controls for the existing quantum-group memory theorem.

These checks do not prove the previously derived large-L asymptotic. They test
corollaries about its local dynamical realization and the interpretation of the
conserved operator algebra. No network requests or repository operations.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
import sys
from pathlib import Path
import numpy as np
from scipy.linalg import eigh, expm, svdvals

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'prior/prior/prior/prior'))
from check_memory import (qschur, project_schur, embed1, embed2, local_R,
                          source_hamiltonian, complete_bound_fast, X,Y,Z)
TOL=3e-10

def schur_projector(L: int,q: float) -> np.ndarray:
    """Build the orthogonal superoperator via orthonormal irrep matrix units."""
    groups={}
    for (_,h),B in qschur(L,q).items():groups.setdefault(h,[]).append(B)
    columns=[]
    for h,bases in sorted(groups.items()):
        for a in range(h+1):
            for b in range(h+1):
                E=sum(np.outer(B[:,a],B[:,b].conj()) for B in bases)/math.sqrt(len(bases))
                columns.append(E.reshape(-1,order='F'))
    Q=np.column_stack(columns)
    assert np.linalg.norm(Q.conj().T@Q-np.eye(Q.shape[1]))<TOL
    return Q@Q.conj().T

def noise(L: int,q: float,rates) -> np.ndarray:
    D=2**L;I=np.eye(D);S=np.zeros((D*D,D*D),complex)
    for j,g in enumerate(rates):
        if g<0:raise ValueError('rates must be nonnegative')
        R=embed2(local_R(q),j,L)
        Pj=(q*I-R)/(q+1/q)
        Uj=I-2*Pj
        assert np.linalg.norm(Uj.conj().T@Uj-I)<TOL
        S+=g*(np.kron(Uj.conj(),Uj)-np.eye(D*D))
    return S

def coherent(H: np.ndarray) -> np.ndarray:
    D=H.shape[0]
    return 1j*(np.kron(np.eye(D),H)-np.kron(H.T,np.eye(D)))

def norm2(v,D):return float(np.vdot(v,v).real/D)

def run() -> dict:
    report={'scope':'Local noisy attainment and operator-algebra interpretation; no new bulk exponent, local-Hamiltonian saturation or mixing-time scaling claim.'}
    cases=[]
    for L,q in [(3,1.0),(3,1.4),(4,2.6)]:
        D=2**L;P=schur_projector(L,q)
        rates=np.linspace(.7,1.3,L-1)
        S=noise(L,q,rates)
        ev,V=eigh(S)
        zero=V[:,abs(ev)<1e-10]
        delta=-float(ev[ev < -1e-10].max())
        assert np.linalg.norm(zero@zero.conj().T-P)<TOL
        assert zero.shape[1]==math.comb(L+3,3)
        Q=V[:,ev < -1e-10]
        for lam in [0.,1.]:
            H=source_hamiltonian(L,q,lam,stagger=True)
            K=coherent(H)
            assert np.linalg.norm(K@P)<TOL and np.linalg.norm(P@K)<TOL
            assert np.linalg.norm(K+K.conj().T)<TOL
            for eps in [.03,.5]:
                G=K+eps*S
                QG=Q.conj().T@G@Q
                # This has no stationary vectors outside the full symmetry algebra.
                singular=svdvals(QG)
                assert singular[-1] >= eps*delta-5*TOL
                for site in sorted(set([0,L//2,L-1])):
                    O=embed1(X,site,L).reshape(-1,order='F')
                    p=P@O; residual=O-p;M=norm2(p,D)
                    assert abs(M-complete_bound_fast(L,site+1,q))<TOL
                    times=[0.,.12,.85,4.]
                    largest=0.
                    for t in times:
                        E=expm(t*G);evolved=E@O
                        actual=norm2(evolved-p,D)
                        bound=(1-M)*math.exp(-2*eps*delta*t)
                        C=float(np.vdot(O,evolved).real/D)
                        cbound=(1-M)*math.exp(-eps*delta*t)
                        assert actual<=bound+TOL
                        assert abs(C-M)<=cbound+TOL
                        assert np.linalg.norm(P@evolved-p)<TOL
                        largest=max(largest,actual-bound)
                    cases.append(dict(L=L,q=q,site=site+1,lam=lam,epsilon=eps,
                                      M=M,delta=delta,smallest_residual_singular_value=float(singular[-1]),
                                      maximum_bound_excess=largest))
        # Large-time limit of noise + interacting H, evaluated on operator space.
        G=coherent(source_hamiltonian(L,q,1.,True))+.5*S
        t=32/(.5*delta)
        err=float(np.linalg.norm(expm(t*G)-P))
        assert err<2e-9
    report['local_coherent_noisy_attainment']={'passed':True,'cases':cases,'max_hilbert_dimension':16,'max_superoperator_dimension':256}

    # An actual piecewise Hamiltonian drive preserving the same algebra.
    L=4;q=2.6;D=16;P=schur_projector(L,q);S=noise(L,q,[.7,1.0,1.3]);delta=-max(x for x in eigh(S,eigvals_only=True) if x < -1e-10)
    eps=.3;O=embed1(X,1,L).reshape(-1,order='F');p=P@O;M=norm2(p,D);cur=O.copy();elapsed=0.;driven=[]
    for duration,lam,scale in [(.3,0.,1.),(.2,1.,.7),(.55,-.4,1.2),(.4,.8,.9)]:
        H=scale*source_hamiltonian(L,q,lam,True)
        cur=expm(duration*(coherent(H)+eps*S))@cur;elapsed+=duration
        residual=norm2(cur-p,D);bound=(1-M)*math.exp(-2*eps*delta*elapsed)
        assert residual<=bound+TOL
        assert np.linalg.norm(P@cur-p)<TOL
        driven.append(dict(elapsed=elapsed,residual_norm_squared=residual,bound=float(bound)))
    report['piecewise_control_no_new_conservation_assumption']={'passed':True,'records':driven}

    # The same dimension of the conserved algebra is not nesting.
    identity=[]
    for L in [2,3,4]:
        D=2**L;P1=schur_projector(L,1.);Pq=schur_projector(L,2.6)
        rank=math.comb(L+3,3)
        assert abs(np.trace(P1).real-rank)<TOL
        assert abs(np.trace(Pq).real-rank)<TOL
        n1=float(np.linalg.norm((np.eye(D*D)-Pq)@P1));nq=float(np.linalg.norm((np.eye(D*D)-P1)@Pq))
        assert n1>.1 and nq>.1
        totals={}
        for q,PP in [(1.,P1),(2.6,Pq)]:
            total=0.
            for labels in itertools.product(range(4),repeat=L):
                A=np.array([[1.]],complex)
                for label in labels:A=np.kron(A,[np.eye(2),X,Y,Z][label])
                v=PP@A.reshape(-1,order='F');total+=norm2(v,D)
            assert abs(total-rank)<TOL
            totals[str(q)]=total
        identity.append(dict(L=L,rank=rank,unnested_1_to_q=n1,unnested_q_to_1=nq,Pauli_sum=totals))
    report['equal_dimension_not_nested_symmetry']={'passed':True,'records':identity}

    # Broken hypotheses cannot be hidden: remove one bond with H=0.
    L=4;q=2.6;D=16;P=schur_projector(L,q)
    cut=noise(L,q,[1.,0.,1.]);ev,V=eigh(cut);Z0=V[:,abs(ev)<1e-10]
    assert Z0.shape[1]==100>math.comb(7,3)
    O=embed1(X,0,L).reshape(-1,order='F');cut_M=norm2(Z0@(Z0.conj().T@O),D);full_M=norm2(P@O,D)
    assert cut_M>full_M
    # Retaining only U(1), with H=omega*sum Z/2, rotates the conserved X sector.
    omega=.7;H=.5*omega*sum(embed1(Z,j,L) for j in range(L));S=noise(L,q,[1.,1.,1.]);G=coherent(H)+.2*S
    assert np.linalg.norm(coherent(H)@P)>.1
    p=P@O;M=norm2(p,D);osc=[]
    for t in [0.,math.pi/(2*omega),math.pi/omega,2*math.pi/omega]:
        value=float(np.vdot(p,expm(t*G)@p).real/D)
        expected=M*math.cos(omega*t)
        assert abs(value-expected)<TOL
        osc.append(dict(t=t,stationary_sector_correlation=value,cosine_prediction=expected))
    report['scope_controls']={'passed':True,'cut_stationary_dimension':Z0.shape[1],
                              'cut_M':cut_M,'connected_M':full_M,'U1_only_oscillation':osc}
    report['groups_passed']=4
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    report=run()
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'groups_passed':report['groups_passed'],'output':str(args.output)}))
