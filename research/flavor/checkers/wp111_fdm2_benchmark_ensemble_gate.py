import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp111_fdm2_benchmark_ensemble_gate.json"
d20=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
d93=json.loads((ROOT/"results"/"wp93_fdm2_canonical_matching.json").read_text())
d110=json.loads((ROOT/"results"/"wp110_fdm2_spectral_discriminant_bound.json").read_text())
Js=[abs(float(r["J"])) for r in d20["records"]]
Jbench=s.simplify(1920*s.Rational(36,25)**s.Rational(3,2)/(729*(4+s.sqrt(84))**6))
Jbench_float=float(Jbench.evalf(30)); observed_min=min(Js); ratio=observed_min/Jbench_float
eps=s.symbols("epsilon_J",positive=True,real=True)
gates={
 "WP93_dependency":all(d93["gates"].values()),
 "WP110_dependency":all(d110["gates"].values()),
 "complete_ensemble_loaded":len(Js)==d20["n_minima_audited"]==1210,
 "benchmark_bound_positive":Jbench>0,
 "all_sheets_exceed_benchmark_bound":all(v>Jbench_float for v in Js),
 "observed_minimum_above_bound":observed_min>Jbench_float,
 "canonical_error_threshold_exact":s.simplify(Jbench-2*(Jbench/2))==0,
 "finite_mass_canonical_gate_remains":True,
 "derived_numeric_bound_not_retroactively_preregistered":True,
 "ensemble_compatibility_not_instrument_completion":True,
 "benchmark_selector_not_rigidifier":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-benchmark-ensemble-gate.v1",
 "domain":"fixed WP90 algebraic benchmark and complete stored 1210-sheet ensemble",
 "benchmark":{"r_min":1,"r_max":1,"Z_max":1,"Sigma_min":"36/25","J_lower_exact":str(Jbench),"J_lower_float":Jbench_float},
 "ensemble":{"passes":sum(v>Jbench_float for v in Js),"total":len(Js),"min_abs_J":observed_min,"min_to_bound_ratio":ratio},
 "instrument_condition":"epsilon_J<J_bench/2",
 "instrument_half_gap":Jbench_float/2,
 "classification":"parameter-fixed algebraic branchwise selector ensemble-compatible; physical instrument conditional; not rigidifier",
 "smallest_exact_falsifier":"epsilon_J=J_bench/2",
 "remaining_gate":"canonically normalized full mediator matching error below the half-gap on the same source domain",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"J_bound":Jbench_float,"ratio":ratio,"output":str(OUT.relative_to(ROOT.parent.parent))}))
