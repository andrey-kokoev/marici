#!/usr/bin/env python3
"""Wide theta-disk Cauchy budget using uncancelled Gram terms."""
import json,math,glob
from pathlib import Path
root=Path(__file__).parents[1]/'results';rows=[]
for f in glob.glob(str(root/'gate3_complex_physical_residual_E21_rho2.696529_*.json')):rows.append(json.loads(Path(f).read_text()))
mg=max(x['physical_gram_norm'] for x in rows);mp=max(x['projected_source_gram_norm'] for x in rows);r=.25;M=8.;d4=24*M/r**4;out={'schema':'marici.voevodsky.gate3-residual-wide-cauchy-triangle.v1','theta_radius':r,'outer_rho':2.1*math.exp(r),'sampled_physical_gram_max':mg,'sampled_projected_gram_max':mp,'adopted_uniform_component_bounds':[4.,4.],'residual_norm_bound_by_triangle':M,'cauchy_fourth_derivative_bound':d4,'required_fourth_derivative_bound':60000.,'passed_conditionally':d4<60000.,'passed':False,'conditions':['physical Gram norm <=4 on theta strip','projected source Gram norm <=4 on theta strip'],'rh_proved':False};p=root/'gate3_residual_wide_cauchy_triangle.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
