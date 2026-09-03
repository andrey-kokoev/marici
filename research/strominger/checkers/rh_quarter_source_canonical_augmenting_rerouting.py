import contextlib,io,itertools,json,runpy
from collections import deque
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
with contextlib.redirect_stdout(io.StringIO()):
 g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')))
source_terms,k=g['source_terms'],g['k']
def edge(K,L):
 if len(K)<=1:return True
 return all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1))
def flow(neg,pos):
 neg=sorted(neg);pos=sorted(pos);N=len(neg);P=len(pos);s=N+P;t=s+1;n=t+1;cap=[[F(0)]*n for _ in range(n)];original=set();demand=sum(-z for _,z in neg)
 for a,(K,z) in enumerate(neg):cap[s][a]=-z;original.add((s,a))
 for b,(L,z) in enumerate(pos):cap[N+b][t]=z;original.add((N+b,t))
 for a,(K,z) in enumerate(neg):
  for b,(L,w) in enumerate(pos):
   if edge(K,L):cap[a][N+b]=demand;original.add((a,N+b))
 sent=F(0);reverse_used=False;augmentations=0
 while True:
  prev=[None]*n;prev[s]=s;q=deque([s])
  while q and prev[t] is None:
   u=q.popleft()
   for v in range(n):
    if prev[v] is None and cap[u][v]>0:prev[v]=u;q.append(v)
  if prev[t] is None:break
  path=[];v=t
  while v!=s:path.append((prev[v],v));v=prev[v]
  qmin=min(cap[u][v] for u,v in path);sent+=qmin;augmentations+=1
  if any((u,v) not in original for u,v in path):reverse_used=True
  for u,v in path:cap[u][v]-=qmin;cap[v][u]+=qmin
 return sent==demand,reverse_used,augmentations
cases=0;feasible=0;rerouted=0;first=None;maxaug=0
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));sgn=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,sgn*z) for K,z in source_terms(R,Q)];neg=[x for x in vals if x[1]<0];pos=[x for x in vals if x[1]>0];ok,rev,a=flow(neg,pos);cases+=1;feasible+=ok;rerouted+=rev;maxaug=max(maxaug,a)
   if rev and first is None:first={'base':S,'i':i,'j':j,'augmentations':a}
checks={'all_769_cases_checked':cases==769,'all_feasible':feasible==cases,'rerouting_classified':rerouted==0 or first is not None};r={'schema':'marici.strominger.rh_quarter_source_canonical_augmenting_rerouting.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'Canonical lexicographic Edmonds-Karp transport is audited for reverse residual-edge use, distinguishing forward-only allocation from globally coordinated rerouting.','case_count':cases,'feasible_case_count':feasible,'rerouting_case_count':rerouted,'first_rerouting_case':first,'maximum_augmentations':maxaug,'checks':checks};(base/'results'/'rh_quarter_source_canonical_augmenting_rerouting.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,indent=2))
