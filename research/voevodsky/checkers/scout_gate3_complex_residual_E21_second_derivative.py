#!/usr/bin/env python3
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';h=.01;rows=[]
def get(x):return np.load(root/f'gate3_complex_physical_residual_E21_theta{x:.6f}.npz')['residual_gram']
for j in range(8):
 t=j*math.pi/4;M=(get(t+h)-2*get(t)+get(t-h))/(h*h);rows.append({'theta':t,'direct_second_derivative_norm':float(np.linalg.norm(M,2))})
mx=max(x['direct_second_derivative_norm'] for x in rows);out={'schema':'marici.voevodsky.gate3-complex-residual-E21-second-derivative.v1','step':h,'rows':rows,'maximum':mx,'adopted_bound':.2,'reserve_factor':.2/mx,'passed_scout':mx<.2,'passed':False,'remaining':'finite-difference truncation/evaluation error and between-node second-derivative variation','rh_proved':False};p=root/'gate3_complex_residual_E21_second_derivative.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
