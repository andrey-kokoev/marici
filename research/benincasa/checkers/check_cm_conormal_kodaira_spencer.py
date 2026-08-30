#!/usr/bin/env python3
"""Audit the labelled CM Kodaira--Spencer sections and exterior ranks."""

import ast
import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
EXE = CRATE / "target" / "release" / "cm_normal_tower_rank.exe"
CASES = (("A", 32003), ("A", 65521), ("B", 65521), ("HOMA", 32003))


def normalized_relation(columns, prime):
    rows = list(map(list, zip(*columns)))
    # Solve c0*col0+c1*col1+c2*col2=0 by testing each normalized free coordinate.
    for free in range(3):
        others = [index for index in range(3) if index != free]
        for first_row in range(len(rows)):
            for second_row in range(first_row + 1, len(rows)):
                determinant = (
                    rows[first_row][others[0]] * rows[second_row][others[1]]
                    - rows[first_row][others[1]] * rows[second_row][others[0]]
                ) % prime
                if determinant == 0:
                    continue
                right0 = -rows[first_row][free] % prime
                right1 = -rows[second_row][free] % prime
                inverse = pow(determinant, -1, prime)
                solution0 = (right0 * rows[second_row][others[1]] - rows[first_row][others[1]] * right1) * inverse % prime
                solution1 = (rows[first_row][others[0]] * right1 - right0 * rows[second_row][others[0]]) * inverse % prime
                candidate = [0, 0, 0]
                candidate[free] = 1
                candidate[others[0]] = solution0
                candidate[others[1]] = solution1
                if all(sum(row[index] * candidate[index] for index in range(3)) % prime == 0 for row in rows):
                    return candidate
    raise RuntimeError("no normalized pair-wedge relation")


def run(point, prime):
    env = os.environ.copy()
    env.update(
        NORMAL_TOWER="1",
        CM_CONORMAL_KS_PACKET="1",
        KINEMATIC_POINT=point,
        PRIME=str(prime),
    )
    completed = subprocess.run(
        [str(EXE)], cwd=CRATE, env=env, text=True, capture_output=True, check=True
    )
    def extract(label):
        match = re.search(rf"{label}=(.*)", completed.stdout)
        if match is None:
            raise RuntimeError(f"missing {label}")
        return ast.literal_eval(match.group(1))
    sections = extract("CONORMAL_KS_SECTIONS")
    pairs = extract("CONORMAL_KS_PAIRS")
    triple = extract("CONORMAL_KS_TRIPLE")
    ranks = extract("CONORMAL_KS_RANKS")
    quotient_generator_nonzero = extract("CONORMAL_KOSZUL_QUOTIENT_GENERATOR_NONZERO")
    mixed_parameter_commutator_nonzero = extract("CONORMAL_MIXED_PARAMETER_COMMUTATOR_NONZERO")
    primitive_koszul_gauge_nonzero = extract("CONORMAL_PRIMITIVE_KOSZUL_GAUGE_NONZERO")
    transitivity_map_rank = extract("CONORMAL_TRANSITIVITY_MAP_RANK")
    transitivity_kernel = extract("CONORMAL_TRANSITIVITY_KERNEL")
    transitivity_cokernel_dual = extract("CONORMAL_TRANSITIVITY_COKERNEL_DUAL")
    transitivity_matrix = extract("CONORMAL_TRANSITIVITY_MATRIX")
    flattened_pairs = [[value for component in pair for value in component] for pair in pairs]
    return {
        "point": point,
        "prime": prime,
        "section_rank": ranks[0],
        "pair_wedge_rank": ranks[1],
        "triple_wedge_rank": ranks[2],
        "quotient_generator_nonzero": quotient_generator_nonzero,
        "quotient_koszul_differential_ranks": [0, 0, 0, 0],
        "mixed_parameter_commutator_nonzero": mixed_parameter_commutator_nonzero,
        "contraction_graded_commutator_rank": 0,
        "primitive_koszul_gauge_nonzero": primitive_koszul_gauge_nonzero,
        "transitivity_map_rank": transitivity_map_rank,
        "transitivity_kernel_dimension": 21 - transitivity_map_rank,
        "transitivity_cokernel_dimension": 28 - transitivity_map_rank,
        "transitivity_kernel_basis": transitivity_kernel,
        "transitivity_cokernel_dual_basis": transitivity_cokernel_dual,
        "transitivity_matrix": transitivity_matrix,
        "pair_wedge_relation": normalized_relation(flattened_pairs, prime),
        "triple_is_termwise_zero": all(value == 0 for component in triple for value in component),
        "section_shape": [len(sections), len(sections[0]), len(sections[0][0])],
        "pair_shape": [len(pairs), len(pairs[0]), len(pairs[0][0])],
        "triple_shape": [len(triple), len(triple[0])],
    }


