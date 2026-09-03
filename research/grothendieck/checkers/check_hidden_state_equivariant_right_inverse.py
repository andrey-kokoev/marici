"""Finite control fixture: regulation does not imply equivariant realization."""
import json
import sympy as sp


def main():
    alpha, y = sp.symbols("alpha y", real=True)
    B = sp.Matrix([[1, 0]])
    S = sp.diag(1, -1)
    K = sp.Matrix([[1], [alpha]])
    regulation = sp.simplify(B * K)
    equivariance_residual = sp.simplify(S * K - K)
    hidden_difference = sp.simplify(K - sp.Matrix([1, 0]))
    checks = {
        "all_selectors_are_right_inverses": regulation == sp.eye(1),
        "selector_difference_is_output_null": B * hidden_difference == sp.zeros(1, 1),
        "equivariance_selects_alpha_zero": sp.solve(list(equivariance_residual), [alpha], dict=True) == [{alpha: 0}],
        "unbounded_hidden_family_has_fixed_output": B * (K * y) == sp.Matrix([y]),
    }
    result = {
        "schema": "marici.grothendieck.hidden-state-equivariant-right-inverse.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "output_map": [[1, 0]],
        "state_reflection": [[1, 0], [0, -1]],
        "right_inverse_family": ["1", "alpha"],
        "equivariance_residual": [str(x) for x in equivariance_residual],
        "hidden_state_norm_squared_for_unit_output": "1 + alpha^2",
        "disposition": "Endpoint regulation leaves an arbitrary hidden kernel gain. Reflection equivariance selects alpha=0; uniform boundedness is additionally needed under refinement.",
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
