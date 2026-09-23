"""Positive monomial row presentation changes transport exact Farkas paths."""
from fractions import Fraction as Q
from itertools import permutations,product
from hashlib import sha256
from pathlib import Path
import json
base=(((-Q(1),Q(0)),Q(0)),((Q(1),Q(0)),Q(1)),((Q(0),-Q(1)),Q(0)),((Q(0),Q(1)),Q(1)))
P=(Q(1),Q(2),Q(0),Q(0));R=(Q(0),Q(1),Q(1),Q(1));K=tuple(R[i]-P[i] for i in range(4))
def image(rows,m):return tuple(sum(rows[i][0][j]*m[i] for i in range(len(rows))) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(len(rows)))
def transform(rows,m,order,scale):
 if len(order)!=len(rows) or sorted(order)!=list(range(len(rows))) or len(scale)!=len(rows):raise ValueError('ROW_BIJECTION_REQUIRED')
 if any(s<=0 for s in scale):raise ValueError('POSITIVE_SCALE_REQUIRED')
 out=tuple((tuple(s*x for x in rows[i][0]),s*rows[i][1]) for i,s in zip(order,scale))
 return out,tuple(m[i]/s for i,s in zip(order,scale))
assert image(base,P)==image(base,R)==((Q(1),Q(0)),Q(2)) and image(base,K)==((Q(0),Q(0)),Q(0))
checks=0
for order in ((3,0,2,1),(1,0,3,2),(2,3,0,1)):
 for scale in ((Q(2),Q(3),Q(1,2),Q(4)),(Q(1,2),Q(1),Q(3),Q(2))):
  new,p=transform(base,P,order,scale);_,r=transform(base,R,order,scale);_,k=transform(base,K,order,scale)
  assert image(new,p)==image(base,P) and image(new,r)==image(base,R) and image(new,k)==image(base,K)
  assert tuple(r[i]-p[i] for i in range(4))==k and min((*p,*r))>=0
  inv=tuple(order.index(i) for i in range(4));invscale=tuple(1/scale[inv[i]] for i in range(4))
  restored,back=transform(new,p,inv,invscale)
  assert restored==base and back==P
  assert {order[j] for j,x in enumerate(p) if x}=={i for i,x in enumerate(P) if x}
  checks+=1
assert checks==6
new,_=transform(base,P,(3,0,2,1),(Q(2),Q(3),Q(1,2),Q(4)))
assert sha256(repr(new).encode()).hexdigest()!=sha256(repr(base).encode()).hexdigest()
for order,scale,code in [((0,1,2),(Q(1),)*3,'ROW_BIJECTION_REQUIRED'),((0,1,2,3),(Q(1),Q(-1),Q(1),Q(1)),'POSITIVE_SCALE_REQUIRED')]:
 try:transform(base,P,order,scale)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('bad presentation accepted')
report={'passed':True,'permutation_rescaling_path_cases':checks,'exact_inverse_restores_rows_and_proof':True,'signed_kernel_and_support_transport':True,'new_manifest_digest_differs':True,'negative_scale_and_omitted_row_refused':True,'scope':'Positive monomial isomorphisms of fixed square inequality PRESENTATION, not source owner identity, proof-history execution, arbitrary row operations or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/square-row-isomorphism.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
