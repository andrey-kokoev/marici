#!/usr/bin/env python3
import glob,json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';rho=2.696529;h=.01;ds=[]
def get(t):return np.load(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta{t:.6f}.npz')['residual_gram']
for j in range(32):
 t=j*math.pi/16;ds.append(float(np.linalg.norm((get(t+h)-get(t-h))/(2*h),2)))
js=[json.loads(Path(f).read_text()) for f in glob.glob(str(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta*.json'))];sm=max(x['residual_gram_norm'] for x in js);targetd=7.5;radius=max(h,math.pi/32-h);covered=sm+targetd*radius;out={'schema':'marici.voevodsky.gate3-wide-residual-cover32.v1','sampled_residual_norm_max':sm,'sampled_derivative_max':max(ds),'adopted_global_derivative_bound':targetd,'cover_radius':radius,'covered_residual_norm':covered,'cauchy_norm_target':1.,'passed_conditionally':covered<1,'passed':False,'remaining':'promote global residual derivative <=7.5 and evaluation error','rh_proved':False};p=root/'gate3_wide_residual_cover32.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
