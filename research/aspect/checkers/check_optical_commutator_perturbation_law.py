#!/usr/bin/env python3
"""Audit the exact transport law and one-parameter commutator falsifier."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "optical-commutator-perturbation-law.v1.json"
RESULT = ASPECT / "results" / "optical_commutator_perturbation_law.json"

I = ((1 + 0j, 0j), (0j, 1 + 0j))
X = ((0j, 1 + 0j), (1 + 0j, 0j))
Z = ((1 + 0j, 0j), (0j, -1 + 0j))


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def dagger(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(2)) for i in range(2))


def scale(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def close(a, b, tol=1e-12):
    return all(abs(a[i][j] - b[i][j]) < tol for i in range(2) for j in range(2))


def word(z, x, zinv, xinv):
    return mm(mm(mm(z, x), zinv), xinv)


def overlap(a, psi):
    apsi = tuple(sum(a[i][j] * psi[j] for j in range(2)) for i in range(2))
    return sum(psi[i].conjugate() * apsi[i] for i in range(2))


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    theta, phi = 0.41, -0.27
    c, s = math.cos(theta), math.sin(theta)
    rotation = ((c, -s), (s, c))
    phase = ((cmath.exp(1j * phi), 0j), (0j, cmath.exp(-1j * phi)))
    u = mm(phase, rotation)
    alpha, beta = 0.37, -0.61
    zt = scale(cmath.exp(1j * alpha), mm(mm(u, Z), dagger(u)))
    xt = scale(cmath.exp(1j * beta), mm(mm(u, X), dagger(u)))
    transported = word(zt, xt, dagger(zt), dagger(xt))

    epsilon = contract["finite_falsifier"]["epsilon_radians"]
    ze = ((1 + 0j, 0j), (0j, -cmath.exp(1j * epsilon)))
    broken = word(ze, X, Z, X)
    predicted = ((-1 + 0j, 0j), (0j, -cmath.exp(1j * epsilon)))
    rail_zero = overlap(broken, (1 + 0j, 0j))
    rail_one = overlap(broken, (0j, 1 + 0j))

    checks = {
        "common_conjugation_and_rephasing_invariant": close(transported, scale(-1, I)),
        "finite_falsifier_matches_closed_form": close(broken, predicted),
        "one_parameter_breaks_centrality": not close(broken, scale(-1, I)),
        "rail_one_Y_is_minus_sine": abs(rail_one.imag + math.sin(epsilon)) < 1e-12,
        "target_dependence_detected": abs(rail_zero - rail_one) > 1e-6,
        "claim_boundary_preserved": not any(contract["claim_boundary"].values())
    }
    passed = all(checks.values())
    out = {
        "schema": "marici.aspect.optical-commutator-perturbation-law-result.v1",
        "passed": passed,
        "positive_transport_word": [[str(x) for x in row] for row in transported],
        "epsilon_radians": epsilon,
        "broken_word": [[str(x) for x in row] for row in broken],
        "rail_zero_record": [rail_zero.real, rail_zero.imag, abs(rail_zero)],
        "rail_one_record": [rail_one.real, rail_one.imag, abs(rail_one)],
        "checks": checks,
        "physical_status": "not_run",
        "conclusion": "exact_transport_law_and_one_parameter_falsifier_compiled"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
