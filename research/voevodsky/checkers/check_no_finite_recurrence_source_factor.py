from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/no-finite-recurrence-source-factor-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    z = sp.symbols("z")
    bases = [sp.Rational(1, 5), sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(4, 5)]
    weights = [sp.Rational(2), sp.Rational(3), sp.Rational(5), sp.Rational(7)]
    order = len(bases)
    moments = [sum(w * y**n for w, y in zip(weights, bases)) for n in range(2 * order + 2)]

    characteristic = sp.Poly(sp.prod(sp.Symbol("X") - y for y in bases), sp.Symbol("X"))
    coefficients = characteristic.all_coeffs()
    for n in range(order + 1):
        recurrence = sum(coefficients[k] * moments[n + order - k] for k in range(order + 1))
        assert sp.simplify(recurrence) == 0

    # No recurrence of lower order exists: the leading square Hankel/Vandermonde matrix is nonsingular.
    hankel = sp.Matrix(order, order, lambda i, j: moments[i + j])
    assert hankel.det() != 0

    transform = sp.factor(sum(w / (1 - y * z) for w, y in zip(weights, bases)))
    denominator = sp.denom(transform)
    assert sp.degree(denominator, z) == order
    for y in bases:
        assert sp.simplify(denominator.subs(z, 1 / y)) == 0

    # Grouping repeated bases adds residues and reduces pole count only when bases coincide.
    repeated_bases = [bases[0], bases[0], bases[1]]
    repeated_weights = [sp.Rational(2), sp.Rational(11), sp.Rational(3)]
    grouped_transform = sp.factor(sum(w / (1 - y * z) for w, y in zip(repeated_weights, repeated_bases)))
    assert sp.degree(sp.denom(grouped_transform), z) == 2
    assert sp.simplify((repeated_weights[0] + repeated_weights[1])) != 0

    result = {
        "schema":"marici.voevodsky.no-finite-recurrence-source-factor-check.v1",
        "status":"finite_recurrence_obstruction_verified",
        "distinct_base_count":order,
        "minimal_recurrence_order":order,
        "rational_transform_pole_count":order,
        "grouped_repeated_base_pole_count":2,
        "infinite_distinct_source_rates_verified":False,
        "fixed_finite_source_factor_falsified":"conditional_on_source_expansion",
        "all_rank_positive_kernel_falsified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
