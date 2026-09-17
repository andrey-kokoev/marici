#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';old={}
for a in range(0,128,8):
 for x in json.loads((root/f'gate3_E10_pivot17_derivative_chunk_{a}_{a+8}.json').read_text())['rows']:old[x['index']]=x['derivative_abs']
new={}
for a in range(0,128,16):
 for x in json.loads((root/f'gate3_E10_pivot17_derivative_chunk_{a}_{a+16}_h5e-08.json').read_text())['rows']:new[x['index']]=x['derivative_abs']
d=[abs(old[i]-new[i]) for i in range(128)];mx=max(new.values());out={'schema':'marici.voevodsky.gate3-E10-derivative-step-halving.v1','steps':[1e-7,5e-8],'maximum_absolute_change':max(d),'maximum_relative_change':max(d[i]/max(new[i],1e-300) for i in range(128)),'maximum_half_step_derivative':mx,'required_bound':.04188,'roundoff_and_truncation_allocation':.005,'observed_change_to_allocation':max(d)/.005,'passed_scout':mx+.005<.04188,'passed':False,'remaining':'analytic fifth-derivative truncation and floating source-evaluation roundoff bounds','rh_proved':False};p=root/'gate3_E10_derivative_step_halving.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
