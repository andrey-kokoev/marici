#!/usr/bin/env python3
"""Compute provenance-corrected rank-seven mixed curvature over dual numbers."""

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
DIMENSION = 7
RETAIN_CROSS_GRADE = os.environ.get("CM_RETAIN_EXACT_CROSS_GRADE") == "1"


def run_dual(point, prime, variation):
    env = os.environ.copy()
    env.update(
        NORMAL_TOWER="1",
        CM_DUAL_RANK7_MATRICES="1",
        CM_DUAL_DIRECTION=str(variation),
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
    return extract("DUAL_RANK7_VALUES"), extract("DUAL_RANK7_TANGENTS"), extract("DUAL_RANK7_PIVOTS")


def product(left, right, prime):
    return [
        [sum(left[r][k] * right[k][c] for k in range(DIMENSION)) % prime for c in range(DIMENSION)]
        for r in range(DIMENSION)
    ]


def subtract(left, right, prime):
    return [[(left[r][c] - right[r][c]) % prime for c in range(DIMENSION)] for r in range(DIMENSION)]


def add(left, right, prime):
    return [[(left[r][c] + right[r][c]) % prime for c in range(DIMENSION)] for r in range(DIMENSION)]


def count_nonzero(matrix):
    return sum(value != 0 for row in matrix for value in row)


def confined_to_rank_four(matrix):
    return all(
        value == 0
        for row, entries in enumerate(matrix)
        for column, value in enumerate(entries)
        if row >= 4 or column >= 4
    )


def run_case(point, prime):
    runs = [run_dual(point, prime, variation) for variation in range(3)]
    value_packets = [run[0] for run in runs]
    tangents = [run[1] for run in runs]
    pivots = [run[2] for run in runs]
    derivative_terms = {}
    commutators = {}
    curvature_minus = {}
    curvature_plus = {}
    for first, second in ((0, 1), (0, 2), (1, 2)):
        name = f"F_{first+1}{second+1}"
        derivative = subtract(tangents[first][second], tangents[second][first], prime)
        commutator = subtract(
            product(value_packets[0][first], value_packets[0][second], prime),
            product(value_packets[0][second], value_packets[0][first], prime),
            prime,
        )
        derivative_terms[name] = derivative
        commutators[name] = commutator
        curvature_minus[name] = subtract(derivative, commutator, prime)
        curvature_plus[name] = add(derivative, commutator, prime)
    return {
        "point": point,
        "prime": prime,
        "value_packets_identical_across_variations": value_packets[0] == value_packets[1] == value_packets[2],
        "pivot_packets_identical": pivots[0] == pivots[1] == pivots[2],
        "pivots": pivots[0],
        "value_matrices": value_packets[0],
        "derivative_nonzero_counts": {name: count_nonzero(matrix) for name, matrix in derivative_terms.items()},
        "commutator_nonzero_counts": {name: count_nonzero(matrix) for name, matrix in commutators.items()},
        "derivative_terms": derivative_terms,
        "commutators": commutators,
        "minus_sign_curvature_nonzero_counts": {name: count_nonzero(matrix) for name, matrix in curvature_minus.items()},
        "plus_sign_curvature_nonzero_counts": {name: count_nonzero(matrix) for name, matrix in curvature_plus.items()},
        "minus_sign_curvatures": curvature_minus,
        "plus_sign_curvatures": curvature_plus,
        "both_curvature_signs_confined_to_rank_four": all(
            confined_to_rank_four(matrix)
            for packet in (curvature_minus, curvature_plus)
            for matrix in packet.values()
        ),
    }


def main():
    runs = [run_case(point, prime) for point, prime in CASES]
    minus_flat = all(
        all(count == 0 for count in run["minus_sign_curvature_nonzero_counts"].values())
        for run in runs
    )
    plus_flat = all(
        all(count == 0 for count in run["plus_sign_curvature_nonzero_counts"].values())
        for run in runs
    )
    checks = {
        "value_matrices_are_variation_independent": all(run["value_packets_identical_across_variations"] for run in runs),
        "pivot_packets_are_variation_independent": all(run["pivot_packets_identical"] for run in runs),
        "both_commutator_conventions_are_nonflat": not minus_flat and not plus_flat,
    }
    if RETAIN_CROSS_GRADE:
        checks["retained_cross_grade_does_not_restore_flatness"] = all(
            any(count > 0 for count in run["minus_sign_curvature_nonzero_counts"].values())
            and any(count > 0 for count in run["plus_sign_curvature_nonzero_counts"].values())
            for run in runs
        )
    else:
        checks["curvature_is_confined_to_rank_four_block"] = all(
            run["both_curvature_signs_confined_to_rank_four"] for run in runs
        )
    packet = {
        "schema": "marici.cm_rank_seven_dual_cross_grade.v1" if RETAIN_CROSS_GRADE else "marici.cm_rank_seven_dual_flatness.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "retain_exact_cross_grade": RETAIN_CROSS_GRADE,
        "flat_convention": "derivative_minus_commutator" if minus_flat else "derivative_plus_commutator" if plus_flat else None,
        "runs": runs,
        "checks": checks,
    }
    output = ROOT / "results" / (
        "cm-rank-seven-dual-cross-grade.json"
        if RETAIN_CROSS_GRADE
        else "cm-rank-seven-dual-flatness.json"
    )
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": packet["status"],
        "flat_convention": packet["flat_convention"],
        "checks": checks,
        "runs": [{
            "point": run["point"],
            "prime": run["prime"],
            "derivative": run["derivative_nonzero_counts"],
            "commutator": run["commutator_nonzero_counts"],
            "minus": run["minus_sign_curvature_nonzero_counts"],
            "plus": run["plus_sign_curvature_nonzero_counts"],
            "pivots": run["pivots"],
        } for run in runs],
    }, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
