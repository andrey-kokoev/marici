#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';rows=[]
for a in range(0,128,16):rows+=json.loads((root/f'gate3_E10_all_pivot_derivative_chunk_{a}_{a+16}.json').read_text())['rows']
target=json.loads((root/'gate3_E10_local_analytic_disks.json').read_text())['pivots_0_16'];mx=[max(x['derivative_abs'][k] for x in rows) for k in range(18)];items=[{'pivot':k,'maximum_direct_derivative':mx[k],'adopted_target':target[k]['adopted_derivative_target'],'reserve_factor':target[k]['adopted_derivative_target']/mx[k]} for k in range(17)];out={'schema':'marici.voevodsky.gate3-E10-all-pivot-direct-derivatives.v1','nodes':128,'rows':items,'minimum_reserve_factor':min(x['reserve_factor'] for x in items),'pivot17_maximum':mx[17],'passed_scout':all(x['maximum_direct_derivative']<x['adopted_target'] for x in items),'passed':False,'remaining':'direct truncation and evaluation-error promotion for pivots 0-16','rh_proved':False};p=root/'gate3_E10_all_pivot_direct_derivatives.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
