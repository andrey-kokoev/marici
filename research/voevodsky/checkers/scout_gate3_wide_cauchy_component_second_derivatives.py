#!/usr/bin/env python3
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';rho=2.696529;h=.01;rows=[]
def get(t):return np.load(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta{t:.6f}.npz')
for j in range(16):
 t=j*math.pi/8;a=get(t-h);b=get(t);c=get(t+h);rows.append({'theta':t,'physical':float(np.linalg.norm((c['physical_gram']-2*b['physical_gram']+a['physical_gram'])/h**2,2)),'projected':float(np.linalg.norm((c['projected_source_gram']-2*b['projected_source_gram']+a['projected_source_gram'])/h**2,2))})
mg=max(x['physical'] for x in rows);mp=max(x['projected'] for x in rows);out={'schema':'marici.voevodsky.gate3-wide-cauchy-component-second-derivatives.v1','rows':rows,'maxima':[mg,mp],'passed_scout':mg<10 and mp<60,'passed':False,'rh_proved':False};p=root/'gate3_wide_cauchy_component_second_derivatives.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
