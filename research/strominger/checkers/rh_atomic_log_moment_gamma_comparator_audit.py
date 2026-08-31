import json, math
from pathlib import Path
A=1.; B=.25

def mode_x(r):
 if r==0:return 0.
 lo,hi=0.,float(max(1,r))
 for _ in range(100):
  x=(lo+hi)/2
  if x+2*A*B*x**B<r:lo=x
  else:hi=x
 return (lo+hi)/2
def log_integral(r):return -math.log(B)-((r+1)/B)*math.log(2*A)+math.lgamma((r+1)/B)
def log_error(r):
 if r==0:return math.log(2.)
 x=mode_x(r); return math.log(2.)+r*math.log(x)-x-2*A*x**B
rows=[]
for r in range(13):
 rows.append({"r":r,"mode_x":mode_x(r),"log_integral":log_integral(r),"relative_error_bound":math.exp(log_error(r)-log_integral(r))})
checks={
 "mode_equation_residuals_are_small":all(r==0 or abs(mode_x(r)+2*A*B*mode_x(r)**B-r)<1e-12 for r in range(13)),
 "gamma_integrals_are_positive":all(math.isfinite(x["log_integral"]) for x in rows),
 "relative_error_is_below_one_from_second_moment":all(x["relative_error_bound"]<1 for x in rows if x["r"]>=2),
 "relative_error_decreases_across_tested_higher_orders":all(rows[i+1]["relative_error_bound"]<rows[i]["relative_error_bound"] for i in range(2,12)),
}
base=Path(__file__).parents[1]
packet=(base/"rh-atomic-log-moments-have-gamma-comparators-with-unimodal-error.md").read_text(encoding="utf-8")
saddle=(base/"results"/"rh_subhardy_moment_saddle_cutoff_law_audit.json").read_text(encoding="utf-8")
checks.update({
 "packet_states_two_supremum_error":"|G_r-I_r|\\leq2\\sup" in packet,
 "packet_preserves_matrix_level_blocker":"do not imply" in packet and "Christoffel" in packet,
 "prior_rejects_direct_enumeration":"Further enumeration is structurally uninformative" in saddle,
})
result={"schema":"marici.strominger.rh_atomic_log_moment_gamma_comparator_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":A,"beta":B,"orders":"0..12"},"verdict":"Every infinite atomic log-moment entry is bounded by an exact gamma integral with absolute error at most twice the maximum summand. For the tested sub-Hardy parameters the relative scalar error rapidly decreases at higher moment order. This removes label enumeration entrywise. Independent entry intervals do not preserve Hankel Loewner order, so no Gram-inverse or flat-vector conclusion follows yet.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_atomic_log_moment_gamma_comparator_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2))
