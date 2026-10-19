"""Exact illustrative controls; not source-matrix or general-theorem verification."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NOTE = "research/nima/scattering-hamiltonian-bridge-conceptual-audit-v1.md"
RESULT = "research/nima/results/scattering-bridge-conceptual-audit-v1.json"


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def norm2(v):
    return sum(x.real * x.real + x.imag * x.imag for x in v)


def expectation(a, v):
    return sum(x.conjugate() * y for x, y in zip(v, matvec(a, v)))


def run():
    checks = []

    # Integer complex arithmetic is exact for these small integer fixtures.
    a = [[0, -2], [2, 0]]
    q = [[0, -2j], [2j, 0]]  # hbar=1; Q=iA, not A^T A/2.
    plus, minus = [1 + 0j, 1j], [1 + 0j, -1j]
    assert matvec(q, plus) == [2 * x for x in plus]
    assert matvec(q, minus) == [-2 * x for x in minus]
    assert norm2(matvec(a, plus)) == norm2(matvec(a, minus)) == 8
    assert expectation(q, plus) == 4 and expectation(q, minus) == -4
    checks.append("equal coefficient quadratic energy does not identify Q expectation")

    # With B=1 and chi=0, the core's derivative depends on the lead trace.
    # With a fixed zero lead trace, opposite chi gives opposite boundary force.
    core_drive = lambda chi, trace: 2 * chi - trace
    assert core_drive(0, 0) != core_drive(0, 1)
    boundary_force = lambda trace, chi: trace - chi
    assert boundary_force(0, 1) != boundary_force(0, -1)
    checks.append("retained lead/core data are needed for the coupled dynamics")

    # D=diag(1,3), eta=ell=1, W=(1,1)/sqrt(2).
    # K_core=D-WW^dagger is positive: first pivot=1/2, determinant=1.
    assert F(1, 2) * F(5, 2) - F(1, 2) ** 2 == 1
    response = lambda e: 1 + F(1, 2) * (1 / (e - 1) + 1 / (e - 3))
    derivative = lambda e: -F(1, 2) * (1 / (e - 1) ** 2 + 1 / (e - 3) ** 2)
    assert response(F(4)) == F(5, 3)
    assert response(F(5)) == F(11, 8)
    assert response(F(4)) != response(F(5))
    for e in (F(-1), F(0), F(2), F(4), F(5)):
        assert derivative(e) < 0
    checks.append("nonzero retained-core coupling gives energy-dependent response")

    # Same D=diag(2,4), but W=e1 or e2. Both K_core=D-WW^dagger
    # remain positive. Core spectrum alone does not determine response.
    e = F(5)
    port_one = 1 + 1 / (e - 2)
    port_two = 1 + 1 / (e - 4)
    assert port_one == F(4, 3) and port_two == 2
    checks.append("same contact-dressed core spectrum can have distinct channel response")

    # A two-dimensional autonomous Q=diag(1,3) has no energy-E eigenvector
    # at E=2 or 4. Only a finite illustration, not a proof about AC spectra.
    for e in (F(2), F(4)):
        assert (1 - e) * (3 - e) != 0
    checks.append("finite spectral illustration does not encode a continuum of energies")

    inputs = [NOTE, "research/strominger/interface-preserving-carrier-hamiltonian.md",
              "research/strominger/retained-hamiltonian-observer.md",
              "research/strominger/neutron-autonomous-rim-scattering.md",
              "research/scattering/high-energy/pentachoron_autonomous_contact_note.md",
              "research/nima/contracts/scattering-strominger-update.v1.json",
              str(Path(__file__).resolve().relative_to(ROOT)).replace("\\", "/")]
    result = {
        "schema": "marici.scattering.conceptual-audit-controls.v1",
        "status": "pass", "check_count": len(checks), "checks": checks,
        "verification_level": "exact finite illustrative algebra; general arguments written only",
        "source_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in inputs},
        "actual_source_matrices_verified": False,
        "general_spectral_theorem_kernel_verified": False,
        "source_suites_rerun": False, "stationary_scattering_solves": 0,
        "scientific_outcomes_assigned": False, "physical_realization_admitted": False,
    }
    out = ROOT / RESULT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "check_count": len(checks), "receipt": RESULT}))


if __name__ == "__main__":
    run()
