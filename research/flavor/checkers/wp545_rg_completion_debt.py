"""Exact conservative coordinate lower bound for a selector-authoritative RG system."""

import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp491 = load("wp491_yukawa_tensor_completeness_gate.json")
wp492 = load("wp492_canonical_messenger_tensor_grammar.json")
wp493 = load("wp493_radial_quartic_rg_closure.json")
wp494 = load("wp494_port_alignment_rg_closure.json")
wp495 = load("wp495_adjoint_gram_rg_closure.json")
wp496 = load("wp496_adjoint_quartic_cayley_hamilton.json")
wp498 = load("wp498_entrance_stabilizer_quartic_obstruction.json")
wp499 = load("wp499_o2_connector_hessian.json")
wp543 = load("wp543_existing_source_constraint_kernel.json")
wp544 = load("wp544_typed_source_instrument_pencil.json")

coordinate_sectors = {
    "messenger_tensor_normalizations": list(wp492["tensor_packet"]),
    "radial_leaf_cross_portals": list(wp493["one_loop_generated_support"]["missing_invariants"]),
    "connector_adjoint_alignment": [wp494["new_compulsory_invariant"]],
    "pure_adjoint_gram": [wp495["new_compulsory_invariant"]],
    "connector_O2_complement": [
        "O2 complement direction 1 relative to retained radial/frame span",
        "O2 complement direction 2 relative to retained radial/frame span",
        "O2 complement direction 3 relative to retained radial/frame span",
    ],
}

tagged_coordinates = [
    f"{sector}:{coordinate}"
    for sector, coordinates in coordinate_sectors.items()
    for coordinate in coordinates
]
sector_counts = {sector: len(coordinates) for sector, coordinates in coordinate_sectors.items()}
completion_debt = len(tagged_coordinates)

# The O(2) branch is the maximal symmetry compatible with the frozen entrance.
# Its five quartics contain the two retained directions and three missing ones.
o2_missing = wp498["missing_o2_codimension"]
o2_completed_quartics = len(wp499["potential_coordinates"]["quartic"])

instrument_controls = wp544["external_control_registry"]["dimension"]

checks = {
    "dependencies_passed": all(
        bool(packet["passed"])
        for packet in (wp491, wp492, wp493, wp494, wp495, wp496, wp498, wp499, wp543, wp544)
    ),
    "ten_messenger_normalizations_are_unresolved": sector_counts["messenger_tensor_normalizations"] == 10,
    "three_radial_cross_portals_are_compulsory": sector_counts["radial_leaf_cross_portals"] == 3,
    "one_alignment_coordinate_is_compulsory": sector_counts["connector_adjoint_alignment"] == 1,
    "one_adjoint_gram_coordinate_is_compulsory": sector_counts["pure_adjoint_gram"] == 1,
    "pure_adjoint_sector_closes_after_gram_addition": "algebraically closed" in wp496["classification"],
    "o2_connector_complement_has_dimension_three": o2_missing == sector_counts["connector_O2_complement"] == 3,
    "o2_completed_quartic_basis_has_dimension_five": o2_completed_quartics == 5,
    "tagged_coordinate_names_are_unique": len(set(tagged_coordinates)) == completion_debt,
    "conservative_completion_debt_is_eighteen": completion_debt == 18,
    "instrument_controls_are_not_counted_as_source_coordinates": instrument_controls == 29 and not any(
        name.startswith("instrument:") for name in tagged_coordinates
    ),
    "existing_selector_kernel_is_still_nonzero": wp543["authorized_equalities"]["kernel_dimension"] == 1,
    "fixed_control_source_rank_remains_one": wp544["typed_factorization"]["fixed_control_source_image_rank"] == 1,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP545",
    "domain": "Conservative lower bound from WP491-WP499 on unresolved source-side coordinates required before deriving a selector-authoritative coupled RG vector field.",
    "coordinate_sectors": coordinate_sectors,
    "sector_counts": sector_counts,
    "conservative_unresolved_coordinate_count": completion_debt,
    "non_double_counting_rule": "The five sectors carry different field content or tensor contractions: messenger Yukawa/mass maps, radial leaf-leaf portals, connector-adjoint alignment, pure-adjoint Gram, and the O(2) connector complement. Instrument controls are excluded.",
    "scope": {
        "included": "Only coordinates explicitly proved necessary and still unresolved by WP491-WP499.",
        "excluded": "Already-present source couplings, Standard Model gauge/Yukawa coordinates, quadratic masses, scheme parameters, higher-loop evanescent structures, and all 29 WP544 external instrument controls.",
        "meaning": "Eighteen is a lower bound on completion debt, not the full beta-system dimension.",
    },
    "selector_authority_gate": {
        "current_t_kernel_dimension": wp543["authorized_equalities"]["kernel_dimension"],
        "required_completion": "Derive beta components and threshold maps on at least this 18-coordinate unresolved source packet, together with all already-present and Standard Model couplings.",
        "acceptance": "A candidate fixed point or invariant manifold may carry selector authority only after closure of the complete declared vector field and after its stable constraint Jacobian has nonzero contraction with the WP543 t tangent.",
        "truncation_falsifier": "Any proposed t-fixing beta zero that omits one of the tagged coordinates is a zero of a non-closed truncation, not a source selector.",
    },
    "theorem": "The admitted source programme has at least eighteen unresolved independent RG coordinates before a selector-authoritative beta system can be formed. This lower bound is disjoint from the 29 external instrument controls. Therefore neither WP544's calibrated-control rank nor a beta zero computed on a smaller source truncation can remove WP543's t kernel with authority.",
    "classification": "Exact RG-completion lower bound and truncation gate. It does not derive a fixed point or select t.",
    "selector": False,
    "instrument": "WP544's 29 controls remain separately typed and do not reduce the eighteen-coordinate source completion debt.",
    "smallest_exact_falsifier": "A beta calculation omitting even the single connector-adjoint alignment coordinate is not closed: WP494's parallel and orthogonal configurations have equal radial data but distinct gauge counterterms.",
    "remaining_gate": "Write the complete renormalized action with these eighteen coordinates plus all inherited and Standard Model couplings, derive its scheme-declared beta functions and finite threshold maps, then search for a stable equation transverse to the WP543 t tangent.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp545_rg_completion_debt.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
