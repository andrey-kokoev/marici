#!/usr/bin/env python3
import glob,json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';rho=2.696529;h=.01;ders=[]
def get(t):return np.load(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta{t:.6f}.npz')
for j in range(16):
 t=j*math.pi/8;a=get(t-h);b=get(t+h);ders.append((np.linalg.norm((b['physical_gram']-a['physical_gram'])/(2*h),2),np.linalg.norm((b['projected_source_gram']-a['projected_source_gram'])/(2*h),2)))
js=[json.loads(Path(f).read_text()) for f in glob.glob(str(root/f'gate3_complex_physical_residual_E21_rho{rho:.6f}_theta*.json'))];mg=max(x['physical_gram_norm'] for x in js);mp=max(x['projected_source_gram_norm'] for x in js);dg=max(x[0] for x in ders);dp=max(x[1] for x in ders);spacing=math.pi/16+h;bg=mg+1.5*spacing;bp=mp+7.5*spacing;total=bg+bp;d4=24*total/.25**4;out={'schema':'marici.voevodsky.gate3-wide-cauchy-component-cover16.v1','sampled_component_maxima':[mg,mp],'sampled_derivative_maxima':[dg,dp],'adopted_global_derivative_bounds':[1.5,7.5],'cover_radius':spacing,'covered_component_bounds':[bg,bp],'covered_sum':total,'cauchy_fourth_derivative_bound':d4,'required_fourth_derivative_bound':60000.,'passed_conditionally':d4<60000.,'passed':False,'conditions':['promote component derivative bounds 1.5 and 7.5','evaluation error <=1e-8'],'rh_proved':False};p=root/'gate3_wide_cauchy_component_cover16.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
