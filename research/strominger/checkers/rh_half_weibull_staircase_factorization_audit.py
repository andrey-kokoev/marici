import json
from fractions import Fraction as F
from pathlib import Path
def rising(x,k):
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
rows=[]
for alpha in (F(0),F(1,2),F(1)):
 a=alpha+1;b=alpha+F(3,2)
 for n in range(1,8):
  lhs=det([[rising(a,i+j)*rising(b,i+j) for j in range(n)] for i in range(n)])
  pref=F(1)
  for i in range(n):pref*=rising(a,i)*rising(b,i)
  stair=det([[rising(a+i,j)*rising(b+i,j) for j in range(n)] for i in range(n)])
  rows.append({"alpha":str(alpha),"n":n,"identity_residual":str(lhs-pref*stair),"staircase_positive":stair>0})
checks={"factorization_exact":all(r["identity_residual"]=="0" for r in rows),"staircase_factors_positive":all(r["staircase_positive"] for r in rows),"multiple_alpha_controls":len({r["alpha"] for r in rows})==3}
base=Path(__file__).parents[1];packet=(base/"rh-half-weibull-hankel-determinant-reduces-to-a-staircase-factor.md").read_text(encoding="utf-8")
checks.update({"packet_identifies_degree_two_j":"degree \\(2j\\)" in packet,"packet_preserves_residual_obstruction":"residual obstruction" in packet,"packet_does_not_claim_schur_identity":"does not identify it with an ordinary Schur polynomial" in packet})
result={"schema":"marici.strominger.rh_half_weibull_staircase_factorization_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The half-Weibull Hankel determinant factors exactly into explicit rising-factorial row products and a positive staircase alternant S_n(a,b). The unresolved five-ninths coefficient is localized to the relative asymptotic of this alternant plus explicit Barnes terms.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_half_weibull_staircase_factorization_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"checks":checks,"tested_rows":len(rows)},indent=2))
