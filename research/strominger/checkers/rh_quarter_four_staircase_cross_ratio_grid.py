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
  q=a[k][k];out*=q
  for j in range(k,n):a[k][j]/=q
  for i in range(k+1,n):
   q=a[i][k]
   for j in range(k,n):a[i][j]-=q*a[k][j]
 return out
@lru_cache(maxsize=None)
def S(n,ss):return F(1) if n==0 else det([[reduce(lambda z,s:z*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
def sh(ss,c):return tuple(s+c for s in ss)
def q(ss,i):return reduce(lambda z,s:z*(s+i),ss,F(1))
ss=(F(1),F(5,4),F(3,2),F(7,4));rows=[]
for n in range(2,61):
 first=q(ss,n-1)*S(n-1,ss)*S(n-1,sh(ss,2));cross=q(ss,0)*S(n-1,sh(ss,1))**2;theta=cross/first
 rows.append({"n":n,"theta":float(theta),"n_theta":float(n*theta),"n2_theta":float(n*n*theta),"identity_residual":str(S(n,ss)*S(n-2,sh(ss,2))-first+cross)})
late=rows[-5:]
spread1=max(r["n_theta"] for r in late)-min(r["n_theta"] for r in late);spread2=max(r["n2_theta"] for r in late)-min(r["n2_theta"] for r in late)
rel1=spread1/(sum(r["n_theta"] for r in late)/len(late));rel2=spread2/(sum(r["n2_theta"] for r in late)/len(late))
checks={"condensation_identity_exact":all(r["identity_residual"]=="0" for r in rows),"cross_ratios_between_zero_and_one":all(0<r["theta"]<1 for r in rows),"theta_decreases":all(rows[i+1]["theta"]<rows[i]["theta"] for i in range(len(rows)-1)),"inverse_square_has_smaller_relative_spread":rel2<rel1,"finite_scaled_values":all(math.isfinite(r["n2_theta"]) for r in rows)}
winner="n^-1" if rel1<rel2 else "n^-2"
result={"schema":"marici.strominger.rh_quarter_four_staircase_cross_ratio_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"Exact four-staircase cross ratios through n=60 favor {winner} scaling by late-window spread. This finite diagnostic identifies the candidate order but not a limit theorem.","checks":checks,"winner":winner,"rows":rows,"late_rows":late,"late_spreads":{"n_theta":spread1,"n2_theta":spread2,"relative_n_theta":rel1,"relative_n2_theta":rel2},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
