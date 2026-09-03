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
def signature(neg,pos):
 neg=sorted(neg);pos=sorted(pos);N=len(neg);P=len(pos);s=N+P;t=s+1;n=t+1;cap=[[F(0)]*n for _ in range(n)];original=set();demand=sum(-z for _,z in neg)
 for a,(K,z) in enumerate(neg):cap[s][a]=-z;original.add((s,a))
 for b,(L,z) in enumerate(pos):cap[N+b][t]=z;original.add((N+b,t))
 for a,(K,z) in enumerate(neg):
  for b,(L,w) in enumerate(pos):
   if edge(K,L):cap[a][N+b]=demand;original.add((a,N+b))
 sent=F(0);rev=0;aug=0
 while True:
  prev=[None]*n;prev[s]=s;q=deque([s])
  while q and prev[t] is None:
   u=q.popleft()
   for v in range(n):
    if prev[v] is None and cap[u][v]>0:prev[v]=u;q.append(v)
  if prev[t] is None:break
  path=[];v=t
  while v!=s:path.append((prev[v],v));v=prev[v]
  qmin=min(cap[u][v] for u,v in path);sent+=qmin;aug+=1;rev+=any((u,v) not in original for u,v in path)
  for u,v in path:cap[u][v]-=qmin;cap[v][u]+=qmin
 return sent==demand,(aug,rev,N,P)
groups={};cases=0;first=None
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));sgn=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,sgn*z) for K,z in source_terms(R,Q)];neg=[x for x in vals if x[1]<0];pos=[x for x in vals if x[1]>0];ok,sig=signature(neg,pos);key=(r,j-i);cases+=1
   if key not in groups:groups[key]={'signature':sig,'base':S,'i':i,'j':j,'count':1}
   else:
    groups[key]['count']+=1
    if sig!=groups[key]['signature'] and first is None:first={'rank':r,'gap':j-i,'first_case':{'base':groups[key]['base'],'i':groups[key]['i'],'j':groups[key]['j'],'signature':groups[key]['signature']},'second_case':{'base':S,'i':i,'j':j,'signature':sig}}
checks={'all_769_cases_checked':cases==769,'rank_gap_recurrence_classified':first is not None};res={'schema':'marici.strominger.rh_quarter_source_rank_gap_recurrence_obstruction.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'The simplest source recurrence rival, in which canonical augmenting data depend only on source rank and endpoint gap, is tested exactly.','case_count':cases,'group_count':len(groups),'first_rank_gap_collision':first,'checks':checks};(base/'results'/'rh_quarter_source_rank_gap_recurrence_obstruction.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8');print(json.dumps(res,indent=2))