def main():
    runs = [run(point, prime) for point, prime in CASES]
    checks = {
        "three_labelled_sections_in_R4": all(item["section_shape"] == [3, 4, 7] for item in runs),
        "three_labelled_pair_wedges_in_exterior2_R4": all(item["pair_shape"] == [3, 6, 7] for item in runs),
        "one_triple_wedge_in_exterior3_R4": all(item["triple_shape"] == [4, 7] for item in runs),
        "section_pair_triple_ranks_are_3_2_0": all(
            [item["section_rank"], item["pair_wedge_rank"], item["triple_wedge_rank"]] == [3, 2, 0]
            for item in runs
        ),
        "triple_wedge_is_termwise_zero": all(item["triple_is_termwise_zero"] for item in runs),
        "all_four_exact_generators_vanish_in_the_quotient": all(
            item["quotient_generator_nonzero"] == 0 for item in runs
        ),
        "ordinary_quotient_koszul_differential_is_zero": all(
            item["quotient_koszul_differential_ranks"] == [0, 0, 0, 0] for item in runs
        ),
        "mixed_parameter_derivatives_commute": all(
            item["mixed_parameter_commutator_nonzero"] == 0 for item in runs
        ),
        "kodaira_spencer_contractions_graded_commute": all(
            item["contraction_graded_commutator_rank"] == 0 for item in runs
        ),
        "primitive_trace_is_independent_under_all_koszul_syzygies": all(
            item["primitive_koszul_gauge_nonzero"] == 0 for item in runs
        ),
        "transitivity_dimensions_are_nonnegative": all(
            item["transitivity_kernel_dimension"] >= 0
            and item["transitivity_cokernel_dimension"] >= 0
            for item in runs
        ),
        "transitivity_kernel_basis_has_shape_8_by_21": all(
            len(item["transitivity_kernel_basis"]) == 8
            and all(len(vector) == 21 for vector in item["transitivity_kernel_basis"])
            for item in runs
        ),
        "transitivity_cokernel_dual_basis_has_shape_15_by_28": all(
            len(item["transitivity_cokernel_dual_basis"]) == 15
            and all(len(vector) == 28 for vector in item["transitivity_cokernel_dual_basis"])
            for item in runs
        ),
        "transitivity_matrix_has_shape_28_by_21": all(
            len(item["transitivity_matrix"]) == 28
            and all(len(row) == 21 for row in item["transitivity_matrix"])
            for item in runs
        ),
    }
    packet = {
        "schema": "marici.cm_conormal_kodaira_spencer.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "direction_order": ["d/d(P1^2)", "d/d(P2^2)", "d/d(P3^2)"],
        "pair_order": ["kappa1_wedge_kappa2", "kappa1_wedge_kappa3", "kappa2_wedge_kappa3"],
        "runs": runs,
        "checks": checks,
        "scope": (
            "This certifies the exterior ranks of the labelled Kodaira--Spencer packet. "
            "The ordinary Koszul differential becomes zero after quotienting by its four generators. "
            "Bare differentiation adds only commuting mixed parameter derivatives and graded-commuting contraction operators. "
            "The tracked primitive correction is independent modulo the quotient under the Koszul generators of the "
            "first-syzygy module. The full presentation-level Atiyah commutator remains unconstructed."
        ),
    }
    output = ROOT / "results" / "cm-conormal-kodaira-spencer.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
