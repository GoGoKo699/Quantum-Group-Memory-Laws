"""Analytical coefficient and independent spectral controls for the bulk proof.

The spin parameter is q>1. The orthogonal-polynomial base is z=q**-2,
not q. No physical Hilbert-space truncation is used in the theorem.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad


def criterion(q: float) -> float:
    if not math.isfinite(q) or q <= 1:
        raise ValueError('q must be finite and >1')
    z=q**-2
    return (q**-1+q**-3)/(1-z)**2


def threshold() -> float:
    x=(1+math.sqrt(17))/2
    return (x+math.sqrt(x*x-4))/2


def logpoch(a: float, z: float, eps: float=1e-17) -> float:
    if not (0<z<1) or a >= 1 or abs(a)>1:
        raise ValueError('real product arguments must satisfy |a|<=1 and a<1')
    total=0.; t=a
    while abs(t)/(1-z)>eps:
        total+=math.log1p(-t);t*=z
    return total


def amplitudes(q: float) -> tuple[float,float]:
    z=q**-2; a=1/q
    P=logpoch(z,z)
    ap=math.exp(math.log1p(-a)+4*(P-logpoch(a,z)))
    am=math.exp(math.log1p(a)+4*(P-logpoch(-a,z)))
    return ap,am


def multiplier(q: float) -> float:
    ap,am=amplitudes(q)
    return (ap*ap+am*am)/2


def shape(x: float) -> float:
    if not 0<x<1:raise ValueError('interior x required')
    w=x*(1-x)
    value=quad(lambda u:u*u*(1-u)**2/(.5+(u-x)**2/w)**2.5,
               0,1,epsabs=2e-12,epsrel=2e-12)[0]
    return 3*math.sqrt(2)*value/(4*math.pi*w**3)


def jacobi(q: float, size: int, upper_tilt: float|None=None):
    z=q**-2;r=np.arange(size,dtype=float)
    diagonal=.5*(q**-1+q**-3)*z**r
    if upper_tilt is None:
        off=.5*np.sqrt((1-z**(r[1:]))*(1-z**(r[1:]+1)))
    else:
        diagonal*=math.exp(upper_tilt)
        off=np.full(size-1,.5)
    return off,diagonal


def step(v, off, diag):
    w=diag*v
    w[:-1]+=off*v[1:];w[1:]+=off*v[:-1]
    return w


def kernel_vector(n: int,q:float,size:int|None=None, upper_tilt=None):
    # The initial exponential tail beyond size is discarded for this diagnostic.
    # The theorem, its exact spectral formula and all-code scope use no cutoff.
    if size is None:size=n+100
    r=np.arange(size,dtype=float);z=q**-2
    v=q**(-r)*np.sqrt(1-z**(r+1)) if upper_tilt is None else (r+1)*q**(-r)
    off,diag=jacobi(q,size,upper_tilt)
    for _ in range(n):v=step(v,off,diag)
    return v


def kernel_asym(n,q,r):
    ap,am=amplitudes(q);z=q**-2
    mu=2*math.sqrt(2/math.pi)*(r+1)*n**-1.5*math.exp(-(r+1)**2/(2*n))
    return .5*mu*(ap+(-1)**(n+r)*am)/(1-z)


def spectral_arrays(q:float,theta):
    z=q**-2;a=1/q;b=a*z
    theta=np.asarray(theta);zz=np.exp(1j*theta)
    A=np.ones(theta.shape,dtype=complex);B=A.copy();E=A.copy()
    p=1.
    while p>1e-18:
        A*=1-a*p*zz; B*=1-b*p*zz; E*=1-p*zz**2
        p*=z
    norm=math.exp(logpoch(z,z)+logpoch(z*z,z))
    measure=norm/(2*math.pi)*np.abs(E/(A*B))**2
    fhat=math.sqrt(1-z)*norm/np.abs(A)**2
    return measure,fhat


def spectral_moment(q:float,n:int,r:int,nodes=600):
    from scipy.special import roots_legendre
    xx,ww=roots_legendre(nodes);theta=(xx+1)*math.pi/2;wt=ww*math.pi/2
    measure,fhat=spectral_arrays(q,theta)
    off,di=jacobi(q,max(2,r+2))
    pm=np.zeros(nodes);p=np.ones(nodes)
    for k in range(r):
        pn=((np.cos(theta)-di[k])*p-(off[k-1]*pm if k else 0))/off[k]
        pm,p=p,pn
    return float(np.dot(wt,measure*fhat*p*np.cos(theta)**n))
