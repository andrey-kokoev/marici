"""Try one newcomer per square edge. Seed it with the endpoints, import all compatible red neighbors of either opposite corner, optionally greedily complete in vertex-label order. Compare to arbitrary maximal completions of the edge seed. Whole rooted graph checked for each first witness; no endpoint used to build the candidates."""
import itertools,json,collections
from ramsey_retention_slice import D,CAT,decode,check
P=D.parent;src=(CAT/'r37_22.g6').read_text().splitlines();out=[]
def run(a,kmax=7):
 n=len(a);F=(1<<n)-1;I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 G=[sum(1<<j for j in range(n) if j!=i and not(v>>j&1 or v&a[j])) for i,v in enumerate(a)];cycles=[(u,v,w,x) for u in range(n) for v in range(u+1,n) if G[u]>>v&1 for w in range(u+1,n) if G[v]>>w&1 for x in range(v+1,n) if x!=w and G[w]&G[u]&(1<<x)];
 if not cycles:return None
 Q={k:[q for q in I if q.bit_count()==k] for k in (kmax-3,kmax-2,kmax-1)};S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];cache={};wins={};stats=collections.Counter()
 def miss(s):
  if s not in cache:cache[s]=[sum(1<<j for j,q in enumerate(Q[k]) if not q&s) for k in (kmax-3,kmax-2,kmax-1)]
  return cache[s]
 def solution(dom):
  def choose(rows,indices):
   if len(rows)==4:return rows
   for s in sorted(dom[len(rows)]):
    m=miss(s)
    if any(m[2]&v[2] for v in indices) or any(m[1]&v[1]&w[1] for v,w in itertools.combinations(indices,2)) or any(m[0]&v[0]&w[0]&x[0] for v,w,x in itertools.combinations(indices,3)):continue
    ok=choose(rows+[s],indices+[m]);
    if ok:return ok
  return choose([],[])
 patterns=[]
 for c in cycles:
  ordered=[];pools={k:[] for k in ('import','greedy','edge_seed')}
  for i in range(4):
   u,v=c[i],c[(i+1)%4];p=(1<<u)|(1<<v);opts=[p|(a[c[(i+h)%4]]&~(a[u]|a[v])) for h in (2,3)];ordered.append(opts);base=set(opts);pools['import'].append(base);ext=set()
   for s in base:
    for j in range(n):
     if not s&a[j]:s|=1<<j
    ext.add(s)
   pools['greedy'].append(ext);pools['edge_seed'].append([s for s in S if s&p==p])
  patterns.append([mask for mask in range(16) if solution([[v[(mask>>i)&1]] for i,v in enumerate(ordered)])]);
  for k,dom in pools.items():
   w=solution(dom)
   if w:
    stats[k]+=1
    if k not in wins:
     g=a.copy()+[0]*5
     for j,t in enumerate(w,n):
      g[j]=t|1<<(n+4);g[n+4]|=1<<j
      for i in range(n):g[i]|=((t>>i)&1)<<j
     assert check(g,(1<<len(g))-1,3,kmax+1);wins[k]=dict(square=c,supports=w)
 return dict(cycles=len(cycles),patterns=patterns,successful=dict(stats),examples=wins)
for i,s in enumerate(src):
 r=run(decode(s));
 if r:out.append(dict(row=i,**r))
print(len(out),sum(r['cycles'] for r in out),[(k,sum(k in r['examples'] for r in out),sum(r['successful'].get(k,0) for r in out)) for k in ('import','greedy','edge_seed')]);(P/'ramsey_square_support_lift.json').write_text(json.dumps(out)+'\n')
