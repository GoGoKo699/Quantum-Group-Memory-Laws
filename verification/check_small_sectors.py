import json, argparse
import numpy as np
from pathlib import Path

def kronall(xs):
    out=np.array([[1.]])
    for x in xs: out=np.kron(out,x)
    return out

def generators(n,r):
    Z=np.diag([1.,-1.]); up=np.array([[0.,1.],[0.,0.]])
    E=sum(kronall([np.diag([r**(-.5),r**.5]) if j<i else up if j==i else np.diag([r**.5,r**(-.5)]) for j in range(n)]) for i in range(n))
    return E,E.T

def embeddings(r):
    D=1+r*r; S=1+r*r+r**4
    T=np.zeros((4,3)); T[0,0]=1; T[1,1]=D**-.5; T[2,1]=r*D**-.5; T[3,2]=1
    A=np.zeros((8,2)); A[2,0]=r*D**-.5; A[4,0]=-D**-.5; A[3,1]=r*D**-.5; A[5,1]=-D**-.5
    B=np.zeros((8,2)); B[1,0]=r*D/(D*S)**.5; B[2,0]=-1/(D*S)**.5; B[4,0]=-r/(D*S)**.5
    B[3,1]=r*r/(D*S)**.5; B[5,1]=r**3/(D*S)**.5; B[6,1]=-D/(D*S)**.5
    return T,A,B

def erase_kraus(embs,n,i):
    ans=[]
    for V in embs:
      for b in range(2):
        K=np.take(V.reshape([2]*n+[V.shape[1]]),b,axis=i).reshape(2**(n-1),V.shape[1]) / len(embs)**.5
        ans.append(K)
    return ans

def choi(Ks):
    d=Ks[0].shape[1]
    return sum(np.outer(K.flatten(order='F'),K.flatten(order='F'))/d for K in Ks)

def entropy(J):
    es=np.linalg.eigvalsh(J); es=es[es>1e-12]
    return float(-np.sum(es*np.log2(es)))

def binary_entropy(x):
    if x<=0 or x>=1:return 0.
    return float(-x*np.log2(x)-(1-x)*np.log2(1-x))

def operational_checks():
    finite_rates=0;patterns_checked=0;lower_rates=0
    for r in [1.,1.2,2.,3.]:
      lam=(1+2*r*r)/(3*(1+r*r))
      for p in [.1,.25,.5,.9]:
        achieved=(1-p*p)*np.log2(3)-2*p*(1-p)*binary_entropy(lam)
        benchmark=(1-p*p)*np.log2(3)-2*p*(1-p)
        assert achieved>=benchmark-1e-12
        if r>1:assert achieved>benchmark+1e-7
        finite_rates+=1
    for n in range(1,7):
      r=2.;z=r**-2;weights=(1-z)*z**np.arange(n-1,-1,-1)/(1-z**n)
      V=np.zeros((2**n,2));V[-1,0]=1
      for i,w in enumerate(weights):V[(2**n-1)^(1<<(n-1-i)),1]=np.sqrt(w)
      E,_=generators(n,r);raised=E@V[:,0];raised/=np.linalg.norm(raised)
      assert np.allclose(raised,V[:,1])
      rates=[]
      for mask in range(2**n):
        erased=[i for i in range(n) if mask&(1<<i)]
        surviving=[i for i in range(n) if not mask&(1<<i)]
        eta=float(sum(weights[i] for i in surviving))
        # Independent physical environment Gram matrix of the pure Choi vector.
        psi=V.reshape([2]*n+[2]).transpose(erased+surviving+[n]).reshape(2**len(erased),-1)/np.sqrt(2)
        eigen=np.linalg.eigvalsh(psi@psi.T)
        nonzero=eigen[eigen>1e-10]
        target=np.array([(1-eta)/2,(1+eta)/2]);target=target[target>1e-10]
        assert np.allclose(nonzero,target,atol=2e-12)
        rates.append(1-binary_entropy((1-eta)/2));patterns_checked+=1
      for p in [.1,.25,.5,.9]:
        mean=sum(p**mask.bit_count()*(1-p)**(n-mask.bit_count())*rates[mask] for mask in range(2**n))
        assert mean>=1-binary_entropy(p/2)-2e-12
        lower_rates+=1
    return {'two_site_rate_comparisons':finite_rates,'physical_one_excitation_patterns':patterns_checked,'pattern_averaged_lower_bounds':lower_rates}

def main(output):
    report=[]
    for r in [1.,1.2,2.,3.]:
      T,A,B=embeddings(r)
      E,F=generators(3,r)
      assert np.allclose(np.column_stack([A,B]).T@np.column_stack([A,B]),np.eye(4))
      for V in [A,B]:
        assert np.allclose(E@V[:,0],0)
        assert np.allclose(F@V[:,0],V[:,1])
        assert np.allclose(E@V[:,1],V[:,0])
        assert np.allclose(F@V[:,1],0)
      for n,embs in [(2,[T]),(3,[A,B])]:
       for i in range(n):
        Ks=erase_kraus(embs,n,i); d=Ks[0].shape[1]
        assert np.allclose(sum(K.T@K for K in Ks),np.eye(d))
        J=choi(Ks)
        assert np.linalg.eigvalsh(J).min()>-1e-12
        # Check channel directly on all matrix units, which proves reference-stable identity.
        for a in range(d):
         for b in range(d):
          X=np.eye(d)[:,a:a+1]@np.eye(d)[b:b+1]
          physical=sum(V@X@V.T for V in embs)/len(embs)
          shaped=physical.reshape([2]*n*2)
          direct=np.trace(shaped,axis1=i,axis2=n+i).reshape(2**(n-1),2**(n-1))
          assert np.allclose(direct,sum(K@X@K.T for K in Ks))
        report.append({'r':r,'n':n,'erased_site':i+1,'choi_spectrum':np.linalg.eigvalsh(J)[np.linalg.eigvalsh(J)>1e-10].tolist(),'choi_entropy':entropy(J),'reverse_coherent_information':np.log2(d)-entropy(J)})
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps({'checks':'orthonormal embeddings, correct quantum-group spin-1/2 ladders, TP and CP, all input matrix units against physical partial trace','rows':report,'operational':operational_checks()},indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('build/verification/small_sectors.json'))
    main(parser.parse_args().output)
