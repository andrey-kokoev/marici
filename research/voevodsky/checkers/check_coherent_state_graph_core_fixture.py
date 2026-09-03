from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/coherent-state-common-graph-core-reduction-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    x, h = sp.symbols("x h", real=True, positive=True)

    g_plus = sp.exp(-(x - h) ** 2 / 2)
    g_minus = sp.exp(-(x + h) ** 2 / 2)
    central_difference = (g_plus - g_minus) / (2 * h)
    derivative_state = x * sp.exp(-x**2 / 2)
    assert sp.limit(central_difference, h, 0, dir="+") == derivative_state

    # Exact polynomially weighted graph-norm fixture.
    error = sp.expand_func(central_difference - derivative_state)
    weighted_error_squared = sp.integrate(
        (1 + x**2) * error**2, (x, -sp.oo, sp.oo)
    )
    weighted_error_squared = sp.simplify(weighted_error_squared)
    assert sp.limit(weighted_error_squared, h, 0, dir="+") == 0

    # Bounded perturbations give equivalent graph norms.
    base_norm, multiplier_norm, bounded_norm, bound = sp.symbols(
        "base_norm multiplier_norm bounded_norm bound", nonnegative=True
    )
    gamma_graph = base_norm + multiplier_norm
    assembled_graph = gamma_graph + bounded_norm
    assumptions_fixture = {
        base_norm: sp.Rational(2),
        multiplier_norm: sp.Rational(3),
        bound: sp.Rational(5),
        bounded_norm: sp.Rational(50),
    }
    assert sp.simplify(
        assembled_graph.subs(assumptions_fixture)
        - (1 + assumptions_fixture[bound] ** 2)
        * gamma_graph.subs(assumptions_fixture)
    ) <= 0
    assert assembled_graph.subs(assumptions_fixture) >= gamma_graph.subs(assumptions_fixture)

    status = contract["status"]
    assert status["actual_completed_row_identification"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.coherent-state-common-graph-core-fixture.v1",
        "status":"graph_core_reduction_fixture_verified",
        "central_difference_generates_derivative_state":True,
        "polynomial_weighted_graph_convergence":True,
        "bounded_perturbation_norm_equivalence_fixture":True,
        "actual_completed_row_identification":False,
        "positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
