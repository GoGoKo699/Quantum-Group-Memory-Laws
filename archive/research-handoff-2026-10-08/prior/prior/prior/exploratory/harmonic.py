import math,numpy as np
for q in [1.2,1.5,2,2.6,4,10,100]:
 Q=q**-2;N=400
 off=.5*np.sqrt((1-Q**np.arange(1,N+1))*(1-Q**np.arange(2,N+2)))
 diag=.5*(1/q+1/q**3)*Q**np.arange(N)
 h=np.zeros(N);h[0]=1
 h[1]=(1-diag[0])*h[0]/off[0]
 for r in range(1,N-1):h[r+1]=((1-diag[r])*h[r]-off[r-1]*h[r-1])/off[r]
 slope=h[-1]-h[-2];h/=slope
 f=q**(-np.arange(N,dtype=float))*np.sqrt(1-Q**(np.arange(N)+1))
 amp=(1-Q)*np.dot(h,f)
 print(q,'amp',amp,'square',amp**2,'h0',h[0],'intercept',h[-1]-(N-1))
