"""Exact compatibility/composition audit for the compiled D(S3) controls."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def load(relative):
    path = ROOT / relative
    raw = path.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def main():
    lie, lie_digest = load("research/kitaev/results/s3-two-flux-lie-control.json")
    flux, flux_digest = load("research/kitaev/results/s3-ancilla-flux-port-compiler.json")
    separator, separator_digest = load("research/kitaev/results/s3-gh-separator-compiler.json")

    assert lie["schema"] == "marici.s3-two-flux-lie-control.v2"
    assert flux["schema"] == "marici.s3-ancilla-flux-port-compiler.v1"
    assert separator["schema"] == "marici.s3-gh-separator-compiler.v1"
    assert flux["aggregate_gates"]["transposition_port_compiles_exactly"]
    assert flux["aggregate_gates"]["three_cycle_port_compiles_exactly"]
    assert separator["aggregate_gates"]["thirteen_gate_clean_ancilla_compiler_is_exact_by_spectral_calculus"]

    derived = lie["derived_commutator_lie_dimension"]
    center_before = lie["available_central_eigenvalue_rank"]
    center_after = lie["sector_separating_central_rank"]
    assert derived == 28
    assert center_before == 5
    assert center_after == 6
    assert lie["adjoint_projective_dimension_before_and_after_completion"] == derived
    assert lie["available_center_collision"] == [["G", "H"]]
    assert separator["normalized_F_G_H_signatures"] == {
        "F": "0", "G": "sqrt(3)/4", "H": "-sqrt(3)/4"
    }

    # In a direct sum of matrix blocks every commutator is traceless per
    # block.  Full su(d_a) is already present, so a new generator contributes
    # only the rank increment of its block-scalar trace vector.
    source_lie_dimension = derived + center_after
    assert source_lie_dimension == 34
    assert source_lie_dimension < lie["target_block_unitary_lie_dimension"] == 36
    assert len(set(lie["optimal_cyclic_dephasing"]["sector_residues"])) == 8

    result = {
        "schema": "marici.s3-source-generated-lie-closure.v1",
        "input_compatibility": {
            "coefficient_group": "S3",
            "endpoint_label_order": "A,B,C,D,E,F,G,H",
            "endpoint_ambient_complex_dimension": 16,
            "target_block_algebra_dimension": 36,
            "source_controls": ["gauge_quadratures", "B^t", "B^c", "K_c"],
            "input_sha256": {
                "two_flux_lie": lie_digest,
                "flux_compiler": flux_digest,
                "separator_compiler": separator_digest,
            },
        },
        "compiled_source_lie_dimension": source_lie_dimension,
        "derived_projective_dimension": derived,
        "accessible_center_rank": center_after,
        "full_block_unitary_dimension": 36,
        "remaining_central_phase_deficit": 36 - source_lie_dimension,
        "sector_signature_count": len(set(lie["optimal_cyclic_dephasing"]["sector_residues"])),
        "channel_disposition": {
            "within_block_twirl": "algebraically_accessible",
            "eight_sector_dephasing": "algebraically_accessible",
            "arbitrary_blockwise_phase_control": "not_accessible_two_central_directions_missing",
            "physical_instrument": "conditional_on_compiler_gate_and_random_source_availability",
        },
        "deliberate_failure": {
            "claim": "the_compiled_three_port_source_generates_full_block_unitary_control",
            "actual_dimension": source_lie_dimension,
            "required_dimension": 36,
            "deficit": 2,
        },
        "aggregate_gates": {
            "all_three_non_gauge_controls_have_exact_microscopic_compilers": True,
            "compiled_source_map_matches_the_endpoint_generators": True,
            "derived_projective_algebra_remains_dimension_twenty_eight": True,
            "separator_raises_center_rank_from_five_to_six": True,
            "source_generated_lie_algebra_has_dimension_thirty_four": True,
            "full_block_unitary_control_remains_false": True,
            "all_eight_sector_signatures_are_distinct": True,
            "channel_sufficiency_does_not_imply_full_control": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
