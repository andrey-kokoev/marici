import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def leq(K,L):return all(a<=b for a,b in zip(K,L))
def flow(pos,neg,direction):
 P,N=len(pos),len(neg);s=P+N;t=s+1;adj=[[] for _ in range(t+1)]
 def add(u,v,c):adj[u].append([v,c,len(adj[v])]);adj[v].append([u,0,len(adj[u])-1])
 demand=sum(-v for _,v in neg)
 for a,(_,v) in enumerate(pos):add(s,a,v)
 for b,(_,v) in enumerate(neg):add(P+b,t,-v)
 for a,(K,_) in enumerate(pos):
  for b,(L,_) in enumerate(neg):
   if (leq(K,L) if direction=='up' else leq(L,K)):add(a,P+b,demand)
 total=0
 while True:
  level=[-1]*(t+1);level[s]=0;q=[s]
  for u in q:
   for v,c,_ in adj[u]:
    if c>0 and level[v]<0:level[v]=level[u]+1;q.append(v)
  if level[t]<0:break
  it=[0]*(t+1)
  def dfs(u,f):
   if u==t:return f
   while it[u]<len(adj[u]):
    e=adj[u][it[u]]
    if e[1]>0 and level[e[0]]==level[u]+1:
     z=dfs(e[0],min(f,e[1]))
     if z:e[1]-=z;adj[e[0]][e[2]][1]+=z;return z
    it[u]+=1
   return 0
  while True:
   z=dfs(s,demand-total)
   if not z:break
   total+=z
 return total,demand
stats={d:{'failed_cases':0,'first':None} for d in ('up','down')};cases=0
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));et=(-1)**(j-i+1) if i<j else (-1)**(i-j);expected=et*(-1)**(sum(x>i for x in T)+sum(x>j for x in T));terms=[(K,expected*v) for K,v in source_terms(R,S)];pos=[x for x in terms if x[1]>0];neg=[x for x in terms if x[1]<0];cases+=1
   for d in stats:
    sent,demand=flow(pos,neg,d)
    if sent<demand:
     stats[d]['failed_cases']+=1
     if stats[d]['first'] is None:stats[d]['first']={'base':T,'i':i,'j':j,'demand':str(demand),'sent':str(sent),'deficit':str(demand-sent)}
success=[d for d,s in stats.items() if s['failed_cases']==0]
result={'schema':'marici.strominger.rh_quarter_fixed_eight_gale_weighted_transport.v1','status':'passed' if success else 'failed','terminal_case_count':cases,'successful_directions':success,'statistics':stats,'verdict':'Exact Gale-comparable max flow covers all negative oriented mass only when the direction has zero failed cases.','checks':{'all_cases':cases==3584,'weighted_gale_certificate_found':bool(success)}}
(base/'results'/'rh_quarter_fixed_eight_gale_weighted_transport.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
