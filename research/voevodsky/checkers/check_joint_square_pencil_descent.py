"""Exact descent of actual filling pencils through jointly restricted paths."""
from pathlib import Path
from collections import defaultdict
import subprocess
import sys
import json
import hashlib
ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'research/voevodsky/results'
subprocess.run([sys.executable,str(Path(__file__).with_name('check_filling_restriction_fibers.py'))],check=True,capture_output=True,text=True)
p=OUT/'filling-restriction-fibers.json';d=json.loads(p.read_text())
W={tuple(t) for t in d['source_witness_rows']};assert len(W)==70

def audit(W):
 u={(a,b) for a,b,c,e in W};v={(b,c) for a,b,c,e in W}
 x={(a,e) for a,b,c,e in W};w={(e,c) for a,b,c,e in W}
 UV={(a,b,c) for a,b in u for bb,c in v if b==bb}
 XW={(a,e,c) for a,e in x for ee,c in w if e==ee}
 # The common diagonal admits exactly the AC source image; restricting either
 # path to that image is insufficient in general, so retain full joint match.
 joint={(a,b,c,e) for a,b,c in UV for aa,e,cc in XW if a==aa and c==cc}
 assert joint==W
 pencils=defaultdict(set)
 for a,b,c,e in W:pencils[a,c].add((b,e))
 # Both projections of each pencil, with the actual compatibility relation.
 rectangles=0;correlated=0
 for fiber in pencils.values():
  left={b for b,e in fiber};right={e for b,e in fiber}
  if fiber=={(b,e) for b in left for e in right}:rectangles+=1
  else:correlated+=1
 return {'UV':UV,'XW':XW,'pencils':pencils,'rectangular_fibers':rectangles,'correlated_fibers':correlated}
base=audit(W)
# Quarter-turn transports the complete boundary constraint, not an assumption
# of equivalence between separately marginalized path spaces.
def rotate(t):a,b,c,e=t;return e,a,b,c
def reflect(t):a,b,c,e=t;return a,e,c,b
current=W;rotations=[]
for k in range(4):
 result=audit(current)
 rotations.append({'turns':k,'UV_size':len(result['UV']),'XW_size':len(result['XW']),
                   'diagonal_pencils':len(result['pencils']),
                   'fiber_cardinalities':dict((str(n),sum(len(v)==n for v in result['pencils'].values())) for n in sorted({len(v) for v in result['pencils'].values()})),
                   'rectangular_pencils':result['rectangular_fibers'],'correlated_pencils':result['correlated_fibers']})
 current={rotate(t) for t in current}
assert current==W
assert {reflect(reflect(t)) for t in W}==W
for t in W:
 rt=t
 for _ in range(3):rt=rotate(rt)
 assert reflect(rotate(reflect(t)))==rt
# Every rotated/reflected presentation gets a canonical inverse to its source
# rows by explicit boundary permutation. No physical protocol is reversed.
permutations=[]
for reflected in (False,True):
 for k in range(4):
  perm=list(range(4))
  if reflected:perm=[perm[0],perm[3],perm[2],perm[1]]
  for _ in range(k):perm=[perm[3],perm[0],perm[1],perm[2]]
  permutations.append(tuple(perm))
assert len(set(permutations))==8
presentations=[{tuple(t[j] for j in perm) for t in W} for perm in permutations]
for carrier in presentations:audit(carrier)
checks=0
for i,pi in enumerate(permutations):
 for j,pj in enumerate(permutations):
  def change(t,pa,pb):
   source=[None]*4
   for k,v in enumerate(t):source[pa[k]]=v
   return tuple(source[k] for k in pb)
  assert {change(t,pi,pj) for t in presentations[i]}==presentations[j]
  for k,pk in enumerate(permutations):
   for t in presentations[i]:
    assert change(change(t,pi,pj),pj,pk)==change(t,pi,pk)
    checks+=1
report={'passed':True,'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'source_fillings':len(W),'joint_path_fiber_product_exact':True,
 'rotation_profiles':rotations,'dihedral_presentations':8,'comparison_triangle_point_checks':checks,
 'corrected_equivalence':'W is the fiber product of the TWO full path-factorization sets over their shared diagonal (a,c), for this actual frozen boundary arrangement. Neither path set separately is equivalent to W.',
 'symmetry_scope':'Coordinate-permuted presentations with transported boundary types and constraints. This is not invariance of W under fixed-label rotation or an independently executable reversed protocol.',
 'logical_boundary':'The fiber-product property is checked on this source. General pairwise-source completeness is false.'}
(OUT/'joint-square-pencil-descent.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
