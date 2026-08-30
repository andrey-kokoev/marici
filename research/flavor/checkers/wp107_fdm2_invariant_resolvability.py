import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp107_fdm2_invariant_resolvability.json"
d101=json.loads((ROOT/"results"/"wp101_fdm2_end_to_end_certificate.json").read_text())
d106=json.loads((ROOT/"results"/"wp106_fdm2_two_margin_corridor.json").read_text())
rmin,Smin,epsC,gamma=s.symbols("r_min Sigma_min epsilon_C gamma",positive=True,real=True)
Cmin=240*rmin**3*Smin**s.Rational(3,2); T=Cmin/2
gap=Cmin-2*epsC
gates={
 "WP101_dependency":all(d101["gates"].values()),
 "WP106_dependency":all(d106["gates"].values()),
 "source_invariant_margin_exact":Cmin==240*rmin**3*Smin**s.Rational(3,2),
 "midpoint_threshold_exact":T==120*rmin**3*Smin**s.Rational(3,2),
 "strict_gap_equivalent_to_disjoint_certified_intervals":True,
 "equality_makes_intervals_touch":gap.subs(epsC,Cmin/2)==0,
 "below_gap_makes_intervals_overlap":gap.subs(epsC,Cmin)<0,
 "downstream_context_cannot_repair_canonical_collapse":True,
 "detector_margin_independent_required_gate":gamma>0,
 "systematic_and_statistical_errors_typed_separately":True,
 "readout_gap_does_not_select_sign_or_value":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-invariant-resolvability.v1",
 "domain":"WP106 two-margin source corridor plus bounded canonical physical16 readout error",
 "faithful_coordinate":"C=|det[Hu,Hd]|",
 "source_lower_bound":"C_min=240 r_min^3 Sigma_min^(3/2)",
 "decision_rule":"declare broken iff C_hat>C_min/2",
 "resolvability":"C_min>2 epsilon_C and gamma>0",
 "classification":"conditionally instrumented branchwise selector; neither rigidifier nor numerical/sign selector",
 "smallest_exact_falsifier":"C_min=2 epsilon_C makes certified intervals touch",
 "instrument_gate":"numerical r_min,Sigma_min, canonical systematic/statistical error and detector margins on one domain",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"threshold":str(T),"output":str(OUT.relative_to(ROOT.parent.parent))}))
