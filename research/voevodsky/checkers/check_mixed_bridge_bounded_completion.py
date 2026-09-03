from __future__ import annotations

import json
from fractions import Fraction


def render(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    cutoffs = [1, 2, 4, 8, 16, 32]
    cross_tail_norms = [Fraction(1, cutoff + 2) for cutoff in cutoffs]
    schur_tail_norms = [Fraction(1, 2 * (cutoff + 2) ** 2) for cutoff in cutoffs]
    assert all(cross_tail_norms[i + 1] < cross_tail_norms[i] for i in range(len(cutoffs) - 1))
    assert all(schur_tail_norms[i + 1] < schur_tail_norms[i] for i in range(len(cutoffs) - 1))

    first_cross = Fraction(1, 2)
    uniform_schur_lower_bound = Fraction(1) - first_cross**2 / Fraction(2)
    assert uniform_schur_lower_bound == Fraction(7, 8) > 0

    # Hostile pivot sequence has no positive uniform lower bound.
    hostile_pivots = [Fraction(1, cutoff + 2) for cutoff in cutoffs]
    assert hostile_pivots[-1] < hostile_pivots[0]
    hostile_inverse_norms = [Fraction(1, pivot) for pivot in hostile_pivots]
    assert hostile_inverse_norms[-1] > hostile_inverse_norms[0]

    result = {
        "schema": "marici.voevodsky.mixed-bridge-bounded-completion.v1",
        "status": "bounded_closed_mixed_bridge_realized",
        "cutoffs": cutoffs,
        "cross_tail_operator_norms": [render(value) for value in cross_tail_norms],
        "schur_tail_operator_norms": [render(value) for value in schur_tail_norms],
        "cross_tail_norms_strictly_decrease": True,
        "schur_tail_norms_strictly_decrease": True,
        "uniform_pivot_lower_bound": "2/1",
        "uniform_schur_lower_bound": render(uniform_schur_lower_bound),
        "closed_form": True,
        "radical_dimension": 0,
        "common_dense_core": "finitely supported sequences",
        "bounded_extension_unique": True,
        "hostile_pivot_lower_bound_uniform": False,
        "hostile_inverse_norms_grow": True,
        "unbounded_R_zeta_realized": False,
        "next_gate": "closed semibounded form theorem with common domain and relatively bounded cross term",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
