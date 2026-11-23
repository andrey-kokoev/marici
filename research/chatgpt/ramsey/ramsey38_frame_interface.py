"""Predict the square interface by marked frame words; validate against archived named wirings (all roots). See two frozen protocols for move contracts."""
from pathlib import Path
import itertools as it,json
from collections import deque,Counter
D=Path(__file__).parent;r=json.loads((D/'ramsey_seven_all_wirings.json').read_text());W=set(r['wirings']);S=r['address_masks'];E=list(map(tuple,r['edge_order']));G=[]
for swaps in [[(0,1),(2,3)],[(0,1),(4,5)],[(2,4),(3,5)]]:
 p=list(range(7))
 for u,v in swaps:p[u],p[v]=p[v],p[u]
 m=[S.index(sum(1<<p[i] for i in range(7) if s>>i&1)) for s in S];perm=[E.index(tuple(sorted((m[u],m[v])))) for u,v in E];G.append({w:sum((w>>i&1)<<j for i,j in enumerate(perm)) for w in W});assert set(G[-1].values())==W
A,B,C=G;adj={w:{g[w] for g in G} for w in W};dist={}
for w in W:
 d={w:0};q=deque([w]);
 while q:
  u=q.popleft()
  for v in adj[u]-d.keys():d[v]=1+d[u];q.append(v)
 dist[w]=d
for w in sorted(W):
 table={}
 for i,j,t in it.product(range(2),repeat=3):
  v=w
  for b,g in [(j,B),(i,A),(t,C)]:
   if b:v=g[v]
  table[i,j,t]=v
 assert set(table.values())==W
 for k,v in table.items():
  for h,u in table.items():assert dist[v][u]==sum(x!=y for x,y in zip(k,h))
  assert C[v]==table[k[:2]+(1-k[2],)]
  if not k[2]:assert all((dist[C[v]][u]<dist[v][u])==bool(h[2]) for h,u in table.items())
raw=Counter((x^y).bit_count() for x,y in it.combinations(W,2));out=dict(states=len(W),literal_edges=raw[1],min_raw_distance=min(raw),literal_first_site_double_addresses=sum((x^1) in W for x in W)//2,verified_marked_roots=len(W),transport_edges=sum(map(len,adj.values()))//2,addresses_per_layer=4,matched_bridges=4,bridge_raw_sizes=sorted((w^C[w]).bit_count() for w in W if w<C[w]),interface_shape='square',within_layer_edges_per_layer=4,all_distances_hamming=True);print(out);(D/'ramsey38_frame_interface.json').write_text(json.dumps(out,indent=2)+'\n')
