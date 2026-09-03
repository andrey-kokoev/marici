import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def cover(A,B):
 d=[b-a for a,b in zip(A,B)];return (all(x>=0 for x in d) and sum(d)==1) or (all(x<=0 for x in d) and sum(d)==-1)
def cut(pos,neg,force):
 P,N=len(pos),len(neg);s=P+N;t=s+1;Q=sum(-v for _,v in neg);INF=Q+sum(v for _,v in pos)+1;G=[[] for _ in range(t+1)]
 def add(u,v,c):G[u].append([v,c,len(G[v])]);G[v].append([u,0,len(G[u])-1])
 for a,(_,v) in enumerate(pos):add(a,t,v)
 for b,(_,v) in enumerate(neg):add(s,P+b,-v)
 add(s,P+force,INF)
 for b,(L,_) in enumerate(neg):
  for a,(K,_) in enumerate(pos):
   if cover(K,L):add(P+b,a,INF)
 f=0
 while True:
  lev=[-1]*(t+1);lev[s]=0;q=[s]
  for u in q:
   for v,c,_ in G[u]:
    if c and lev[v]<0:lev[v]=lev[u]+1;q.append(v)
  if lev[t]<0:break
  it=[0]*(t+1)
  def dfs(u,x):
   if u==t:return x
   while it[u]<len(G[u]):
    e=G[u][it[u]]
    if e[1] and lev[e[0]]==lev[u]+1:
     z=dfs(e[0],min(x,e[1]))
     if z:e[1]-=z;G[e[0]][e[2]][1]+=z;return z
    it[u]+=1
   return 0
  while True:
   z=dfs(s,INF)
   if not z:break
   f+=z
 seen={s};st=[s]
 while st:
  u=st.pop()
  for v,c,_ in G[u]:
   if c and v not in seen:seen.add(v);st.append(v)
 D=[neg[b][0] for b in range(N) if P+b in seen]
 return f-Q,D
cases=0;cuts=0;best=None;rec=None
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   xs=source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))));o=1 if sum(v for _,v in xs)>0 else -1;xs=[(K,o*v) for K,v in xs];pos=[x for x in xs if x[1]>0];neg=[x for x in xs if x[1]<0];cases+=1
   for q in range(len(neg)):
    z,D=cut(pos,neg,q);cuts+=1
    if best is None or z<best:best=z;rec={'base':T,'i':i,'j':j,'forced_label':neg[q][0],'demand_set':D,'demand_set_size':len(D),'slack':str(z)}
result={'schema':'marici.strominger.rh_quarter_gale_cover_minimum_multidemand_cut.v1','status':'passed' if best>=0 else 'failed','bold_conjecture':'The minimum nonempty Hasse Hall cut is genuinely multi-demand.','terminal_cases':cases,'forced_cuts':cuts,'minimum_slack':str(best),'minimum_record':rec,'falsification':{'survives':rec['demand_set_size']>1,'extremal_size':rec['demand_set_size']},'checks':{'all_cases':cases==3584,'nonnegative':best>=0}}
(base/'results'/'rh_quarter_gale_cover_minimum_multidemand_cut.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
