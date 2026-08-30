import json
from pathlib import Path
import sympy as sp


def finite_part(expression, epsilon):
    return sp.expand(expression).coeff(epsilon, 0)


def main():
    epsilon = sp.symbols("epsilon", positive=True)
    a, b, c = sp.symbols("a b c", real=True)

    square = (epsilon**-1 - epsilon) ** 2
    square_fp = finite_part(square, epsilon)
    assert sp.simplify(square - (epsilon**2 - 1) ** 2 / epsilon**2) == 0
    assert square_fp == -2

    arbitrary = epsilon**-2 + c
    assert finite_part(arbitrary, epsilon) == c

    f = epsilon**-1 + a
    g = epsilon + b
    product_fp = finite_part(f * g, epsilon)
    assert product_fp == a * b + 1
    assert product_fp - finite_part(f, epsilon) * finite_part(g, epsilon) == 1

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_algebraic_finite_part_order_no_go",
        "positive_square": str(sp.expand(square)),
        "positive_square_finite_part": str(square_fp),
        "arbitrary_constant_fixture": str(arbitrary),
        "arbitrary_finite_part": str(finite_part(arbitrary, epsilon)),
        "multiplicativity_residual": "1",
        "finite_part_linear": True,
        "finite_part_positive": False,
        "finite_part_multiplicative": False,
        "off_seam_divisor_avoidance": "requires_new_relative_structure",
    }
    out = Path(__file__).parents[1] / "results" / "theta-finite-part-order.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
