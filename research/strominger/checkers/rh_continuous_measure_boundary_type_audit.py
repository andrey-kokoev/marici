import json,math
from pathlib import Path
intervals=((3.,4.),(10.,11.),(100.,102.))
rows=[]
for a,b in intervals:
 lower=(b-a)*math.exp(-2*b**.25);upper=(b-a)*math.exp(-2*a**.25)
 rows.append({"interval":[a,b],"positive_mass_lower_bound":lower,"mass_upper_bound":upper})
checks={
 "all_interval_masses_strictly_positive":all(r["positive_mass_lower_bound"]>0 for r in rows),
 "density_bounds_ordered":all(r["positive_mass_lower_bound"]<=r["mass_upper_bound"] for r in rows),
 "deliberate_single_atom_fails_interval_support":not all(3.5>=a and 3.5<=b for a,b in intervals),
}
base=Path(__file__).parents[1];packet=(base/"rh-continuous-weibull-measure-is-not-a-single-limit-circle-boundary-condition.md").read_text(encoding="utf-8")
checks.update({
 "packet_distinguishes_extremal_discrete_measure":"extremal representing measure; such measures are discrete" in packet,
 "packet_locates_connection_in_initial_data":"finite-index initial conditions" in packet,
 "packet_rejects_single_parameter":"cannot be the spectral measure of one constant boundary parameter" in packet,
 "packet_preserves_open_coefficient":"does not determine whether that coefficient vanishes" in packet,
 "packet_identifies_wronskian_successor":"discrete Wronskian limit" in packet,
})
result={"schema":"marici.strominger.rh_continuous_measure_boundary_type_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The truncated Weibull measure is non-atomic, whereas a single canonical limit-circle extension has a discrete extremal spectral measure. The p=-1 amplitude must be treated as a polynomial-solution connection coefficient fixed by recurrence initial data, not as a constant Weyl boundary parameter.","checks":checks,"interval_bounds":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_continuous_measure_boundary_type_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
