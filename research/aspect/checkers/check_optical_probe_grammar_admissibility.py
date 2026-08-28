#!/usr/bin/env python3
"""Check source reachability and the constrained dual-rail syndrome optimum."""
from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "optical-probe-grammar-admissibility.v1.json"
RESULT = ASPECT / "results" / "optical_probe_grammar_admissibility.json"


def gram(a):
    return [[sum(row[i] * row[j] for row in a) for j in range(4)] for i in range(4)]


def rank(a, tol=1e-11):
    a = [row[:] for row in a]
    rows, cols, p = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(p, rows) if abs(a[r][col]) > tol), None)
        if pivot is None:
            continue
        a[p], a[pivot] = a[pivot], a[p]
        scale = a[p][col]
        a[p] = [x / scale for x in a[p]]
        for r in range(rows):
            if r != p:
                f = a[r][col]
                a[r] = [a[r][j] - f * a[p][j] for j in range(cols)]
        p += 1
    return p


def eig_symmetric(a, tol=1e-14):
    a = [row[:] for row in a]
    n = len(a)
    for _ in range(100):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)), key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < tol:
            break
        angle = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
        c, s = math.cos(angle), math.sin(angle)
        for k in range(n):
            if k not in (p, q):
                x, y = a[p][k], a[q][k]
                a[p][k] = a[k][p] = c * x - s * y
                a[q][k] = a[k][q] = s * x + c * y
        x, y, z = a[p][p], a[q][q], a[p][q]
        a[p][p] = c*c*x - 2*s*c*z + s*s*y
        a[q][q] = s*s*x + 2*s*c*z + c*c*y
        a[p][q] = a[q][p] = 0.0
    return sorted(a[i][i] for i in range(n))


def condition(a):
    values = eig_symmetric(gram(a))
    return math.sqrt(values[-1] / values[0])


def equator(phi):
    return [1.0, 0.0, math.cos(phi), math.sin(phi)]


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    frozen = [equator(k * math.pi / 4) for k in range(8)]
    frozen_rank = rank(frozen)

    constrained = [
        [1.0, 1.0, 0.0, 0.0],
        equator(0.0),
        equator(2 * math.pi / 3),
        equator(4 * math.pi / 3)
    ]
    values = eig_symmetric(gram(constrained))
    expected_values = sorted([
        (5 - math.sqrt(13)) / 2,
        1.5,
        1.5,
        (5 + math.sqrt(13)) / 2
    ])
    constrained_condition = condition(constrained)

    two_pole_best_condition = math.sqrt((2 + 2 * math.sqrt(2)) / (2 - math.sqrt(2)))
    tetra_z = 1 / math.sqrt(3)
    checks = {
        "fixed_post_splitter_rank_at_most_three": frozen_rank == 3,
        "fixed_grammar_has_zero_Z_column": all(row[1] == 0 for row in frozen),
        "tetrahedral_latitude_is_forbidden": tetra_z != 0,
        "selector_frame_is_faithful": rank(constrained) == 4,
        "selector_frame_spectrum_is_exact": all(abs(a - b) < 1e-12 for a, b in zip(values, expected_values)),
        "selector_condition_matches_contract": abs(constrained_condition - contract["selector_extended_grammar"]["condition_number"]) < 1e-12,
        "one_pole_branch_beats_two_pole_branch": constrained_condition < two_pole_best_condition,
        "tetrahedral_optimum_requires_next_constructor": contract["variable_splitter_optimum"]["condition_number"] < constrained_condition,
        "epsilon_falsifier_preserved": contract["frozen_finite_falsifier_epsilon"] == 0.01,
        "claim_boundary_preserved": not any(contract["claim_boundary"].values())
    }
    passed = all(checks.values())
    out = {
        "schema": "marici.aspect.optical-probe-grammar-admissibility-result.v1",
        "passed": passed,
        "frozen_post_splitter_rank": frozen_rank,
        "first_missing_constructor": contract["first_missing_constructor"],
        "selector_frame_eigenvalues": values,
        "selector_frame_condition_number": constrained_condition,
        "two_pole_branch_best_condition_number": two_pole_best_condition,
        "tetrahedral_condition_number": contract["variable_splitter_optimum"]["condition_number"],
        "checks": checks,
        "physical_status": "not_run",
        "conclusion": "frozen_grammar_not_faithful_selector_is_first_missing_constructor"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
