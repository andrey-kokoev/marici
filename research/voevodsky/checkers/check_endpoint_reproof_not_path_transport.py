"""Delete x-low: x<=2 still true, but original P/Q comparison does not transport."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1));new=old[1:]
p=(Q(1),Q(2),Q(0),Q(0));q=(Q(0),Q(1),Q(1),Q(1));old_delta=tuple(q[i]-p[i] for i in range(4))
def value(rows,m,c=Q(0)):
 return tuple(sum(rows[i][0][j]*m[i] for i in range(len(m))) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(len(m)))+c
assert value(old,p)==value(old,q)==((Q(1),Q(0)),Q(2)) and value(old,old_delta)==((0,0),0)
assert p[0] and old_delta[0] # forbidden deleted-row coefficient
q_new=(Q(1),Q(1),Q(1));reproof=(Q(1),Q(0),Q(0))
assert value(new,q_new)==value(new,reproof,Q(1))==((Q(1),Q(0)),Q(2))
new_delta=tuple(q_new[i]-reproof[i] for i in range(3))
assert value(new,new_delta,Q(-1))==((0,0),0)
# Naively drop the deleted coordinate from the old signed comparison: nonzero normal.
assert value(new,old_delta[1:])!=((0,0),0)
def digest(rows):return sha256(repr(rows).encode()).hexdigest()
assert digest(old)!=digest(new)
report={'passed':True,'removed_row':'x-low','endpoint':'x<=2 remains provable','old_P_and_comparison':'invalid due to deleted nonzero row coefficient','new_reproof':'x-high with multiplier1 and surplus1','new_signed_delta':{'rows':list(map(str,new_delta)),'surplus':'-1'},'naive_old_delta_restriction':'not zero-normal/bound','different_manifest':True,'scope':'Reproof is a new local mathematical path, not transport of old history, source owner permission or analytic role functor.'}
out=Path(__file__).resolve().parents[1]/'results/endpoint-reproof-not-path-transport.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
