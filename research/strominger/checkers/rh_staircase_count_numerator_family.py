import json,math
from fractions import Fraction as F
from functools import reduce,lru_cache
from pathlib import Path
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def det(a):
 a=[r[:] for r in a];n=len(a);out=F(1)
 for k in range(n):
  p=next(i for i in range(k,n) if a[i][k]);a[k],a[p]=a[p],a[k]
  if p!=k:out=-out
  z=a[k][k];out*=z
  for j in range(k,n):a[k][j]/=z
  for i in range(k+1,n):
   z=a[i][k]
   for j in range(k,n):a[i][j]-=z*a[k][j]
 return out
@lru_cache(None)
def S(n,p,t):
 ss=tuple(F(1)+F(k,p)+t for k in range(p))
 return F(1) if n==0 else det([[reduce(lambda z,s:z*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  k=max(range(i,m),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];z=A[i][i]
  for j in range(i,m+1):A[i][j]/=z
  for r in range(m):
   if r!=i:
    z=A[r][i]
    for j in range(i,m+1):A[r][j]-=z*A[i][j]
 return [A[i][-1] for i in range(m)]
def fit(p,t):
 ms=range(20,29);X=[[1,1/m,1/m**2] for m in ms];y=[float(S(m,p,t+1)**2/(S(m,p,t)*S(m,p,t+2)))/m**2 for m in ms];G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];return solve(G,b)[0]
rows=[]
for p in (3,4,5):
 vals=[]
 for t in range(8,13):
  C=fit(p,t);vals.append({"shift":t,"C_fit":C,"count_scaled":p*(t+2)**2*C})
 rows.append({"staircase_count":p,"values":vals,"last":vals[-1]["count_scaled"]})
scaling=[]
for p in (3,4,5):
 vals={k:[float(S(m,p,9)**2/(S(m,p,8)*S(m,p,10)))/m**k for m in range(20,29)] for k in range(5)}
 spreads={k:(max(v)-min(v))/(sum(v)/len(v)) for k,v in vals.items()};winner=min(spreads,key=spreads.get)
 scaling.append({"staircase_count":p,"relative_spreads":spreads,"winner":winner})
checks={"all_fits_positive":all(v["C_fit"]>0 for r in rows for v in r["values"]),"four_count_amplitude_control_near_one":abs(rows[1]["last"]-1)<.08,"control_window_fails_to_select_known_p4_power":scaling[1]["winner"]!=2,"cross_count_comparison_inadmissible":not all(r["winner"]==2 for r in scaling),"one_over_p_not_promoted_from_incompatible_fits":abs(rows[0]["last"]-1)>.5 and abs(rows[2]["last"]-1)>1}
result={"schema":"marici.strominger.rh_staircase_count_numerator_family.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The p=3,4,5 comparison is not compatible: the declared degree window fails to recover the known m^2 control for p=4 and does not establish common scaling for adjacent counts. Therefore the quarter numerator cannot be derived or refuted by these 1/p fits.","checks":checks,"rows":rows,"degree_scaling":scaling,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_staircase_count_numerator_family.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
