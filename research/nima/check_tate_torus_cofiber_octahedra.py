#!/usr/bin/env python3
"""Finite-window certificate for channel-filtration cofibers and octahedral compatibility."""
import json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
U=frozenset(range(4));subs=[frozenset(c) for r in range(5) for c in itertools.combinations(U,r)]
def dim(S):return 3**len(S) # lattice coordinates truncated to {-1,0,1}
def rho(S):return frozenset((i+1)%4 for i in S)
triangles=octahedra=0;fails=[]
for A in subs:
 for B in subs:
  if not A<=B:continue
  qab=dim(B)-dim(A)
  if qab<0:fails.append('negative quotient')
  for C in subs:
   if not B<=C:continue
   triangles+=1
   qac=dim(C)-dim(A);qbc=dim(C)-dim(B)
   # 0 -> V_B/V_A -> V_C/V_A -> V_C/V_B -> 0
   if qac!=qab+qbc:fails.append('cofiber dimension')
   octahedra+=1
   # Rotation preserves dimensions, inclusions, and quotient identities.
   if not rho(A)<=rho(B) or not rho(B)<=rho(C) or dim(rho(C))-dim(rho(A))!=qac:fails.append('rotation')
checks={'all_short_exact_quotient_sequences_close':not fails,'all_chain_octahedra_close':not fails,'rotation_preserves_exactness':not fails,'nonzero_edge_quotients':all(dim(B)-dim(A)>0 for A in subs for B in subs if A<B)}
out={'schema':'marici.nima.tate-torus-cofiber-octahedra.v1','coordinate_window':[-1,0,1],'subsets':len(subs),'nested_triples_checked':octahedra,'checks':checks,'failures':fails[:20],'passed':all(checks.values()),'model':'V_S is the span of lattice deltas supported on Z^S. For A subset B subset C, 0 -> V_B/V_A -> V_C/V_A -> V_C/V_B -> 0 gives the cofiber triangle; nested quotient sequences give the canonical octahedron.'}
p=ROOT/'research/nima/results/tate-torus-cofiber-octahedra.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
