import json
from fractions import Fraction as F
from pathlib import Path
beta=F(1,4);rows=[]
for k in range(1,6):rows.append({"translation_order":k,"degree_exponent":str((beta-k)/beta)})
checks={
 "first_translation_exponent_is_minus_three":(beta-1)/beta==-3,
 "translation_exponents_advance_by_minus_four":all((beta-(k+1))/beta-(beta-k)/beta==-4 for k in range(1,5)),
 "first_five_exponents_exact":rows==[{"translation_order":k,"degree_exponent":str(1-4*k)} for k in range(1,6)],
}
base=Path(__file__).parents[1]
prior=json.loads((base/"results"/"rh_truncation_relative_exponent_discrimination_audit.json").read_text(encoding="utf-8"))
checks["offdiagonal_finite_slopes_match_minus_three"]=all(abs(r["relative_a_power_slope"]+3)<.03 for r in prior["rows"])
packet=(base/"rh-fixed-start-weibull-perturbation-enters-at-n-minus-three.md").read_text(encoding="utf-8")
checks.update({
 "packet_uses_fixed_start_saddle":"At fixed \\(X\\)" in packet and "y_n\\asymp n^{1/\\beta}" in packet,
 "packet_rejects_three_quarter_degree_term":"does not source an \\(n^{-3/4}\\) term" in packet,
 "packet_preserves_ordinary_inverse_degree_terms":"may still contain ordinary inverse-degree corrections" in packet,
 "packet_marks_power_counting_not_proof":"does not prove full Jacobi expansions" in packet,
})
result={"schema":"marici.strominger.rh_fixed_start_weibull_expansion_class_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"At the fixed-X saddle y_n~n^(1/beta), the k-th compact-translation term scales as n^(1-k/beta). For beta=1/4, truncation-specific powers are n^-3,n^-7,..., while ordinary 1/n corrections may come from the unshifted Jacobi expansion. This sources the observed relative n^-3 effect and rejects 3/4 as a degree exponent.","checks":checks,"translation_exponents":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_fixed_start_weibull_expansion_class_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
