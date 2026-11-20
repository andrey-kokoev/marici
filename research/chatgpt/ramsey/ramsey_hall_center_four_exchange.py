"""Search exact four-edge exchanges preserving a fixed Hall-center labeling, via all incidence perfect matchings. Not an unrestricted four-edge exchange census."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode,independent
from ramsey_regular_two_switch import relation,iso
P=list(combinations(range(6),2));T=[t for t in combinations(range(15),3) if len(set(x for i in t for x in P[i]))==6]
def matchings(i=0,used=frozenset(),m=()):
 if i==15:yield m;return
 for j,t in enumerate(T):
  if i in t and j not in used:yield from matchings(i+1,used|{j},m+((i,j),))

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());graphs={r['record']:decode(r['graph6'].encode()) for r in data['regular']};rels={k:relation(A) for k,A in graphs.items()};ms=list(matchings());assert len(ms)==288;out=[]
 for source in (190,191):
  A=graphs[source];U=[i for i in range(22) if A[0]>>i&1];W=[i for i in range(1,22) if i not in U];label={tuple(k for k,u in enumerate(U) if A[w]>>u&1):w for w in W};assert set(label)==set(P);E={e for e in combinations(range(22),2) if A[e[0]]>>e[1]&1};fixed={e for e in E if e[0] not in W or e[1] not in W};base={tuple(sorted((label[P[i]],label[P[j]]))) for i,j in combinations(range(15),2) if not set(P[i])&set(P[j])};counts=Counter();witnesses={}
  for m in ms:
   removed={tuple(sorted(label[P[k]] for k in T[j] if k!=i)) for i,j in m};F=fixed|(base-removed)
   if len(E-F)!=4:continue
   B=[0]*22
   for i,j in F:B[i]|=1<<j;B[j]|=1<<i
   assert not independent(B,(1<<22)-1,7);rb=relation(B)
   hits=[(target,mapping) for target,C in graphs.items() if (mapping:=iso(B,C,rb,rels[target])) is not None];assert len(hits)==1;target,mapping=hits[0];counts[target]+=1;witnesses.setdefault(target,{'target':target,'removed':sorted(E-F),'added':sorted(F-E),'isomorphism':mapping})
  r={'source':source,'targets':dict(counts),'witnesses':list(witnesses.values())};out.append(r);print(r)
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
