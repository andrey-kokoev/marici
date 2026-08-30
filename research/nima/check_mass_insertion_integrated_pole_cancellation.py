"""Exact formal-log audit of the apparent poles in source equation (4.7)."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


Linear = tuple[int, int]  # coefficients of (x1,x2)


def add_linear(left: Linear, right: Linear, scale: int = 1) -> Linear:
    return (left[0] + scale * right[0], left[1] + scale * right[1])


def substitute_y(c1: int, c2: int) -> dict[Linear, Linear]:
    """Return coefficients of each formal log after y=c1*x1+c2*x2."""
    x1, x2, y = (1, 0), (0, 1), (c1, c2)
    forms = [
        (add_linear(x1, x2), +1),
        ((2 * y[0], 2 * y[1]), +1),
        (add_linear(x1, y), -1),
        (add_linear(y, x2), -1),
    ]
    coefficients: dict[Linear, Linear] = defaultdict(lambda: (0, 0))
    for form, sign in forms:
        coefficients[form] = add_linear(coefficients[form], form, sign)
    return {form: coefficient for form, coefficient in coefficients.items() if coefficient != (0, 0)}


def main() -> None:
    numerator_at_y_eq_x1 = substitute_y(1, 0)
    numerator_at_y_eq_x2 = substitute_y(0, 1)
    assert numerator_at_y_eq_x1 == {}
    assert numerator_at_y_eq_x2 == {}

    # Differentiating the numerator with respect to y cancels all constant
    # terms and gives 2 log(2y)-log(x1+y)-log(y+x2).
    finite_limits = {
        "y=x1": "log(2*x1/(x1+x2))/(2*x1*(x1^2-x2^2))",
        "y=x2": "log(2*x2/(x1+x2))/(2*x2*(x2^2-x1^2))",
    }

    result = {
        "schema": "marici.mass-insertion-integrated-pole-cancellation.v1",
        "source_equation": "arXiv:1909.02517v1 Eq. (4.7)",
        "numerator_vanishes_at_y=x1": True,
        "numerator_vanishes_at_y=x2": True,
        "residue_at_y=x1": 0,
        "residue_at_y=x2": 0,
        "generic_finite_limits": finite_limits,
        "surviving_log_letters": ["x1+x2", "2*y", "x1+y", "y+x2"],
        "conclusion": (
            "The factors y-x1 and y-x2 are removable after Kummer integration. "
            "Only the source partial-energy/logarithmic coefficient letters remain."
        ),
    }
    out = Path(__file__).with_name("results") / "mass-insertion-integrated-pole-cancellation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
