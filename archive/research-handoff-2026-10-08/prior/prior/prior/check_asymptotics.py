#!/usr/bin/env python3
"""Boundary asymptotics and a bulk lower bound for quantum-group symmetry memory.

No dynamical exponent or exact finite-q bulk asymptotic is asserted. The original
full finite-chain recursion is preserved in prior/check_memory.py. This program
checks independent finite formulas and diagnostic sequences; the asymptotic
statements require the analytical arguments in FOLLOWUP.md.
"""
from pathlib import Path
from fractions import Fraction
import argparse,json,math,sys
import numpy as np
from scipy.special import gammaln
from scipy.integrate import quad
sys.path.insert(0,str(Path(__file__).parent/'prior'))
from check_memory import complete_bound_fast,project_schur,embed1,X
from fast_grid import fast


def mult(n,h):
    if n<0 or h<0 or h>n or (n-h)%2:return 0
    k=(n-h)//2
    return math.comb(n,k)-(math.comb(n,k-1) if k>0 else 0)

def logmult(n,h):
    h=np.asarray(h);k=(n-h)/2
    return np.log(h+1)-math.log(n+1)+gammaln(n+2)-gammaln(k+1)-gammaln(n+2-k)

def edge_exact(L,q):
    if L<1 or q<=1 or not math.isfinite(q):raise ValueError
    h=np.arange(1 if L%2 else 2,L+1,2,dtype=float)
    if not len(h):return 0.
    Q=q**-2
    probs=np.exp(logmult(L,h)-L*math.log(2))
    dh=-np.expm1(-2*math.log(q)*h)
    dh2=-np.expm1(-2*math.log(q)*(h+2))
    pm=h*(L+h+2)/(2*L*(h+1))
    pp=(h+2)*(L-h)/(2*L*(h+1))
    B=pm/dh-Q*pp/dh2
    S=dh*(1+Q**(h+2))/(1-Q*Q)-h*Q**h
    return float(2*np.dot(probs,B*B*S))

def edge_coefficient(q):
    return math.tanh(math.log(q))/math.sqrt(2*math.pi)

def jacobi(q,K=180,diagonal=True):
    Q=q**-2;r=np.arange(K,dtype=float)
    off=.5*np.sqrt((1-Q**(r[1:]))*(1-Q**(r[1:]+1)))
    diag=.5*(1/q+1/q**3)*Q**r if diagonal else np.zeros(K)
    return off,diag

def apply_j(v,off,diag):
    return diag*v+np.r_[off*v[1:],0]+np.r_[0,off*v[:-1]]

def edge_profile_coefficient(q,d,K=180):
    Q=q**-2;r=np.arange(K,dtype=float)
    v=q**(-r)*np.sqrt(1-Q**(r+1))
    off,diag=jacobi(q,K)
    for _ in range(d):v=apply_j(v,off,diag)
    return float((1-Q)**2/math.sqrt(2*math.pi)*np.dot(v,v))

def crystal_exact_small(L,i):
    p=i-1;n=L-i
    v=Fraction(0)
    for a in range(p%2,p+1,2):
        for b in range(n%2,n+1,2):
            v+=Fraction(mult(p,a)**2*mult(n,b)**2,mult(L,a+b+1))
    return v/Fraction(2**(L-1))

def crystal(L,i):
    p=i-1;n=L-i
    a=np.arange(p%2,p+1,2)[:,None];b=np.arange(n%2,n+1,2)[None,:]
    return float(np.exp((1-L)*math.log(2)+2*logmult(p,a)+2*logmult(n,b)-logmult(L,a+b+1)).sum())

def crystal_bulk_function(x):
    z=x*(1-x)
    value=quad(lambda u:u*u*(1-u)**2/(.5+(u-x)**2/z)**2.5,0,1,epsabs=1e-12,epsrel=1e-12)[0]
    return 3*math.sqrt(2)/(4*math.pi*z**3)*value

def killed(n,x,y):
    if abs(y-x)>n or (n+y-x)%2:return 0.
    k=(n+y-x)//2;kr=(n+y+x+2)//2
    a=math.comb(n,k) if 0<=k<=n else 0
    b=math.comb(n,kr) if 0<=kr<=n else 0
    return (a-b)/2**n


