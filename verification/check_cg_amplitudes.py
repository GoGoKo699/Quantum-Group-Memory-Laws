"""Independent physical-generator check of stochastic CG coefficients."""
import json, math, argparse
from pathlib import Path
import numpy as np
from check_estimator import paths,branches

def embedding(path,r):
    n=len(path)-1;K=path[-1];z=r**-2
    V=np.zeros((1<<n,K+1))
    def rec(t,h,upmask,amp,hfinal):
        if not t:
            assert h==0;V[upmask,hfinal]=amp;return
        down=path[t]==path[t-1]-1
        for s,hp,pr in branches(path,t,h,z):
            if pr<=0:continue
            sign=-1 if down and s==1 else 1
            rec(t-1,hp,upmask|((1<<(t-1)) if s==1 else 0),amp*sign*math.sqrt(pr),hfinal)
    for h in range(K+1):rec(n,h,0,1.,h)
    return V

def raising(n,r):
    E=np.zeros((1<<n,1<<n))
    for x in range(1<<n):
        zs=[1 if x&(1<<i) else -1 for i in range(n)]
        for i,z in enumerate(zs):
            if z<0:E[x|(1<<i),x]=r**((-sum(zs[:i])+sum(zs[i+1:]))/2)
    return E

def qnum(k,r):return (r**k-r**-k)/(r-r**-1)

def main(output):
    rows=[]
    for r in (1.2,2.,3.):
      for n in range(1,8):
        E=raising(n,r);cols=[];err=0.
        for path in paths(n):
            V=embedding(path,r);K=path[-1];cols.append(V)
            L=np.zeros((K+1,K+1))
            for h in range(K):L[h+1,h]=math.sqrt(qnum(h+1,r)*qnum(K-h,r))
            err=max(err,float(np.max(np.abs(E@V-V@L))))
            assert np.allclose(E@V,V@L,atol=2e-10,rtol=2e-12),(r,n,path,err)
        U=np.column_stack(cols);ortho=float(np.max(np.abs(U.T@U-np.eye(1<<n))))
        assert ortho<2e-11
        rows.append({'r':r,'n':n,'physical_dimension':1<<n,'path_count':len(cols),'max_E_intertwining_error':err,'max_orthogonality_error':ortho})
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps({'status':'passed','checks':'all path embeddings orthonormal and complete; independent physical E coproduct intertwining with exact spin ladders','rows':rows},indent=2)+'\n')
    print(json.dumps(rows,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('build/verification/cg_amplitudes.json'))
    main(parser.parse_args().output)
