"""Enumerate the 3x3 join for one marked (3,4) witness and its reverse. Test the same joins inside the stored 17-vertex (4,4) graph."""
from itertools import permutations,combinations
from collections import Counter
import json
from ramsey_retention_slice import D,decode,check
rows=json.loads(D.read_text());r=next(z for z in rows if (z['l'],z['k'])==(3,4));a=decode(r['graph6']);S=[i for i in range(8) if r['seed5']>>i&1];T=[i for i in range(8) if i not in S];edge=lambda i,j:a[i]>>j&1
r=rows[-1];full=decode(r['graph6']);P=[i for i in range(24) if r['seed17']>>i&1];assert check(full,r['seed17'],4,4)
import networkx as nx
G=nx.Graph();G.add_nodes_from(P);G.add_edges_from((i,j) for i,j in combinations(P,2) if full[i]>>j&1)
L=nx.Graph();L.add_nodes_from(range(8));L.add_edges_from((i,j) for i,j in combinations(range(8),2) if edge(i,j));emb=[]
for side in [L,nx.complement(L)]:
 maps=[{j:i for i,j in m.items()} for m in nx.isomorphism.GraphMatcher(G,side).subgraph_isomorphisms_iter()];emb.append(maps)
right={tuple(m[i] for i in S) for m in emb[1]};out=[]
for p in permutations(S):
 if any(edge(i,j)==edge(u,v) for (i,u),(j,v) in combinations(zip(S,p),2)):continue
 b=[0]*11
 for order,slots,rev in [(S+T,list(range(8)),0),(list(p)+T,[0,1,2,3,4,8,9,10],1)]:
  for (i,u),(j,v) in combinations(zip(slots,order),2):
   if edge(u,v)^rev:b[i]|=1<<j;b[j]|=1<<i
 good=[]
 for bits in range(512):
  h=b.copy()
  for k in range(9):
   if bits>>k&1:i,j=5+k//3,8+k%3;h[i]|=1<<j;h[j]|=1<<i
  if check(h,2047,4,4):good.append(bits)
 extended=any(tuple(m[S[p.index(i)]] for i in S) in right for m in emb[0]);out.append(dict(match=p,legal=len(good),forced=sum(len({v>>k&1 for v in good})==1 for k in range(9)),inside17=extended))
print(out);(D.parent/'ramsey_square_33.json').write_text(json.dumps(out,indent=1)+'\n')
