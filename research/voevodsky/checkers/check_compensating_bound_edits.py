"""Zero signed comparison after edits can mask invalid endpoint proof packets."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
new=(((-1,0),0),((1,0),2),((0,-1),0),((0,1),2))
p=(Q(1),Q(2),Q(0),Q(0));q=(Q(0),Q(1),Q(1),Q(1));k=tuple(q[i]-p[i] for i in range(4))
def value(rows,m,c=Q(0)):
 return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))+c
assert value(old,p)==value(old,q)==((Q(1),Q(0)),Q(2))
assert value(new,k)==((Q(0),Q(0)),Q(0))
assert value(new,p)==value(new,q)==((Q(1),Q(0)),Q(4))
assert Q(2)-value(new,p)[1]==Q(-2) # nonnegative-surplus rule blocks target2
# Endpoint x<=2 remains true on edited square (x-upper itself is x<=2).
single=(Q(0),Q(1),Q(0),Q(0))
assert value(new,single)==((Q(1),Q(0)),Q(2))
assert sha256(repr(old).encode()).digest()!=sha256(repr(new).encode()).digest()
report={'passed':True,'edits':'x-upper and y-upper bounds each 1->2','old_signed_delta':'still zero normal and bound by cancellation','old_P_Q':'both now normal(1,0), implied bound4; target bound2 requires invalid surplus -2','endpoint':'x<=2 still valid via edited x-upper alone','full_manifest':'changed; no issuer rebind','scope':'Frozen chosen proof packets and target; comparison-only zero test insufficient, not historical proof transport or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/compensating-bound-edits.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
