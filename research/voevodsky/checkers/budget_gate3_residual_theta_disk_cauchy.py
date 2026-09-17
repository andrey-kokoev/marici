#!/usr/bin/env python3
"""Theta-strip Cauchy budget for the physical residual fourth derivative."""
import glob,json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results';rows=[]
for f in glob.glob(str(root/'gate3_complex_physical_residual_E21_rho*.json')):rows.append(json.loads(Path(f).read_text()))
mx=max(x['residual_gram_norm'] for x in rows);radius=.15;M=1.;fourth=24*M/radius**4;out={'schema':'marici.voevodsky.gate3-residual-theta-disk-cauchy.v1','theta_disk_radius':radius,'annulus_rho_range':[2.1*math.exp(-radius),2.1*math.exp(radius)],'sampled_annulus_extreme_max':mx,'adopted_full_annulus_residual_norm_bound':M,'sample_to_target_reserve':M/mx,'cauchy_fourth_derivative_bound':fourth,'required_fourth_derivative_bound':60000.,'passed_conditionally':fourth<60000.,'passed':False,'remaining':'direct full-annulus norm bound <=1 and tail-map no-pole certificate on rho<=2.44','rh_proved':False};p=root/'gate3_residual_theta_disk_cauchy.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
