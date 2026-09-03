import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def cover(A,B):
 d=[b-a for a,b in zip(A,B)];return (all(x>=0 for x in d) and sum(d)==1) or (all(x<=0 for x in d) and sum(d)==-1)
def flow(pos,neg):
 P,N=len(pos),len(neg);s=P+N;t=s+1;Q=sum(-v for _,v in neg);INF=Q+1;adj=[[] for _ in range(t+1)]
 def add(u,v,c):adj[u].append([v,c,len(adj[v])]);adj[v].append([u,0,len(adj[u])-1])
 for a,(_,v) in enumerate(pos):add(s,a,v)
 for b,(_,v) in enumerate(neg):add(P+b,t,-v)
 for a,(K,_) in enumerate(pos):
  for b,(L,_) in enumerate(neg):
   if cover(K,L):add(a,P+b,INF)
 total=0
 while True:
  lev=[-1]*(t+1);lev[s]=0;q=[s]
  for u in q:
   for v,c,_ in adj[u]:
    if c and lev[v]<0:lev[v]=lev[u]+1;q.append(v)
  if lev[t]<0:return total,Q
  it=[0]*(t+1)
  def dfs(u,f):
   if u==t:return f
   while it[u]<len(adj[u]):
    e=adj[u][it[u]]
    if e[1] and lev[e[0]]==lev[u]+1:
     z=dfs(e[0],min(f,e[1]))
     if z:e[1]-=z;adj[e[0]][e[2]][1]+=z;return z
    it[u]+=1
   return 0
  while True:
   z=dfs(s,INF)
   if not z:break
   total+=z
cases=0;obstruction=None
for r in range(k-1):
 if obstruction:break
 for T in itertools.combinations(range(k),r):
  if obstruction:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   xs=source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))));o=1 if sum(v for _,v in xs)>0 else -1;xs=[(K,o*v) for K,v in xs];pos=[x for x in xs if x[1]>0];neg=[x for x in xs if x[1]<0];f,Q=flow(pos,neg);cases+=1
   if f<Q:obstruction={'base':T,'i':i,'j':j,'negative_demand':str(Q),'max_cover_flow':str(f),'deficit':str(Q-f),'positive_count':len(pos),'negative_count':len(neg)};break
result={'schema':'marici.strominger.rh_quarter_gale_cover_edge_maxflow.v1','status':'failed' if obstruction else 'passed','terminal_cases_reached':cases,'first_obstruction':obstruction,'verdict':'Gale-cover edges do not suffice for exact signed transport.' if obstruction else 'Gale-cover edges support exact signed transport in all fixed-eight terminal cases.','checks':{'cases_tested':cases>0,'universal_cover_flow':obstruction is None}}
(base/'results'/'rh_quarter_gale_cover_edge_maxflow.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
