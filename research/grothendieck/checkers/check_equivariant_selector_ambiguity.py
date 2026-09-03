"""Exact representation-theoretic ambiguity of equivariant right inverses."""
import json
import sympy as sp


def main():
    a0, a1 = sp.symbols("a0 a1", real=True)
    B = sp.Matrix([[1, 0]])
    T = sp.eye(1)
    K0 = sp.Matrix([1, a0])
    K1 = sp.Matrix([1, a1])
    S_odd = sp.diag(1, -1)
    S_even = sp.eye(2)
    avg_odd = sp.simplify((K0 + S_odd * K0 * T) / 2)
    avg_even = sp.simplify((K0 + S_even * K0 * T) / 2)
    refinement_residual_even = sp.simplify(K0 - K1)
    checks = {
        "odd_hidden_gain_removed_by_averaging": avg_odd == sp.Matrix([1, 0]),
        "even_hidden_gain_survives_averaging": avg_even == K0,
        "both_even_selectors_are_equivariant": S_even * K0 == K0 * T and S_even * K1 == K1 * T,
        "even_refinement_residual_can_be_nonzero": refinement_residual_even == sp.Matrix([0, a0 - a1]),
        "residual_is_output_null": B * refinement_residual_even == sp.zeros(1, 1),
    }
    result = {
        "schema": "marici.grothendieck.equivariant-selector-ambiguity.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "odd_averaged_selector": [str(x) for x in avg_odd],
        "even_averaged_selector": [str(x) for x in avg_even],
        "even_refinement_residual": [str(x) for x in refinement_residual_even],
        "criterion": "Equivariant right inverses form an affine space over Hom_G(Y, ker B); symmetry selects uniquely only when this intertwiner space vanishes.",
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
