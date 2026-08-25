"""Exact finite within-block twirl protocol and primitive-pulse gap audit."""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]


def weyl(dim, p, q):
    omega = {2: -sp.Integer(1), 3: -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2}[dim]
    out = sp.zeros(dim)
    for j in range(dim): out[(j + p) % dim, j] = omega ** (q * j)
    return out


def main():
    source_path = ROOT / "research/kitaev/results/s3-source-generated-lie-closure.json"
    source_raw = source_path.read_bytes()
    source = json.loads(source_raw)
    assert source["schema"] == "marici.s3-source-generated-lie-closure.v1"
    assert source["derived_projective_dimension"] == 28

    stages = [("C", 2), ("D", 3), ("E", 3), ("F", 2), ("G", 2), ("H", 2)]
    protocol = []
    total_matrix_units = 0
    for label, dim in stages:
        branches = []
        operators = []
        for p, q in itertools.product(range(dim), repeat=2):
            u = weyl(dim, p, q)
            assert sp.simplify(u.H * u) == sp.eye(dim)
            operators.append(u)
            branches.append({"p": p, "q": q, "probability": f"1/{dim * dim}"})
        for i, j in itertools.product(range(dim), repeat=2):
            unit = sp.zeros(dim); unit[i, j] = 1
            actual = sp.simplify(sum((u * unit * u.H for u in operators), sp.zeros(dim)) / dim ** 2)
            expected = sp.trace(unit) * sp.eye(dim) / dim
            assert sp.simplify(actual - expected) == sp.zeros(dim)
            total_matrix_units += 1
        protocol.append({
            "stage": label,
            "dimension": dim,
            "branch_count": dim ** 2,
            "branches": branches,
            "control_target": f"block_{label}_Weyl(p,q)_identity_elsewhere",
        })

    flattened = sp.prod(item["branch_count"] for item in protocol)
    assert flattened == 20736
    assert total_matrix_units == 34

    result = {
        "schema": "marici.s3-within-block-twirl-protocol.v1",
        "source_lie_result_sha256": hashlib.sha256(source_raw).hexdigest(),
        "stage_count": 6,
        "stage_order": [label for label, _ in stages],
        "protocol": protocol,
        "branch_choices_across_stages": sum(item["branch_count"] for item in protocol),
        "flattened_ensemble_size": int(flattened),
        "matrix_units_checked": total_matrix_units,
        "ideal_randomness_entropy_bits": "8+4*log2(3)",
        "projective_reachability": {
            "status": "exact_group_level_from_full_direct_sum_su_da",
            "global_phase_relevance": "none_for_conjugation_channels",
        },
        "primitive_pulse_schedule": {
            "status": "unresolved",
            "missing": [
                "finite_words_in_the_compiled_source_generators",
                "pulse_amplitudes",
                "pulse_durations",
                "geometric_parallelization",
            ],
        },
        "deliberate_failure": {
            "claim": "the_lie_rank_certificate_itself_supplies_explicit_timed_primitive_pulses",
            "actual": False,
        },
        "aggregate_gates": {
            "six_stage_protocol_is_explicit": True,
            "every_branch_target_is_unitary": True,
            "every_local_matrix_unit_is_exactly_depolarized": True,
            "all_targets_are_projectively_reachable": True,
            "flattened_within_block_ensemble_has_20736_members": True,
            "ideal_branch_law_is_typed": True,
            "global_phases_do_not_affect_the_channel": True,
            "primitive_timed_pulse_words_remain_unresolved": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
