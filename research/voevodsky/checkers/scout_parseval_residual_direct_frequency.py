#!/usr/bin/env python3
"""Direct positive-frequency Parseval residual scout, avoiding cross-term decomposition."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre,iv
root=Path(__file__).parents[1]/'results';d=np.load(root/'two_prime_regularized_rank670_vectors.npz');Z=d['schur_vectors'];P=d['retained'];S=d['finite_schur'];L=.55;N=670;o=np.arange(N);norm=2*L*np.sqrt((2*o+1)/(2*L));ph=(-1.)**(o//2);qR=(digamma(.25+125j).real-math.log(math.pi))/2;terms=[(math.log(p),math.log(p)/math.sqrt(p)) for p in (2,3)];x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in o]);am=ap*((-1.)**o);Ecoeff=.5*(np.outer(ap,am@Z)+np.outer(am,ap@Z));G=np.zeros((92,92));z,w=roots_legendre(300);edges=list(range(0,20250,250))
for aa,bb in zip(edges[:-1],edges[1:]):
 u=(aa+bb)/2+(bb-aa)*z/2;ww=(bb-aa)*w/2;V=(norm[:,None]*ph[:,None]*spherical_jn(o[:,None],L*u[None,:])).T;FZ=V@Z;FE=V@Ecoeff;q=np.where(u<=250,(digamma(.25+.5j*u).real-math.log(math.pi))/2,qR);b=q-sum(c*np.cos(u*a) for a,c in terms);FA=b[:,None]*FZ+FE
 # parity cross terms are zero; accumulate columns by parity after full product.
 G+=FA.T@((ww/math.pi)[:,None]*FA)
parity=np.array([0 if np.linalg.norm(Z[0::2,j])>=np.linalg.norm(Z[1::2,j]) else 1 for j in range(92)])
for i in range(92):
 for j in range(92):
  if parity[i]!=parity[j]:G[i,j]=0
A=np.load(root/'rank670_gamma_floor_midpoint.npz')['matrix'];PAZ=P.T@A@Z;RG=G-PAZ.T@PAZ;RG=(RG+RG.T)/2;alpha=.5897761979384148;lower=S-RG/alpha;lower=(lower+lower.T)/2;eg=np.linalg.eigvalsh(RG);el=np.linalg.eigvalsh(lower)
out={'schema':'marici.voevodsky.parseval-residual-direct-frequency-scout.v1','frequency_cutoff':20000,'residual_gram_range':[float(eg[0]),float(eg[-1])],'a_posteriori_lower_form_min':float(el[0]),'status':'floating direct positive-frequency integral; tail beyond 20000 omitted','passed':float(eg[0])>-1e-8 and float(el[0])>0,'rh_proved':False};p=root/'parseval_residual_direct_frequency_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
