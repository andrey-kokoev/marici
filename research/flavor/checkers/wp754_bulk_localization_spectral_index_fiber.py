"""Exact spectral-index audit for source-required product-group multiplets."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

# Degree-weighted five-dimensional vector multiplicity for
# SU(3)c x SU(2)A x SU(2)B x U(1)Y.
vector_dimensions = {
    "SU3_c": 8,
    "SU2_A": 3,
    "SU2_B": 3,
    "U1_Y": 1,
}
N_V = sum(vector_dimensions.values())

# Degree-weighted hypermultiplet multiplicities already required by the
# four-dimensional flavor grammar.
hyper_dimensions = {
    "bifundamental_link": 2 * 2,
    "three_lepton_doublets_L": 3 * 2,
    "one_Higgs_doublet_H": 2,
    # One S1/Z2 hypermultiplet has only one chiral zero mode.  Each
    # four-dimensional vectorlike pair therefore needs two hypers.
    "three_vectorlike_bifundamentals_Psi": 3 * 2 * 2 * 2,
    "three_vectorlike_quark_doublet_mediators": 3 * 2 * 3 * 2,
    "three_vectorlike_lepton_doublet_mediators": 3 * 2 * 2,
}

gravity_offset = 2
link_only_bulk = hyper_dimensions["bifundamental_link"]
portal_operands_bulk = link_only_bulk + sum(
    hyper_dimensions[name]
    for name in (
        "three_lepton_doublets_L",
        "one_Higgs_doublet_H",
        "three_vectorlike_bifundamentals_Psi",
    )
)
mediator_completion_bulk = sum(hyper_dimensions.values())

kappa_link_only = gravity_offset + N_V - link_only_bulk
kappa_portal_bulk = gravity_offset + N_V - portal_operands_bulk
kappa_mediators_bulk = gravity_offset + N_V - mediator_completion_bulk

# The full-tower endpoint gap has the sign of kappa.
R4 = sp.symbols("R_fourth", positive=True)
gap_unit = sp.factor(31 * sp.zeta(5) / (16 * R4))
gap_link_only = sp.factor(kappa_link_only * gap_unit)
gap_portal_bulk = sp.factor(kappa_portal_bulk * gap_unit)
gap_mediators_bulk = sp.factor(kappa_mediators_bulk * gap_unit)

checks = {
    "product_group_vector_dimension_is_fifteen": N_V == 15,
    "link_hyper_dimension_is_four": link_only_bulk == 4,
    "link_plus_portal_operand_hyper_dimension_is_thirty_six": portal_operands_bulk == 36,
    "complete_required_mediator_hyper_dimension_is_eighty_four": mediator_completion_bulk == 84,
    "link_only_bulk_index_is_positive_thirteen": kappa_link_only == 13,
    "portal_operands_bulk_index_is_negative_nineteen": kappa_portal_bulk == -19,
    "mediator_completion_bulk_index_is_negative_sixty_seven": kappa_mediators_bulk == -67,
    "link_only_lift_selects_half_twist": gap_link_only.is_positive is True,
    "portal_bulk_lift_selects_zero_twist": gap_portal_bulk.is_negative is True,
    "mediator_bulk_lift_selects_zero_twist": gap_mediators_bulk.is_negative is True,
    "same_4d_packet_has_opposite_spectral_signs": kappa_link_only * kappa_portal_bulk < 0,
    "deliberate_localization_falsifier_is_nonzero": (
        sp.factor(gap_link_only - gap_portal_bulk) == 32 * gap_unit
    ),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP754",
    "status": "PASS",
    "checks": checks,
    "admitted_domain": "the WP737 four-dimensional anomaly-compatible product-group packet and WP738 required mediators, lifted to five dimensions with bulk gauge multiplets and variable bulk-versus-boundary placement of matter",
    "spectral_formula": "kappa=2+N_V-N_H with degree-weighted bulk multiplet multiplicities",
    "vector_multiplicity": N_V,
    "bulk_hyper_multiplicities": {
        "link_only": link_only_bulk,
        "link_plus_portal_operands": portal_operands_bulk,
        "link_plus_portal_operands_plus_required_mediators": mediator_completion_bulk,
    },
    "spectral_indices": {
        "link_only": kappa_link_only,
        "portal_operands": kappa_portal_bulk,
        "required_mediator_completion": kappa_mediators_bulk,
    },
    "classification": "bulk-localization authority fiber: the same four-dimensional source grammar admits opposite Scherk-Schwarz selector branches",
    "smallest_exact_falsifier": "moving the source-required L, H, and vectorlike Psi packet from a boundary to the bulk changes kappa from 13 to -19 and reverses the full-tower endpoint ordering",
    "deutschian_status": "the radiative selector is not yet hard to vary because localization can be changed without changing the four-dimensional representation grammar",
    "claim_boundary": "degree-weighted massless multiplets; a five-dimensional anomaly and locality completion may restrict placements, but none is currently declared",
    "next_source_gate": "derive bulk-versus-boundary placement from a five-dimensional anomaly-inflow and locality principle, then recompute the complete massive spectral measure",
    "remaining_physical_gate": "g_* normalization, radion stabilization, boundary counterterms, threshold accessibility, physical16 descent, and calibrated instrument remain unproved",
}
(ROOT / "results" / "wp754_bulk_localization_spectral_index_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
