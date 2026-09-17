#!/usr/bin/env python3
"""4096-ulp special-function perturbation budget for projected frequency block on E10."""
import json,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn
 from numpy.polynomial.legendre import leggauss
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn
 from numpy.polynomial.legendre import leggauss
root=Path(__file__).parents[1]/'results';Aend=np.load(root/'gamma_floor_L065_rank1000_midpoint.npz')['matrix'];ev,W=np.linalg.eigh(Aend);W=np.column_stack((W[:,1:20],W[:,0]));o=np.arange(1000);zg,wg=leggauss(140);eps=4096*2**-53;rows=[]
for th in (0,np.pi/2,np.pi,3*np.pi/2):
 z=.5*(10*np.exp(1j*th)+.1*np.exp(-1j*th));L=.6495+.0005*z;norm=2*L*np.sqrt((2*o+1)/(2*L));ph=(-1.)**(o//2);err=0
 for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
  u=(aa+bb)/2+(bb-aa)*zg/2;ww=(bb-aa)*wg/2;V=(norm[:,None]*ph[:,None]*spherical_jn(o[:,None],L*u[None,:])).T;q=(digamma(.25+.5j*u).real-np.log(np.pi))/2;X=np.zeros((len(u),20),complex);E=np.zeros_like(X)
  X[:,0::2]=V[:,0::2]@W[0::2,0::2];X[:,1::2]=V[:,1::2]@W[1::2,1::2];E[:,0::2]=eps*(np.abs(V[:,0::2])@np.abs(W[0::2,0::2]));E[:,1::2]=eps*(np.abs(V[:,1::2])@np.abs(W[1::2,1::2]));weight=np.abs(ww*(q-1.841791592392184)/np.pi);sx=np.linalg.norm(np.sqrt(weight)[:,None]*X,2);se=np.linalg.norm(np.sqrt(weight)[:,None]*E,2);err+=2*sx*se+se*se
 rows.append({'theta':float(th),'frequency_block_error':float(err)})
out={'schema':'marici.voevodsky.gate3-E10-frequency-special-roundoff.v1','special_function_ulp_reserve':4096,'rows':rows,'maximum_frequency_block_error':max(x['frequency_block_error'] for x in rows),'strong_block_error_target':1e-8,'passed_scout':max(x['frequency_block_error'] for x in rows)<1e-8,'passed':False,'remaining':'prime recurrence/matmul, endpoint Bessel, ordinary arithmetic, and all-arc promotion','rh_proved':False};p=root/'gate3_E10_frequency_special_roundoff.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
