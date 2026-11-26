"""Detect empty completion domains using only support triples: repeatedly delete faces with an edge of incidence one. Every compatible quartet would contribute a tetrahedron boundary. Nonempty peel is inconclusive. Clone a repeatable support four times for distinct slot vertices."""
import json,itertools,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';gs=[r['core'] for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==11 and r['d']==4];priors=json.loads((P/'ramsey_shared_fourth.json').read_text());out=[]
for ref in priors:
 a=gs[ref['row']];I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not v&s])
 Q=[q for q in I if q.bit_count()==4];T=[q for q in I if q.bit_count()==3];S=[];M=[]
 for s in I:
  if not all(s&(v|1<<i) for i,v in enumerate(a)):continue
  m=sum(1<<i for i,q in enumerate(Q) if not s&q);r=1 if m else 4;S.extend([s]*r);M.extend([m]*r)
 faces={z:S[z[0]]|S[z[1]]|S[z[2]] for z in itertools.combinations(range(len(S)),3) if all(not M[i]&M[j] for i,j in itertools.combinations(z,2))};
 def bipartite(edges):
  g=collections.defaultdict(list);colors={}
  for x,y in edges:g[x].append(y);g[y].append(x)
  for x in g:
   if x in colors:continue
   colors[x]=0;stack=[x]
   while stack:
    u=stack.pop()
    for v in g[u]:
     if v not in colors:colors[v]=1-colors[u];stack.append(v)
     elif colors[v]==colors[u]:return False
  return True
 def peel(panel,links=True):
  live=[z for z,u in faces.items() if all(u&t for t in panel)];trace=[len(live)]
  while live:
   c=collections.Counter(e for z in live for e in itertools.combinations(z,2));nxt=[z for z in live if all(c[e]>=2 for e in itertools.combinations(z,2))];
   if links:
    cut={i for i in range(len(S)) if bipartite([tuple(j for j in z if j!=i) for z in nxt if i in z])};nxt=[z for z in nxt if cut.isdisjoint(z)]
   if len(nxt)==len(live):break
   live=nxt;trace.append(len(live))
  return trace
 edge_only=[peel(ref['panel'][:j],False) for j in range(len(ref['panel'])+1)];prefix=[peel(ref['panel'][:j]) for j in range(len(ref['panel'])+1)];active=[t for t in T if any(not t&u for u in faces.values())];sol=None
 for k in range(len(ref['panel'])+1):
  for ts in itertools.combinations(active,k):
   trace=peel(ts)
   if not trace[-1]:sol=dict(panel=ts,trace=trace);break
  if sol:break
 print(ref['row'],prefix,sol);out.append(dict(row=ref['row'],prefix=prefix,edge_only_prefix=edge_only,minimum_peel=sol,active=active))
(P/'ramsey_triple_peel.json').write_text(json.dumps(out)+'\n')
