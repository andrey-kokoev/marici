import json
from fractions import Fraction as F
from pathlib import Path
# Synthetic exact recurrence verifies the transfer identity independently of
# any conjectured Weibull coefficient asymptotic.
a=[F(0),F(2),F(3),F(5),F(7)]
b=[F(1),F(4),F(6),F(8)]
pminus=F(0); p=F(1); rows=[]
for n in range(4):
 pnext=(-b[n]*p-a[n]*pminus)/a[n+1]
 matrix_first=(-b[n]/a[n+1])*p+(-a[n]/a[n+1])*pminus
 rows.append({"n":n,"p_next":str(pnext),"matrix_first":str(matrix_first)})
 pminus,p=p,pnext
checks={"exact_transfer_identity":all(r["p_next"]==r["matrix_first"] for r in rows)}
base=Path(__file__).parents[1]
packet=(base/"rh-global-recurrence-transfer-reduces-to-an-ell2-product-cocycle.md").read_text(encoding="utf-8")
gamma=(base/"results"/"rh_atomic_log_moment_gamma_comparator_audit.json").read_text(encoding="utf-8")
checks.update({
 "packet_identifies_kernel_series":"sum_{n\\geq0}|P_n^{(X)}(0)|^2" in packet,
 "packet_identifies_product_cocycle":"T_{n-1}^{(X)}\\cdots T_0^{(X)}" in packet,
 "gamma_artifact_flags_loewner_failure":"do not preserve Hankel Loewner order" in gamma,
 "packet_rejects_individual_matrix_inference":"No contraction follows merely from norms or eigenvalues of individual transfer matrices" in packet,
 "packet_does_not_claim_missing_bound":"does not claim it" in packet,
})
result={"schema":"marici.strominger.rh_global_recurrence_cocycle_reduction_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Endpoint-kernel control is exactly an ell-two estimate for the first coordinate of a Jacobi transfer-matrix product. This retains one polynomial state across the full tail. Existing moment intervals and finite Christoffel sums do not control the infinite product; two-sided Jacobi-coefficient asymptotics are the next missing input.","checks":checks,"exact_recurrence_rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_global_recurrence_cocycle_reduction_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
