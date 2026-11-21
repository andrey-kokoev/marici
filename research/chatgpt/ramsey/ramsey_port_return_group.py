"""Exact return group in the fixed-center 288-matching space. Enumerate four-edge transitions, then realize all S4 port permutations by square-preserving endpoint identifications."""
from pathlib import Path
from itertools import combinations,permutations
from collections import deque,Counter
import json
from ramsey_hall_center_conjecture import decode,independent
from ramsey_hall_center_four_exchange import P,T,matchings
from ramsey_frame_loop_search import lift
D=Path(__file__).parent;catalogue=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());A=decode(catalogue['regular'][-1]['graph6'].encode());U=[u for u in range(22) if A[0]>>u&1];W=[w for w in range(1,22) if w not in U];Q={0,1,3,11};ports=(2,4,5,6);labels={tuple(k for k,u in enumerate(U) if A[w]>>u&1):w for w in W};E=frozenset(e for e in combinations(range(22),2) if A[e[0]]>>e[1]&1);fixed={e for e in E if e[0] not in W or e[1] not in W};base={tuple(sorted((labels[P[i]],labels[P[j]]))) for i,j in combinations(range(15),2) if not set(P[i])&set(P[j])};graphs=[]
for m in matchings():
 removed={tuple(sorted(labels[P[k]] for k in T[j] if k!=i)) for i,j in m};graphs.append(frozenset(fixed|(base-removed)))
assert len(set(graphs))==288;index={g:i for i,g in enumerate(graphs)};start=index[E];adj=[[] for _ in graphs]
for i,j in combinations(range(288),2):
 if len(graphs[i]-graphs[j])==4:adj[i].append(j);adj[j].append(i)
parent={start:None};distance={start:0};queue=deque([start])
while queue:
 i=queue.popleft()
 for j in adj[i]:
  if j not in parent:parent[j]=i;distance[j]=distance[i]+1;queue.append(j)
returns=[]
for p in permutations(range(4)):
 action=list(range(22))
 for i,v in enumerate(ports):action[v]=ports[p[i]]
 f=lift(A,0,action);assert all(f[q]==q for q in Q);target=frozenset(tuple(sorted((f[i],f[j]))) for i,j in E);j=index[target]
 if j not in parent:continue
 path=[];k=j
 while parent[k] is not None:
  before=parent[k];path.append({'removed':sorted(graphs[before]-graphs[k]),'added':sorted(graphs[k]-graphs[before])});k=before
 path.reverse();F=set(E)
 for step in path:
  F-=set(map(tuple,step['removed']));F|=set(map(tuple,step['added']));B=[0]*22
  for a,b in F:B[a]|=1<<b;B[b]|=1<<a
  assert all(x.bit_count()==6 for x in B) and all(not(B[a]&B[b]) for a,b in F) and not independent(B,(1<<22)-1,7)
 assert F==set(target);returns.append({'port_permutation':p,'distance':distance[j],'path':path,'endpoint_isomorphism':f})
assert len(returns)==24
result={'matching_graph_vertices':288,'component_size':len(parent),'degree_histogram':dict(Counter(map(len,adj))),'component_distance_histogram':dict(sorted(Counter(distance.values()).items())),'return_group_order':len(returns),'return_distance_histogram':dict(sorted(Counter(r['distance'] for r in returns).items())),'returns':returns};(D/'ramsey_port_return_group.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k!='returns'})
