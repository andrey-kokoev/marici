#!/usr/bin/env python3
import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from interaction_net_algebra import compile_net_algebra
CP=ROOT/"research/aspect/contracts/scc-interaction-net-domain-algebra.v1.json"
RP=ROOT/"research/aspect/results/scc_interaction_net_domain_algebra.json"
base=json.loads(CP.read_text(encoding="utf-8"));report=compile_net_algebra(base)
hostile=copy.deepcopy(base);hostile["faithfulness_family"]=["coarse_optics"]
coarse=compile_net_algebra(hostile)
checks={
 "compiler_passes":report.get("passed") is True,
 "structural_variants_share_complete_class":report["fingerprints"]["open_path_a"]==report["fingerprints"]["open_path_b"],
 "typed_motifs_are_separated":len(set(report["fingerprints"][x] for x in ["open_path_a","schur_loop","gamma_extension","bell_cover","phase_loop","dilation_loop"]))==6,
 "coarse_shadow_is_not_faithful":coarse.get("first_failed_gate")=="finite_family_faithfulness",
 "coarse_collision_contains_phase_and_dilation":any({fid for group in x for fid in group}>={"phase_loop","dilation_loop"} for x in coarse.get("collisions",[])),
 "combined_declared_family_is_faithful":report["faithfulness"]["faithful"],
 "claim_boundary_is_finite":report["faithfulness"]["scope"]=="declared_finite_fixture_only",
}
out={"schema":"marici.aspect.scc-interaction-net-domain-algebra-check.v1","passed":all(checks.values()),"checks":checks,"report":report,"coarse_only_hostile":coarse}
RP.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2));raise SystemExit(0 if out["passed"] else 1)
