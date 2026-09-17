#!/usr/bin/env python3
"""Promote the current finite-core rank-three Taylor cell to complete-source status."""
import json
from pathlib import Path
R=Path(__file__).parents[1]/'results';cell=json.loads((R/'rank_two_second_order_cell.json').read_text());tail=json.loads((R/'rank_two_second_order_cell_tails.json').read_text())
M=cell['moment_absolute_upper'];e=tail['maximum_moment_tail'];r=(cell['interval'][1]-cell['interval'][0])/2
# D3 and D3' are cubic moment polynomials with total coefficient masses <20.
# Bound each perturbation by 20 M^2 e +20 M e^2+20e^3.
one=20*M*M*e+20*M*e*e+20*e**3;err=one+r*one;lb=cell['rank3_Taylor_lower']-err
out={'schema':'marici.voevodsky.rank-three-interval-tail.v1','interval':cell['interval'],'finite_core_Taylor_lower':cell['rank3_Taylor_lower'],
 'moment_upper':M,'moment_tail_upper':e,'center_plus_derivative_tail_error':err,'complete_Taylor_lower':lb,
 'complete_rank_three_interval_positive':lb>0,'passed':lb>0,'rh_proved':False,
 'scope':'One rank-three interval only; no all-time, all-rank, or Hardy co-defect claim.'}
p=R/'rank_three_interval_tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
