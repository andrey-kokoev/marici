from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/endpoint-separation-direct-summand-obstruction-v1.json")


def moment_localizer(q: sp.Rational, atoms: list[tuple[sp.Rational, sp.Rational]], m: sp.Rational, c: sp.Rational, size: int) -> sp.Matrix:
    return sp.Matrix(
        size,
        size,
        lambda i, j: sum(weight * (q - y) * y ** (i + j) for y, weight in atoms)
        + (m - c),
    )


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    q = sp.Rational(1, 2)
    c = sp.Rational(3, 2)
    atoms = [(sp.Rational(0), sp.Rational(2)), (sp.Rational(1, 3), sp.Rational(5))]
    interior_mass = sum(weight for _, weight in atoms)

    # With no endpoint summand, a monomial diagonal is forced negative.
    n = 3
    no_endpoint = moment_localizer(q, atoms, sp.Rational(0), c, n + 1)
    exact_diagonal = no_endpoint[n, n]
    bound = q ** (2 * n + 1) * interior_mass - c
    assert exact_diagonal <= bound < 0

    # Insufficient endpoint mass also fails at sufficiently high degree.
    m_small = sp.Rational(1)
    n_small = 4
    insufficient = moment_localizer(q, atoms, m_small, c, n_small + 1)
    insufficient_bound = q ** (2 * n_small + 1) * interior_mass - (c - m_small)
    assert insufficient[n_small, n_small] <= insufficient_bound < 0

    # Exact cancellation leaves the interior Gram localizer.
    exact_cancel = moment_localizer(q, atoms, c, c, 5)
    vectors = [sp.Matrix([y**i for i in range(5)]) for y, _ in atoms]
    expected = sum(
        (weight * (q - y) * (vector * vector.T) for (y, weight), vector in zip(atoms, vectors)),
        sp.zeros(5),
    )
    assert exact_cancel == expected
    assert all(minor >= 0 for minor in exact_cancel.berkowitz_minors())

    excess = moment_localizer(q, atoms, sp.Rational(2), c, 5)
    excess_expected = expected + sp.Rational(1, 2) * sp.ones(5)
    assert excess == excess_expected
    assert all(minor >= 0 for minor in excess.berkowitz_minors())

    result = {
        "schema":"marici.voevodsky.endpoint-separation-direct-summand-check.v1",
        "status":"endpoint_direct_summand_necessity_verified",
        "separating_monomial_degree_no_endpoint":n,
        "separating_monomial_degree_insufficient_endpoint":n_small,
        "exact_endpoint_cancellation_factor":True,
        "passed":True,
        "gamma_prime_endpoint_summand":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"]
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
