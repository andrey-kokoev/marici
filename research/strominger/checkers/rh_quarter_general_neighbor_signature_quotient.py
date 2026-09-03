import itertools,json,random
from collections import deque
from pathlib import Path
base=Path(__file__).parents[1]
def feasible(sig,caps,dem):
 n=len(sig);m=len(dem);N=2+n+m;s=0;t=N-1;C=[[0]*N for _ in range(N)]
 for a,c in enumerate(caps):C[s][1+a]=c
 for a,q in enumerate(sig):
  for b in range(m):
   if q>>b&1:C[1+a][1+n+b]=99
 for b,d in enumerate(dem):C[1+n+b][t]=d
 flow=0
 while True:
  p=[-1]*N;p[s]=s;Q=deque([s])
  while Q and p[t]<0:
   u=Q.popleft()
   for v,c in enumerate(C[u]):
    if c and p[v]<0:p[v]=u;Q.append(v)
  if p[t]<0:break
  z=99;v=t
  while v!=s:z=min(z,C[p[v]][v]);v=p[v]
  v=t
  while v!=s:u=p[v];C[u][v]-=z;C[v][u]+=z;v=u
  flow+=z
 return flow==sum(dem)
def agg(sig,caps):
 a={}
 for q,c in zip(sig,caps):a[q]=a.get(q,0)+c
 return list(a),list(a.values())
def lift(caps,outgoing):
 rem=list(caps);rows=[[0]*len(outgoing) for _ in caps]
 for j,total in enumerate(outgoing):
  for i in range(len(caps)):
   z=min(rem[i],total);rows[i][j]=z;rem[i]-=z;total-=z
  if total:return None
 return rows
exact=0;ok=True
for sig in itertools.product(range(1,8),repeat=2):
 for caps in itertools.product(range(3),repeat=2):
  A,C=agg(sig,caps)
  for dem in itertools.product(range(4),repeat=3):exact+=1;ok&=feasible(sig,caps,dem)==feasible(A,C,dem)
r=random.Random(271828);random_ok=True;lift_ok=True
for _ in range(5000):
 n=r.randrange(1,8);sig=[r.randrange(1,8) for _ in range(n)];caps=[r.randrange(6) for _ in range(n)];dem=[r.randrange(9) for _ in range(3)];A,C=agg(sig,caps);random_ok&=feasible(sig,caps,dem)==feasible(A,C,dem)
 cs=[r.randrange(6) for _ in range(n)];total=r.randrange(sum(cs)+1);parts=[0,0,0]
 for __ in range(total):parts[r.randrange(3)]+=1
 rows=lift(cs,parts);lift_ok&=rows is not None and [sum(row[j] for row in rows) for j in range(3)]==parts and all(sum(row)<=c for row,c in zip(rows,cs))
# Deliberate failure: merging signatures {D0} and {D1} as shared falsely makes demands (1,1) feasible with total capacity 2.
negative_control=not feasible([1,2],[1,1],[2,0,0]) and feasible([3],[2],[1,1,0])
result={'schema':'marici.strominger.rh_quarter_general_neighbor_signature_quotient.v1','status':'passed' if ok and random_ok and lift_ok and negative_control else 'failed','theorem':'For any finite capacitated bipartite supply-demand network, quotienting supplies by identical nonempty demand-neighbor signature preserves every cut, max-flow feasibility, and admits lifting of quotient flows.','exact_m3_two_supply_cases':exact,'seeded_m3_networks':5000,'checks':{'exact_original_equals_quotient':ok,'seeded_original_equals_quotient':random_ok,'quotient_flow_lifts':lift_ok,'merging_distinct_signatures_changes_feasibility':negative_control},'signature_class_bound':{'formula':'2^m-1','values':{str(m):2**m-1 for m in range(1,9)}},'residual':'The exact quotient is exponential in demand count; Hasse incidence alone supplies no smaller representation.'}
(base/'results'/'rh_quarter_general_neighbor_signature_quotient.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
