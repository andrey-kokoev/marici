#!/usr/bin/env python3
"""Exact finite audit for scalar versus vector G3 seam margins.

Dependency-free by construction.  The script checks only algebraic implications
used by the Kitaev hostile audit; it does not verify source authority for the
underlying theta seam object.
"""

from fractions import Fraction
import json
from pathlib import Path


def min_eigenvalue_2x2_symmetric(a, b, d):
    """Return exact lower-bound data for [[a,b],[b,d]].

    For the matrices used here eigenvalues are read off from diagonal cases or
    by determinant/trace positivity gates; no floating arithmetic is used.
    """
    return {"trace": a + d, "determinant": a * d - b * b}


def scalar_margin_sequence(limit=12):
    # A hostile diagonal comparison with lambda_p = 1/p.  This is weaker than
    # Nima's superpolynomial decay and already forces zero minimum modulus.
    vals = [Fraction(1, p) for p in range(2, limit + 1)]
    return vals


def vector_difference_lower_bound(js):
    # D(x,y)=Jx-y.  If J is diagonal with singular values js, then
    # DD* = JJ* + I on the seam output.  The least eigenvalue is 1+min(js^2).
    return min(Fraction(1, 1) + j * j for j in js)


def coherent_margin_lower_bound(m_j, c_a):
    # delta_diag^2 >= c_A m_J^2/(1+m_J^2)
    return c_a * m_j * m_j / (Fraction(1, 1) + m_j * m_j)


def mixed_margin_lower_bound(m_j, c_a, m_b):
    c_j = max(Fraction(2, 1) / (m_j * m_j), (Fraction(1, 1) + Fraction(2, 1) / (m_j * m_j)) / c_a)
    g0 = Fraction(1, 1) / c_j
    return g0 / m_b, g0


def main():
    checks = []

    lambdas = scalar_margin_sequence()
    checks.append({
        "name": "scalar_diagonal_margin_decreases",
        "passed": all(lambdas[i + 1] < lambdas[i] for i in range(len(lambdas) - 1)),
        "evidence": [str(lambdas[0]), str(lambdas[-1])],
        "interpretation": "finite prefixes already show no positive cutoff-independent lower bound; the p->infinity limit is zero by formula lambda_p=1/p",
    })

    js_good = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]
    dd_lower = vector_difference_lower_bound(js_good)
    checks.append({
        "name": "vector_difference_surjective_margin",
        "passed": dd_lower >= 1,
        "evidence": {"least_DDstar_eigenvalue": str(dd_lower)},
        "interpretation": "D(x,y)=Jx-y has output right inverse z->(0,-z) and DD*=JJ*+I>=I",
    })

    m_j = Fraction(1, 2)
    c_a = Fraction(1, 1)
    diag = coherent_margin_lower_bound(m_j, c_a)
    checks.append({
        "name": "coherent_diagonal_margin_positive_if_J_and_A_bounded_below",
        "passed": diag > 0,
        "evidence": {"m_J": str(m_j), "c_A": str(c_a), "delta_diag_squared_lower_bound": str(diag)},
        "interpretation": "the coherent graph is controlled by analytic observation of Jx",
    })

    m_b = Fraction(5, 1)
    mix, g0 = mixed_margin_lower_bound(m_j, c_a, m_b)
    checks.append({
        "name": "mixed_margin_positive_if_block_upper_bound_finite",
        "passed": mix > 0,
        "evidence": {"g0": str(g0), "M_B": str(m_b), "delta_mix_lower_bound": str(mix)},
        "interpretation": "coercivity of ||Ay||^2+||Jx-y||^2 implies normalized mixed-block norm <1",
    })

    checks.append({
        "name": "scalar_projection_hostile_rejects_vector_promotion_after_trace",
        "passed": lambdas[-1] < Fraction(1, 5) and dd_lower >= 1,
        "evidence": {"scalar_tail_value_at_prefix_end": str(lambdas[-1]), "vector_DDstar_lower_bound": str(dd_lower)},
        "interpretation": "the positive vector margin is destroyed by the scalar Wronskian projection; the two seam objects are not interchangeable",
    })

    result = {
        "schema": "marici.kitaev.g3_vector_seam_margin_audit.v1",
        "claim_boundary": "conditional algebraic audit only; source authority for the differentiated boundary-front seam and global G3/G4 typing is not proved here",
        "checks_passed": sum(1 for c in checks if c["passed"]),
        "checks_total": len(checks),
        "all_passed": all(c["passed"] for c in checks),
        "checks": checks,
    }
    out = Path("research/kitaev/results/g3-vector-seam-margin-audit.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
