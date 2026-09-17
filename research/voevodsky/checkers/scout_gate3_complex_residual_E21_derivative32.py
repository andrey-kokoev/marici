#!/usr/bin/env python3
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';h=.01;rows=[]
def get(x):return np.load(root/f'gate3_complex_physical_residual_E21_theta{x:.6f}.npz')['residual_gram']
for j in range(32):
 t=j*math.pi/16;der=(get(t+h)-get(t-h))/(2*h);rows.append({'index':j,'theta':t,'norm':float(np.linalg.norm(der,2))})
mx=max(x['norm'] for x in rows);second=.2;half=math.pi/32;covered=mx+second*half;out={'schema':'marici.voevodsky.gate3-complex-residual-E21-derivative32.v1','nodes':32,'maximum_direct_derivative':mx,'adopted_second_derivative_bound':second,'half_arc':half,'conditional_global_derivative_bound':covered,'required_global_derivative_bound':.12,'passed_conditionally':covered<.12,'passed':False,'remaining':'direct global second-derivative bound and finite-difference error','rh_proved':False};p=root/'gate3_complex_residual_E21_derivative32.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
