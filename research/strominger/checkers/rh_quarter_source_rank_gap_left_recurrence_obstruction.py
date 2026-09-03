import contextlib,io,itertools,json,runpy
from collections import deque
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')))
source_terms,k=g['source_terms'],g['k']
def edge(K,L):
 if len(K)<=1:return True
 return all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1))
def sig(neg,pos):
 neg=sorted(neg);pos=sorted(pos);N=len(neg);P=len(pos);s=N+P;t=s+1;n=t+1;C=[[F(0)]*n for _ in range(n)];E=set();d=sum(-z for _,z in neg)
 for a,(_,z) in enumerate(neg):C[s][a]=-z;E.add((s,a))
 for b,(_,z) in enumerate(pos):C[N+b][t]=z;E.add((N+b,t))
 for a,(K,_) in enumerate(neg):
  for b,(L,_) in enumerate(pos):
   if edge(K,L):C[a][N+b]=d;E.add((a,N+b))
 aug=rev=0;sent=F(0)
 while True:
  p=[None]*n;p[s]=s;q=deque([s])
  while q and p[t] is None:
   u=q.popleft()
   for v in range(n):
    if p[v] is None and C[u][v]>0:p[v]=u;q.append(v)
  if p[t] is None:break
  path=[];v=t
  while v!=s:path.append((p[v],v));v=p[v]
  x=min(C[u][v] for u,v in path);sent+=x;aug+=1;rev+=any((u,v) not in E for u,v in path)
  for u,v in path:C[u][v]-=x;C[v][u]+=x
 return sent==d,(aug,rev,N,P)
groups={};first=None;cases=0
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));sgn=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));V=[(K,sgn*z) for K,z in source_terms(R,Q)];ok,x=sig([v for v in V if v[1]<0],[v for v in V if v[1]>0]);key=(r,j-i,i);cases+=1
   if key not in groups:groups[key]=(x,S,j)
   elif x!=groups[key][0] and first is None:first={'rank':r,'gap':j-i,'left_endpoint':i,'first':{'base':groups[key][1],'right_endpoint':groups[key][2],'signature':groups[key][0]},'second':{'base':S,'right_endpoint':j,'signature':x}}
checks={'all_769_cases_checked':cases==769,'rank_gap_left_state_classified':first is not None};res={'schema':'marici.strominger.rh_quarter_source_rank_gap_left_recurrence_obstruction.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'Canonical augmenting data are tested for determination by rank, endpoint gap, and absolute left endpoint.','case_count':cases,'state_count':len(groups),'first_state_collision':first,'checks':checks};(base/'results'/'rh_quarter_source_rank_gap_left_recurrence_obstruction.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
