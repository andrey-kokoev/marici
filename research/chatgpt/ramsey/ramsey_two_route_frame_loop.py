"""Compare two distinct four-edge completions with a common second Hall center. Canonically transport 0->h in one completion, change chart at h to the other completion, and return h->0."""
from pathlib import Path
from itertools import combinations,permutations
from collections import defaultdict
import json
from ramsey_hall_center_conjecture import decode,root_profile
from ramsey_hall_center_four_exchange import P,T,matchings
D=Path(__file__).parent;data=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());A=decode(next(r for r in data['regular'] if r['record']==191)['graph6'].encode());U=[u for u in range(22) if A[0]>>u&1];W=[w for w in range(1,22) if w not in U];labels={tuple(k for k,u in enumerate(U) if A[w]>>u&1):w for w in W}
def edges(G):return {e for e in combinations(range(22),2) if G[e[0]]>>e[1]&1}
def lift(G,v,action):
 L=[u for u in range(22) if G[v]>>u&1];assert {action[u] for u in L}==set(L);lookup={frozenset(u for u in L if G[w]>>u&1):w for w in range(22) if w!=v and w not in L};assert len(lookup)==15;out=list(range(22))
 for u in L:out[u]=action[u]
 for S,w in lookup.items():out[w]=lookup[frozenset(action[u] for u in S)]
 return tuple(out)
E=edges(A);fixed={e for e in E if e[0] not in W or e[1] not in W};base={tuple(sorted((labels[P[i]],labels[P[j]]))) for i,j in combinations(range(15),2) if not set(P[i])&set(P[j])};groups=defaultdict(list)
for m in matchings():
 removed={tuple(sorted(labels[P[k]] for k in T[j] if k!=i)) for i,j in m};F=fixed|(base-removed)
 if len(E-F)!=4:continue
 B=[0]*22
 for i,j in F:B[i]|=1<<j;B[j]|=1<<i
 other=[v for v in range(1,22) if root_profile(B,v)['hall_center']];assert len(other)==1;groups[other[0]].append(B)
assert len(groups)==5 and all(len(g)==2 for g in groups.values());results=[]
for h,(B,C) in sorted(groups.items()):
 assert B[h]==C[h];V=B[h];outside=[w for w in range(22) if w!=h and not V>>w&1];changed=[w for w in outside if B[w]&V!=C[w]&V];finite=[u for u in U if u!=h];tested=0;different_middle=0;drift=[]
 for perm in permutations(finite):
  action=list(range(22))
  for a,b in zip(finite,perm):action[a]=b
  R=lift(A,0,action);S=lift(B,h,R);S2=lift(C,h,S);R2=lift(A,0,S2);tested+=1;different_middle+=S!=S2
  if R2!=R:drift.append(perm)
 results.append({'second_center':h,'comparisons_tested':tested,'changed_h_chart_signatures':changed,'middle_edge_replacements':len(edges(B)-edges(C)),'different_middle_comparisons':different_middle,'nontrivial_returns':len(drift),'completion_B':B,'completion_C':C});print({k:v for k,v in results[-1].items() if not k.startswith('completion_')})
(D/'ramsey_two_route_frame_loop.json').write_text(json.dumps(results,indent=2)+'\n')
