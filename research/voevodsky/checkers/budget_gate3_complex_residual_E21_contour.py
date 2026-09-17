#!/usr/bin/env python3
"""Contour-cover budget for the complex physical residual Gram on E2.1."""
import json,math,glob,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree32_residual_gram_family_L0649_L065.npz')['coefficients'];Cd=np.polynomial.chebyshev.chebder(C,axis=0);rho=2.1;md=0
for j in range(4096):
 th=2*math.pi*j/4096;z=(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th))/2;zp=.5j*(rho*np.exp(1j*th)-rho**-1*np.exp(-1j*th));md=max(md,float(np.linalg.norm(np.polynomial.chebyshev.chebval(z,Cd)*zp,2)))
samples=[]
for f in glob.glob(str(root/'gate3_complex_physical_residual_E21_theta*.json')):samples.append(json.loads(Path(f).read_text())['residual_gram_norm'])
mx=max(samples);half=math.pi/4;target=json.loads((root/'gate3_residual_gram_E21_budget.json').read_text())['maximum_admissible_full_residual_gram_norm'];covered=mx+md*half;out={'schema':'marici.voevodsky.gate3-complex-residual-E21-contour-budget.v1','quadrant_samples':len(samples),'maximum_sampled_norm':mx,'degree32_theta_derivative_scout':md,'four_node_half_arc':half,'conditional_contour_bound':covered,'allowed_bound':target,'passed_conditionally':covered<target,'passed':False,'remaining':'direct derivative bound for true complex physical residual family','rh_proved':False};p=root/'gate3_complex_residual_E21_contour_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
