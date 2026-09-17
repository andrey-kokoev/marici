#!/usr/bin/env python3
import glob,json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree32_residual_gram_family_L0649_L065.npz')['coefficients'];rows=[]
for f in glob.glob(str(root/'gate3_complex_physical_residual_E21_rho*.json')):
 d=json.loads(Path(f).read_text());r=d['rho'];t=d['theta'];z=(r*np.exp(1j*t)+r**-1*np.exp(-1j*t))/2;M=np.load(str(f).replace('.json','.npz'))['residual_gram'];E=M-np.polynomial.chebyshev.chebval(z,C);rows.append({'rho':r,'theta':t,'discrepancy_norm':float(np.linalg.norm(E,2))})
mx=max(x['discrepancy_norm'] for x in rows);out={'schema':'marici.voevodsky.gate3-physical-minus-polynomial-annulus.v1','rows':rows,'maximum_scout':mx,'available_remainder_budget':.978,'reserve_factor':.978/mx,'passed_scout':mx<.978,'passed':False,'remaining':'direct uniform physical-minus-polynomial bound on annulus','rh_proved':False};p=root/'gate3_physical_minus_polynomial_annulus.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
