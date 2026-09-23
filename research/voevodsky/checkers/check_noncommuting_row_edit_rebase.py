"""Distinct row-bound edits can exhaust a shared proof-surplus budget."""
from fractions import Fraction as Q
from pathlib import Path
import json
base=(((-1,0),Q(0)),((1,0),Q(1)),((0,-1),Q(0)),((0,1),Q(1)))
a=base[:1]+(((1,0),Q(7,4)),)+base[2:]
b=base[:3]+(((0,1),Q(7,4)),)
ab=a[:3]+(((0,1),Q(7,4)),)
weights=(Q(0),Q(1),Q(1),Q(1));target=Q(3)
def surplus(rows):
 assert tuple(sum(rows[i][0][j]*weights[i] for i in range(4)) for j in (0,1))==(Q(1),Q(0))
 return target-sum(rows[i][1]*weights[i] for i in range(4))
assert surplus(base)==Q(1) and surplus(a)==surplus(b)==Q(1,4)
assert surplus(ab)==Q(-1,2)
assert all(surplus(x)>=0 for x in (a,b)) and surplus(ab)<0
# After A wins, B cannot be rebased while preserving this required Q packet.
# Target x<=3 itself survives via x-upper bound 7/4 plus 5/4 surplus.
assert target-a[1][1]==Q(5,4)
report={'passed':True,'target':'x<=3','required_Q_packet':'multipliers (0,1,1,1)','base_surplus':'1','A_x_upper_plus_3_4_surplus':'1/4','B_y_upper_plus_3_4_surplus':'1/4','combined_surplus':'-1/2; REBASE_PROOF_INVALID','endpoint':'still locally provable via x-upper alone','scope':'Pure rational candidate validation, no actual edited source or issuer/analytic authorization.'}
out=Path(__file__).resolve().parents[1]/'results/noncommuting-row-edit-rebase.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
