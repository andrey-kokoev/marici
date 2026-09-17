#!/usr/bin/env python3
import json,math
from pathlib import Path
import sys
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';h=.01;centers=[j*math.pi/4 for j in range(8)];rows=[]
for t in centers:
 def get(x):return np.load(root/f'gate3_complex_physical_residual_E21_theta{x:.6f}.npz')['residual_gram']
 der=(get(t+h)-get(t-h))/(2*h);rows.append({'theta':t,'direct_central_derivative_norm':float(np.linalg.norm(der,2))})
mx=max(x['direct_central_derivative_norm'] for x in rows);target=.1;out={'schema':'marici.voevodsky.gate3-complex-residual-E21-direct-derivative.v1','step_theta':h,'rows':rows,'maximum':mx,'adopted_derivative_target':target,'reserve_factor':target/mx,'passed_scout':mx<target,'passed':False,'remaining':'truncation, evaluation roundoff, and between-quadrant derivative variation','rh_proved':False};p=root/'gate3_complex_residual_E21_direct_derivative.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
