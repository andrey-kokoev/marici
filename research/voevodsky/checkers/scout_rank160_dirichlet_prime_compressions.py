#!/usr/bin/env python3
"""Finite-section scout of the two-prime Dirichlet tail and low-tail coupling."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np

def one(L,size,a):
 n=np.arange(1,size+1,dtype=float);al=n[:,None]*math.pi/(2*L);be=n[None,:]*math.pi/(2*L);w=2*L-a;dm=al-be;sp=al+be
 first=np.empty((size,size));mask=np.eye(size,dtype=bool)
 np.divide(np.sin(dm*w-be*a)+np.sin(be*a),dm,out=first,where=~mask)
 first[mask]=w*np.cos((n*math.pi/(2*L))*a)
 second=(np.sin(sp*w+be*a)-np.sin(be*a))/sp
 return (first-second)/(2*L)

def opnorm(A):
 if A.shape[0]==A.shape[1] and np.max(np.abs(A-A.T))<1e-12:
  e=np.linalg.eigvalsh(A);return float(np.max(np.abs(e))),float(e[0]),float(e[-1])
 return float(np.linalg.svd(A,compute_uv=False)[0]),None,None
L=.55;N=160;terms=[(math.log(2),math.log(2)/math.sqrt(2)),(math.log(3),math.log(3)/math.sqrt(3))];rows=[]
for size in (240,320,480,640):
 P=np.zeros((size,size))
 for a,c in terms:
  A=one(L,size,a);P+=0.5*c*(A+A.T)
 tail=P[N:,N:];mix=P[:N,N:];d=np.log1p(np.arange(1,size+1)*math.pi/(2*L));wt=tail/np.sqrt(d[N:,None]*d[None,N:])
 tn,tmin,tmax=opnorm(tail);wn,wmin,wmax=opnorm(wt);mn,_,_=opnorm(mix)
 rows.append({'matrix_size':size,'tail_dimension':size-N,'tail_norm':tn,'tail_eigenvalue_range':[tmin,tmax],'low_tail_mix_norm':mn,'log_weighted_tail_norm':wn,'weighted_eigenvalue_range':[wmin,wmax]})
out={'schema':'marici.voevodsky.rank160-dirichlet-prime-compressions-scout.v1','L':L,'low_dirichlet_modes':N,'prime_terms':[{'n':int(round(math.exp(a))),'shift':a,'weight':c} for a,c in terms],'absolute_symmetric_translation_mass':sum(c for _,c in terms),'rows':rows,'normalization':'-weight*(T_a+T_a^*)/2, matching certify_two_prime_overlap_arb_160.py (sign omitted for norms)','claim_boundary':'floating finite sections only; omitted modes and the Legendre-to-Dirichlet basis mismatch are not certified','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'rank160_dirichlet_prime_compressions_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
