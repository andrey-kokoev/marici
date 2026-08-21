"""Joint invariant audit for ballistic memory and its logarithmic tail jet."""

import json
from pathlib import Path

import sympy as sp


A, B, E, D, M2, M3, a, ell = sp.symbols("A B E D M2 M3 a ell")
VARS = (A, B, E, D, M2, M3)
MAX_DEGREE = 5


def monomials_of_degree(degree):
    out = []
    for i in range(degree + 1):
        for j in range(degree - i + 1):
            for k in range(degree - i - j + 1):
                for l in range(degree - i - j - k + 1):
                    for m in range(degree - i - j - k - l + 1):
                        n = degree - i - j - k - l - m
                        out.append(A**i * B**j * E**k * D**l * M2**m * M3**n)
    return out


def operator_matrix(images, basis):
    rows = []
    for expr in images:
        poly = sp.Poly(sp.expand(expr), *VARS)
        rows.append([poly.coeff_monomial(mon) for mon in basis])
    return sp.Matrix(rows).T


def main():
    scale = lambda f: sp.expand(A * sp.diff(f, B) + E * sp.diff(f, D))
    time = lambda f: sp.expand(
        -2 * A * sp.diff(f, E)
        + (A - 2 * B) * sp.diff(f, D)
        - M2 * sp.diff(f, M3)
    )
    J = sp.expand(A * D - B * E + A * E / 2)
    K = sp.expand(2 * A * M3 - M2 * E)

    scale_sub = {
        A: A, B: B + A * ell, E: E, D: D + E * ell,
        M2: M2, M3: M3,
    }
    time_sub = {
        A: A, B: B, E: E - 2 * a * A,
        D: D + a * A - 2 * a * B,
        M2: M2, M3: M3 - a * M2,
    }

    census = []
    all_match = True
    for degree in range(MAX_DEGREE + 1):
        basis = monomials_of_degree(degree)
        matrix = operator_matrix([scale(x) for x in basis], basis).col_join(
            operator_matrix([time(x) for x in basis], basis)
        )
        kernel_dim = len(basis) - matrix.rank()

        predicted = []
        for jk in range(degree // 2 + 1):
            rem = degree - 2 * jk
            for jpow in range(jk + 1):
                kpow = jk - jpow
                for apow in range(rem + 1):
                    predicted.append(
                        A**apow * M2**(rem - apow) * J**jpow * K**kpow
                    )
        predicted_rank = operator_matrix(predicted, basis).T.rank()
        match = kernel_dim == predicted_rank == len(predicted)
        all_match &= match
        census.append({
            "degree": degree,
            "ambient_dimension": len(basis),
            "joint_invariant_dimension": kernel_dim,
            "predicted_dimension": len(predicted),
            "predicted_span_rank": predicted_rank,
            "match": match,
        })

    checks = {
        "actions_commute": all(
            sp.expand(scale(time(v)) - time(scale(v))) == 0 for v in VARS
        ),
        "J_finitely_invariant": (
            sp.expand(J.subs(scale_sub, simultaneous=True) - J) == 0
            and sp.expand(J.subs(time_sub, simultaneous=True) - J) == 0
        ),
        "K_finitely_invariant": (
            sp.expand(K.subs(scale_sub, simultaneous=True) - K) == 0
            and sp.expand(K.subs(time_sub, simultaneous=True) - K) == 0
        ),
        "bounded_ring_matches_Q_A_M2_J_K": all_match,
    }
    assert all(checks.values()), (checks, census)

    out = {
        "checker": "strominger_memory_tail_joint_invariants",
        "author": "marici.Nima",
        "canonical_generators": {
            "degree_1": ["A", "M2"],
            "degree_2": [
                "J=A*D-B*E+A*E/2",
                "K=2*A*M3-M2*E",
            ],
        },
        "degree_bound": MAX_DEGREE,
        "degree_census": census,
        "checks": checks,
        "verdict": (
            "Through total degree 5, the joint invariant ring is exactly "
            "Q[A,M2,J,K]. K is a canonical mixed ballistic-memory/tail "
            "readout despite the separate time-origin and scale torsors."
        ),
        "scope": (
            "The finite invariance of J and K is exact. Full ring generation "
            "is certified only through degree 5 and assumes Strominger's "
            "declared affine transformation laws."
        ),
    }
    target = Path(
        "research/nima/results/strominger-memory-tail-joint-invariants.json"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks": checks, "degree_census": census}, indent=2))


if __name__ == "__main__":
    main()
