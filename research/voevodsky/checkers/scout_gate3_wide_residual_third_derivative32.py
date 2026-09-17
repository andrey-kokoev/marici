#!/usr/bin/env python3
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';rho=2.696529;h=.01;rows=[]
def g(t):return np.load(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta{t:.6f}.npz')['residual_gram']
for j in range(32):
 t=j*math.pi/16;M=(g(t+2*h)-2*g(t+h)+2*g(t-h)-g(t-2*h))/(2*h**3);rows.append(float(np.linalg.norm(M,2)))
mx=max(rows);out={'schema':'marici.voevodsky.gate3-wide-residual-third-derivative32.v1','step':h,'maximum':mx,'target':6800.,'passed_scout':mx<6800,'passed':False,'remaining':'third-difference truncation and physical quadrature/roundoff error','rh_proved':False};p=root/'gate3_wide_residual_third_derivative32.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
