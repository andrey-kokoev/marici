#!/usr/bin/env python3
"""Scout dangerous-eigenvector residuals in Legendre modes 1000..1999."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv,roots_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,iv,roots_legendre
from numpy.polynomial.legendre import leggauss
root=Path(__file__).parents[1]/'results';d=np.load(root/'two_prime_regularized_rank670_vectors.npz');U=d['schur_vectors'];L=.55;input_dim=670;lo=4000;hi=5000;orders=np.arange(hi);norm=2*L*np.sqrt((2*orders+1)/(2*L));ph=(-1.)**(orders//2);Rmat=np.zeros((hi-lo,U.shape[1]));qR=(digamma(.25+125j).real-math.log(math.pi))/2;nodes,wts=leggauss(320)
for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
 u=(aa+bb)/2+(bb-aa)*nodes/2;w=(bb-aa)*wts/2;V=(norm[:,None]*ph[:,None]*spherical_jn(orders[:,None],L*u[None,:])).T;sym=(digamma(.25+.5j*u).real-math.log(math.pi))/2-qR;FV=V[:,:input_dim]@U;Rmat+=(V[:,lo:].T*(w*sym/math.pi))@FV
# Prime action by exact-degree Gauss scout.
xg,wg=roots_legendre(hi);n=np.arange(hi);lnorm=np.sqrt((2*n+1)/(2*L))
def LV(x):
 V=np.empty((len(x),hi));V[:,0]=1;V[:,1]=x
 for k in range(1,hi-1):V[:,k+1]=((2*k+1)*x*V[:,k]-k*V[:,k-1])/(k+1)
 return V*lnorm
for p in (2,3):
 a=math.log(p);left=-L;right=L-a;t=(left+right)/2+(right-left)*xg/2;ww=(right-left)*wg/2;X=LV(t/L);Y=LV((t+a)/L);c=math.log(p)/math.sqrt(p);Rmat-=.5*c*(X[:,lo:].T@(ww[:,None]*(Y[:,:input_dim]@U))+Y[:,lo:].T@(ww[:,None]*(X[:,:input_dim]@U)))
# Endpoint rank-two cross.
x=L/2;ap=np.array([2*L*math.sqrt((2*k+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(k+.5,x) for k in orders]);am=ap*((-1.)**orders);Rmat+=.5*(np.outer(ap[lo:],am[:input_dim]@U)+np.outer(am[lo:],ap[:input_dim]@U))
norms=np.linalg.norm(Rmat,axis=0);Rprev=np.load(root/'two_prime_regularized_residual_through_3999.npz')['residual'];R=np.vstack((Rprev,Rmat));np.savez(root/'two_prime_regularized_residual_through_4999.npz',residual=R);alpha=.5897761979384148;S=d['finite_schur'];lower=(S-R.T@R/alpha);lower=(lower+lower.T)/2;ev=np.linalg.eigvalsh(lower)
out={'schema':'marici.voevodsky.two-prime-regularized-residual-to-5000-scout.v1','new_mode_range':[lo,hi-1],'new_block_norm':float(np.linalg.svd(Rmat,compute_uv=False)[0]),'combined_residual_norm':float(np.linalg.svd(R,compute_uv=False)[0]),'a_posteriori_lower_form_min':float(ev[0]),'status':'floating; modes >=5000 omitted','passed':float(ev[0])>0,'rh_proved':False};p=root/'two_prime_regularized_residual_to_5000_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
