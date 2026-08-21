"""Exact phase-modulus defect and near-line latency asymptotic for an off-line zero."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    alpha, beta, epsilon = sp.symbols("alpha beta epsilon", positive=True)
    rho = sp.Rational(1, 2) + alpha + sp.I * beta
    u = 1 - 1 / rho
    modulus_squared = sp.simplify(u * sp.conjugate(u))
    denominator = (sp.Rational(1, 2) + alpha) ** 2 + beta**2
    expected = 1 - 2 * alpha / denominator
    assert sp.simplify(modulus_squared - expected) == 0

    reflected_rho = 1 - rho
    reflected_u = sp.simplify(1 - 1 / reflected_rho)
    assert sp.simplify(reflected_u - 1 / u) == 0

    # With epsilon=2 alpha/|rho|^2, log amplification per order is
    # -log|u|=-1/2 log(1-epsilon)=epsilon/2+O(epsilon^2).
    log_amplification = -sp.log(1 - epsilon) / 2
    expansion = sp.series(log_amplification, epsilon, 0, 4)
    assert expansion == epsilon / 2 + epsilon**2 / 4 + epsilon**3 / 6 + sp.Order(epsilon**4)

    print("right_zero_phase_modulus_squared=1-2*alpha/abs(rho)^2")
    print("reflected_phase=inverse_phase")
    print("per_order_log_amplification=alpha/abs(rho)^2+O(alpha^2/abs(rho)^4)")
    print("order_one_detection_scale=abs(rho)^2/alpha")
    print("finite_rank_latency_unbounded=True")


if __name__ == "__main__":
    main()
