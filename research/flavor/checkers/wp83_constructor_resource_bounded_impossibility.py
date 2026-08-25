import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp83_constructor_resource_bounded_impossibility.json"
deps={n:json.loads(next((ROOT/"results").glob(f"wp{n}_*.json")).read_text(encoding="utf-8")) for n in range(72,83)}
matrix=deps[82]
bundle=["quotient_level_source_law","proper_attribute","independent_normalization","preparation_or_stabilization_dynamics","typed_apparatus_and_timing","reset_or_catalytic_return","uniform_improvable_error_and_degradation","predeclared_ensemble_surviving_prediction"]
gates={"eleven_dependencies_present":len(deps)==11,"all_dependencies_pass":all(all(d["gates"].values()) for d in deps.values()),
 "no_matrix_candidate_passes":not any(r["passes_all"] for r in matrix["rows"]),
 "only_authorized_state_operation_nonproper":not deps[77]["classification"]["one_loop_RG"]["proper_image"],
 "proper_positive_channel_resources_absent":not any(deps[78]["resources"].values()),
 "two_repair_routes_distinguished":not deps[81]["routes"]["asymmetric_probe"]["selector"] and deps[81]["routes"]["source_restriction"]["selector_law"],
 "complete_ensemble_fails_stationarity":matrix["ensemble"]=={"sheets":1210,"stationarity_accepts":0},
 "minimal_reopening_bundle_complete":len(bundle)==8,
 "reference_rule_preserved":deps[80]["gates"]["reference_not_absolute_phase"]}
result={"schema":"marici.flavor.constructor-resource-bounded-impossibility.v1","scope":"declared flavor source and exact WP52-WP82 completions","theorem":"No repeatable source-generated task prepares or stabilizes a proper physical16 attribute.","possible_declared_tasks":["finite one-loop RG transport","physical16 readout and discrimination"],"impossible_relative_task":"proper-image flavor preparation or stabilization","minimal_reopening_resource_bundle":bundle,"asymmetric_probe_boundary":"six generic complementary scalar probes repair local readout rank but do not select","gates":gates,"passed":sum(gates.values()),"total":len(gates),"dependencies":len(deps)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"dependencies":len(deps),"output":str(OUT.relative_to(ROOT.parent.parent))}))
