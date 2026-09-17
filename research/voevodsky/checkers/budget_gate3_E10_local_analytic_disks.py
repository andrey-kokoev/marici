#!/usr/bin/env python3
"""Local radius-1e-5 no-pole disk budgets for recursive E10 pivots."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';d=json.loads((root/'complex_schur_ellipse_L0649_L065_rho10_scout128.json').read_text());r=d['samples'];z=[complex(x['L_real'],x['L_imag']) for x in r];rad=1e-5;rows=[]
for k in range(17):
 p=[complex(x['strong_ldl_pivot_real'][k],x['strong_ldl_pivot_imag'][k]) for x in r];sec=max(abs((p[(i+1)%128]-p[i])/(z[(i+1)%128]-z[i])) for i in range(128));mn=min(abs(x) for x in p);target=4*sec;rows.append({'pivot':k,'sampled_min':mn,'maximum_secant_derivative':sec,'adopted_derivative_target':target,'disk_variation':target*rad,'conditional_disk_floor':mn-target*rad,'passes':mn>target*rad})
p17max=max(abs(complex(x['strong_ldl_pivot_real'][17],x['strong_ldl_pivot_imag'][17])) for x in r);p17der=.04188;p17disk=p17max+p17der*rad;out={'schema':'marici.voevodsky.gate3-E10-local-analytic-disks.v1','disk_radius':rad,'pivots_0_16':rows,'minimum_conditional_disk_floor':min(x['conditional_disk_floor'] for x in rows),'pivot17_disk_magnitude_bound':p17disk,'required_pivot17_bound':1.0,'passed_conditionally':all(x['passes'] for x in rows) and p17disk<1,'passed':False,'remaining':'direct interval derivative bounds at adopted four-times-secant targets for pivots 0-16','rh_proved':False};p=root/'gate3_E10_local_analytic_disks.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
