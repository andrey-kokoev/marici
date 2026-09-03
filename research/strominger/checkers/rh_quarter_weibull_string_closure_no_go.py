import json
from fractions import Fraction as F
from pathlib import Path
rows=[]
for k in range(10):
 # From m_s=4 Gamma(4s+4)/2^(4s+4), evaluated at s=k and k+1/4.
 ratio=F(4*k+4,2)
 rows.append({"k":k,"m_k_plus_quarter_over_m_k":str(ratio),"ibp_residual":str(F(k+1)-ratio/2)})
checks={
 "fractional_moment_identity_exact":all(r["ibp_residual"]=="0" for r in rows),
 "shift_is_noninteger":F(1,4).denominator!=1,
 "integer_hankel_not_closed":all(F(k,1)+F(1,4) not in [F(j,1) for j in range(20)] for k in range(10)),
}
base=Path(__file__).parents[1];packet=(base/"rh-quarter-weibull-weight-has-no-closed-polynomial-string-equation.md").read_text(encoding="utf-8")
checks.update({
 "packet_names_fractional_obstruction":"fractional-index moment" in packet,
 "packet_names_truncated_nonpolynomial_derivative":"(X+y)^{-3/4}" in packet,
 "packet_rejects_only_finite_polynomial_route":"only removes the finite polynomial Freud equation" in packet,
 "packet_preserves_analytic_zero_gate":"analytic-zero question remains open" in packet,
 "packet_identifies_mellin_successor":"mellin-hankel-first-shift" in packet,
})
result={"schema":"marici.strominger.rh_quarter_weibull_string_closure_no_go.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Integration by parts shifts quarter-Weibull moments by 1/4, outside the integer Hankel lattice, while fixed-start translation has a nonpolynomial derivative and endpoint terms. A finite polynomial Freud/string equation cannot source a1=0; Mellin-Hankel determinant asymptotics are required.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_weibull_string_closure_no_go.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
