#!/usr/bin/env python3
"""Sample the rho=4 complex ellipse for the reduced 20x20 Schur block."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv
 from scipy.linalg import svdvals
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,iv
 from scipy.linalg import svdvals
from numpy.polynomial.legendre import leggauss
root=Path(__file__).parents[1]/'results';Aend=np.load(root/'gamma_floor_L065_rank1000_midpoint.npz')['matrix'];ev,V=np.linalg.eigh(Aend);W=np.column_stack((V[:,1:20],V[:,0]));N=1000;o=np.arange(N);zg,wg=leggauss(140);xs,ws=leggauss(500);rho=4.;center=.6495;radius=.0005;q250=(digamma(.25+125j).real-math.log(math.pi))/2
def projected_legendre(y,L):
 U=np.zeros((len(y),20),dtype=complex);p0=np.ones(len(y),complex);U+=p0[:,None]*(np.sqrt(1/(2*L))*W[0]);p1=y;U+=p1[:,None]*(np.sqrt(3/(2*L))*W[1])
 for n in range(1,N-1):
  p2=((2*n+1)*y*p1-n*p0)/(n+1);U+=p2[:,None]*(np.sqrt((2*n+3)/(2*L))*W[n+1]);p0,p1=p1,p2
 return U
def block(L):
 norm=2*L*np.sqrt((2*o+1)/(2*L));ph=(-1.)**(o//2);G=np.zeros((20,20),complex);K=np.zeros_like(G)
 for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
  u=(aa+bb)/2+(bb-aa)*zg/2;ww=(bb-aa)*wg/2;Vbase=(norm[:,None]*ph[:,None]*spherical_jn(o[:,None],L*u[None,:])).T;Ve=Vbase[:,0::2]@W[0::2];Vo=Vbase[:,1::2]@W[1::2];q=(digamma(.25+.5j*u).real-math.log(math.pi))/2;G+=(Ve.T*(ww*q/math.pi))@Ve+(Vo.T*(ww*q/math.pi))@Vo;K+=(Ve.T*(ww/math.pi))@Ve+(Vo.T*(ww/math.pi))@Vo
 P=np.zeros_like(G)
 for p,c in ((2,math.log(2)/math.sqrt(2)),(3,math.log(3)/math.sqrt(3))):
  a=math.log(p);lo=-L;hi=L-a;t=(lo+hi)/2+(hi-lo)*xs/2;ww=(hi-lo)*ws/2;X=projected_legendre(t/L,L);Y=projected_legendre((t+a)/L,L);T=(X.T*ww)@Y;P-=c*(T+T.T)/2
 x=L/2;ap=np.array([2*L*np.sqrt((2*n+1)/(2*L))*np.sqrt(np.pi/(2*x))*iv(n+.5,x) for n in o]);am=ap*((-1.)**o);a=ap@W;m=am@W;E=(np.outer(a,m)+np.outer(m,a))/2
 return G+P+E+q250*(np.eye(20)-K)
rows=[]
for theta in np.linspace(0,2*np.pi,9)[:-1]:
 z=.5*(rho*np.exp(1j*theta)+rho**-1*np.exp(-1j*theta));L=center+radius*z;M=block(L);F=M[:19,:19];b=M[:19,19];s=M[19,19]-M[19,:19]@np.linalg.solve(F,b);rows.append({'theta':float(theta),'L_real':float(L.real),'L_imag':float(L.imag),'schur_abs':float(abs(s)),'robust_min_singular':float(svdvals(F)[-1])})
out={'schema':'marici.voevodsky.complex-schur-ellipse-L0649-L065-scout.v1','rho':rho,'samples':rows,'maximum_sampled_schur_abs':max(x['schur_abs'] for x in rows),'minimum_sampled_robust_singular':min(x['robust_min_singular'] for x in rows),'target_schur_abs':1e-7,'passed':max(x['schur_abs'] for x in rows)<1e-7 and min(x['robust_min_singular'] for x in rows)>1e-10,'status':'floating 8-point ellipse scout; boundary enclosure remains required','rh_proved':False};p=root/'complex_schur_ellipse_L0649_L065_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
