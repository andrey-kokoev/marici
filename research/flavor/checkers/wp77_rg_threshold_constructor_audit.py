import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp77_rg_threshold_constructor_audit.json"
deps={n:json.loads(next((ROOT/"results").glob(f"wp{n}_*.json")).read_text(encoding="utf-8")) for n in (61,62,63,76)}
classification={
 "one_loop_RG":{"descends":True,"authorized":True,"proper_image":False},
 "threshold_Schur":{"descends":True,"authorized":False,"proper_image":False},
 "RG_plus_frozen_UV_boundary":{"descends":True,"authorized":False,"proper_image":True}}
gates={"WP61_all":all(deps[61]["gates"].values()),"WP62_all":all(deps[62]["gates"].values()),
 "WP63_all":all(deps[63]["gates"].values()),"WP76_all":all(deps[76]["gates"].values()),
 "RG_authorized_but_nonproper":classification["one_loop_RG"]["authorized"] and not classification["one_loop_RG"]["proper_image"],
 "threshold_noninjective_surjective":deps[63]["gates"]["threshold_map_has_nontrivial_source_fibers"] and deps[63]["gates"]["threshold_map_is_surjective_on_eft_targets"],
 "frozen_boundary_proper_but_absent":classification["RG_plus_frozen_UV_boundary"]["proper_image"] and not classification["RG_plus_frozen_UV_boundary"]["authorized"],
 "no_candidate_constructor":not any(v["authorized"] and v["proper_image"] for v in classification.values())}
result={"schema":"marici.flavor.rg-threshold-constructor-audit.v1","classification":classification,"first_missing_resource":"independently normalized UV boundary plus implementation","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
