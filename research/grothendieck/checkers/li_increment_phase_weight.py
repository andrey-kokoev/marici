"""Exact phase identity behind the finite Li increment measure."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    theta = sp.symbols("theta", real=True)
    k = sp.symbols("k", integer=True, nonnegative=True)

    a_prev = 2 - 2 * sp.cos((k - 1) * theta)
    a_now = 2 - 2 * sp.cos(k * theta)
    a_next = 2 - 2 * sp.cos((k + 1) * theta)
    second_difference = sp.trigsimp((a_next - 2 * a_now + a_prev) / 2)
    target = sp.trigsimp((2 - 2 * sp.cos(theta)) * sp.cos(k * theta))
    residual = sp.trigsimp(sp.expand_trig(second_difference - target))
    assert residual == 0

    sigma, gamma = sp.symbols("sigma gamma", real=True)
    rho = sigma + sp.I * gamma
    u = 1 - 1 / rho
    phase_weight = sp.simplify((1 - u) * sp.conjugate(1 - u))
    inverse_square = 1 / (sigma**2 + gamma**2)
    assert sp.simplify(phase_weight - inverse_square) == 0

    print("second_difference_phase_residual=0")
    print("phase_weight=1/abs(rho)^2")
    print("increment_measure_finite_if_inverse_square_zero_sum_converges=True")


if __name__ == "__main__":
    main()
