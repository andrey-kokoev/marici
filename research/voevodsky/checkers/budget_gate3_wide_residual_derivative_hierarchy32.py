#!/usr/bin/env python3
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';rho=2.696529;h=.01;d1=[];d2=[];norms=[]
def get(t):return np.load(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta{t:.6f}.npz')['residual_gram']
for j in range(32):
 t=j*math.pi/16;a=get(t-h);b=get(t);c=get(t+h);norms.append(np.linalg.norm(b,2));d1.append(np.linalg.norm((c-a)/(2*h),2));d2.append(np.linalg.norm((c-2*b+a)/h**2,2))
third=5000.;second=max(d2)+third*math.pi/32;first=max(d1)+second*math.pi/32;res=max(norms)+first*math.pi/32;d4=24*8/.25**4;out={'schema':'marici.voevodsky.gate3-wide-residual-derivative-hierarchy32.v1','sampled_maxima':{'residual':float(max(norms)),'first':float(max(d1)),'second':float(max(d2))},'adopted_global_third_derivative':third,'covered_second_derivative':float(second),'covered_first_derivative':float(first),'covered_residual':float(res),'adopted_cauchy_norm':8.,'cauchy_fourth_derivative_bound':d4,'required_fourth_derivative_bound':60000.,'passed_conditionally':res<8 and d4<60000,'passed':False,'remaining':'promote global third derivative <=5000 and finite-difference evaluation errors','rh_proved':False};p=root/'gate3_wide_residual_derivative_hierarchy32.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
