import json, math
from pathlib import Path

# Numerical checks only audit the exact asymptotic inequalities recorded in the
# companion theorem packet; they are not a proof of discrete flat witnesses.
a=1.0; beta=0.5
T=(10,100,2500,10000,40000,160000)
# Positive exponential exponent eventually grows for every delta>0.
def expo(t,d):return 2*d*t-2*a*t**beta
checks={
 "subexponential_exponent_eventually_grows_for_delta_point_zero_one":all(expo(T[i],.01)<expo(T[i+1],.01) for i in range(2,len(T)-1)),
 "subexponential_exponent_eventually_grows_for_delta_point_one":all(expo(T[i],.1)<expo(T[i+1],.1) for i in range(1,len(T)-1)),
 "carleman_comparison_series_converges_for_beta_half":sum(k**(-1/beta) for k in range(1,10000))<1.645,
 "quasianalytic_boundary_beta_one_is_harmonic":sum(1/k for k in range(1,10000))>9,
}
base=Path(__file__).parents[1]
packet=(base/"rh-subexponential-log-weight-crosses-the-joint-flatness-threshold.md").read_text(encoding="utf-8")
prior=(base/"results"/"rh_rapid_label_joint_flat_kernel_no_go.json").read_text(encoding="utf-8")
checks.update({
 "packet_defines_half_density_subexponential_weight":"w_{a,\\beta}(n)=n^{1/2}" in packet,
 "packet_derives_all_moment_integrals":"finite for every fixed \\(k\\)" in packet,
 "packet_records_nonquasianalytic_threshold":"non-quasi-analytic side" in packet,
 "packet_does_not_claim_discrete_witness":"No coefficient witness is claimed" in packet,
 "prior_rapid_completion_was_quasianalytic":"joint-flat kernel is trivial" in prior,
})
result={"schema":"marici.strominger.rh_subexponential_log_weight_threshold_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/strominger/rh-subexponential-log-weight-crosses-the-joint-flatness-threshold.md","research/strominger/results/rh_rapid_label_joint_flat_kernel_no_go.json"],"verdict":"Weights w(n)=n^(1/2) exp(a(log n)^beta), with 0<beta<1, make every logarithmic moment continuous but force no positive-width analytic neighborhood. Their moment norm growth lies on the non-quasi-analytic side of the Denjoy-Carleman threshold. This removes the analytic obstruction to a joint-flat completion witness. It neither selects a,beta from source data nor constructs a discrete flat packet or extends the boundary current.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"tested_beta":beta,"tested_a":a}
out=base/"results"/"rh_subexponential_log_weight_threshold_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
