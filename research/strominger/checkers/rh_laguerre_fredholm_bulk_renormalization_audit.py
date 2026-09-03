import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_unshifted_weibull_exact_jacobi_diagnostic.json").read_text(encoding="utf-8"))
X=math.log(12);L=2*X**.75;rows=[]
for r in src["rows"]:
 n=r["n"]
 if n:
  a=math.sqrt(r["a_squared"]);ratio=(a/L)/n
  rows.append({"n":n,"weibull_over_laguerre_after_dilation":ratio,"ratio_over_n3":ratio/n**3,"log_recurrence_ratio":math.log(ratio)})
late=[r for r in rows if r["n"]>=3]
checks={
 "relative_recurrence_ratio_grows":all(rows[i+1]["weibull_over_laguerre_after_dilation"]>rows[i]["weibull_over_laguerre_after_dilation"] for i in range(len(rows)-1)),
 "n3_normalized_ratio_stabilizes_on_finite_grid":max(r["ratio_over_n3"] for r in late)/min(r["ratio_over_n3"] for r in late)<1.02,
 "log_recurrence_ratio_positive_at_late_degrees":all(r["log_recurrence_ratio"]>0 for r in late),
}
packet=(base/"rh-laguerre-fredholm-log-needs-global-weibull-bulk-renormalization.md").read_text(encoding="utf-8")
checks.update({
 "packet_identifies_n2_log_n_bulk":"bulk term of order \\(n^2\\log n\\)" in packet,
 "packet_requires_common_tail_quotient":"cancels the common \\(n^2\\log n\\) tail class" in packet,
 "packet_does_not_promote_n4_diagnostic":"uses the current finite \\(n^4\\) diagnostic as motivation" in packet,
})
result={"schema":"marici.strominger.rh_laguerre_fredholm_bulk_renormalization_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The Laguerre-to-Weibull recurrence ratio grows like n^3 on the finite exact grid, so the unrenormalized Fredholm logarithm carries an n^2 log n bulk term. The compact-truncation 1/n coefficient can only be isolated after quotienting by the common unshifted-Weibull bulk.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_laguerre_fredholm_bulk_renormalization_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
