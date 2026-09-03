#!/usr/bin/env python3
"""Apply SCC lifting IR to the current Flavor Interaction Net state."""
import hashlib,json
from pathlib import Path
from lifting_ir import compile_lifting_ir
ROOT=Path(__file__).resolve().parents[3];packet=ROOT/"research/flavor/flavor-interaction-net-state.md";result_path=ROOT/"research/flavor/results/wp1043_flavor_interaction_net_state.json";source=json.loads(result_path.read_text(encoding="utf-8"))
frontier=source["frontier"]
layers=[{"id":"verified_interaction_net","base_ref":"flavor_source_label_lattice","total_ref":"verified_interaction_net:total","kind":"mathematical","state":"coherent_section","projection":"forget_interaction_net","inhabitance_witness":str(result_path.relative_to(ROOT)),"selector":"deterministic_negative_rigidifier_net","selector_invariance_witness":"wp1043_dependency_and_rewrite_checks","section_coherence_witness":"wp1043_PASS"}]
base="verified_interaction_net:total"
for name in frontier:
 layers.append({"id":name,"base_ref":base,"total_ref":name+":total","kind":"mathematical","state":"not_constructed"});base=name+":total"
layers.append({"id":"flavor_physical_selector_terminal","base_ref":base,"kind":"readout","state":"not_constructed"})
report=compile_lifting_ir({"root_object":"flavor_source_label_lattice","layers":layers})
checks={"source_replay_passed":source["status"]=="PASS","frontier_exact":frontier==["common_integer_substrate_with_preparation_law","typed_pole_spectrum_and_mass_clock","calibrated_momentum_and_ratio_law","physical16_gain_or_interference_law"],"coherent_prefix_is_obstruction_net_only":report["surviving_prefix"]==["verified_interaction_net"],"first_obstruction_is_source_preparation":report["first_obstruction"]["layer"]==frontier[0],"all_later_layers_globally_blocked":all(x["global_status"]=="blocked_by_prior_layer" for x in report["layers"][2:]),"terminal_remains_open":source["terminal_status"]=="open" and report["physical_readout_status"]=="not_constructed","no_physical_selector_promoted":not report["explanation_complete"]}
out={"schema":"marici.scc.latest-flavor-lifting-ir.v1","sources":{"packet":str(packet.relative_to(ROOT)),"packet_sha256":hashlib.sha256(packet.read_bytes()).hexdigest(),"result":str(result_path.relative_to(ROOT)),"result_sha256":hashlib.sha256(result_path.read_bytes()).hexdigest()},"source_counts":{"constructed_nodes":source["constructed_nodes"],"open_nodes":source["open_nodes"],"hostile_fixtures":source["hostile_fixture_count"]},"report":report,"acceptance_checks":checks,"passed":report["passed"] and all(checks.values()),"claim_boundary":"WP1043 obstruction-net translation only; no source selector or physical16 prediction"}
path=Path(__file__).parent/"latest_flavor_lifting_ir_results.json";path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps({"passed":out["passed"],"source_counts":out["source_counts"],"first_obstruction":report["first_obstruction"],"surviving_prefix":report["surviving_prefix"],"checks":checks},indent=2));raise SystemExit(0 if out["passed"] else 1)
