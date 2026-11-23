"""Calibrate source orbit motif on one marked wiring only. Candidate point permutations, never output wiring. Count simultaneous input reds on edge motifs transported with candidate. Rank by edge count, connectedness, orbit size, lexical tie-break."""
from itertools import permutations,combinations
from pathlib import Path
import json
D=Path(__file__).parent;r=json.loads((D/'ramsey_seven_all_wirings.json').read_text());S=r['address_masks'];E=list(map(tuple,r['edge_order']));w=min(r['wirings']);C=(0,1,4,5,2,3,6);J=(0,1,5,4,3,2,6);P={}
for p in permutations(range(7)):
 T=[sum(1<<p[i] for i in range(7) if s>>i&1) for s in S];
 if set(T)!=set(S):continue
 m=list(map(S.index,T));P[p]=[E.index(tuple(sorted((m[a],m[b])))) for a,b in E]
def images(c,m):return {tuple(sorted(g[i] for i in m)) for p,g in P.items() if all(p[C[i]]==c[p[i]] for i in range(7))}
def val(w,O):return sum(all(w>>i&1 for i in t) for t in O)
def find():
 for n in (1,2,3):
  used=set();best=None
  for m in combinations(range(len(E)),n):
   if m in used:continue
   O=images(C,m);used|=O;Q=images(J,m);a,b=val(w,O),val(w,Q)
   if a==b:continue
   key=(len({v for i in m for v in E[i]}),len(O),m)
   if best is None or key<best[0]:best=(key,m,a,b)
  if best:return best
if __name__=='__main__':
 key,m,a,b=find();print(key,a,b,[[[i for i in range(7) if S[v]>>i&1] for v in E[e]] for e in m]);o=dict(source='C=(24)(35)',motif_edge_indices=m,orbit_size=key[1],input0_counts=[a,b],choose='larger' if b>a else 'smaller');(D/'ramsey38_direction_motif_freeze.json').write_text(json.dumps(o,indent=2)+'\n')
