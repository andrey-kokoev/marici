import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")));Q,D,mu=g["Q"],g["D"],g["mu"]
def add(a,b,s=1):
 r=[F(0)]*max(len(a),len(b))
 for i,z in enumerate(a):r[i]+=z
 for i,z in enumerate(b):r[i]+=s*z
 while len(r)>1 and r[-1]==0:r.pop()
 return r
def routh(p):
 a=list(reversed(p));n=len(a)-1;m=(n+2)//2;T=[[F(0)]*m for _ in range(n+1)];T[0][:len(a[0::2])]=a[0::2];T[1][:len(a[1::2])]=a[1::2]
 for i in range(2,n+1):
  if T[i-1][0]==0:return False,i
  for j in range(m-1):T[i][j]=(T[i-1][0]*T[i-2][j+1]-T[i-2][0]*T[i-1][j+1])/T[i-1][0]
 return all(row[0]>0 for row in T),None
records=[];first_failure=None
for n in range(2,9):
 for s in range(3):
  P=mu(mu(Q(s+n-1),D(n-1,s)),D(n-1,s+2));R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));A=add(P,R,-1);N=add(P,R);ast,az=routh(A);nst,nz=routh(N);same_degree=len(P)==len(R) and P[-1]==R[-1];rec={"n":n,"shift":s,"A_degree":len(A)-1,"N_degree":len(N)-1,"A_hurwitz":ast,"N_hurwitz":nst,"ratio_feedthrough_one":same_degree,"A_zero_pivot":az,"N_zero_pivot":nz};records.append(rec)
  if not(ast and nst and same_degree) and first_failure is None:first_failure=rec
checks={"twenty_one_cayley_pairs_checked":len(records)==21,"difference_denominators_hurwitz":all(r["A_hurwitz"] for r in records),"sum_numerators_hurwitz":all(r["N_hurwitz"] for r in records),"bounded_real_ratio_has_unit_feedthrough":all(r["ratio_feedthrough_one"] for r in records)}
result={"schema":"marici.strominger.rh_quarter_D_cayley_positive_real_pair.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The Cayley transform of S=R/P is F=(1+S)/(1-S)=(P+R)/(P-R). Exact Routh arrays test whether both numerator and denominator are Hurwitz while S has unit feedthrough. Passing supplies a stable positive-real pair but not the missing positivity of Re F.","records":records,"first_failure":first_failure,"checks":checks}
(base/"results"/"rh_quarter_D_cayley_positive_real_pair.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"first_failure":first_failure,"checks":checks},indent=2))
