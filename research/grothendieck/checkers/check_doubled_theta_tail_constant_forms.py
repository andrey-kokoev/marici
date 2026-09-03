"""Exact audit of constant forms on conjugate and reciprocal doubled tail planes."""
import json
import sympy as sp


def tail(s, f):
    return sp.Matrix([[-s / 2, -f], [0, s / 2]])


def main():
    a, t, f = sp.symbols("a t f", real=True)
    s = a + sp.I * t
    J = sp.Matrix([[0, 1], [-1, 0]])
    Z = sp.zeros(2)
    H = Z.row_join(J).col_join(J.T.row_join(Z))

    conjugate_double = sp.diag(tail(s, f), tail(sp.conjugate(s), f))
    conjugate_residual = sp.simplify(sp.conjugate(conjugate_double).T * H + H * conjugate_double)
    eigenvalues = H.eigenvals()

    # Cross-block K for the reciprocal partner -conjugate(s).
    k11, k12, k21, k22 = sp.symbols("k11 k12 k21 k22")
    K = sp.Matrix([[k11, k12], [k21, k22]])
    reciprocal_cross = sp.expand(
        sp.conjugate(tail(s, f)).T * K + K * tail(-sp.conjugate(s), f)
    )
    forcing_equations = [sp.expand(x).coeff(f) for x in reciprocal_cross]
    forcing_solution = sp.solve(forcing_equations, [k11, k21], dict=True)[0]
    reduced = sp.simplify(reciprocal_cross.subs(forcing_solution).subs(k21, -k12))
    generic_reciprocal_solution = sp.solve(list(reduced), [k12, k22], dict=True)
    reciprocal_determinants = [sp.simplify(K.subs(forcing_solution).subs(k21, -k12).subs(sol).det()) for sol in generic_reciprocal_solution]

    checks = {
        "conjugate_double_conserves_constant_form": conjugate_residual == sp.zeros(4),
        "conserved_form_is_nondegenerate": H.det() != 0,
        "conserved_form_has_split_signature": eigenvalues.get(sp.Integer(1)) == 2 and eigenvalues.get(sp.Integer(-1)) == 2,
        "reciprocal_forcing_sets_k11_zero": forcing_solution.get(k11) == 0,
        "generic_reciprocal_cross_block_is_degenerate": bool(reciprocal_determinants) and all(x == 0 for x in reciprocal_determinants),
    }
    result = {
        "schema": "marici.grothendieck.doubled-theta-tail-constant-forms.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "conjugate_form": [[str(x) for x in H.row(i)] for i in range(4)],
        "conjugate_form_eigenvalues": {str(k): v for k, v in eigenvalues.items()},
        "reciprocal_cross_residual_after_forcing": [[str(x) for x in reduced.row(i)] for i in range(2)],
        "disposition": "Conjugate doubling supplies only a split (2,2) conserved form; reciprocal doubling has no generic nondegenerate constant cross form. Positivity or exclusion requires q-dependent/source-sewn structure.",
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
