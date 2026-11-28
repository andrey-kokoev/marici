from itertools import combinations,islice
from pathlib import Path
import json
from collections import deque
D=Path(__file__).resolve().parents[1]/'voevodsky/results';cores=json.loads((D/'ramsey_37_catalogue_free.json').read_text())['certificates'];first={};counts=[0]*3
w=json.loads((D/'ramsey_37_root_glue.json').read_text())['witness'];edges=set(map(tuple,w['plus_edges']));assert all(sum(not set(q).intersection(s) for s in w['cross_plus'])<=1 for q in combinations(w['core'],5) if all(e not in edges for e in combinations(q,2)))
for idx,rec in enumerate(cores):
 a=rec['core'];R=[sum(1<<i for i in t) for t in combinations(range(16),5) if all(not a[i]>>j&1 for i,j in combinations(t,2))];M={r:sum(1<<i for i,q in enumerate(R) if not r&q) for r in R};A={r:[] for r in R};arcs=[]
 for r in R:
  for i in range(15):
   t=r^(3<<i)
   if (r>>i)&3==1 and t in A:A[r].append(t);A[t].append(r);arcs.append((i,r,t))
 dist={}
 for r in R:
  q=deque([r]);dist[r,r]=0
  while q:
   s=q.popleft()
   for t in A[s]:
    if (r,t) not in dist:dist[r,t]=1+dist[r,s];q.append(t)
 for rows in islice(combinations(R,6),10000):
  pairs=list(combinations(rows,2));m=min(dist.get(p,999) for p in pairs)
  if m==999 or not any(M[x]&M[y] for x,y in pairs if dist.get((x,y))==m):
   counts[0]+=1;first.setdefault(1,(idx,rows,m));break
 rows=sorted(R,key=lambda r:M[r].bit_count())[:6];mass=sum(M[r].bit_count() for r in rows)
 if mass<=len(R):counts[1]+=1;first.setdefault(2,(idx,rows,mass,len(R)))
 for (i,r,t),(j,v,u) in combinations(arcs,2):
  if i!=j or len({r,t,u,v})!=4:continue
  if not ((M[r]&M[v]|M[t]&M[u])&~(M[r]&M[u]|M[t]&M[v])):
   counts[2]+=1;first.setdefault(3,(idx,i,(r,t),(u,v)));break
print('cores with refutations',counts,'examples',first)
