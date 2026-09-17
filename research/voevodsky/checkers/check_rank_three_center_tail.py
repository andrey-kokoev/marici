#!/usr/bin/env python3
"""Propagate source tails to the rank-three center determinant."""
import json,re
from pathlib import Path
R=Path(__file__).parents[1]/'results';cell=json.loads((R/'rank_two_second_order_cell.json').read_text());tails=json.loads((R/'rank_two_second_order_cell_tails.json').read_text())
def lower(s):return float(re.match(r'\[([^ ]+)',s).group(1))
d=lower(cell['rank3_center_determinant']);M=cell['moment_absolute_upper'];e=tails['maximum_moment_tail']
# Five determinant monomials, total coefficient mass six. The factor 20 safely
# dominates all one-tail placements; 20 M e^2 + 20 e^3 covers higher placements.
err=20*M*M*e+20*M*e*e+20*e**3;lb=d-err
out={'schema':'marici.voevodsky.rank-three-center-tail.v1','t':sum(cell['interval'])/2,'finite_core_det_lower':d,
 'moment_absolute_upper':M,'maximum_moment_tail':e,'determinant_tail_error':err,'complete_det_lower':lb,
 'complete_rank_three_point_positive':lb>0,'passed':lb>0,'rh_proved':False,
 'scope':'One rank-three point only; no interval, all-time, all-rank, or Hardy co-defect claim.'}
p=R/'rank_three_center_tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
