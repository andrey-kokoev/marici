#!/usr/bin/env python3
"""4096-ulp endpoint-moment perturbation budget on E10."""
import json,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import iv
root=Path(__file__).parents[1]/'results';A=np.load(root/'gamma_floor_L065_rank1000_midpoint.npz')['matrix'];e,W=np.linalg.eigh(A);W=np.column_stack((W[:,1:20],W[:,0]));o=np.arange(1000);eps=4096*2**-53;rows=[]
for th in (0,np.pi/2,np.pi,3*np.pi/2):
 z=.5*(10*np.exp(1j*th)+.1*np.exp(-1j*th));L=.6495+.0005*z;x=L/2;ap=np.array([2*L*np.sqrt((2*n+1)/(2*L))*np.sqrt(np.pi/(2*x))*iv(n+.5,x) for n in o]);am=ap*((-1.)**o);a=ap@W;m=am@W;ea=eps*(np.abs(ap)@np.abs(W));em=eps*(np.abs(am)@np.abs(W));err=np.linalg.norm(a)*np.linalg.norm(em)+np.linalg.norm(m)*np.linalg.norm(ea)+np.linalg.norm(ea)*np.linalg.norm(em);rows.append({'theta':float(th),'endpoint_block_error':float(err)})
out={'schema':'marici.voevodsky.gate3-E10-endpoint-roundoff.v1','bessel_ulp_reserve':4096,'rows':rows,'maximum_endpoint_block_error':max(x['endpoint_block_error'] for x in rows),'strong_block_error_target':1e-8,'passed_scout':max(x['endpoint_block_error'] for x in rows)<1e-8,'passed':False,'remaining':'ordinary matrix arithmetic and all-arc promotion','rh_proved':False};p=root/'gate3_E10_endpoint_roundoff.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
