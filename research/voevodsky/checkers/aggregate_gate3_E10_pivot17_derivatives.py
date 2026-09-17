#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';rows=[]
for a in range(0,128,8):rows+=json.loads((root/f'gate3_E10_pivot17_derivative_chunk_{a}_{min(a+8,128)}.json').read_text())['rows']
out={'schema':'marici.voevodsky.gate3-E10-pivot17-direct-derivative-scout.v1','nodes':128,'maximum_direct_five_point_derivative':max(x['derivative_abs'] for x in rows),'minimum_direct_five_point_derivative':min(x['derivative_abs'] for x in rows),'required_bound':.04188,'reserve_factor':.04188/max(x['derivative_abs'] for x in rows),'passed_scout':max(x['derivative_abs'] for x in rows)<.04188,'passed':False,'remaining':'direct five-point truncation, source quadrature, and inter-node derivative variation bounds','rh_proved':False};p=root/'gate3_E10_pivot17_direct_derivative_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
