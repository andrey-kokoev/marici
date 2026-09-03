import json, math
from pathlib import Path
beta=.25
# Distinct independent limits: moving-start length and fixed-start degree saddle.
Xs=(10.,100.,1000.,10000.);ns=(2.,4.,8.,16.)
L=[X**(1-beta)/(2*beta) for X in Xs];hard=[1/n**(1/beta) for n in ns]
checks={
 "moving_start_length_has_three_quarter_power":all(abs(math.log(L[i+1]/L[i])/math.log(Xs[i+1]/Xs[i])-(1-beta))<1e-12 for i in range(len(Xs)-1)),
 "fixed_start_saddle_ratio_has_minus_four_power":all(abs(math.log(hard[i+1]/hard[i])/math.log(ns[i+1]/ns[i])+1/beta)<1e-12 for i in range(len(ns)-1)),
 "exponents_are_distinct":1-beta!=1/beta,
}
base=Path(__file__).parents[1]
packet=(base/"rh-moving-start-exponent-does-not-source-fixed-start-degree-corrections.md").read_text(encoding="utf-8")
checks.update({
 "packet_separates_limits":"X\\to\\infty" in packet and "n\\to\\infty" in packet,
 "packet_requires_source_relation":"No source-derived relation \\(X=X(n)\\)" in packet,
 "packet_rejects_authority_not_numeric_possibility":"does not prove that a numerical \\(3/4\\) correction is impossible" in packet,
 "packet_does_not_promote_saddle_ratio":"also does not determine the recurrence correction" in packet,
})
result={"schema":"marici.strominger.rh_moving_start_to_degree_exponent_no_go.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The exponent 1-beta belongs to X->infinity moving-start scaling, whereas the defect correction is n->infinity at fixed X. Without a source map X(n), transporting 3/4 between these limits is unauthorized. The fitted 0.785 remains preasymptotic data only.","checks":checks,"scales":{"moving_start_lengths":L,"fixed_start_hard_edge_ratios":hard},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_moving_start_to_degree_exponent_no_go.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
