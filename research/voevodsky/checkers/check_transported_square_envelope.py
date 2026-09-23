"""Positive row transport needs a coordinate-wise grid, not raw caps."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
perm=(3,1,0,2);scale=(Q(2),Q(1,4),Q(3),Q(1))
new=tuple((tuple(s*x for x in old[i][0]),s*old[i][1]) for i,s in zip(perm,scale))
grid=tuple(Q(k,2) for k in range(5));target=((Q(1),Q(1)),Q(3))
def image(rows,m,c):return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))+c
def packets(rows,grids):
 out=set()
 for m in product(*grids):
  c=target[1]-sum(rows[i][1]*m[i] for i in range(4))
  if c in grid and image(rows,m,c)==target:out.add((m,c))
 return out
source=packets(old,(grid,)*4)
transport=lambda p:(tuple(p[0][i]/s for i,s in zip(perm,scale)),p[1])
expected={transport(p) for p in source}
transported_grids=tuple(tuple(x/s for x in grid) for s in scale)
actual=packets(new,transported_grids)
raw=packets(new,(grid,)*4)
assert source and actual==expected
lost=expected-raw
assert lost
assert all(image(new,*p)==target for p in lost)
assert transport(((Q(0),Q(1),Q(0),Q(1)),Q(1))) in lost
assert all(x in transported_grids[i] for p in expected for i,x in enumerate(p[0]))
report={'passed':True,'source_envelope_packets':len(source),'transported_envelope_packets':len(actual),'raw_grid_packets':len(raw),'valid_transported_packets_lost_by_raw_grid':len(lost),'example_lost_packet':{'multipliers':list(map(str,sorted(lost)[0][0])),'surplus':str(sorted(lost)[0][1])},'scale':list(map(str,scale)),'permutation':list(perm),'scope':'Exact bounded rational grid covariance for fixed old square row isomorphism. Raw-grid loss is catalogue drift, not loss of mathematical proof or source authority.'}
out=Path(__file__).resolve().parents[1]/'results/transported-square-envelope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
