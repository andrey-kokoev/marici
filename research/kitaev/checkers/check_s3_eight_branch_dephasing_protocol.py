"""Exact typed three-bit protocol for optimal D(S3) sector dephasing."""

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]


def main():
    path = ROOT / "research/kitaev/results/s3-two-flux-lie-control.json"
    raw = path.read_bytes()
    source = json.loads(raw)
    optimal = source["optimal_cyclic_dephasing"]
    eigenvalues = optimal["integer_sector_eigenvalues"]
    residues = optimal["sector_residues"]
    assert optimal["minimum_branch_count"] == 8
    assert [value % 8 for value in eigenvalues] == residues
    assert sorted(residues) == list(range(8))

    omega = sp.sqrt(2) / 2 + sp.I * sp.sqrt(2) / 2
    branch_table = []
    for k in range(8):
        bits = [(k >> j) & 1 for j in range(3)]
        branch_table.append({
            "bits_b0_b1_b2": bits,
            "branch": k,
            "probability": "1/8",
            "pulse_angle_over_2pi": f"{k}/8",
            "binary_power_schedule": [bits[0], 2 * bits[1], 4 * bits[2]],
        })

    residuals = {}
    checked = 0
    for a in range(8):
        for b in range(8):
            multiplier = sp.simplify(sum(
                omega ** (k * (eigenvalues[a] - eigenvalues[b])) for k in range(8)
            ) / 8)
            expected = sp.Integer(1) if a == b else sp.Integer(0)
            assert sp.simplify(multiplier - expected) == 0
            if a != b:
                residuals[f"{a}->{b}"] = str(multiplier)
                checked += 1
    assert checked == 56

    # The Fourier system plus normalization has the unique uniform solution.
    probabilities = sp.symbols("p0:8", real=True)
    equations = [sum(probabilities) - 1]
    equations += [sp.simplify(sum(probabilities[j] * omega ** (k * j) for j in range(8))) for k in range(1, 8)]
    solution = sp.linsolve(equations, probabilities)
    assert solution == sp.FiniteSet(tuple([sp.Rational(1, 8)] * 8))

    result = {
        "schema": "marici.s3-eight-branch-dephasing-protocol.v1",
        "input_lie_result_sha256": hashlib.sha256(raw).hexdigest(),
        "central_generator": {
            "sector_order": "A,B,C,D,E,F,G,H",
            "integer_eigenvalues": eigenvalues,
            "residues_mod_8": residues,
            "source_basis_coefficients": optimal["basis_coefficients"],
            "basis_typing": "exact_reachable_center_basis_but_not_named_primitive_pulse_words",
        },
        "random_source": {
            "type": "three_independent_unbiased_classical_bits",
            "branch_map": "k=b0+2*b1+4*b2",
            "entropy_bits": 3,
            "reset_requirement": "fresh_independent_draw_per_channel_use",
        },
        "branch_table": branch_table,
        "ordered_cross_sector_units_checked": checked,
        "all_cross_sector_residuals": residuals,
        "within_sector_multiplier": "1",
        "uniform_distribution_is_unique": True,
        "minimum_branch_count": 8,
        "primitive_pulse_schedule": {
            "group_level_target": "reachable",
            "single_selected_duration_form": "exp(-2*pi*i*k*Z/8)",
            "three_binary_power_form": "apply_U1_if_b0_then_U2_if_b1_then_U4_if_b2",
            "timed_words_in_microscopic_generators": "unresolved",
        },
        "deliberate_failure": {
            "claim": "seven_or_fewer_classical_branches_can_dephase_eight_distinct_sector_residues",
            "actual": False,
            "reason": "eight_labels_require_eight_distinct_characters",
        },
        "aggregate_gates": {
            "three_bits_index_all_eight_branches": True,
            "branch_probabilities_are_exactly_uniform": True,
            "all_fifty_six_ordered_cross_sector_units_vanish": True,
            "all_within_sector_units_are_fixed": True,
            "uniform_branch_law_is_unique": True,
            "eight_branches_are_minimal": True,
            "central_target_is_group_level_reachable": True,
            "timed_primitive_pulse_words_remain_unresolved": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
