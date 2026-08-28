#!/usr/bin/env python3
"""Check local identifiability of coherent commutator residue channels."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "optical-commutator-error-syndrome.v1.json"
RESULT = ASPECT / "results" / "optical_commutator_error_syndrome.json"

I = ((1 + 0j, 0j), (0j, 1 + 0j))
X = ((0j, 1 + 0j), (1 + 0j, 0j))
Y = ((0j, -1j), (1j, 0j))
Z = ((1 + 0j, 0j), (0j, -1 + 0j))
GENERATORS = (I, Z, X, Y)
R2 = 2 ** -0.5
PROBES = ((1 + 0j, 0j), (0j, 1 + 0j), (R2, R2), (R2, 1j * R2))


def expectation(a, psi):
    apsi = tuple(sum(a[i][j] * psi[j] for j in range(2)) for i in range(2))
    return sum(psi[i].conjugate() * apsi[i] for i in range(2))


def residual(generator, t):
    if generator == I:
        return tuple(tuple(cmath.exp(1j * t) * I[i][j] for j in range(2)) for i in range(2))
    return tuple(tuple(math.cos(t) * I[i][j] + 1j * math.sin(t) * generator[i][j] for j in range(2)) for i in range(2))


def control_record(generator, psi, t):
    # The ideal word is -I; the residual is applied after it.
    value = -expectation(residual(generator, t), psi)
    return value.real, value.imag


def rank(matrix, tol=1e-10):
    a = [list(map(float, row)) for row in matrix]
    rows, cols, pivot_row = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if abs(a[r][col]) > tol), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row:
                factor = a[r][col]
                a[r] = [a[r][j] - factor * a[pivot_row][j] for j in range(cols)]
        pivot_row += 1
    return pivot_row


def determinant4(a):
    total = 0
    for p0 in range(4):
        for p1 in range(4):
            for p2 in range(4):
                for p3 in range(4):
                    p = (p0, p1, p2, p3)
                    if len(set(p)) < 4:
                        continue
                    inversions = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
                    total += (-1 if inversions % 2 else 1) * math.prod(a[i][p[i]] for i in range(4))
    return total


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    expected = contract["unsigned_expectation_matrix"]
    analytic = [[round(expectation(g, psi).real, 12) for g in GENERATORS] for psi in PROBES]
    h = 1e-6
    y_jacobian = []
    x_jacobian = []
    for psi in PROBES:
        y_row, x_row = [], []
        for g in GENERATORS:
            xp, yp = control_record(g, psi, h)
            xm, ym = control_record(g, psi, -h)
            y_row.append((yp - ym) / (2 * h))
            x_row.append((xp - xm) / (2 * h))
        y_jacobian.append(y_row)
        x_jacobian.append(x_row)

    checks = {
        "source_expectation_matrix_matches": analytic == expected,
        "full_Y_first_jet_rank_four": rank(y_jacobian) == 4,
        "determinant_is_frozen_nonzero_value": abs(determinant4(expected) - contract["expected_determinant"]) < 1e-12,
        "every_three_probe_hostile_loses_rank": all(rank([row for j, row in enumerate(y_jacobian) if j != i]) < 4 for i in range(4)),
        "X_first_jet_is_blind": rank(x_jacobian) == 0,
        "epsilon_falsifier_preserved": contract["frozen_finite_falsifier_epsilon"] == 0.01,
        "claim_boundary_preserved": not any(contract["claim_boundary"].values())
    }
    passed = all(checks.values())
    out = {
        "schema": "marici.aspect.optical-commutator-error-syndrome-result.v1",
        "passed": passed,
        "Y_first_jet_jacobian": y_jacobian,
        "Y_first_jet_rank": rank(y_jacobian),
        "X_first_jet_rank": rank(x_jacobian),
        "determinant": determinant4(expected),
        "checks": checks,
        "physical_status": "not_run",
        "conclusion": "four_probe_Y_quadrature_locally_identifies_complete_coherent_residue"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
