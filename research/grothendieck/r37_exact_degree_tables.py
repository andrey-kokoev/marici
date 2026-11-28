"""Meet three-row incidence sums against their complements; test distinct six-row completions."""
from itertools import combinations
from collections import defaultdict,deque,Counter
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'voevodsky/results';cores=json.loads((D/'ramsey_37_catalogue_free.json').read_text())['certificates'];tot=Counter();examples={}
for idx,rec in enumerate(cores):
 a=rec['core'];R=[sum(1<<i for i in t) for t in combinations(range(16),5) if all(not a[i]>>j&1 for i,j in combinations(t,2))];M={r:sum(1<<i for i,s in enumerate(R) if not r&s) for r in R};V={r:sum(1<<(3*i) for i in range(16) if r>>i&1) for r in R};target=sum((6-x.bit_count())<<(3*i) for i,x in enumerate(a));A={r:[t for i in range(15) if (r>>i)&3 in (1,2) and (t:=r^(3<<i)) in V] for r in R};dist={}
 for r in R:
  q=deque([r]);dist[r,r]=0
  while q:
   x=q.popleft()
   for y in A[x]:
    if (r,y) not in dist:dist[r,y]=1+dist[r,x];q.append(y)
 buckets=defaultdict(list)
 for t in combinations(sorted(R),3):buckets[sum(V[r] for r in t)].append(t)
 count=Counter()
 for k,L in buckets.items():
  for left in L:
   for right in buckets.get(target-k,()):
    if left[-1]>=right[0]:continue
    T=left+right;count['tuples']+=1;pairs=list(combinations(T,2));d=min(dist.get(p,999) for p in pairs);mass=sum(M[r].bit_count() for r in T)
    for typ,ok,detail in [('distance',d==999 or not any(M[r]&M[s] for r,s in pairs if dist.get((r,s))==d),d),('weight',mass<=len(R),(mass,len(R)))]:
     if ok:count[typ]+=1;examples.setdefault(typ,(idx,T,detail))
    for r,s in pairs:
     for t in A[r]:
      u=s^(r^t)
      if u not in A[s] or (r&(r^t))!=(u&(r^t)) or len({r,s,t,u})!=4 or t in T or u in T:continue
      if not ((M[r]&M[u]|M[t]&M[s])&~(M[r]&M[s]|M[t]&M[u])):
       count['square_fail']+=1;examples.setdefault('square_fail',(idx,T,(r,s,t,u)))
      count['square']+=1
 for key,v in count.items():tot[key]+=v;tot[key+'_cores']+=1
print(tot,examples)
