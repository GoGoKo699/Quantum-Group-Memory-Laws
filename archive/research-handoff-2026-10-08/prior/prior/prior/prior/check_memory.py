#!/usr/bin/env python3
"""Complete U_q(sl_2) symmetry contribution to a local spin-memory plateau.

All spin labels in the recurrence are doubled integers. For fixed finite q>=1,
the recurrence evaluates the full symmetry-algebra Hilbert--Schmidt projection,
not the dynamics of a 2**L-dimensional state. Generic Hamiltonian long-time
correlations are bounded below by this quantity, not asserted equal to it.

Run: python check_memory.py --output report.json
Dependencies: numpy, scipy. No network access and no prior-project imports.
"""
from pathlib import Path
import argparse
import json
import math
import numpy as np
from scipy.linalg import eigh

# Vectorized q-Clebsch-Gordan transition tables.


def cg_array(parentJ, childJ, M2s, spin2, q):
    M2s=np.asarray(M2s,dtype=int)
    prevM=M2s-spin2
    mask=(np.abs(M2s)<=childJ)&((M2s-childJ)%2==0)&(np.abs(prevM)<=parentJ)&((prevM-parentJ)%2==0)
    n=(parentJ+M2s+1)//2
    D=parentJ+1
    valid=mask&(n>=0)&(n<=D)
    nn=np.clip(n,0,D).astype(float)
    if q==1:
        ap=np.sqrt(nn/D);bp=np.sqrt((D-nn)/D)
    elif math.isinf(q):
        ap=(nn>0).astype(float);bp=(nn==0).astype(float)
    else:
        eta=math.log(q);den=-math.expm1(-2*eta*D)
        ap=np.sqrt(np.maximum(0,-np.expm1(-2*eta*nn)/den))
        bp=np.exp(-eta*nn)*np.sqrt(np.maximum(0,-np.expm1(-2*eta*(D-nn))/den))
    if childJ==parentJ+1: out=ap if spin2==1 else bp
    elif childJ==parentJ-1: out=-bp if spin2==1 else ap
    else: out=np.zeros(len(M2s))
    return np.where(valid,out,0.0)

def complete_bound_fast(L,site,q,return_t=False):
    if L<1 or not 1<=site<=L or q<1: raise ValueError
    deg={0:1.0};T={}
    for n in range(1,L+1):
        nd={};nt={}
        for childJ in range(n%2,n+1,2):
            parents=[J for J in (childJ-1,childJ+1) if J in deg]
            nd[childJ]=0.5*sum(deg[J] for J in parents)
            if n>=site:
                M2s=np.arange(-childJ,childJ,2)
                vals=np.zeros(childJ)
                for J in parents:
                    if n==site:
                        vals+=0.5*deg[J]*cg_array(J,childJ,M2s+2,1,q)*cg_array(J,childJ,M2s,-1,q)
                    else:
                        for spin2 in (-1,1):
                            ix=(M2s-spin2+J)//2
                            ok=(ix>=0)&(ix<J)
                            old=np.zeros(childJ)
                            old[ok]=T[J][ix[ok]]
                            vals+=0.5*old*cg_array(J,childJ,M2s+2,spin2,q)*cg_array(J,childJ,M2s,spin2,q)
                nt[childJ]=vals
        deg,T=nd,nt
    bound=2*sum(float(vals@vals)/deg[J] for J,vals in T.items() if deg[J]>0)
    return (bound,deg,T) if return_t else bound



I2=np.eye(2)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)
sp=(X+1j*Y)/2
def embed1(op,i,L):
    out=np.array([[1]],complex)
    for j in range(L):out=np.kron(out,op if j==i else I2)
    return out

