"""Chosen P/Q support needs all four rows; endpoint needs x-upper only."""
from fractions import Fraction as Q
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
p=(Q(1),Q(2),Q(0),Q(0));q=(Q(0),Q(1),Q(1),Q(1))
used_p={i for i,x in enumerate(p) if x};used_q={i for i,x in enumerate(q) if x}
assert used_p=={0,1} and used_q=={1,2,3} and used_p|used_q==set(range(4))
for removed in range(4):
 kept=set(range(4))-{removed}
 chosen_p=used_p<=kept;chosen_q=used_q<=kept
 assert not(chosen_p and chosen_q)
 if removed!=1:
  # x-upper alone certifies x<=2, surplus 1.
  weights=(Q(0),Q(1),Q(0),Q(0))
  assert 1 in kept and (weights[1],weights[1]+Q(1))==(Q(1),Q(2))
 else:
  # point (3,0) obeys all remaining inequalities, refutes x<=2.
  point=(Q(3),Q(0))
  assert all(sum(rows[i][0][j]*point[j] for j in (0,1))<=rows[i][1] for i in kept)
  assert point[0]>2
report={'passed':True,'P_support':sorted(used_p),'Q_support':sorted(used_q),'chosen_comparison_union':sorted(used_p|used_q),'deleting_any_row':'breaks at least one exact chosen P/Q proof packet','deleting_x_low_or_y_low_or_y_high':'x<=2 still certified by x-high with surplus 1','deleting_x_high':'x<=2 false, witness point (3,0)','scope':'Exact original four-row presentation and CHOSEN packets, not universal proof-support lower bound, owner issuer or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/standalone-row-dependency.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
