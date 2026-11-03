"""Exhaustive finite checks of the first-erased-mismatch converse.

No sampling: enumerate every nonnegative CG path through n=7, every weight,
every nonzero physical word, and every Bernoulli erasure flag. CG word
probabilities use rational arithmetic for r=6/5,2,3; flag sums and entropies
use double precision. This supports, and does not prove, the uniform theorem.
"""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import math, json, argparse
import numpy as np

from first_event import first_event_law

def paths(n):
    ans=[(0,)]
    for _ in range(n):
        ans=[a+(a[-1]+e,) for a in ans for e in (-1,1) if a[-1]+e>=0]
    return ans

def branches(path,t,h,z):
    k,J=path[t],path[t-1]
    if k==J+1:
        return [(1,h-1,(1-z**h)/(1-z**k)),
                (-1,h,z**h*(1-z**(k-h))/(1-z**k))]
    return [(1,h,z**(h+1)*(1-z**(k+1-h))/(1-z**(k+2))),
            (-1,h+1,(1-z**(h+1))/(1-z**(k+2)))]

def words(path,delta,z):
    n=len(path)-1;K=path[-1]
    ans=[]
    def rec(t,h,upmask,mmask,S,prob):
        assert h-path[t]==-delta+S
        if t==0:
            assert h==0 and S==delta and mmask.bit_count()>=delta
            assert upmask.bit_count()==(n-K)//2+K-delta
            ans.append((upmask,mmask,prob));return
        bs=branches(path,t,h,z)
        assert sum(b[2] for b in bs)==1
        q=sum(pr for s,hp,pr in bs if s!=path[t]-path[t-1])
        assert q<=z**h/(1-z)
        if path[t]-h>=1: assert q>=z*(1-z)*z**h
        for s,hp,pr in bs:
            if not pr:continue
            assert 0<=hp<=path[t-1] and 0<pr<=1
            mm=s!=path[t]-path[t-1]
            rec(t-1,hp,upmask|((1<<(t-1)) if s==1 else 0),
                mmask|((1<<(t-1)) if mm else 0),
                S+(path[t]-path[t-1] if mm else 0),prob*pr)
    rec(n,K-delta,0,0,0,F(1))
    assert sum(a[2] for a in ans)==1
    return ans

def B(t,z,p):
    g=t//3
    x=p*z*(1-z)**2*z**(g-t)
    return 2*(1-p)**g+p/(1-z)*z**(t-g)+math.exp(-x)+(1-p)**t

def mean_bound(z,p,k0=60):
    # Sum t>=3*k0 analytically except the superexponential term, whose
    # consecutive k ratios are bounded by q0<1, separately for each residue.
    a=1-p;u=p*z*(1-z)**2*z**(-2*k0)
    q0=math.exp(-u*(z**-2-1)) if u*(z**-2-1)<745 else 0.
    assert q0<1
    tail=6*a**k0/(1-a)
    tail+=p/(1-z)*z**(2*k0)*(1+z+z*z)/(1-z*z)
    tail+=a**(3*k0)/(1-a)
    tail+=sum(math.exp(-u*z**(-s)) if u*z**(-s)<745 else 0. for s in range(3))/(1-q0)
    total=3+sum(min(1.,B(t,z,p)) for t in range(3,3*k0))+tail
    return total,tail

def entropy(x):
    x=np.asarray(x);x=x[x>0]
    return float(-np.sum(x*np.log2(x)))

def geom_entropy(m):
    return (m+1)*math.log2(m+1)-m*math.log2(m) if m else 0.

