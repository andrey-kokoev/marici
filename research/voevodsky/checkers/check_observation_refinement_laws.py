"""Finite semantic controls; no continuum theorem inferred from enumeration."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
P=set(product(range(3),repeat=3))
def A(x):return sum(x),sum(Q(v,128**j) for j,v in enumerate(x))
def B(x):return A(x)+(x[0],)
def projection(y):return y[:2]
def denote(obs,e):return {x for x in P if e(obs(x))}
def forget(C,obs):
 image={obs(x) for x in C};return {x for x in P if obs(x) in image}
checks=0
for bound,threshold in product(range(7),range(3)):
 e=lambda y:y[0]<=bound
 f=lambda y:y[1]<=threshold
 old=denote(A,e);exposed=denote(B,lambda y:e(projection(y)))
 assert old==exposed
 left=denote(A,lambda y:e(y) and f(y))
 right=denote(B,lambda y:e(projection(y)) and f(projection(y)))
 assert left==right and left<=old
 coarse=forget(left,lambda x:A(x)[0])
 assert left<=coarse and forget(coarse,lambda x:A(x)[0])==coarse
 assert {A(x)[0] for x in left}=={A(x)[0] for x in coarse}
 for r in range(7):
  assert any(sum(x)<=r for x in left)==any(sum(x)<=r for x in coarse)
  assert all(sum(x)<=r for x in left)==all(sum(x)<=r for x in coarse)
  checks+=1
# Fine evidence x0=0 with total=1. Coarse total-image remains {1}, but the
# fine audit x0=0 is lost on saturation (1,0,0 is newly admitted).
C={x for x in P if sum(x)==1 and x[0]==0};F=forget(C,sum)
assert C<F and all(x[0]==0 for x in C) and not all(x[0]==0 for x in F)
# Discarding the constraining row is not exact projection.
R={(u,h) for u,h in product(range(3),repeat=2) if u==h and h<=1}
projected={u for u,h in R};naive={u for u,h in product(range(3),repeat=2) if u==h}
assert projected=={0,1} and naive=={0,1,2}
# Universal-answer truth alone does not establish nonemptiness after add.
assert C and not {x for x in C if sum(x)<0}
report={'passed':True,'coarse_query_comparisons':checks,'source_grid_size':len(P),
 'fine_audit_lost_under_coarse_saturation':True,'row_deletion_is_not_projection':True,
 'scope':'Finite operation-law controls; continuum laws have image/preimage proofs. This is not a new backend or an analytical-source admission proof.'}
(OUT/'observation-refinement-laws.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
