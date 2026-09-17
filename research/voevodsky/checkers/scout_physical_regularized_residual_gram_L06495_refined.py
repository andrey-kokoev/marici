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
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');P=d['packet'];Z=P-d['tail_maps'][4];S=d['schur'][4];L=.6495;N=1000;k=np.arange(N);sc=np.sqrt((2*k+1)/(2*L));qR=(digamma(.25+125j).real-math.log(math.pi))/2;terms=[(math.log(p),math.log(p)/math.sqrt(p)) for p in (2,3)];breaks=sorted(set([-L,L]+[-L+a for a,c in terms]+[L-a for a,c in terms]));xp,wp=roots_legendre(1100);xall=[];wall=[];Hall=[]
x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in k]);am=ap*((-1.)**k);ep_plus=am@Z;ep_minus=ap@Z
for left,right in zip(breaks[:-1],breaks[1:]):
 x=(left+right)/2+(right-left)*xp/2;w=(right-left)*wp/2;base=np.column_stack([legval(x/L,Z[:,j]*sc) for j in range(40)]);H=qR*base
 for a,c in terms:
  shifted=np.zeros_like(H);mp=x+a<=L;mm=x-a>=-L
  if np.any(mp):shifted[mp]+=np.column_stack([legval((x[mp]+a)/L,Z[:,j]*sc) for j in range(40)])
  if np.any(mm):shifted[mm]+=np.column_stack([legval((x[mm]-a)/L,Z[:,j]*sc) for j in range(40)])
  H-=.5*c*shifted
 H+=.5*(np.exp(x[:,None]/2)*ep_plus+np.exp(-x[:,None]/2)*ep_minus);xall.append(x);wall.append(w);Hall.append(H)
xall=np.concatenate(xall);wall=np.concatenate(wall);H=np.vstack(Hall);KZ=np.zeros_like(H);o=np.arange(N);norm=2*L*np.sqrt((2*o+1)/(2*L));phase=np.array([(-1)**(n//2)*(1 if n%2==0 else -1j) for n in o]);z,w=roots_legendre(520)
for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
 u=(aa+bb)/2+(bb-aa)*z/2;ww=(bb-aa)*w/2;Vc=(norm[:,None]*phase[:,None]*spherical_jn(o[:,None],L*u[None,:])).T;FZ=Vc@Z;m=(digamma(.25+.5j*u).real-math.log(math.pi))/2-qR;KZ+=np.real(np.exp(1j*xall[:,None]*u[None,:])@((ww*m/math.pi)[:,None]*FZ))
AZ=H+KZ;G=AZ.T@(wall[:,None]*AZ);A=np.load(root/'gamma_floor_L06495_rank1000_midpoint.npz')['matrix'];PAZ=P.T@A@Z;RG=G-PAZ.T@PAZ;RG=(RG+RG.T)/2;alpha=1.067569476012246;lower=S-RG/alpha;lower=(lower+lower.T)/2;eg=np.linalg.eigvalsh(RG);el=np.linalg.eigvalsh(lower);np.savez(root/'physical_regularized_residual_gram_L06495_refined_matrices.npz',output_gram=G,residual_gram=RG,lower_form=lower)
out={'schema':'marici.voevodsky.physical-regularized-residual-gram-L06495-refined-scout.v1','physical_nodes':len(xall),'frequency_nodes':9*520,'residual_gram_range':[float(eg[0]),float(eg[-1])],'complete_residual_norm':float(math.sqrt(max(0,eg[-1]))),'a_posteriori_lower_form_min':float(el[0]),'status':'floating physical compressed-operator scout','passed':float(eg[0])>-1e-8 and float(el[0])>0,'rh_proved':False};p=root/'physical_regularized_residual_gram_L06495_refined_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
