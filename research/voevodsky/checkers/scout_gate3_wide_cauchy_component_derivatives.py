#!/usr/bin/env python3
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';rho=2.696529;h=.01;rows=[]
def get(t):return np.load(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta{t:.6f}.npz')
for j in range(8):
 t=j*math.pi/4;a=get(t-h);b=get(t+h);rows.append({'theta':t,'physical_derivative':float(np.linalg.norm((b['physical_gram']-a['physical_gram'])/(2*h),2)),'projected_derivative':float(np.linalg.norm((b['projected_source_gram']-a['projected_source_gram'])/(2*h),2))})
mx=max(max(x['physical_derivative'],x['projected_derivative']) for x in rows);out={'schema':'marici.voevodsky.gate3-wide-cauchy-component-derivatives.v1','rows':rows,'maximum':mx,'required_global_derivative_for_bound4':(4-3.546)/(math.pi/8),'passed_scout':mx<(4-3.546)/(math.pi/8),'passed':False,'remaining':'global derivative promotion and evaluation error','rh_proved':False};p=root/'gate3_wide_cauchy_component_derivatives.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
