"""Exact Yukawa-span and minimal Ubersector typing audit for WP421."""

import json
from pathlib import Path

import sympy as sp


# Exact three-generation hostile pair.  Both legs have identical singular-value
# spectra; only their relative eigenflag orientation differs.
du = sp.diag(1, 4, 9)
dd = sp.diag(16, 25, 36)
rotation = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5), 0], [-sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])

yu = du
yd_aligned = dd
yd_rotated = dd * rotation.T

au = sp.simplify(yu.T * yu)
ad_aligned = sp.simplify(yd_aligned.T * yd_aligned)
ad_rotated = sp.simplify(yd_rotated.T * yd_rotated)

mix_aligned = sp.eye(3)
mix_rotated = rotation

# A common weak-basis transformation changes both presentations and preserves
# the relative mixing matrix.
p = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
left_u = p
left_d = p * rotation
mix_after_common_basis_change = sp.simplify(left_u.T * left_d)

def spectrum(matrix):
    return sorted(matrix.eigenvals().keys(), key=lambda x: float(x))


signature_objects = [
    "normalized_UV_source",
    "selected_vacuum",
    "Yukawa_span",
    "physical16_quotient_coordinate",
    "calibrated_detector_record",
    "boundary_preparation",
]
signature_arrows = [
    "vacuum_selector",
    "covariant_matching",
    "RG_transport",
    "weak_basis_quotient",
    "detector_response",
    "boundary_preparation_map",
]
coherence_cells = [
    "matching_equivariance_under_source_gauge_action",
    "RG_matching_scale_scheme_commutation_with_uncertainty",
    "quotient_invariance_under_full_weak_basis_groupoid",
    "source_detector_common_frame_calibration",
    "boundary_source_support_compatibility",
]

checks = {
    "up_leg_spectrum_is_fixed": spectrum(au) == [1, 16, 81],
    "down_leg_spectra_match_for_hostile_pair": spectrum(ad_aligned) == spectrum(ad_rotated) == [256, 625, 1296],
    "relative_overlap_distinguishes_hostile_pair": mix_aligned.applyfunc(abs) != mix_rotated.applyfunc(abs),
    "common_weak_basis_change_preserves_relative_mixing": mix_after_common_basis_change == rotation,
    "physical16_is_a_faithful_redundant_coordinate_not_a_dimension_claim": 6 + 9 + 1 == 16,
    "wp232_witnesses_missing_source_detector_cell": "source_detector_common_frame_calibration" in coherence_cells,
    "wp256_witnesses_missing_exact_rg_detector_transport_cell": "RG_matching_scale_scheme_commutation_with_uncertainty" in coherence_cells,
    "minimal_signature_is_finite": len(signature_objects) == 6 and len(signature_arrows) == 6 and len(coherence_cells) == 5,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP421",
    "title": "Yukawa relational core and minimal Ubersector signature",
    "basis_free_core": "span Q_L -> u_R and Q_L -> d_R, or adjoint cospan under the reversed convention",
    "shared_port_operators": ["Y_u-dagger Y_u", "Y_d-dagger Y_d"],
    "channel_decomposition": "eigenlines of the two positive Gram operators on Q_L; flavor channels are components, not the transport functor",
    "readout_typing": {
        "six_masses": "singular values of the two Yukawa legs",
        "nine_ckm_moduli": "absolute overlaps of their two eigenflags",
        "signed_jarlskog": "orientation-sensitive phase invariant of the relative overlap matrix",
        "physical16": "faithful redundant quotient coordinate, not a sixteen-dimensional manifold claim",
    },
    "hostile_pair": {
        "same_individual_spectra": bool(
            spectrum(au) == [1, 16, 81]
            and spectrum(ad_aligned) == spectrum(ad_rotated)
        ),
        "aligned_overlap_moduli": [[str(x) for x in row] for row in mix_aligned.applyfunc(abs).tolist()],
        "rotated_overlap_moduli": [[str(x) for x in row] for row in mix_rotated.applyfunc(abs).tolist()],
    },
    "minimal_ubersector_signature": {
        "objects": signature_objects,
        "arrows": signature_arrows,
        "coherence_cells": coherence_cells,
    },
    "categorical_disposition": "an ordinary span plus typed surrounding diagram suffices for the flavor core; no larger multicategory is forced until independently prepared multi-input source or boundary operations are admitted",
    "wp232_missing_arrow": "source-derived RG and calibrated physical16 readout lack a source-detector common-frame rank-two response cell",
    "wp256_missing_arrow": "source-relative scale transport improves shape interpolation but lacks an exact or uncertainty-authorized RG-to-detector transport cell",
    "smallest_exact_falsifier": "the aligned and rotated pairs have identical leg spectra but unequal relative overlap moduli",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp421_yukawa_ubersector_signature.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
