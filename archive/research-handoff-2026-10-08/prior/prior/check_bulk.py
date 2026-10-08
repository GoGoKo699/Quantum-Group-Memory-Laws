#!/usr/bin/env python3
"""Finite-q bulk proof controls. Numerical checks are not asymptotic proofs.

Run with one BLAS thread. The physical model and predecessor files are unchanged.
The newly proved sufficient regime is criterion(q)<1, not every q>1.
"""
from __future__ import annotations
from pathlib import Path
import argparse,json,math,sys
import numpy as np
from scipy.special import roots_legendre
from scipy.linalg import eigh_tridiagonal
ROOT=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT),str(ROOT/'prior'),str(ROOT/'prior'/'prior')]
from bulk_tools import (criterion,threshold,amplitudes,multiplier,shape,jacobi,step,
                        kernel_vector,kernel_asym,spectral_arrays,spectral_moment)
from fast_grid import fast
from check_memory import project_schur,embed1,X

TOL=5e-10

def coefficients(r,u,q):
    z=q**-2;h=r+u+1
    f=lambda k: -math.expm1(-2*math.log(q)*k) if k>0 else 0.
    return (.5*math.sqrt(f(r)*f(r+1))/f(h),
            .5*z**(r+.5)*math.sqrt(f(u)*f(u+1))/f(h),
            .5*z**(r+1.5)*math.sqrt(f(u+2)*f(u+1))/f(h+2),
            .5*math.sqrt(f(r+1)*f(r+2))/f(h+2))


def walk_bound(n,r,u,q,theta):
    # Exact finite set of backward paths from one target. No large-state cutoff.
    paths={(r,u):1.}
    for _ in range(n):
        new={}
        for (rr,uu),v in paths.items():
            a,b,c,d=coefficients(rr,uu,q)
            for key,w in [((rr-1,uu),a),((rr,uu-1),b),((rr,uu+1),c),((rr+1,uu),d)]:
                if min(key)>=0 and w:
                    new[key]=new.get(key,0.)+v*w
        paths=new
    lhs=sum(v*math.exp(theta*abs(uu-u))*(rr+1)*q**(-rr) for (rr,uu),v in paths.items())
    rhs=kernel_vector(n,q,size=n+r+100,upper_tilt=theta)[r]
    return lhs,rhs


def independent_shape(x):
    # Independent two-dimensional Gaussian integral, not the 1D reduction.
    t,w=roots_legendre(160);a=(t+1)*5;w=w*5
    A=a[:,None];B=a[None,:]
    f=A*A*B*B/(A+B)*np.exp(-A*A/x-B*B/(1-x)+.5*(A+B)**2)
    return (2/math.pi)**1.5/(x*(1-x))**3*float(w@f@w)


