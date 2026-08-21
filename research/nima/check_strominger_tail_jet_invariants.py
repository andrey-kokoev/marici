"""Exact invariant-ring audit for Strominger's logarithmic tail jet.

The scale and retarded-time actions on (A,B,E,D) are those verified in
research/strominger/subsubleading-memory-candidate.md.  This checker asks
whether their joint affine ambiguity still admits canonical polynomial
readouts.  It proves the answer degree-by-degree through a declared bound.
"""

import json
from pathlib import Path

import sympy as sp


A, B, E, D, a, ell = sp.symbols("A B E D a ell")
VARS = (A, B, E, D)
MAX_DEGREE = 8


def monomials_of_degree(degree):
    out = []
    for i in range(degree + 1):
        for j in range(degree - i + 1):
            for k in range(degree - i - j + 1):
                l = degree - i - j - k
                out.append(A**i * B**j * E**k * D**l)
    return out


def coefficient_matrix(expressions, basis):
    rows = []
    for expr in expressions:
        poly = sp.Poly(sp.expand(expr), *VARS)
        rows.append([poly.coeff_monomial(m) for m in basis])
    return sp.Matrix(rows)


def main():
    # Infinitesimal generators of scale and time-origin changes.
    scale = lambda f: sp.expand(A * sp.diff(f, B) + E * sp.diff(f, D))
    time = lambda f: sp.expand(-2 * A * sp.diff(f, E)
                               + (A - 2 * B) * sp.diff(f, D))

    J = sp.expand(A * D - B * E + A * E / 2)

    # The finite actions are included as an independent exact certificate.
    scale_sub = {A: A, B: B + A * ell, E: E, D: D + E * ell}
    time_sub = {A: A, B: B, E: E - 2 * a * A,
                D: D + a * A - 2 * a * B}
    finite_scale = sp.expand(J.subs(scale_sub, simultaneous=True) - J)
    finite_time = sp.expand(J.subs(time_sub, simultaneous=True) - J)

    degree_rows = []
    all_match = True
    for degree in range(MAX_DEGREE + 1):
        basis = monomials_of_degree(degree)
        # Each derivation preserves total degree.  Kernel of the stacked
        # coefficient map is the joint homogeneous invariant space.
        scale_matrix = coefficient_matrix([scale(m) for m in basis], basis).T
        time_matrix = coefficient_matrix([time(m) for m in basis], basis).T
        matrix = scale_matrix.col_join(time_matrix)
        kernel_dim = len(matrix.nullspace())

        predicted = [sp.expand(A ** (degree - 2 * k) * J**k)
                     for k in range(degree // 2 + 1)]
        predicted_rank = coefficient_matrix(predicted, basis).rank()
        expected_dim = degree // 2 + 1
        match = kernel_dim == predicted_rank == expected_dim
        all_match &= match
        degree_rows.append({
            "degree": degree,
            "ambient_dimension": len(basis),
            "joint_invariant_dimension": kernel_dim,
            "predicted_dimension": expected_dim,
            "predicted_span_rank": predicted_rank,
            "match": match,
        })

    checks = {
        "generators_commute": sp.expand(scale(time(D)) - time(scale(D))) == 0,
        "J_scale_invariant_infinitesimally": scale(J) == 0,
        "J_time_invariant_infinitesimally": time(J) == 0,
        "J_scale_invariant_finitely": finite_scale == 0,
        "J_time_invariant_finitely": finite_time == 0,
        "bounded_invariant_ring_matches_Q_A_J": all_match,
    }
    assert all(checks.values()), checks

    out = {
        "checker": "strominger_tail_jet_invariants",
        "author": "marici.Nima",
        "source_action": {
            "scale": "(A,B,E,D)->(A,B+A*l,E,D+E*l)",
            "time_origin": "(A,B,E,D)->(A,B,E-2*a*A,D+a*A-2*a*B)",
        },
        "canonical_generators": {
            "degree_1": "A",
            "degree_2": "J=A*D-B*E+A*E/2",
        },
        "degree_bound": MAX_DEGREE,
        "degree_census": degree_rows,
        "checks": checks,
        "verdict": (
            "Through total degree 8, the joint polynomial invariant ring "
            "is exactly Q[A,J]. The affine torsors erase scalar finite "
            "parts but retain a canonical mixed tail-jet readout J."
        ),
        "scope": (
            "Finite-action invariance of A and J is exact; generation of "
            "the full invariant ring is certified only through degree 8."
        ),
    }
    target = Path("research/nima/results/strominger-tail-jet-invariants.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks": checks, "degree_census": degree_rows}, indent=2))


if __name__ == "__main__":
    main()