def main(output):
    out=[];rng=np.random.default_rng(20261103)
    for rfrac in (F(6,5),F(2),F(3)):
      r=float(rfrac);zf=1/rfrac**2;z=float(zf)
      word_cache={}
      # Rational word generation is independent of erasure probability.
      for n in range(1,8):
       for path in paths(n):
        for delta in range(path[-1]+1):
          word_cache[(path,delta)]=words(path,delta,zf)
      for p in (.2,.5,.8):
        M,remainder=mean_bound(z,p);C=1+geom_entropy(M+1)
        row={'r':r,'p':p,'n_max':7,'logical_cases':0,'physical_words':0,
             'word_flag_cases':0,'tail_comparisons':0,'nontrivial_tail_comparisons':0,
             'prior_cases':0,'max_normalization_error':0.,'max_dp_error':0.,
             'max_mean_absolute_error':0.,'max_rounded_error':0.,
             'max_posterior_entropy':0.,'max_tail_ratio':0.,
             'M_upper':M,'M_tail_remainder_upper':remainder,'C_upper_bits':C}
        for n in range(1,8):
         flags=np.arange(1<<n,dtype=np.int64)
         counts=np.array([int(f).bit_count() for f in flags])
         fw=p**counts*(1-p)**(n-counts)
         assert abs(fw.sum()-1)<1e-12
         for path in paths(n):
          K=path[-1];A=0.;est=np.zeros(n+1)
          for t in range(n,0,-1):
            A+=z**path[t]
            est[t]=min(K,max(0.,math.log(A)/math.log(z)))
          laws=[];obslaws=[]
          for delta in range(K+1):
            row['logical_cases']+=1
            wd=word_cache[(path,delta)]
            row['physical_words']+=len(wd)
            law=np.zeros(n+1);obs=defaultdict(float)
            gtail=np.zeros(n+1)
            for upmask,mmask,wr in wd:
              w=float(wr)
              observed=flags&mmask
              tau=np.array([int(v).bit_length() for v in observed])
              ps=w*fw
              law+=np.bincount(tau,weights=ps,minlength=n+1)
              # Count hidden mismatches before the first observed mismatch.
              gs=np.array([(mmask>>(int(t))).bit_count() if t else mmask.bit_count() for t in tau])
              for g in range(n+1):gtail[g]+=float(ps[gs>=g].sum())
              for f,pr in zip(flags,ps):obs[(int(f),upmask&int(f))]+=float(pr)
              row['word_flag_cases']+=len(flags)
            err=abs(law.sum()-1)
            row['max_normalization_error']=max(row['max_normalization_error'],err)
            assert err<2e-12
            assert law[0]<=(1-p)**delta+2e-12
            assert np.all(gtail<=(1-p)**np.arange(n+1)+2e-12)
            # Independent state-propagation recurrence has one event per step.
            dp=first_event_law(path,delta,r,p)
            target=np.array([dp[-1][0]]+[dp[n-t][0] for t in range(1,n+1)])
            dperr=float(np.max(np.abs(law-target)))
            row['max_dp_error']=max(row['max_dp_error'],dperr)
            assert dperr<2e-12
            mean=float(np.dot(law,np.abs(est-delta)))
            rounded=float(np.dot(law,np.abs(np.rint(est)-delta)))
            assert mean<=M+2e-12 and rounded<=M+1+2e-12
            row['max_mean_absolute_error']=max(row['max_mean_absolute_error'],mean)
            row['max_rounded_error']=max(row['max_rounded_error'],rounded)
            for t in range(3,K+2):
              early=float(law[est-delta>=t-1e-12].sum())
              late=float(law[delta-est>=t-1e-12].sum())
              total=float(law[np.abs(est-delta)>=t-1e-12].sum())
              g=t//3
              eb=(1-p)**g+p/(1-z)*z**(t-g)
              lb=(1-p)**g+math.exp(-p*z*(1-z)**2*z**(g-t))+(1-p)**t
              for actual,bound in ((early,eb),(late,lb),(total,B(t,z,p))):
                assert actual<=bound+2e-12,(path,delta,r,p,t,actual,bound)
                row['tail_comparisons']+=1
                if bound<1:
                  row['nontrivial_tail_comparisons']+=1
                  row['max_tail_ratio']=max(row['max_tail_ratio'],actual/bound)
            laws.append(law);obslaws.append(obs)
          # Arbitrary-prior posterior calculation from full observed records,
          # not only the first mismatch. Five reproducible representative priors.
          priors=[np.ones(K+1)/(K+1),np.eye(K+1)[0],np.eye(K+1)[K],
                  np.array([.25 if i in (0,K) else 1. for i in range(K+1)]),
                  rng.dirichlet(np.ones(K+1))]
          priors[3]/=priors[3].sum()
          keys=set().union(*(d.keys() for d in obslaws))
          for prior in priors:
            Hcond=0.;errprobs=defaultdict(float);meanerr=0.
            for key in keys:
              joint=np.array([prior[d]*obslaws[d].get(key,0.) for d in range(K+1)])
              mass=joint.sum()
              if mass<=0:continue
              Hcond+=mass*entropy(joint/mass)
              f,up=key
              mmask=0
              for site in range(1,n+1):
                if f&(1<<(site-1)):
                  s=1 if up&(1<<(site-1)) else -1
                  if s!=path[site]-path[site-1]:mmask|=1<<(site-1)
              t=mmask.bit_length();dhat=int(np.rint(est[t]))
              for d,pr in enumerate(joint):
                errprobs[d-dhat]+=float(pr);meanerr+=abs(d-dhat)*float(pr)
            Herr=entropy(list(errprobs.values()))
            assert Hcond<=Herr+3e-11
            assert Herr<=1+geom_entropy(meanerr)+3e-11
            assert Hcond<=C+3e-11 and meanerr<=M+1+3e-11
            row['prior_cases']+=1
            row['max_posterior_entropy']=max(row['max_posterior_entropy'],Hcond)
        out.append(row);print(json.dumps(row),flush=True)
    result={'status':'passed','method':'exhaustive paths, weights, nonzero words, all erasure flags; rational CG word probabilities; double-precision flag sums/entropies',
            'scope':'finite tests support the analytical proof; no asymptotic or capacity conclusion follows from tests alone',
            'source_proof':'science/first_mismatch.md','rows':out}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('build/verification/estimator.json'))
    main(parser.parse_args().output)
