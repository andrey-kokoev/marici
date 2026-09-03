from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/xi-paired-hadamard-multiplicity-contract-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    y, x, a = sp.symbols("y x a", nonzero=True)
    m = sp.symbols("m", integer=True, positive=True)

    paired = (1 / (y - a) + 1 / (y + a)) / (2 * y)
    assert sp.simplify(paired - 1 / (y**2 - a**2)) == 0
    squared_resolvent = 1 / (x - a**2)
    assert sp.simplify(squared_resolvent.subs(x, y**2) - paired) == 0

    paired_factor = (1 - y**2 / a**2) ** m
    log_derivative_x = sp.simplify(sp.diff(sp.log((1 - x / a**2) ** m), x))
    assert sp.simplify(log_derivative_x - m / (x - a**2)) == 0

    # Completed elementary factors have exactly one endpoint resolvent after division by 2y.
    s = sp.Rational(1, 2) + y
    endpoint = sp.simplify((1 / s + 1 / (s - 1)) / (2 * y))
    assert sp.simplify(endpoint - 1 / (y**2 - sp.Rational(1, 4))) == 0

    beta, gamma = sp.symbols("beta gamma", real=True, nonzero=True)
    off_axis_a = beta - sp.Rational(1, 2) + sp.I * gamma
    off_axis_lambda = sp.simplify(-off_axis_a**2)
    conjugate_lambda = sp.simplify(-sp.conjugate(off_axis_a) ** 2)
    assert sp.simplify(conjugate_lambda - sp.conjugate(off_axis_lambda)) == 0

    critical_a = sp.I * gamma
    assert sp.simplify(sp.conjugate(critical_a) + critical_a) == 0
    assert sp.simplify(-critical_a**2 - gamma**2) == 0

    result = {
        "schema":"marici.voevodsky.xi-paired-hadamard-multiplicity-contract-check.v1",
        "status":"paired_orbit_multiplicity_algebra_verified",
        "paired_resolvent_factor":True,
        "multiplicity_not_doubled":True,
        "endpoint_resolvent":True,
        "off_axis_conjugate_orbits":True,
        "critical_line_positive_ordinate_counted_once":True,
        "authoritative_classical_citations":False,
        "source_complete_equivalence":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