def run():
    report={'scope':'full symmetry projection; infinite-temperature Pauli X; open spin-1/2 chain',
            'bulk_statement':'M(L,i,q) >= c(q,epsilon)/L**2 proved for fixed q>sqrt(3), epsilon L<=i<=(1-epsilon)L; no matching finite-q upper bound',
            'boundary_statement':'M(L,1,q)=tanh(log(q))/sqrt(2*pi*L)+O_q(1/L), fixed finite q>1'}
    tol=2e-10
    err_edge=0.;err_grid=0.;cases=0
    for q in [1.05,1.5,2.6,5.0]:
        for L in [2,3,6,10,20]:
            edge=edge_exact(L,q)
            reference=complete_bound_fast(L,L,q)
            err_edge=max(err_edge,abs(edge-reference))
            assert abs(edge-reference)<tol
            for i in sorted(set([1,L//2,L])):
                val=fast(L,i,q);ref=complete_bound_fast(L,i,q)
                err_grid=max(err_grid,abs(val-ref));assert abs(val-ref)<tol
                assert abs(val-fast(L,L+1-i,q))<tol
                cases+=1
    for q in [1.5,2.6]:
        L=4;O=embed1(X,L-1,L);P,_=project_schur(O,L,q)
        assert abs(np.vdot(P,P).real/2**L-edge_exact(L,q))<tol
    report['finite_formula_checks']={'passed':True,'grid_cases':cases,'max_edge_error':err_edge,'max_grid_error':err_grid}

    # Analytical edge formula evaluated independently at large L.
    rows=[]
    for q in [1.5,2.6,5.]:
        c=edge_coefficient(q);previous=math.inf
        for L in [100,400,1600,6400,25600]:
            v=edge_exact(L,q);err=abs(v*math.sqrt(L)-c)
            assert err<previous;previous=err
            rows.append({'q':q,'L':L,'M_edge':v,'sqrtL_times_M':math.sqrt(L)*v,'limit_coefficient':c})
        assert previous<.003
    profile=[]
    for d in range(5):
        q=2.6;c=edge_profile_coefficient(q,d,100);c2=edge_profile_coefficient(q,d,200)
        assert abs(c-c2)<tol
        if d==0:assert abs(c-edge_coefficient(q))<tol
        v=fast(640,640-d,q)
        assert abs(math.sqrt(640)*v-c)<.006
        profile.append({'distance_from_end':d,'asymptotic_coefficient':c,'sqrt640_times_finite_value':math.sqrt(640)*v})
    report['boundary_limits']={'passed':True,'edge_values':rows,'fixed_distance_profile':profile,'not_uniform_in_q_to_1':True}

    # Auxiliary q->infinity limit. This is NOT the commutant of the singular limit Hamiltonian.
    crerr=0
    for L in range(2,11):
        for i in sorted(set([1,L//2,L])):
            exact=float(crystal_exact_small(L,i));ref=complete_bound_fast(L,i,math.inf)
            crerr=max(crerr,abs(exact-ref));assert abs(exact-ref)<tol
            assert abs(exact-crystal(L,i))<tol
    crrows=[]
    for x in [.25,.5]:
        F=crystal_bulk_function(x)
        for L in [80,320,1280]:
            v=crystal(L,round(x*L));crrows.append({'L':L,'x':x,'L2M':L*L*v,'analytical_limit':F})
        assert abs(crrows[-1]['L2M']/F-1)<.002
    report['auxiliary_crystal_limit']={'passed':True,'max_exact_error':crerr,'bulk_values':crrows}

    # Pointwise lower bound: drop nonnegative stay-r terms and use weighted ballot paths.
    patherr=0.;ratios=[]
    for L,i,q in [(16,8,2.),(24,6,2.6),(24,12,2.6),(32,16,5.)]:
        v,deg,T=fast(L,i,q,True);p=i-1;n=L-i;Q=q**-2
        K=n+2;off,di=jacobi(q,K,False)
        w=np.zeros(K);w[0]=1.
        for _ in range(n):w=apply_j(w,off,di)
        c0=(1-3*Q)*math.sqrt(1-Q);assert c0>0
        for a in range(p%2,p+1,2):
            for r in range(n%2,n+1,2):
                h=a+1+r
                lower=c0*(mult(p,a)/2**i)*w[r]
                assert T[h,r]+tol>=lower
                patherr=max(patherr,max(0,lower-T[h,r]))
        # Check the exact bridge occupation/Jensen inequality, not a Monte Carlo probability.
        r=max(1,int(math.sqrt(n)));r+=(n-r)%2
        kn=killed(n,0,r);assert kn>0
        occ=np.zeros(n+1)
        for h in range(n+1):
            occ[h]=sum(killed(j,0,h)*killed(n-j,h,r) for j in range(1,n))/kn
        logj=.5*math.log(1-Q)+.5*math.log(1-Q**(r+1))+sum(occ[h]*math.log1p(-Q**(h+1)) for h in range(n+1))
        assert w[r]/kn+tol>=math.exp(logj)
        ratios.append({'L':L,'i':i,'q':q,'ballot_endpoint':r,'weighted_to_unweighted':float(w[r]/kn),'Jensen_lower':math.exp(logj)})
    report['bulk_lower_bound_controls']={'passed':True,'max_violation':patherr,'weighted_path_tests':ratios,
        'warning':'Numerics check finite identities. Uniform asymptotic lower bound follows from the proved heat-kernel/Green-function argument, not these four tests.'}

    # Finite-q data are deliberately not used to assert a matching bulk exponent.
    bulk=[]
    for L in [80,160,320,640,1280]:
        v=fast(L,L//2,2.6);edge=edge_exact(L,2.6)
        bulk.append({'L':L,'q':2.6,'i':L//2,'M_bulk':v,'L2M_bulk':L*L*v,'M_edge':edge})
        assert 0<v<edge<1
    for L in [8,20,40]:
        for i in [1,L//2,L]:assert abs(complete_bound_fast(L,i,1.)-1/L)<tol
    report['finite_q_diagnostics']={'passed':True,'values':bulk,'no_finite_q_bulk_equality_claim':True}
    report['groups_passed']=5
    return report

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=Path('report.json'));args=ap.parse_args()
    result=run();args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'groups_passed':result['groups_passed'],'output':str(args.output)}))