def run():
    report={'scope':'complete quantum-group symmetry projection; fixed q; no claim of saturation for a selected Hamiltonian',
            'proved_bulk_domain':'criterion(q)<1, equivalently q>2.0810189966245356; fixed i/L in (0,1)',
            'groups_passed':0}
    # 1. Independent quadrant update and coefficient majorant.
    err=0.;count=0;deficit=1.
    for q in [1.05,1.5,2.2,2.6,5.]:
        for n,i in [(4,2),(7,3),(10,5)]:
            _,_,old=fast(n,i,q,True);_,_,new=fast(n+1,i,q,True)
            def get(h,r):
                return old[h,r] if 0<=h<old.shape[0] and 0<=r<h else 0.
            for h in range((n+1)%2,n+2,2):
                for r in range(h):
                    u=h-r-1;a,b,c,d=coefficients(r,u,q)
                    v=a*get(h-1,r-1)+b*get(h-1,r)+c*get(h+1,r)+d*get(h+1,r+1)
                    err=max(err,abs(v-new[h,r]));count+=1
                    assert abs(v-new[h,r])<TOL
        for r in range(35):
            for u in range(35):
                a,b,c,d=coefficients(r,u,q)
                diag=.5*(q**-1+q**-3)*q**(-2*r)
                assert min(a,b,c,d)>=0 and max(a,d)<=.5+1e-14
                assert b+c<=diag+1e-14
                assert a+b+c+d<=1+1e-14
                deficit=min(deficit,1-a-b-c-d)
    for q in [2.2,2.6,5.]:
        L=4;O=embed1(X,1,L);proj,_=project_schur(O,L,q)
        assert abs(float(np.vdot(proj,proj).real)/2**L-fast(L,2,q))<TOL
    report['quadrant_identity']={'passed':True,'entries_checked':count,'max_update_error':err,'minimum_sampled_row_deficit':deficit}

    # 2. The explicit sufficient subcriticality condition and path-tilt bounds.
    qc=threshold();assert abs(criterion(qc)-1)<1e-12
    sub=[];walks=[]
    for q in [2.1,2.2,2.6,4.,6.]:
        B=criterion(q);theta=-.5*math.log(B);assert B<1 and math.exp(theta)*B<1
        r=np.arange(96,dtype=float);pot=.5*(q**-1+q**-3)*q**(-2*r)*math.exp(theta)
        G=2*np.minimum(r[:,None]+1,r[None,:]+1)
        h0=r+1;A=G*pot[None,:]
        norm=float(np.max(A@h0/h0));assert norm<=math.exp(theta)*B+1e-13
        h=np.linalg.solve(np.eye(len(r))-A,h0)
        assert np.min(h/h0)>1-1e-12
        assert np.max(h/h0)<1/(1-math.exp(theta)*B)+1e-10
        off,diag=jacobi(q,192,theta)
        largest=float(eigh_tridiagonal(diag,off,select='i',select_range=(191,191),eigvals_only=True)[0])
        assert largest<1
        sub.append({'q':q,'B':B,'tilt':theta,'tilted_B':math.exp(theta)*B,
                    'finite_weighted_green_norm':norm,'finite_matrix_top_eigenvalue':largest})
        for n,rr,uu in [(6,0,0),(8,4,0),(10,3,8),(12,1,5)]:
            lhs,rhs=walk_bound(n,rr,uu,q,theta)
            assert lhs<=rhs+TOL
            walks.append({'q':q,'n':n,'r':rr,'u':uu,'weighted_true_paths':lhs,'Jacobi_majorant':rhs})
    report['uniform_majorant']={'passed':True,'q_threshold':qc,'controls':sub,'path_checks':walks,
        'not_a_physical_transition':True}

    # 3. Spectral measure, transform, and independently evolved moments.
    spectral=[];orth_error=0.
    for q in [1.5,2.2,2.6,5.]:
        xx,ww=roots_legendre(700);theta=(xx+1)*math.pi/2;wt=ww*math.pi/2
        meas,fhat=spectral_arrays(q,theta)
        off,di=jacobi(q,9);prev=np.zeros_like(theta);p=np.ones_like(theta);polys=[p.copy()]
        for j in range(6):
            pn=((np.cos(theta)-di[j])*p-(off[j-1]*prev if j else 0))/off[j]
            prev,p=p,pn;polys.append(p.copy())
        P=np.array(polys);gram=(P*(wt*meas))@P.T
        orth_error=max(orth_error,float(np.max(abs(gram-np.eye(7)))))
        assert np.max(abs(gram-np.eye(7)))<TOL
        for n,r in [(0,0),(0,3),(3,2),(12,5),(64,8)]:
            direct=float(kernel_vector(n,q)[r]);s1=spectral_moment(q,n,r,500);s2=spectral_moment(q,n,r,750)
            assert abs(direct-s1)<TOL and abs(s1-s2)<TOL
            spectral.append({'q':q,'n':n,'r':r,'recurrence':direct,'spectral':s2,'difference':s2-direct})
    report['orthogonal_polynomial_dictionary']={'passed':True,'max_orthogonality_error':orth_error,'moments':spectral}

    # 4. Endpoint amplitudes checked by an independent harmonic recurrence.
    amp=[];front=[]
    for q in [2.2,2.6,4.,10.]:
        z=q**-2;size=220;off,diag=jacobi(q,size);f=q**(-np.arange(size,dtype=float))*np.sqrt(1-z**(np.arange(size)+1))
        targets=amplitudes(q)
        vals=[]
        for sign in [1,-1]:
            dd=sign*diag;hh=np.zeros(size);hh[0]=1;hh[1]=(1-dd[0])/off[0]
            for r in range(1,size-1):hh[r+1]=((1-dd[r])*hh[r]-off[r-1]*hh[r-1])/off[r]
            slope=hh[-1]-hh[-2];hh/=slope
            ff=f if sign==1 else f*(-1.)**np.arange(size)
            val=(1-z)*float(np.dot(hh,ff));vals.append(val)
        assert max(abs(vals[i]-targets[i]) for i in range(2))<2e-8
        amp.append({'q':q,'product_amplitudes':targets,'harmonic_amplitudes':vals,'multiplier':multiplier(q)})
        for n in [128,512,2048]:
            v=kernel_vector(n,q)
            for r in [int(math.sqrt(n)),int(math.sqrt(n))+1]:
                prediction=kernel_asym(n,q,r)
                front.append({'q':q,'n':n,'r':r,'value':float(v[r]),'leading_prediction':prediction,'ratio':float(v[r]/prediction)})
    report['endpoint_constants']={'passed':True,'amplitudes':amp,'front_diagnostics':front,
             'front_tables_do_not_prove_limits':True}

    # 5. Riemann-sum shape and finite-q full-recursion diagnostics.
    shapes=[]
    for x in [.125,.25,.5,.75]:
        s=shape(x);ind=independent_shape(x)
        assert abs(s-ind)<1e-7
        assert abs(s-shape(1-x))<TOL
        shapes.append({'x':x,'one_dimensional_shape':s,'two_dimensional_shape':ind})
    data=[]
    for L,i,q in [(80,40,2.6),(160,80,2.6),(320,160,2.6),(640,320,2.6),(1280,640,2.6),
                  (320,80,2.6),(640,160,2.6),(320,160,2.2),(320,160,5.)]:
        v,m,t=fast(L,i,q,True);p=i-1;n=L-i
        coeff=multiplier(q)*shape(i/L)
        pts=[];kvec=kernel_vector(n,q)
        for parity in [0,1]:
            r=int(math.sqrt(n));r+=(parity-r)%2
            u=int(math.sqrt(p));u+=(L-(r+u+1))%2;h=r+u+1
            dp=2*math.sqrt(2/math.pi)*(u+1)*p**-1.5*math.exp(-(u+1)**2/(2*p))
            pred=.5*(1-q**-2)*dp*kvec[r]
            pts.append({'h':h,'r':r,'true_t':float(t[h,r]),'frozen_large_spin_t':float(pred),'ratio':float(t[h,r]/pred)})
        assert 0<v<1 and coeff>0
        data.append({'L':L,'i':i,'q':q,'M':v,'L2M':L*L*v,'limit_coefficient':coeff,'ratio':L*L*v/coeff,'pointwise_diagnostics':pts})
    report['bulk_scaling_checks']={'passed':True,'shape_integrals':shapes,'values':data,
           'no_fit_used_for_exponent_or_prefactor':True,'no_claim_of_validated_numerical_intervals':True}

    # 6. Independent consistency with the fixed-distance boundary spectrum.
    boundary=[]
    for q in [2.2,2.6,5.]:
        const=multiplier(q)/(math.sqrt(2)*math.pi)
        for d in [100,400,1600]:
            v=kernel_vector(d,q)
            B=(1-q**-2)**2/math.sqrt(2*math.pi)*float(np.dot(v,v))
            boundary.append({'q':q,'d':d,'B_d':B,'d32B_d':d**1.5*B,'predicted_limit':const})
    for q in [20.,100.,1000.]:
        assert abs(multiplier(q)-1)<14/q**2
    report['boundary_and_crystal_consistency']={'passed':True,'boundary_distance_values':boundary,
       'boundary_limit_is_iterated_not_uniform_in_distance_over_L':True,
       'q_to_infinity_consistency_not_exchange_of_limits':True}
    report['groups_passed']=6
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'report.json')
    a=p.parse_args();r=run();a.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'groups_passed':r['groups_passed'],'output':str(a.output)}))
