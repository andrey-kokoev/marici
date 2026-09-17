#!/usr/bin/env python3
"""Floating constant-floor lower bound for the positive gamma tail."""
import json,sys,math
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv,eval_legendre
 from scipy.optimize import brentq
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv,eval_legendre
 from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
L=.55;N=80;Q=400;r,w=leggauss(Q);g=lambda u:digamma(.25+.5j*u).real-math.log(math.pi);U=brentq(g,1,20)
def Vals(u):return np.array([2*L*math.sqrt((2*n+1)/(2*L))*((-1)**(n//2))*spherical_jn(n,L*u) for n in range(N)]).T
def integ(R,weighted):
 u=R*(r+1)/2;ww=R*w/2;V=Vals(u);fac=ww*(g(u)/(2*math.pi) if weighted else 1/math.pi);M=(V.T*fac)@V;M[0::2,1::2]=0;M[1::2,0::2]=0;return M
G0=integ(U,True)
# Physical prime overlaps.
P=np.zeros((N,N));z,wz=leggauss(Q)
def phi(n,t):return math.sqrt((2*n+1)/(2*L))*eval_legendre(n,t/L)
for p in (2,3):
 a=math.log(p);lo=-L;hi=L-a;t=(lo+hi)/2+(hi-lo)*z/2;wt=(hi-lo)*wz/2;B=np.array([[phi(n,tt) for n in range(N)] for tt in t]);Bs=np.array([[phi(n,tt+a) for n in range(N)] for tt in t]);T=(B.T*wt)@Bs;P-=math.log(p)/math.sqrt(p)*(T+T.T)/2
x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in range(N)]);am=ap*np.array([(-1)**n for n in range(N)]);E=(np.outer(ap,am)+np.outer(am,ap))/2
rows=[]
for R in (10,20,50,100,200,500,1000):
 # Registered lower bound Re psi >= log(R/2)-3/2 for all u>=R.
 floor=(math.log(R/2)-1.5-math.log(math.pi))/2
 T=integ(R,False);H=G0+floor*(np.eye(N)-T)+P+E;H=(H+H.T)/2;e=np.linalg.eigvalsh(H);rows.append({'R':R,'gamma_half_multiplier_floor':floor,'min_eigenvalue':float(e[0]),'negative_count':int(np.count_nonzero(e<0))})
out={'schema':'marici.voevodsky.two-prime-gamma-tail-floor-scout.v1','L':L,'dimension':N,'gamma_crossing':U,'rows':rows,'method':'retain gamma on [0,U], drop [U,R], and lower-bound [R,infinity] by a constant times I minus the band-concentration matrix','status':'floating scout; concentration and quadrature not directed','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_gamma_tail_floor_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
