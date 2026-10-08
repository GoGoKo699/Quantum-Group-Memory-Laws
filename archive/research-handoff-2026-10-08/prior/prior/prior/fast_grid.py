"""Vectorized version of the unchanged finite-q multiplicity-trace recurrence.

This module changes array scheduling only; it introduces no sector cutoff or
asymptotic approximation. q=1 remains evaluated by the original checker.
For large L memory scales as O(L**2), arithmetic as O(L**3).
"""
import numpy as np,math

def fast(L,site,q,return_t=False):
 if not (L>=1 and 1<=site<=L and q>1 and math.isfinite(q)):raise ValueError
 nmax=L+3
 hh=np.arange(nmax)[:,None]
 rr=np.arange(nmax)[None,:]
 Q=q**-2
 f=lambda x: -np.expm1(np.minimum(-2*math.log(q)*np.maximum(x,0),0))
 # Final h,r recurrence with doubled spin h. Zero rows and triangular padding retained.
 den=f(hh)
 den2=f(hh+2)
 den=np.where(den==0,1,den)
 alpha=np.sqrt(f(rr)*f(rr+1))/den
 beta=np.exp(-math.log(q)*(2*rr+1))*np.sqrt(f(hh-rr-1)*f(hh-rr))/den
 gamma=np.exp(-math.log(q)*(2*rr+3))*np.sqrt(f(hh-rr+1)*f(hh-rr))/den2
 delta=np.sqrt(f(rr+1)*f(rr+2))/den2
 valid=(rr<hh)
 alpha*=valid;beta*=valid;gamma*=valid;delta*=valid
 insp=np.exp(-math.log(q)*rr)*np.sqrt(f(rr+1)*f(hh-rr))/den
 insm=-np.exp(-math.log(q)*(rr+2))*np.sqrt(f(rr+1)*f(hh-rr))/den2
 insp*=valid;insm*=valid
 m=np.zeros(nmax);m[0]=1.
 T=np.zeros((nmax,nmax))
 for n in range(1,L+1):
  hs=np.arange(n%2,n+1,2)
  left=np.maximum(hs-1,0); right=hs+1
  ml=m[left].copy();ml[hs==0]=0
  mr=m[right].copy()
  if n==site:
   T[hs,:n]=.5*(ml[:,None]*insp[hs,:n]+mr[:,None]*insm[hs,:n])
  elif n>site:
   l=T[left,:n].copy();l[hs==0]=0
   rt=T[right,:n+1]
   shifted=np.zeros_like(l);shifted[:,1:]=l[:,:-1]
   T[hs,:n]=.5*(alpha[hs,:n]*shifted+beta[hs,:n]*l+gamma[hs,:n]*rt[:,:n]+delta[hs,:n]*rt[:,1:])
  m[hs]=.5*(ml+mr);m[np.arange(nmax)%2!=(n%2)]=0
 vals=[]
 for h in range(L%2,L+1,2):
  if m[h]>0:vals.append(np.dot(T[h,:h],T[h,:h])/m[h])
 result=2*math.fsum(vals)
 if return_t:return result,m,T
 return result
