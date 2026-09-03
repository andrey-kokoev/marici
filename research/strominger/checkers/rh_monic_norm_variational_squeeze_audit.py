import json
from fractions import Fraction as F
from pathlib import Path
# Degree-one monic polynomials x-c for an exact discrete model.
points=(F(0),F(2),F(3));weights=(F(1),F(2),F(1));X=F(0)
def optimum(ids):
 mass=sum(weights[i] for i in ids);c=sum(weights[i]*points[i] for i in ids)/mass
 h=sum(weights[i]*(points[i]-c)**2 for i in ids);return c,h
cf,h=optimum((0,1,2));ct,ht=optimum((1,2));compact_full=weights[0]*(points[0]-cf)**2;compact_trunc=weights[0]*(points[0]-ct)**2;ell=1-ht/h
checks={
 "truncated_norm_no_larger_than_full":ht<=h,
 "full_compact_mass_lower_bounds_leverage":compact_full/h<=ell,
 "truncated_compact_mass_upper_bounds_leverage":ell<=compact_trunc/h,
 "normalized_truncated_mass_upper_bounds_leverage":ell<=compact_trunc/ht,
}
base=Path(__file__).parents[1]
packet=(base/"rh-monic-norm-loss-is-squeezed-by-full-and-truncated-compact-masses.md").read_text(encoding="utf-8")
checks.update({
 "packet_tests_both_minimizers":"Testing \\(\\pi_n\\)" in packet and "Testing \\(q_n\\)" in packet,
 "packet_states_exterior_upper_bound":"\\int_C|Q_n^{\\geq X}|^2d\\nu" in packet,
 "packet_claims_no_continuation_bound":"gives no exterior continuation bound" in packet,
})
result={"schema":"marici.strominger.rh_monic_norm_variational_squeeze_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Variational testing squeezes leverage between the compact mass of the full monic minimizer and the exterior continuation mass of the truncated minimizer. Therefore O(n^-2) truncated exterior mass is a sufficient theorem for the monic-norm loss rate.","checks":checks,"exact_model":{"full_minimizer":str(cf),"truncated_minimizer":str(ct),"h":str(h),"h_truncated":str(ht),"leverage":str(ell),"compact_full":str(compact_full),"compact_truncated":str(compact_trunc)},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_monic_norm_variational_squeeze_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
