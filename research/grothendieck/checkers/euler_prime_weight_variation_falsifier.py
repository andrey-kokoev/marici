"""Exact hostile test for varying local Euler prime-power weights."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    x, log_p, delta = sp.symbols("x log_p delta")
    order = 8
    weights = sp.symbols(f"w1:{order + 1}")

    local_log_derivative = log_p * x / (1 - x)
    canonical_series = sp.series(local_log_derivative, x, 0, order + 1).removeO()
    varied_series = sum(weights[m - 1] * x**m for m in range(1, order + 1))
    coefficient_equations = [
        sp.Eq(varied_series.coeff(x, m), canonical_series.coeff(x, m))
        for m in range(1, order + 1)
    ]
    solution = sp.solve(coefficient_equations, weights, dict=True)

    altered = canonical_series + delta * x**5
    altered_residual = sp.expand(altered - canonical_series)

    assert solution == [{weight: log_p for weight in weights}]
    assert altered_residual == delta * x**5
    assert altered_residual.subs(delta, 0) == 0

    print(f"truncation_order={order}")
    print("unique_weights=" + str(tuple(solution[0][weight] for weight in weights)))
    print(f"altered_fifth_prime_power_residual={altered_residual}")
    print("nonzero_weight_variation_preserves_local_euler_factor=False")
    print("deliberate_failure_exhibited=True")


if __name__ == "__main__":
    main()
