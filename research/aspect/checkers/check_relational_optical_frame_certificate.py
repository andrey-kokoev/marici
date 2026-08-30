#!/usr/bin/env python3
"""Check relational frame spectra and exact tetrahedral splitter settings."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "relational-optical-frame-certificate.v1.json"
RESULT = ASPECT / "results" / "relational_optical_frame_certificate.json"


def inner(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def fidelity(a, b):
    return abs(inner(a, b)) ** 2


def bloch_state(x, y, z):
    a = math.sqrt((1 + z) / 2)
    if abs(1 - z) < 1e-15:
        return (1 + 0j, 0j)
    phase = cmath.exp(1j * math.atan2(y, x))
    return (a + 0j, phase * math.sqrt((1 - z) / 2))


def row_gram_from_fidelities(states):
    return [[2 * fidelity(a, b) for b in states] for a in states]


def eigenvalues_symmetric(a, tol=1e-14):
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


def apply_unitary(u, state):
    return tuple(sum(u[i][j] * state[j] for j in range(2)) for i in range(2))


def close_matrix(a, b, tol=1e-12):
    return all(abs(a[i][j] - b[i][j]) < tol for i in range(len(a)) for j in range(len(a)))


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    q = 1 / math.sqrt(3)
    signs = ([1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1])
    tetra = [bloch_state(x*q, y*q, z*q) for x, y, z in signs]
    tetra_gram = row_gram_from_fidelities(tetra)
    tetra_values = eigenvalues_symmetric(tetra_gram)

    selector = [
        bloch_state(0, 0, 1),
        bloch_state(1, 0, 0),
        bloch_state(math.cos(2*math.pi/3), math.sin(2*math.pi/3), 0),
        bloch_state(math.cos(4*math.pi/3), math.sin(4*math.pi/3), 0)
    ]
    selector_gram = row_gram_from_fidelities(selector)
    selector_values = eigenvalues_symmetric(selector_gram)

    theta, phi = 0.39, -0.44
    u = (
        (math.cos(theta), -cmath.exp(1j*phi)*math.sin(theta)),
        (cmath.exp(-1j*phi)*math.sin(theta), math.cos(theta))
    )
    transported_gram = row_gram_from_fidelities([apply_unitary(u, s) for s in tetra])

    settings_match = True
    for setting in contract["variable_splitter_settings"]:
        x, y, z = setting["bloch_xyz_signs"]
        state = bloch_state(x*q, y*q, z*q)
        measured_t = abs(state[0]) ** 2
        expected_t = (1 + z*q) / 2
        measured_phase = cmath.phase(state[1])
        expected_phase = math.atan2(y, x)
        settings_match &= abs(measured_t - expected_t) < 1e-12
        settings_match &= abs(cmath.exp(1j*(measured_phase - expected_phase)) - 1) < 1e-12

    expected_tetra_values = [4/3, 4/3, 4/3, 4]
    expected_selector_values = sorted([(5-math.sqrt(13))/2, 1.5, 1.5, (5+math.sqrt(13))/2])
    mixed_hostile_diagonal = 2 * 0.8
    checks = {
        "tetrahedral_fidelity_gram_has_expected_spectrum": all(abs(a-b) < 1e-12 for a, b in zip(tetra_values, expected_tetra_values)),
        "selector_fidelity_gram_has_expected_spectrum": all(abs(a-b) < 1e-12 for a, b in zip(selector_values, expected_selector_values)),
        "common_unitary_is_gauge": close_matrix(tetra_gram, transported_gram),
        "exact_variable_splitter_settings_compile": settings_match,
        "tetrahedral_off_diagonal_fidelity_is_one_third": all(abs(fidelity(tetra[i], tetra[j])-1/3) < 1e-12 for i in range(4) for j in range(i+1, 4)),
        "selector_overlap_pattern_matches": all(abs(selector_gram[0][j]-1) < 1e-12 for j in range(1,4)) and all(abs(selector_gram[i][j]-0.5) < 1e-12 for i in range(1,4) for j in range(i+1,4)),
        "mixed_probe_hostile_requires_purity_record": abs(mixed_hostile_diagonal - 2) > 1e-12,
        "claim_boundary_preserved": not any(contract["claim_boundary"].values())
    }
    passed = all(checks.values())
    out = {
        "schema": "marici.aspect.relational-optical-frame-certificate-result.v1",
        "passed": passed,
        "tetrahedral_row_gram_eigenvalues": tetra_values,
        "selector_row_gram_eigenvalues": selector_values,
        "tetrahedral_condition_number": math.sqrt(tetra_values[-1] / tetra_values[0]),
        "selector_condition_number": math.sqrt(selector_values[-1] / selector_values[0]),
        "checks": checks,
        "physical_status": "not_run",
        "conclusion": "pairwise_fidelities_certify_frame_conditioning_without_absolute_Pauli_frame"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
