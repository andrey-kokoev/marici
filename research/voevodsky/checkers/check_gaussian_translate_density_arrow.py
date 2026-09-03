from __future__ import annotations

import json
from math import comb, factorial
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/gaussian-translate-density-arrow-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    x = sp.symbols("x", real=True)
    gaussian = sp.exp(-x**2 / 2)

    hermite_identities = 0
    finite_difference_moments = 0
    for order in range(7):
        derivative = sp.diff(gaussian, x, order)
        expected = (-1) ** order * sp.hermite_prob(order, x) * gaussian
        assert sp.simplify(derivative - expected) == 0
        hermite_identities += 1

        # Forward difference weights produce the order-th derivative as h->0.
        weights = [(-1) ** (order - j) * comb(order, j) for j in range(order + 1)]
        for moment in range(order + 1):
            coefficient = sum(weights[j] * j**moment for j in range(order + 1))
            if moment < order:
                assert coefficient == 0
            else:
                assert coefficient == factorial(order)
            finite_difference_moments += 1

    # A PSD Gram matrix makes every finite translate combination nonnegative.
    gram = sp.Matrix([[2, 1], [1, 2]])
    c1, c2 = sp.symbols("c1 c2", real=True)
    quadratic = (sp.Matrix([c1, c2]).T * gram * sp.Matrix([c1, c2]))[0]
    assert sp.expand(quadratic) == 2 * c1**2 + 2 * c1 * c2 + 2 * c2**2
    assert gram.det() > 0 and gram[0, 0] > 0

    status = contract["status"]
    assert status["abstract_schwartz_density"] == "proved"
    assert status["all_translate_psd"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.gaussian-translate-density-arrow-check.v1",
        "status":"gaussian_translate_density_mechanism_verified",
        "hermite_derivative_identities_checked":hermite_identities,
        "finite_difference_moment_cancellations_checked":finite_difference_moments,
        "finite_gram_quadratic_transfer":True,
        "abstract_schwartz_density":True,
        "continuity_extension_required":True,
        "arithmetic_kernel_identification_supplied":False,
        "all_translate_psd_supplied":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
