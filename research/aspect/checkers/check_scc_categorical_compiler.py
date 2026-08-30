#!/usr/bin/env python3
import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from categorical_compiler import compile_diagram

p=ROOT/"research/aspect/contracts/scc-categorical-category-lattice.v1.json"
d=json.loads(p.read_text(encoding="utf-8"));r=compile_diagram(d)
fiber=r["fibers"][0]["comparisons"][0]
checks={
 "baseline_compiles":r["passed"],
 "cell_compiled":r["cells"][0]["passed"],
 "same_profile_not_equivalent":fiber["same_profile"] and not fiber["verified_equivalent"] and fiber["first_failed_slot"]=="named_constructor_actions",
 "hostiles_synthesized":{x["mutation"] for x in r["hostiles"]}=={"delete_cell","promote_same_profile_to_equivalence"},
 "unsupported_not_promoted":all(not x["admitted"] for x in r["higher_coherence"]),
 "proof_promotion_admitted":r["promotions"][0]["admitted"],
 "inverse_design_ranked":r["inverse_design"]["physical_claim"]["ranked_experiments"][0]["id"]=="controlled_conjugate_readout",
 "functor_admitted":r["functors"][0]["transfer_admitted"],
}
broken=copy.deepcopy(d);broken["arrows"][3]["map_token"]="wrong"
rb=compile_diagram(broken)
checks["first_cell_failure_propagates"]=(not rb["passed"] and rb["obstruction_cones"]["mixed_action_observer"]==["completion_margin","observer_faithfulness","physical_claim"])
out={"schema":"marici.aspect.scc-categorical-compiler-check.v1","checks":checks,"compilation":r,"passed":all(checks.values()),"claim":"finite declared-diagram compilation only"}
q=ROOT/"research/aspect/results/scc_categorical_compiler.json";q.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"schema":out["schema"],"checks":checks,"passed":out["passed"]},indent=2));raise SystemExit(0 if out["passed"] else 1)
