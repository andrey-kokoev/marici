"""Exhaust all 120 hub-fixing label permutations; test two-way canonical incidence re-lifting across the center-transfer pair. Compare with C5 normalizer without assuming it."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
D=Path(__file__).parent;data=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());A=decode(next(r for r in data['regular'] if r['record']==191)['graph6'].encode());B=json.loads((D/'ramsey_closed_repair_size5.json').read_text())[1]['first_valid_example']['output_adjacency'];U=[i for i in range(22) if A[0]>>i&1];V=[i for i in range(22) if B[1]>>i&1];finite=[i for i in U if i!=1];identity=tuple(range(22));compose=lambda a,b:tuple(a[b[i]] for i in range(22))
def lift(G,center,action):
 labels=[i for i in range(22) if G[center]>>i&1];assert {action[i] for i in labels}==set(labels);out=list(range(22));lookup={frozenset(u for u in labels if G[w]>>u&1):w for w in range(22) if w!=center and w not in labels};assert len(lookup)==15
 for u in labels:out[u]=action[u]
 for S,w in lookup.items():out[w]=lookup[frozenset(action[u] for u in S)]
 return tuple(out)
p=tuple(json.loads((D/'ramsey_repair_cyclic_phase.json').read_text())[1]['unique_C5_generator']);group=set();g=identity
for _ in range(5):group.add(g);g=compose(p,g)
rows=[];stats=Counter()
for perm in permutations(finite):
 initial=list(identity)
 for a,b in zip(finite,perm):initial[a]=b
 R=lift(A,0,initial);S=lift(B,1,R);can_return={S[u] for u in U}==set(U);inv=tuple(R.index(i) for i in range(22));normalizes={compose(R,compose(g,inv)) for g in group}==group;preserves_cycle=compose(R,compose(p,inv)) in (p,tuple(p.index(i) for i in range(22)))
 returns_same=can_return and lift(A,0,S)==R
 order=1;g=R
 while g!=identity:g=compose(R,g);order+=1
 stats['tested']+=1;stats['return_admissible']+=can_return;stats['C5_normalizers']+=normalizes;stats['returns_same']+=returns_same;stats['involutions']+=order==2;stats['admissible_involutions']+=can_return and order==2
 rows.append({'label_images':perm,'order':order,'return_admissible':can_return,'normalizes_C5':normalizes,'returns_same':returns_same})
# Old finite label vertices become the five pairs containing new hub0: a star, not a cycle.
cycle_edges=[sorted(u for u in V if B[w]>>u&1) for w in finite];degree=Counter(u for e in cycle_edges for u in e);assert sum(degree.values())==10
result={'stats':dict(stats),'old_finite_labels_as_new_pairs':cycle_edges,'new_star_degrees':dict(degree),'rows':rows};(D/'ramsey_center_relift_roundtrip.json').write_text(json.dumps(result,indent=2)+'\n');print('stats',dict(stats),'new pair star',cycle_edges)
