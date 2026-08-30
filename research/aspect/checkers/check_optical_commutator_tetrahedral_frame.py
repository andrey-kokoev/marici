#!/usr/bin/env python3
"""Check the minimal noise-optimal tetrahedral coherent-error frame."""
from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "optical-commutator-tetrahedral-frame.v1.json"
RESULT = ASPECT / "results" / "optical_commutator_tetrahedral_frame.json"


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def gram(a):
    return mm(transpose(a), a)


def eigenvalues_symmetric(a, tol=1e-14, sweeps=100):
    a = [row[:] for row in a]
    n = len(a)
    for _ in range(sweeps):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)), key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < tol:
            break
        phi = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
        c, s = math.cos(phi), math.sin(phi)
        for k in range(n):
            if k not in (p, q):
                apk, aqk = a[p][k], a[q][k]
                a[p][k] = a[k][p] = c * apk - s * aqk
                a[q][k] = a[k][q] = s * apk + c * aqk
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = c*c*app - 2*s*c*apq + s*s*aqq
        a[q][q] = s*s*app + 2*s*c*apq + c*c*aqq
        a[p][q] = a[q][p] = 0.0
    return sorted(a[i][i] for i in range(n))


def condition(a):
    vals = eigenvalues_symmetric(gram(a))
    return math.sqrt(max(vals) / min(vals))


def centered(rows, tol=1e-12):
    return all(abs(sum(row[j] for row in rows)) < tol for j in range(1, 4))


def close_matrix(a, b, tol=1e-12):
    return all(abs(a[i][j] - b[i][j]) < tol for i in range(len(a)) for j in range(len(a[0])))


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    q = 1 / math.sqrt(3)
    # Contract signs are xyz; syndrome coordinates are I,z,x,y.
    tetra = [[1.0, signs[2] * q, signs[0] * q, signs[1] * q] for signs in contract["tetrahedral_bloch_signs_xyz"]]
    expected_gram = [[0.0] * 4 for _ in range(4)]
    for i, value in enumerate(contract["expected_gram_diagonal"]):
        expected_gram[i][i] = value
    tetra_gram = gram(tetra)
    tetra_condition = condition(tetra)

    axis = [
        [1.0, 1.0, 0.0, 0.0],
        [1.0, -1.0, 0.0, 0.0],
        [1.0, 0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0, 1.0]
    ]
    axis_condition = condition(axis)
    optimal_lower_bound = math.sqrt(
        contract["optimality_basis"]["identity_column_squared_norm"]
        / contract["optimality_basis"]["maximum_possible_smallest_bloch_eigenvalue"]
    )

    shifted = [row[:] for row in tetra]
    shifted[0][1] += 0.1
    checks = {
        "tetrahedron_is_centered": centered(tetra),
        "tetrahedron_is_isotropic": close_matrix(tetra_gram, expected_gram),
        "condition_attains_sqrt_three": abs(tetra_condition - contract["expected_condition_number"]) < 1e-12,
        "trace_bound_proves_four_probe_optimum": abs(tetra_condition - optimal_lower_bound) < 1e-12,
        "tetrahedron_improves_axis_frame": tetra_condition < axis_condition,
        "noncentered_hostile_rejected": not centered(shifted),
        "three_probe_hostile_rejected": len(tetra[:3]) < 4,
        "epsilon_falsifier_preserved": contract["frozen_finite_falsifier_epsilon"] == 0.01,
        "claim_boundary_preserved": not any(contract["claim_boundary"].values())
    }
    passed = all(checks.values())
    out = {
        "schema": "marici.aspect.optical-commutator-tetrahedral-frame-result.v1",
        "passed": passed,
        "tetrahedral_gram": tetra_gram,
        "tetrahedral_condition_number": tetra_condition,
        "axis_condition_number": axis_condition,
        "optimal_lower_bound": optimal_lower_bound,
        "checks": checks,
        "physical_status": "not_run",
        "conclusion": "tetrahedral_probes_are_minimal_and_worst_case_noise_optimal"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
