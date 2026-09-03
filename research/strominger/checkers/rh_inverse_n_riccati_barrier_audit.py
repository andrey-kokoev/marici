import json
from fractions import Fraction as F
from pathlib import Path
rows=[]
for n in range(2,30):
 r=F(n**4,(n+1)**4);critical=F(1,n+1)-r/F(n-1)
 barrier=F(n-1,n)
 def T(rho,eps):return 1+r-eps-r/rho
 exact=T(barrier,critical);below=T(barrier,critical-F(1,n**5));above=T(barrier,critical+F(1,n**5))
 rows.append({"n":n,"critical_defect":str(critical),"exact_residual":str(exact-F(n,n+1)),"below_margin":str(below-F(n,n+1)),"above_margin":str(above-F(n,n+1))})
checks={
 "critical_barrier_exact":all(r["exact_residual"]=="0" for r in rows),
 "smaller_defect_propagates_above_barrier":all(F(r["below_margin"])>0 for r in rows),
 "deliberate_larger_defect_breaks_barrier":all(F(r["above_margin"])<0 for r in rows),
 "critical_defects_positive":all(F(r["critical_defect"])>0 for r in rows),
}
base=Path(__file__).parents[1];packet=(base/"rh-one-over-n-is-the-exact-riccati-barrier-for-positive-limit.md").read_text(encoding="utf-8")
checks.update({
 "packet_requires_signed_remainder":"Unsigned asymptotics are insufficient" in packet,
 "packet_separates_upper_bound_gate":"independent asymptotic estimate supplies \\(u_n=O(n^{-1})\\)" in packet,
 "packet_states_strict_positive_limit":"strictly positive limit" in packet,
})
result={"schema":"marici.strominger.rh_inverse_n_riccati_barrier_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The ratio (n-1)/n is an exact invariant Riccati barrier at epsilon*=1/(n+1)-r_n/(n-1). Any smaller defect propagates n u_n monotonicity; a deliberate larger defect reverses the barrier. Positive convergence additionally requires u_n=O(1/n).","checks":checks,"tested_degrees":"2..29","gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_inverse_n_riccati_barrier_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
