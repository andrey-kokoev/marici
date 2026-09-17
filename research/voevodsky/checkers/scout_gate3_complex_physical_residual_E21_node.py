#!/usr/bin/env python3
"""Correct physical-space scout of the complete regularized residual Gram."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre,iv
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';theta=float(sys.argv[1]);rho=float(sys.argv[2]) if len(sys.argv)>2 else 2.1;zz=(rho*np.exp(1j*theta)+rho**-1*np.exp(-1j*theta))/2;L=.6495+.0005*zz;base=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');P=base['packet'];Q=np.linalg.qr(P,mode='complete')[0][:,40:];cc=np.load(root/'degree16_regularized_tail_map_L0649_L065.npz')['coefficients'];D=np.polynomial.chebyshev.chebval(zz,cc);Z=P-D;fb=np.load(root/'gate2_source_FB_degree32_L0649_L065.npz');F=np.polynomial.chebyshev.chebval(zz,fb['F']);B=np.polynomial.chebyshev.chebval(zz,fb['B']);Y=Q.T@D;PAZ=F-B@Y;N=1000;k=np.arange(N);sc=np.sqrt((2*k+1)/(2*L));qR=(digamma(.25+125j).real-math.log(math.pi))/2;terms=[(math.log(p),math.log(p)/np.sqrt(p)) for p in (2,3)];breaks=[-L,L-math.log(3),L-math.log(2),-L+math.log(2),-L+math.log(3),L];xp,wp=roots_legendre(1100);xall=[];wall=[];Hall=[]
x=L/2;ap=np.array([2*L*np.sqrt((2*n+1)/(2*L))*np.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in k]);am=ap*((-1.)**k);ep_plus=am@Z;ep_minus=ap@Z
for left,right in zip(breaks[:-1],breaks[1:]):
 x=(left+right)/2+(right-left)*xp/2;w=(right-left)*wp/2;base=np.column_stack([legval(x/L,Z[:,j]*sc) for j in range(40)]);H=qR*base
 for a,c in terms:
  shifted=np.zeros_like(H);mp=x.real+a<=L.real;mm=x.real-a>=-L.real
  if np.any(mp):shifted[mp]+=np.column_stack([legval((x[mp]+a)/L,Z[:,j]*sc) for j in range(40)])
  if np.any(mm):shifted[mm]+=np.column_stack([legval((x[mm]-a)/L,Z[:,j]*sc) for j in range(40)])
  H-=.5*c*shifted
 H+=.5*(np.exp(x[:,None]/2)*ep_plus+np.exp(-x[:,None]/2)*ep_minus);xall.append(x);wall.append(w);Hall.append(H)
xall=np.concatenate(xall);wall=np.concatenate(wall);H=np.vstack(Hall);KZ=np.zeros_like(H);o=np.arange(N);norm=2*L*np.sqrt((2*o+1)/(2*L));phase=np.array([(-1)**(n//2)*(1 if n%2==0 else -1j) for n in o]);z,w=roots_legendre(520)
for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
 u=(aa+bb)/2+(bb-aa)*z/2;ww=(bb-aa)*w/2;J=spherical_jn(o[:,None],L*u[None,:]);Vc=(norm[:,None]*phase[:,None]*J).T;Vcm=(norm[:,None]*np.conj(phase)[:,None]*J).T;FZ=Vc@Z;FZm=Vcm@Z;m=(digamma(.25+.5j*u).real-math.log(math.pi))/2-qR;KZ+=.5*(np.exp(1j*xall[:,None]*u[None,:])@((ww*m/math.pi)[:,None]*FZ)+np.exp(-1j*xall[:,None]*u[None,:])@((ww*m/math.pi)[:,None]*FZm))
AZ=H+KZ;G=AZ.T@(wall[:,None]*AZ);RG=G-PAZ.T@PAZ;out={'schema':'marici.voevodsky.gate3-complex-physical-residual-E21-scout.v1','theta':theta,'rho':rho,'L':[float(L.real),float(L.imag)],'physical_gram_norm':float(np.linalg.norm(G,2)),'projected_source_gram_norm':float(np.linalg.norm(PAZ.T@PAZ,2)),'residual_gram_norm':float(np.linalg.norm(RG,2)),'passed_scout':float(np.linalg.norm(RG,2))<.09776122183844219,'passed':False,'rh_proved':False};print(json.dumps(out,indent=2));np.savez_compressed(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta{theta:.6f}.npz',residual_gram=RG,physical_gram=G,projected_source_gram=PAZ.T@PAZ);p=root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta{theta:.6f}.json';p.write_text(json.dumps(out,indent=2)+'\n')
