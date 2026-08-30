"""Hankel score test for the actual source-word staircase S,D_E S,D_E^2 S."""
from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z
E, sqrt_delta = sp.symbols("E sqrtDelta")
ORDER = 4


def coefficients(expr: sp.Expr, variable: sp.Symbol, order: int) -> list[sp.Expr]:
    return [sp.factor(sp.diff(expr, variable, n).subs(variable, 0) / math.factorial(n))
            for n in range(order + 1)]


def inverse_square_root_coefficients(d: list[sp.Expr]) -> list[sp.Expr]:
    """Return h through the same order with d(E) h(E)^2 = 1 and h(0)=1."""
    assert sp.factor(d[0] - 1) == 0
    h: list[sp.Expr] = [sp.Integer(1)]
    for n in range(1, len(d)):
        trial = sp.symbols(f"h{n}")
        hs = h + [trial]
        coefficient = sum(
            d[i] * hs[j] * hs[n-i-j]
            for i in range(n + 1)
            for j in range(n - i + 1)
        )
        solved = sp.solve(sp.Eq(coefficient, 0), trial)
        assert len(solved) == 1
        h.append(sp.factor(solved[0]))
    return h


def main() -> None:
    substitution, _numerator, denominator = source.walls["g3"]
    restriction = sp.Poly(
        sp.expand(source.K.subs(substitution)), t,
        domain=sp.QQ.frac_field(x, y, z),
    )
    tangent = sp.gcd(restriction, restriction.diff()).monic().as_expr()
    tangent = sp.Poly(sp.fraction(sp.together(tangent))[0], t, x, y, z).as_expr()
    tangent_E = sp.Poly(sp.expand(tangent.subs(z, E-x-y)), t)
    denominator_E = sp.expand(denominator.subs(z, E-x-y))
    leading, linear, constant = tangent_E.all_coeffs()
    discriminant = sp.factor(linear**2 - 4*leading*constant)
    roots = [(-linear + sign*sqrt_delta)/(2*leading) for sign in (1, -1)]
    reciprocal_trace = sp.together(sum(1/denominator_E.subs(t, root) for root in roots))
    reciprocal_trace = sp.factor(sp.cancel(reciprocal_trace).subs(sqrt_delta**2, discriminant))

    rational = sp.factor(-E*reciprocal_trace)
    reduced_delta = sp.factor(discriminant/E)
    r0 = sp.factor(rational.subs(E, 0))
    d0 = sp.factor(reduced_delta.subs(E, 0))
    r = coefficients(sp.cancel(rational/r0), E, ORDER)
    d = coefficients(sp.cancel(reduced_delta/d0), E, ORDER)
    h = inverse_square_root_coefficients(d)
    f = [sp.factor(sum(r[k]*h[n-k] for k in range(n+1))) for n in range(ORDER+1)]
    assert f[0] == 1

    # In a horizontal source frame, score i applied to D_E^j S reads
    # F^(i+j)(0).  The 3x3 Hankel matrix therefore uses moments through 4.
    moments = [sp.factor(math.factorial(n)*f[n]) for n in range(ORDER+1)]
    hankel = sp.Matrix(3, 3, lambda i, j: moments[i+j])
    determinant = sp.factor(hankel.det())
    det_num, det_den = map(sp.factor, sp.fraction(determinant))
    assert determinant != 0

    result = {
        "schema": "marici.benincasa.total-energy-kummer-source-word-scores.v1",
        "source_word_basis": ["S", "D_E S", "D_E^2 S"],
        "score_basis": ["evaluation", "D_E score", "D_E^2 score"],
        "normalized_period_coefficients_E0_to_E4": [str(value) for value in f],
        "normalized_period_derivatives_0_to_4": [str(value) for value in moments],
        "hankel_matrix": [[str(value) for value in row] for row in hankel.tolist()],
        "determinant": str(determinant),
        "determinant_numerator": str(det_num),
        "determinant_denominator": str(det_den),
        "generic_rank": int(hankel.rank()),
        "generic_kernel_dimension": 3-int(hankel.rank()),
        "faithful_on_source_word_staircase": hankel.rank() == 3,
        "scope": (
            "source-derived oriented scalar Kummer period and its total-energy "
            "score tower; excludes soft loci and does not include marked-wall or tensor ports"
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("total-energy-kummer-source-word-scores.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
