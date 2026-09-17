#!/usr/bin/env python3
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results';d=json.loads((root/'gate3_complex_residual_E21_direct_derivative.json').read_text());# Norm-only differences give a lower diagnostic; use polynomial matrix second derivative for target calibration.
import sys
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
C=np.load(root/'degree32_residual_gram_family_L0649_L065.npz')['coefficients'];C1=np.polynomial.chebyshev.chebder(C,axis=0);C2=np.polynomial.chebyshev.chebder(C1,axis=0);rho=2.1;mx2=0
for j in range(4096):
 th=2*math.pi*j/4096;z=(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th))/2;zp=.5j*(rho*np.exp(1j*th)-rho**-1*np.exp(-1j*th));zpp=-.5*(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th));M=np.polynomial.chebyshev.chebval(z,C2)*zp*zp+np.polynomial.chebyshev.chebval(z,C1)*zpp;mx2=max(mx2,float(np.linalg.norm(M,2)))
first=max(x['direct_central_derivative_norm'] for x in d['rows']);target2=.2;half=math.pi/8;covered=first+target2*half;out={'schema':'marici.voevodsky.gate3-complex-residual-derivative-cover.v1','sampled_first_derivative_max':first,'degree32_second_derivative_scout':mx2,'adopted_true_second_derivative_bound':target2,'eight_node_half_arc':half,'covered_first_derivative_bound':covered,'required_first_derivative_bound':.12,'passed_conditionally':covered<.12,'passed':False,'remaining':'direct second-derivative and central-difference error bounds','rh_proved':False};p=root/'gate3_complex_residual_derivative_cover.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
