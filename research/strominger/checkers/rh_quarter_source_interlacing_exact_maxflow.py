import itertools,json,runpy
from fractions import Fraction as F
from collections import deque
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_terminal_minor_source_formula.py")))
source_terms,k=g["source_terms"],g["k"]
def interlace(K,L):
 if len(K)<=1:return True
 return all(K[x]<=L[x]<=K[x+1] for x in range(len(K)-1)) or all(L[x]<=K[x]<=L[x+1] for x in range(len(K)-1))
def flow(neg,pos):
 n,m=len(neg),len(pos);N=n+m+2;s=N-2;t=N-1;cap={};adj=[set() for _ in range(N)];total=sum(z for _,z in neg)
 def add(a,b,z):cap[a,b]=cap.get((a,b),F(0))+z;cap.setdefault((b,a),F(0));adj[a].add(b);adj[b].add(a)
 for a,(_,z) in enumerate(neg):add(s,a,z)
 for b,(_,z) in enumerate(pos):add(n+b,t,z)
 for a,(K,_) in enumerate(neg):
  for b,(L,_) in enumerate(pos):
   if interlace(K,L):add(a,n+b,total)
 value=F(0)
 while True:
  par={s:None};q=deque([s])
  while q and t not in par:
   a=q.popleft()
   for b in adj[a]:
    if b not in par and cap[a,b]>0:par[b]=a;q.append(b)
  if t not in par:break
  z=total-value;b=t
  while b!=s:z=min(z,cap[par[b],b]);b=par[b]
  b=t
  while b!=s:a=par[b];cap[a,b]-=z;cap[b,a]+=z;b=a
  value+=z
 reach={s};q=deque([s])
 while q:
  a=q.popleft()
  for b in adj[a]:
   if b not in reach and cap[a,b]>0:reach.add(b);q.append(b)
 return value,total,{"reachable_negative_count":sum(a in reach for a in range(n)),"reachable_positive_count":sum(n+b in reach for b in range(m)),"deficit":str(total-value)}
cases=0;passed=0;first_failure=None
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));expected=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[(K,expected*z) for K,z in source_terms(R,Q)];neg=[(K,-z) for K,z in vals if z<0];pos=[(K,z) for K,z in vals if z>0];v,total,cut=flow(neg,pos);cases+=1
   if v==total:passed+=1
   elif first_failure is None:first_failure={"base":S,"i":i,"j":j,"negative_term_count":len(neg),"positive_term_count":len(pos),"cut":cut}
checks={"all_769_cases_checked":cases==769,"exact_interlacing_flow_classified":passed<=cases,"universal_interlacing_transport":passed==cases}
result={"schema":"marici.strominger.rh_quarter_source_interlacing_exact_maxflow.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact rational max-flow decides whether interlacing edges carry all negative source mass into positive capacity. Universal success gives a bounded weighted-transport certificate; failure supplies a minimum-cut deficit and rejects interlacing as the all-order cancellation relation.","case_count":cases,"feasible_case_count":passed,"infeasible_case_count":cases-passed,"first_failure":first_failure,"checks":checks}
(base/"results"/"rh_quarter_source_interlacing_exact_maxflow.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
