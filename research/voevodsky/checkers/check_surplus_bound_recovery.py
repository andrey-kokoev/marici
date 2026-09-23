"""Exact target bound recovers surplus; erasing both leaves ambiguity."""
from fractions import Fraction as Q
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
m=(Q(0),Q(1),Q(0),Q(1));normal=(Q(1),Q(1))
def reconstruct(target_bound):
 if target_bound is None:raise ValueError('BOUND_AND_SURPLUS_UNDERDETERMINED')
 c=Q(target_bound)-sum(m[i]*rows[i][1] for i in range(4))
 if c<0:raise ValueError('NEGATIVE_SURPLUS')
 return c
assert reconstruct(Q(3))==Q(1)
assert [(b,reconstruct(b)) for b in (Q(2),Q(3),Q(4))]==[(Q(2),Q(0)),(Q(3),Q(1)),(Q(4),Q(2))]
assert tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1))==normal
try:reconstruct(None)
except ValueError as err:assert str(err)=='BOUND_AND_SURPLUS_UNDERDETERMINED'
else:raise AssertionError('missing bound invented')
try:reconstruct(Q(1))
except ValueError as err:assert str(err)=='NEGATIVE_SURPLUS'
else:raise AssertionError('negative surplus accepted')
report={'passed':True,'source_row_bound_sum':'2','retained_target_bound_3_recovers_surplus':'1','erased_surplus_and_bound':'at least three valid distinct (bound,surplus) completions: (2,0),(3,1),(4,2)','bound_1':'NEGATIVE_SURPLUS','scope':'Same frozen row manifest, multiplier tuple and normal. Surplus is redundant given exact target bound, but bound+surplus jointly erased is underdetermined; no issuer or analytic roles.'}
out=Path(__file__).resolve().parents[1]/'results/surplus-bound-recovery.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
