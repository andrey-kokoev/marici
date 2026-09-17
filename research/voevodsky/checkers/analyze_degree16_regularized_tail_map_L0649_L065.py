#!/usr/bin/env python3
"""Degree-16 regularized tail-map interpolation and rho=4 ellipse scout."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';even=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');odd=np.load(root/'regularized_union_tail_maps_L0649_L065_degree16_extra.npz');D=np.empty((17,1000,40));S=np.empty((17,40,40));D[0::2]=even['tail_maps'];D[1::2]=odd['tail_maps'];S[0::2]=even['schur'];S[1::2]=odd['schur'];t=np.cos(np.arange(16,-1,-1)*np.pi/16);cD=np.polynomial.chebyshev.chebfit(t,D.reshape(17,-1),16).reshape(17,1000,40);dn=[float(np.linalg.norm(x,2)) for x in cD];rho=4.;mx=0
for th in np.linspace(0,2*np.pi,257)[:-1]:
 z=.5*(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th));mx=max(mx,float(np.linalg.norm(np.polynomial.chebyshev.chebval(z,cD),2)))
out={'schema':'marici.voevodsky.degree16-regularized-tail-map-L0649-L065.v1','coefficient_norms':dn,'high_degree_sum_9_to16':sum(dn[9:]),'rho4_interpolant_maximum_norm_256_samples':mx,'target_true_norm':1.0,'passed':mx<1.0,'status':'floating degree-16 interpolant; true analytic remainder remains directed-condition','rh_proved':False};p=root/'degree16_regularized_tail_map_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'degree16_regularized_tail_map_L0649_L065.npz',coefficients=cD);print(json.dumps(out,indent=2));assert out['passed']
