import sys,time,math
import numpy as np
sys.path.insert(0,'/mnt/data/qg_memory_asymptotics_2026-10-08/prior')
from check_memory import complete_bound_fast
for L in [20,40,80,160]:
 t=time.time()
 vals=[]
 for i in [1,2,3,L//4,L//2]:
  m=complete_bound_fast(L,i,2.6)
  vals.append((i,m,m*math.sqrt(L),L*L*m))
 print(L,vals,'seconds',time.time()-t,flush=True)
