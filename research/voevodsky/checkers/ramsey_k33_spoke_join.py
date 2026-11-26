"""Join the three degree-three-star panels on a common 17-core. Let l_i be number of edges from the double opposite root i to its three single vertices. 1<=l_i<=3 since that double must see the blue five on i (all X blue to B). k_ij=l_i+l_j+e(single_i,single_j). For each panel triple enumerate the internal X edges, using support-disjointness on every red edge. Test full degrees of X-singletons, alpha(X)<=5, triangles, and the fixed partial common-neighbor restrictions. No choice of B's pattern or symmetry of the endpoint assumed."""
from ramsey_retention_slice import D
import json,itertools,collections,sys
P=D.parent;comb=itertools.combinations

def solve(z):
 i=z['i'];ed=z['h'];H=[0]*17
 for a,b in ed:H[a]|=1<<b;H[b]|=1<<a
 rows=sorted((p['k'],tuple(r)) for p in z['panels'] for r in p['rows']);stats=collections.Counter();alive=[];group_pairs=[(0,1),(0,2),(1,2)]
 for u,(k0,A) in enumerate(rows):
  if k0*3>len(ed)-11:break
  for v in range(u,len(rows)):
   k1,B=rows[v];
   if k0+2*k1>len(ed)-11:break
   for w in range(v,len(rows)):
    k2,C=rows[w];ks=(k0,k1,k2);D=sum(ks)-len(ed)+20
    if D>9:break
    stats['numeric']+=1;S=A+B+C;opts=[[ (x,y) for x in range(3*a,3*a+3) for y in range(3*b,3*b+3) if not S[x]&S[y]] for a,b in group_pairs];
    if any(len(o)<ks[3-a-b]-6 for o,(a,b) in zip(opts,group_pairs)):continue
    stats['disjoint_capacity']+=1
    if any(sum(1 for o in opts for e in o if j in e)+1<7-s.bit_count() for j,s in enumerate(S)):continue
    for ls in itertools.product(range(1,4),repeat=3):
     if sum(ls)!=D:continue
     req=[ks[3-a-b]-ls[a]-ls[b] for a,b in group_pairs];
     if any(not 0<=n<=len(o) for n,o in zip(req,opts)):continue
     for block in itertools.product(*(comb(o,n) for o,n in zip(opts,req))):
      edges=sum(block,());adj=[0]*12
      for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
      gap=[7-s.bit_count()-adj[j].bit_count() for j,s in enumerate(S)]
      if any(v not in (0,1) for v in gap) or any(sum(gap[3*j:3*j+3])!=ls[j] for j in range(3)):continue
      stats['degrees']+=1
      if any(adj[a]&adj[b] for a,b in edges):continue
      for j,v in enumerate(gap):
       if v:adj[j]|=1<<(9+j//3);adj[9+j//3]|=1<<j
      I=[0]
      for j,x in enumerate(adj):I.extend([q|1<<j for q in I if not x&q]);
      if max(map(int.bit_count,I))>5:continue
      stats['X_legal']+=1;alive.append(dict(S=S,X=adj))
 return dict(i=i,counts=stats,alive=alive)
if __name__=='__main__':
 from concurrent.futures import ProcessPoolExecutor
 src=json.loads((P/'ramsey_k33_three_spokes.json').read_text());
 with ProcessPoolExecutor(7) as ex:out=list(ex.map(solve,src));print([(z['i'],z['counts']) for z in out]);(P/'ramsey_k33_spoke_join.json').write_text(json.dumps(out)+'\n')
