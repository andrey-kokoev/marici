import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp80_probe_reference_constructor_instruments.json"
p=json.loads((ROOT/"results"/"wp67_experimental_probe_algebra.json").read_text(encoding="utf-8"))
r=json.loads((ROOT/"results"/"wp55_relational_reference_port.json").read_text(encoding="utf-8"))
gates={"WP67_dependency":all(p["gates"].values()),"WP55_dependency":all(r["gates"].values()),
 "probe_faithful":p["gates"]["experimental_algebra_separates_measured10_hostile_pair"],
 "probe_preserves_substrate":not p["selector"],"probe_instrument_typed":bool(p["instrument"]),
 "fixed_reference_fails_original_descent":r["gates"]["fixed_reference_readout_fails_original_quotient_descent"],
 "relational_action_restores_descent":r["gates"]["simultaneous_state_reference_action_restores_descent"],
 "reference_instrument_absent":"none declared" in r["classification"]["physical_instrument"],
 "reference_not_absolute_phase":not r["classification"]["absolute_phase_recovery"],
 "neither_selects_original_physical16":not p["selector"] and not r["classification"]["selector_on_original_physical16"]}
result={"schema":"marici.flavor.probe-reference-constructor-instruments.v1","probe_task":"x -> (x,I(x))","reference_domain":r["extended_domain"],"groupoids":r["groupoids"],"gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
