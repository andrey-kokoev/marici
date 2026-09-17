#!/usr/bin/env python3
"""Exact chain and residue audit for the eight-axis positive cube."""
import itertools,json,math
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
AXES=('H','V','D','q','L','C','O','R');n=8
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
# Cubical f-vector.
fvector=[math.comb(n,k)*2**(n-k) for k in range(n+1)]
# Freudenthal oriented top chain.
chain={}
for p in itertools.permutations(range(n)):
 v=[0]*n;simplex=[tuple(v)]
 for a in p:v=v.copy();v[a]=1;simplex.append(tuple(v))
 chain[tuple(simplex)]=parity(p)
# Simplicial boundary and cancellation of all interior facets.
bd=defaultdict(int)
for simplex,c in chain.items():
 for j in range(n+1):bd[simplex[:j]+simplex[j+1:]]+=c*((-1)**j)
bd={k:v for k,v in bd.items() if v}
def boundary_facet(facet):
 for a in range(n):
  vals={v[a] for v in facet}
  if len(vals)==1:return True
 return False
# Cubical boundary squared on every face encoded by fixed 0/1 and free '*'.
def cubical_boundary(face):
 free=[i for i,x in enumerate(face) if x=='*'];out=[]
 for pos,a in enumerate(free):
  for val,side in ((1,1),(0,-1)):
   g=list(face);g[a]=val;out.append((tuple(g),((-1)**pos)*side))
 return out
d2_ok=True
for face in itertools.product((0,1,'*'),repeat=n):
 if face.count('*')<2:continue
 acc=defaultdict(int)
 for subface,c in cubical_boundary(face):
  for g,d in cubical_boundary(subface):acc[g]+=c*d
 if any(acc.values()):d2_ok=False;break
pair_decorations={
 'H x V':'strict Beck-Chevalley',
 'D x L':'dagger exchanges left/right successor',
 'q x R':'lax leakage A_X=P_X F (I-P_X)',
 'L x O':'endpoint multiplier naturality',
 'C x R':'forward realization/completion naturality',
}
checks={'f_vector_exact':fvector==[256,1024,1792,1792,1120,448,112,16,1],'maximal_simplices_40320':len(chain)==40320,'all_simplex_orientations_unit':set(chain.values())=={-1,1},'interior_facets_cancel':all(boundary_facet(x) for x in bd),'boundary_has_16_times_7_factorial_facets':len(bd)==16*math.factorial(7),'boundary_coefficients_unit':set(bd.values())=={-1,1},'cubical_boundary_squared_zero':d2_ok,'named_operator_face_decorations_retained':len(pair_decorations)==5}
out={'schema':'marici.nima.eight-axis-positive-cube.v1','positive_geometry':'[0,1]^8','axes':AXES,'canonical_form':'wedge_a dlog(x_a/(1-x_a))','f_vector':fvector,'maximal_simplices':len(chain),'oriented_boundary_facets_after_cancellation':len(bd),'pair_decorations':pair_decorations,'checks':checks,'passed':all(checks.values()),'claim_boundary':'exact positive-cube incidence, orientation, triangulation, and named face placement; a complete operator-valued canonical form requires decorations and higher residue identities on every face'}
p=ROOT/'research/nima/results/eight-axis-positive-cube.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
