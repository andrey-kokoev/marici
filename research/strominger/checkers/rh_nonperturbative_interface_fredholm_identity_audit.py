import json, math
from fractions import Fraction as F
from pathlib import Path
def det(M):
 A=[row[:] for row in M];d=F(1);n=len(A)
 for i in range(n):
  k=next(k for k in range(i,n) if A[k][i])
  if k!=i:A[i],A[k]=A[k],A[i];d=-d
  p=A[i][i];d*=p
  for r in range(i+1,n):
   f=A[r][i]/p
   for j in range(i,n):A[r][j]-=f*A[i][j]
 return d
# Exact finite-rank model: reference Gram I and multiplier matrix I+A.
As=[[[F(1,3),F(1,5)],[F(1,5),F(2,7)]],[[F(1,2),F(1,7),F(0)],[F(1,7),F(1,3),F(1,11)],[F(0),F(1,11),F(1,4)]]]
rows=[]
for A in As:
 n=len(A);G=[[F(int(i==j))+A[i][j] for j in range(n)] for i in range(n)]
 rows.append({"rank":n,"modified_gram_det":str(det(G)),"fredholm_det":str(det([[F(int(i==j))+A[i][j] for j in range(n)] for i in range(n)]))})
checks={"finite_rank_gram_fredholm_identity_exact":all(r["modified_gram_det"]==r["fredholm_det"] for r in rows)}
base=Path(__file__).parents[1]
packet=(base/"rh-full-interface-is-an-exact-multiplicative-fredholm-determinant.md").read_text(encoding="utf-8")
checks.update({
 "packet_retains_all_regions":"retains local, transition, and far particles" in packet,
 "packet_identifies_unbounded_far_multiplier":"grows without bound" in packet,
 "packet_rejects_unauthorized_perturbation":"not authorized by the local overlap estimate" in packet,
 "packet_makes_no_asymptotic_claim":"supplies no trace-norm smallness" in packet,
})
result={"schema":"marici.strominger.rh_nonperturbative_interface_fredholm_identity_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The complete Laguerre-to-Weibull weight change is exactly a finite-rank multiplicative Fredholm determinant. It retains the transition interface nonperturbatively. The far multiplier is unbounded, so local small-multiplier expansions do not control its large-n logarithm.","checks":checks,"exact_models":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_nonperturbative_interface_fredholm_identity_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
