import json, math
from pathlib import Path
X=math.log(12)
def mu(r):return 4*math.factorial(4*r+3)/2**(4*r+4)
def bound(r):return X**(r+1)/(r+1)/mu(r)
rows=[{"r":r,"relative_omission_upper_bound":bound(r)} for r in range(21)]
checks={
 "bounds_positive":all(x["relative_omission_upper_bound"]>0 for x in rows),
 "bounds_strictly_decrease":all(rows[i+1]["relative_omission_upper_bound"]<rows[i]["relative_omission_upper_bound"] for i in range(len(rows)-1)),
 "order_twenty_bound_is_tiny":rows[-1]["relative_omission_upper_bound"]<1e-80,
}
base=Path(__file__).parents[1]
packet=(base/"rh-compact-truncation-is-superexponentially-small-at-the-moment-saddle.md").read_text(encoding="utf-8")
checks.update({
 "packet_distinguishes_translation_from_truncation":"it does not compare the truncated measure to the original full measure" in packet,
 "packet_rejects_entrywise_recurrence_promotion":"Entrywise high-moment proximity does not imply recurrence-coefficient proximity" in packet,
 "packet_identifies_low_moment_dependence":"including low moments whose truncation error is fixed" in packet,
 "packet_makes_no_jacobi_asymptotic_claim":"proves no asymptotic equality" in packet,
})
result={"schema":"marici.strominger.rh_compact_truncation_moment_ratio_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"X":"log(12)","a":1,"beta":"1/4"},"verdict":"The compactly omitted raw moment is bounded by X^(r+1)/(r+1), while the full moment is 4(4r+3)!/2^(4r+4); their ratio decays superexponentially. This establishes high-moment proximity only. Low moments remain changed and ill-conditioned Hankel inversion blocks promotion to Jacobi-coefficient asymptotics.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_compact_truncation_moment_ratio_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