def qschur(L,q):
    data={((),0):np.ones((1,1),float)}
    for n in range(1,L+1):
        new={}
        for (path,J),B in data.items():
            for K in (J+1,J-1):
                if K<0:continue
                Mvals=range(-K,K+1,2)
                cols=[]
                for M in Mvals:
                    v=np.zeros(B.shape[0]*2)
                    for spin2,vec in ((1,np.array([1.,0.])),(-1,np.array([0.,1.]))):
                        mm=M-spin2
                        if abs(mm)<=J:
                            coeff=float(cg_array(J,K,[M],spin2,q)[0])
                            v+=coeff*np.kron(B[:,(mm+J)//2],vec)
                    cols.append(v)
                new[(path+(K,),K)]=np.column_stack(cols)
        data=new
    return data

def project_schur(O,L,q):
    bs=qschur(L,q);group={}
    for (_,J),B in bs.items():group.setdefault(J,[]).append(B)
    P=np.zeros_like(O,dtype=complex)
    for J, bases in group.items():
        av=sum(B.T.conj()@O@B for B in bases)/len(bases)
        for B in bases:P+=B@av@B.T.conj()
    return P,bs

def local_R(q):
    return np.array([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]],float)
def embed2(op,i,L):
    return np.kron(np.kron(np.eye(2**i),op),np.eye(2**(L-i-2)))


def word(L, mapping):
    ans=np.array([[1.0+0j]])
    for i in range(L):
        ans=np.kron(ans,mapping.get(i,I2))
    return ans

def source_hamiltonian(L,q,lam=1.0,stagger=False):
    delta=(q+1/q)/2
    a=q-1/q
    H=np.zeros((2**L,2**L),complex)
    for j in range(L-1):
        H+=word(L,{j:X,j+1:X})+word(L,{j:Y,j+1:Y})+delta*word(L,{j:Z,j+1:Z})
    H-=a/2*(word(L,{0:Z})-word(L,{L-1:Z}))
    for j in range(L-2):
        V=sum(word(L,{j:P,j+2:P}) for P in (X,Y,Z))
        V+=a*a/4*(word(L,{j:Z,j+1:Z})+word(L,{j+1:Z,j+2:Z}))
        V-=(q*q-q**-2)/4*(word(L,{j:Z})-word(L,{j+2:Z}))
        for P in (X,Y):
            V+=a/2*(word(L,{j:P,j+1:P,j+2:Z})-word(L,{j:Z,j+1:P,j+2:P}))
        H+=lam*((-1)**j if stagger else 1)*V
    return H

def total_E(L,q):
    plus=np.diag([math.sqrt(q),1/math.sqrt(q)])
    minus=np.diag([1/math.sqrt(q),math.sqrt(q)])
    return sum(word(L,{**{j:minus for j in range(i)},i:sp,**{j:plus for j in range(i+1,L)}}) for i in range(L))

def time_average(H,O,tol=1e-9):
    w,v=eigh(H)
    OO=v.conj().T@O@v
    mask=abs(w[:,None]-w[None,:])<tol
    return float(np.sum(abs(OO[mask])**2)/len(w)),w


def one_charge_bound(L, q):
    return ((q + 1/q + 2)/(2*(q + 1/q)))**(L-1)/L

def run_checks():
    report = {"normalization": "C_X(0)=Tr(X_i X_i)/2**L=1",
              "method": "complete symmetry projection, not a transport simulation"}
    tol=2e-10

    # 1. Independent full Hilbert-space q-Schur construction.
    maximum_error=0.0
    maximum_commutator=0.0
    cases=0
    for L,q in [(2,2.6),(3,1.2),(4,2.6),(6,2.6),(6,1.0)]:
        basis=qschur(L,q)
        B=np.column_stack(list(basis.values()))
        assert np.linalg.norm(B.T@B-np.eye(2**L))<tol
        for site in sorted(set((0,L//2,L-1))):
            O=embed1(X,site,L)
            projected,_=project_schur(O,L,q)
            direct=np.trace(projected.conj().T@projected).real/2**L
            rec=complete_bound_fast(L,site+1,q)
            error=abs(direct-rec)
            maximum_error=max(maximum_error,float(error))
            assert error<tol
            for j in range(L-1):
                R=embed2(local_R(q),j,L)
                com=np.linalg.norm(R@projected-projected@R)
                maximum_commutator=max(maximum_commutator,float(com))
                assert com<tol
            E=total_E(L,q)
            single=2*abs(np.trace(E.conj().T@O)/2**L)**2/(np.trace(E.conj().T@E).real/2**L)
            assert abs(single-one_charge_bound(L,q))<tol
            assert direct+tol>=single
            cases+=1
    report["direct_projection"]={"passed":True,"cases":cases,
        "max_value_error":maximum_error,"max_commutator_norm":maximum_commutator}

    # 2. A local random-unitary semigroup saturates the algebraic floor.
    L=4;q=2.6;d=2**L
    generator=np.zeros((d*d,d*d),complex)
    for j in range(L-1):
        R=embed2(local_R(q),j,L)
        Pj=(q*np.eye(d)-R)/(q+1/q)
        Uj=np.eye(d)-2*Pj
        assert np.linalg.norm(Pj@Pj-Pj)<tol
        assert np.linalg.norm(Uj@Uj-np.eye(d))<tol
        generator+=np.kron(Uj.conj(),Uj)-np.eye(d*d)
    eig,basis=eigh(generator)
    zero=basis[:,abs(eig)<1e-10]
    assert zero.shape[1]==math.comb(L+3,3)==35
    assert eig[-1]<tol
    local_values=[]
    for site in range(L):
        O=embed1(X,site,L).reshape(-1,order="F")
        P=zero@(zero.conj().T@O)
        actual=float(np.vdot(P,P).real/d)
        target=complete_bound_fast(L,site+1,q)
        assert abs(actual-target)<tol
        local_values.append(actual)
    report["local_noise_saturation"]={"passed":True,"hilbert_dimension":d,
        "operator_dimension":d*d,"stationary_operator_dimension":zero.shape[1],
        "site_values":local_values}

    # 3. The complete algebraic contribution need not equal a closed H plateau.
    spectral=[]
    for L in (4,6,8):
        q=2.6;site=L//2-1
        O=embed1(X,site,L);E=total_E(L,q)
        lower=complete_bound_fast(L,site+1,q)
        for lam in (0.0,1.0):
            H=source_hamiltonian(L,q,lam)
            com=float(np.linalg.norm(H@E-E@H)/np.linalg.norm(E))
            assert com<tol
            value,_=time_average(H,O,1e-9)
            value2,_=time_average(H,O,1e-10)
            assert abs(value-value2)<tol
            assert value+tol>=lower
            spectral.append({"L":L,"site":site+1,"q":q,"lambda":lam,
                "symmetry_floor":lower,"closed_H_average":value,
                "relative_commutator_norm":com})
    assert spectral[-1]["closed_H_average"]>1.1*spectral[-1]["symmetry_floor"]
    report["closed_hamiltonian_control"]={"passed":True,"values":spectral}

    # 4. Many-site recurrence and the undeformed endpoint.
    for L in (10,40,80):
        for site in (1,L//2,L):
            assert abs(complete_bound_fast(L,site,1.0)-1/L)<tol
    values=[]
    for L in (10,20,40,80,160):
        floor=complete_bound_fast(L,L//2,2.6)
        simple=one_charge_bound(L,2.6)
        assert 0<simple<=floor<=1
        values.append({"L":L,"site":L//2,"q":2.6,
            "one_charge":simple,"full_symmetry":floor,
            "ratio":floor/simple,"L_squared_times_full":L*L*floor})
    report["large_recurrence"]={"passed":True,"values":values,
        "warning":"These finite-size values do not prove an asymptotic power law."}
    report["groups_passed"]=4
    return report

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path("report.json"))
    args=parser.parse_args()
    result=run_checks()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"groups_passed":result["groups_passed"],"output":str(args.output)}))
