import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "wp116_source_selector_final_disposition.json"


def load(name):
    return json.loads((ROOT / "results" / name).read_text(encoding="utf-8"))


d57 = load("wp57_invariant_word_complement.json")
d60 = load("wp60_source_authority_inventory.json")
d67 = load("wp67_experimental_probe_algebra.json")
d68 = load("wp68_fitted_ensemble_contextual_partitions.json")
d69 = load("wp69_hostile_suite.json")
d71 = load("wp71_declared_source_selector_no_go.json")
d75 = load("wp75_constructor_descent_hostile_pairs.json")
d101 = load("wp101_fdm2_end_to_end_certificate.json")
d108 = load("wp108_fdm2_ensemble_certificate_boundary.json")
d112 = load("wp112_fdm2_full_mediator_benchmark.json")
d113 = load("wp113_fdm2_decoupling_phenomenology_window.json")
d114 = load("wp114_fdm2_two_parameter_repair.json")
d115 = load("wp115_fitted_uv_potential_noninheritance.json")

dependencies = [d57, d60, d67, d68, d71, d75, d101, d108, d112, d113, d114, d115]
gates = {
    "all_exact_dependencies_pass": all(all(d["gates"].values()) for d in dependencies),
    "physical16_is_the_faithful_coordinate": d67["typed_generator_data"].endswith("(physical16)"),
    "measured10_collision_has_exact_hostile_pair": d57["probe_values"]["difference"] == "9*sqrt(10)/250",
    "largest_declared_probe_family_is_readout_not_selector": not d67["selector"] and "physical16" in d67["algebra"],
    "declared_context_partition_is_generically_physical16": d67["contextual_equivalence"].startswith("generic equality of physical16"),
    "complete_fitted_domain_accounted": d68["domain"]["complete_stored_viable_sheet_ensemble"] == 1210,
    "declared_source_class_has_no_selector": "No declared source-generated operation" in d71["theorem"],
    "hostile_suite_preserves_reference_groupoid_change": d69["tests"]["H6_reference_repairs_descent_only_on_changed_groupoid"],
    "full_weak_basis_descent_audited_before_image": d75["gates"]["descent_precedes_image"],
    "fdm2_selector_is_conditional_and_branchwise": d101["classification"].startswith("branchwise finite-threshold conditional selector"),
    "fdm2_qualitative_prediction_survives_complete_ensemble": d108["qualitative_prediction"]["passes"] == d108["qualitative_prediction"]["total"] == 1210,
    "fixed_fdm2_physical_instrument_is_falsified": d112["gates"]["physical_benchmark_instrument_falsified"],
    "mass_only_repair_has_no_overlap": d113["gates"]["no_overlap_in_fixed_coupling_mass_family"],
    "two_parameter_overlap_is_fitted_not_selected": d114["gates"]["fitted_witness_has_no_selector_authority"],
    "fitted_uv_potential_does_not_restore_authority": d115["gates"]["fitted_coefficients_do_not_gain_source_authority"],
}
gates = {k: bool(v) for k, v in gates.items()}

result = {
    "schema": "marici.flavor.source-selector-final-disposition.v1",
    "admitted_state_domain": "nondegenerate quark-Yukawa pairs on the complete stored 1210-sheet fitted domain; proposed FDM-2 extensions are separately typed and conditional",
    "faithful_quotient_coordinate": "physical16 = six ordered masses, nine CKM moduli, and signed J modulo the full weak-basis group; measured10 is a nonfaithful projection",
    "measured_ten_map": "forget the six quotient-complement coordinates; finite fibers are not assumed singleton",
    "source_authorized_probe_family": d67["algebra"],
    "contextual_partition": {
        "declared_probe_algebra": d67["contextual_equivalence"],
        "measured10_hostile_pair": d57["contextual_partition"]["measured10"],
        "physical16_complemented_pair": d57["contextual_partition"]["measured10_plus_I11"],
        "fdm2_conditional_routes": d101["contextual_partition"],
    },
    "operation_classification": {
        "declared_texture_atlas": "presentation rigidifier only",
        "declared_experimental_algebra": "faithful separator/readout; neither selector nor rigidifier",
        "proposed_fdm2_thermal_arrow": "branchwise conditional algebraic selector; not a surviving typed physical selector instrument",
        "overall_required_gate": "no genuine source-authorized physical16 selector currently survives descent, proper reduction, instrument, and ensemble gates",
    },
    "separates_physical_points": True,
    "selects_smaller_admissible_family": False,
    "requires_reference_port": False,
    "reference_port_rule": "if added, it defines a new relational experiment over the stabilizer groupoid and never recovers an absolute phase",
    "has_actual_physical_instrument": {
        "declared_probe_algebra": True,
        "declared_selector": False,
        "proposed_fdm2_selector": False,
    },
    "smallest_exact_falsifier": {
        "declared_candidate_class": "source-authorized proper reduction is absent (WP71)",
        "fixed_fdm2_benchmark": "light-block nonunitarity > 9/10 and canonical quartet error > 1/100 (WP112)",
        "fitted_uv_repair": d115["smallest_exact_falsifier"],
    },
    "remaining_physical_instrument_gate": "independently derive the UV fields, coefficients, mediator normalization and viable parameters before flavor readouts, then certify thermal/threshold/RG transport, full canonical matching, collider/global-fit constraints, and repeatable detector calibration on one domain",
    "final_answer": "No complete genuine source-generated flavor selector on physical16 is presently established. The declared texture programme rigidifies presentations; FDM-2 supplies a conditional algebraic selector arrow, but its fixed physical realization is falsified and its viable repair is fitted rather than source-selected.",
    "gates": gates,
    "passed": sum(gates.values()),
    "total": len(gates),
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed": result["passed"], "total": result["total"], "output": str(OUT.relative_to(ROOT.parent.parent))}))
