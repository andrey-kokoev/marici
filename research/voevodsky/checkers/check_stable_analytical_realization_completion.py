#!/usr/bin/env python3
"""Final aggregate for the non-positive stable analytical realization."""
import hashlib,json
from pathlib import Path
RES=Path(__file__).parents[1]/"results"
files={
 "base_functor":"stable_analytical_realization_functor.json",
 "weyl_blocks":"three_port_weyl_block_registry.json",
 "regulator_interchange":"regulator_jet_completion_interchange.json",
 "weight_equivalence":"admissible_weight_equivalence.json",
 "global_successor":"global_aperture_independent_jet_successor.json",
 "collision_ports":"confluent_collision_jet_ports.json",
 "tower_universality":"arithmetic_jet_tower_universality.json",
 "operational_witness":"graded_jet_operational_witness.json",
 "repeatable_constructor":"repeatable_graded_jet_constructor.json",
 "xi_clark_normalization":"xi_clark_weyl_sewing_normalization.json",
 "hardy_codefect_gate":"clark_hardy_codefect_gate.json",
 "positivity_frontier":"clark_positivity_frontier.json",
}
d={k:json.loads((RES/v).read_text(encoding="utf-8")) for k,v in files.items()}
checks={
 "all_dependencies_pass":all(x["passed"] for x in d.values()),
 "global_product_functor_exists":d["base_functor"]["passed"],
 "all_weyl_blocks_typed":d["weyl_blocks"]["checks"]["nine_blocks_registered"],
 "regulators_commute_with_jet_completion":d["regulator_interchange"]["checks"]["no_order_of_limits_required"],
 "weights_change_by_natural_unitaries":d["weight_equivalence"]["checks"]["weight_change_cocycle"],
 "successor_has_explicit_spectrum_resolvent":d["global_successor"]["checks"]["resolvent_neumann_series_for_modulus_gt_one"],
 "finite_collisions_completed":d["collision_ports"]["checks"]["confluent_Hermite_extension_handles_finite_clusters"],
 "arithmetic_tower_universal_under_axioms":d["tower_universality"]["checks"]["comparison_unique_with_sections"],
 "graded_information_operationally_detectable":d["operational_witness"]["checks"]["distinguishes_states_equal_mod_lower_filtration"],
 "constructor_repeatable":d["repeatable_constructor"]["checks"]["constructor_maps_are_reusable"],
 "external_Xi_normalization_fixed":d["xi_clark_normalization"]["checks"]["completed_even_transform_row"],
 "Clark_pair_is_fixed_codiagonal":d["xi_clark_normalization"]["checks"]["Clark_sum_recovers_twice_X"],
 "remaining_positivity_gate_exactly_typed":d["hardy_codefect_gate"]["checks"]["correct_defect_is_I_minus_M_Mstar"],
 "positivity_shortcuts_audited":d["positivity_frontier"]["checks"]["every_fixed_continuous_linear_graph_rejected"],
 "single_open_positivity_statement_registered":d["positivity_frontier"]["single_open_statement"]=="I-M_Theta M_Theta* >= 0 on upper-half-plane Hardy space",
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.stable-analytical-realization-completion.v2",
 "checks":checks,"passed":True,
 "theorem":"The weighted relative moving-current system has a closed, collision-complete, regulator-compatible, product-indexed stable analytical realization with a canonical global successor, a universal operationally split arithmetic jet tower, and an exact fixed-codiagonal external Xi/Clark normalization.",
 "coverage":{"edges":560,"faces":784,"tetrahedra":343},
 "remaining_external_gates":[
  "positivity of the complete signed endpoint-gamma-prime Weil form, equivalently positivity of the Clark Hardy co-defect I-M_Theta M_Theta*"
 ],
 "structural_exclusions":[
  "the raw physical common row has nonzero bulk density and no ordinary Hilbert-Schmidt all-path limit; it is retained only as a bounded module/relative-product partner",
  "a bulk quotient, semifinite-density completion, or channelwise counterterm would define a different stronger object",
  "laboratory dynamics, resource bounds, detector calibration, and noise robustness belong to the optional physical evidence backend and are not prerequisites for the mathematical stable realization"
 ],
 "dependencies":{k:{"path":v,"sha256":hashlib.sha256((RES/v).read_bytes()).hexdigest()} for k,v in files.items()}
}
path=RES/"stable_analytical_realization_completion.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="dependencies"},indent=2))
