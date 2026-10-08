import math,time,sys
import numpy as np
from scipy.special import gammaln
from scipy.integrate import quad
sys.path.insert(0,'/mnt/data/qg_memory_asymptotics_2026-10-08/prior')
from check_memory import complete_bound_fast

def lm(n,h):
 h=np.asarray(h);k=(n-h)/2
 return np.log(h+1)-math.log(n+1)+gammaln(n+2)-gammaln(k+1)-gammaln(n+2-k)
def cr(L,i):
 p=i-1;n=L-i
 a=np.arange(p%2,p+1,2)[:,None];b=np.arange(n%2,n+1,2)[None,:]
 return float(np.exp((1-L)*math.log(2)+2*lm(p,a)+2*lm(n,b)-lm(L,a+b+1)).sum())
def bulkf(x):
 z=x*(1-x)
 val=quad(lambda u:u*u*(1-u)**2/(.5+(u-x)**2/z)**2.5,0,1,epsabs=1e-12)[0]
 return 3*math.sqrt(2)/(4*math.pi*z**3)*val
for x in [.1,.25,.5]:print('F',x,bulkf(x))
for L in [10,40,160,640,2560]:
 for i in [1,L//4,L//2]:
  v=cr(L,i)
  print('cr',L,i,v,'scaled bulk',L*L*v,'edge',math.sqrt(L)*v,flush=True)
for L in [8,20]:
 for i in [1,L//2]:
  print('check',L,i,cr(L,i),complete_bound_fast(L,i,math.inf))
