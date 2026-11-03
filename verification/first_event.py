"""Independent dynamic first-observed-mismatch distribution."""
import numpy as np

def first_event_law(path,delta,r,p):
    K=path[-1];h=K-delta;z=r**-2;logz=np.log(z)
    alive=np.zeros(max(path)+1);alive[h]=1
    logA=-np.inf;law=[]
    for t in reversed(range(1,len(path))):
      k=path[t];J=path[t-1];up=k==J+1
      hs=np.arange(k+1)
      if up:q=z**hs*(1-z**(k-hs))/(1-z**k)
      else:q=z**(hs+1)*(1-z**(k+1-hs))/(1-z**(k+2))
      logA=np.logaddexp(logA,k*logz)
      est=float(np.clip(logA/logz,0,K))
      observed=float(p*np.sum(alive[:k+1]*q))
      law.append((observed,est))
      out=np.zeros_like(alive)
      # Mismatch leaves h unchanged; matching shifts h with the path edge.
      out[:k+1]+=alive[:k+1]*q*(1-p)
      dest=hs-(1 if up else -1);good=(dest>=0)&(dest<=J)
      out[dest[good]]+=alive[hs[good]]*(1-q[good])
      alive=out
    noevent=float(np.sum(alive));law.append((noevent,0.))
    assert abs(sum(prob for prob,_ in law)-1)<1e-10
    assert noevent<=(1-p)**delta+1e-10
    return law

