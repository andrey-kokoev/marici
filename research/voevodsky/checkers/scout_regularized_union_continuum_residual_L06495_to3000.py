#!/usr/bin/env python3
"""Scout dangerous-eigenvector residuals in Legendre modes 1000..1999."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,iv
from numpy.polynomial.legendre import leggauss
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');U=d['packet']-d['tail_maps'][4];L=.6495;lo=2000;hi=3000;orders=np.arange(hi);norm=2*L*np.sqrt((2*orders+1)/(2*L));ph=(-1.)**(orders//2);Rmat=np.zeros((hi-lo,U.shape[1]));qR=(digamma(.25+125j).real-math.log(math.pi))/2;nodes,wts=leggauss(320)
for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
 u=(aa+bb)/2+(bb-aa)*nodes/2;w=(bb-aa)*wts/2;V=(norm[:,None]*ph[:,None]*spherical_jn(orders[:,None],L*u[None,:])).T;sym=(digamma(.25+.5j*u).real-math.log(math.pi))/2-qR;FV=V[:,:1000]@U;Rmat+=(V[:,lo:].T*(w*sym/math.pi))@FV
# Prime action by exact-degree Gauss scout.
xg,wg=leggauss(hi);n=np.arange(hi);lnorm=np.sqrt((2*n+1)/(2*L))
def LV(x):
 V=np.empty((len(x),hi));V[:,0]=1;V[:,1]=x
 for k in range(1,hi-1):V[:,k+1]=((2*k+1)*x*V[:,k]-k*V[:,k-1])/(k+1)
 return V*lnorm
for p in (2,3):
 a=math.log(p);left=-L;right=L-a;t=(left+right)/2+(right-left)*xg/2;ww=(right-left)*wg/2;X=LV(t/L);Y=LV((t+a)/L);c=math.log(p)/math.sqrt(p);Rmat-=.5*c*(X[:,lo:].T@(ww[:,None]*(Y[:,:1000]@U))+Y[:,lo:].T@(ww[:,None]*(X[:,:1000]@U)))
# Endpoint rank-two cross.
x=L/2;ap=np.array([2*L*math.sqrt((2*k+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(k+.5,x) for k in orders]);am=ap*((-1.)**orders);Rmat+=.5*(np.outer(ap[lo:],am[:1000]@U)+np.outer(am[lo:],ap[:1000]@U))
np.savez(root/'regularized_union_continuum_residual_L06495_2000_2999.npz',residual=Rmat);norms=np.linalg.norm(Rmat,axis=0);op=float(np.linalg.svd(Rmat,compute_uv=False)[0]);alpha=1.067569476012246;correction=op*op/alpha
out={'schema':'marici.voevodsky.regularized-union-continuum-residual-L06495-to3000.v1','mode_range':[lo,hi-1],'residual_operator_norm':op,'residual_gram_correction':correction,'target_margin':1.918863145047285e-11,'status':'floating modes 2000..2999 only','passed':correction<1.918863145047285e-11,'rh_proved':False};p=root/'regularized_union_continuum_residual_L06495_to3000.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
