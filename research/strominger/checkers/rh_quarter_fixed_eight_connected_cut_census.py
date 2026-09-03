import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def leq(K,L):return all(a<=b for a,b in zip(K,L))
def comparable(K,L):return leq(K,L) or leq(L,K)
def forced_cut(pos,neg,force):
 P,N=len(pos),len(neg);s=P+N;t=s+1;Q=sum(-v for _,v in neg);INF=Q+sum(v for _,v in pos)+1;adj=[[] for _ in range(t+1)]
 def add(u,v,c):adj[u].append([v,c,len(adj[v])]);adj[v].append([u,0,len(adj[u])-1])
 for a,(_,v) in enumerate(pos):add(a,t,v)
 for b,(_,v) in enumerate(neg):add(s,P+b,-v)
 add(s,P+force,INF)
 for b,(L,_) in enumerate(neg):
  for a,(K,_) in enumerate(pos):
   if comparable(K,L):add(P+b,a,INF)
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
   z=dfs(s,INF)
   if not z:break
   total+=z
 seen={s};stack=[s]
 while stack:
  u=stack.pop()
  for v,c,_ in adj[u]:
   if c>0 and v not in seen:seen.add(v);stack.append(v)
 D=[neg[b][0] for b in range(N) if P+b in seen]
 return total-Q,D
cases=0;forced_cuts=0;global_min=None;record=None;shape_counts={}
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));et=(-1)**(j-i+1) if i<j else (-1)**(i-j);expected=et*(-1)**(sum(x>i for x in T)+sum(x>j for x in T));terms=[(K,expected*v) for K,v in source_terms(R,S)];pos=[x for x in terms if x[1]>0];neg=[x for x in terms if x[1]<0];cases+=1
   for q in range(len(neg)):
    slack,D=forced_cut(pos,neg,q);forced_cuts+=1;shape_counts[str(len(D))]=shape_counts.get(str(len(D)),0)+1
    if global_min is None or slack<global_min:global_min=slack;record={'base':T,'i':i,'j':j,'forced_label':neg[q][0],'minimizing_subset':D,'slack':str(slack)}
result={'schema':'marici.strominger.rh_quarter_fixed_eight_connected_cut_census.v1','status':'passed' if global_min is not None and global_min>=0 else 'failed','terminal_case_count':cases,'forced_cut_count':forced_cuts,'minimum_nonempty_connected_slack':str(global_min),'minimum_record':record,'minimizer_size_counts':shape_counts,'verdict':'Forcing each negative label and minimizing by exact cut enumerates the minimum nonempty Hall slack; any minimizer decomposes to a connected deficient/minimal component by the connected-cut theorem.','checks':{'all_cases':cases==3584,'nonempty_cuts_tested':forced_cuts>0,'all_connected_cut_slacks_nonnegative':global_min>=0}}
(base/'results'/'rh_quarter_fixed_eight_connected_cut_census.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
