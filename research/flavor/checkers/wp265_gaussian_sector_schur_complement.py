"""WP265: exact Schur-complement sign theorem for a Gaussian mediator sector."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    x = sp.symbols("x", real=True)
    m1, m2, m3 = sp.symbols("m1 m2 m3", positive=True)
    g1, g2, g3 = sp.symbols("g1 g2 g3", real=True)
    diagonal_hessian = sp.diag(m1, m2, m3)
    coupling = sp.Matrix([g1, g2, g3])
    induced = sp.factor(-sp.Rational(1, 2) * (coupling.T * diagonal_hessian.inv() * coupling)[0])

    # Exact mixed two-mediator witness with a positive-definite Hessian.
    mixed_hessian = sp.Matrix([[4, 1], [1, 3]])
    mixed_coupling = sp.Matrix([1, 2])
    mixed_principal_minors = [mixed_hessian[:i, :i].det() for i in (1, 2)]
    mixed_induced = sp.factor(-sp.Rational(1, 2) * (mixed_coupling.T * mixed_hessian.inv() * mixed_coupling)[0])

    # Completing the square exactly at the mixed witness.
    s1, s2 = sp.symbols("s1 s2", real=True)
    fields = sp.Matrix([s1, s2])
    ultraviolet = (fields.T * mixed_hessian * fields)[0] / 2 - x * (mixed_coupling.T * fields)[0]
    solution = sp.simplify(mixed_hessian.inv() * mixed_coupling * x)
    effective = sp.factor(ultraviolet.subs({s1: solution[0], s2: solution[1]}))
    curvature = sp.diff(effective, x, 2)

    # Cholesky identity: for K=L L^T, g^T K^-1 g=||L^-1 g||^2.
    cholesky = mixed_hessian.cholesky()
    whitened = sp.simplify(cholesky.inv() * mixed_coupling)
    norm_squared = sp.simplify((whitened.T * whitened)[0])
    quadratic_form = sp.simplify((mixed_coupling.T * mixed_hessian.inv() * mixed_coupling)[0])

    checks = {
        "diagonal_sector_induced_coefficient_is_negative_sum": sp.simplify(induced + g1**2 / (2 * m1) + g2**2 / (2 * m2) + g3**2 / (2 * m3)) == 0,
        "mixed_hessian_positive_definite": all(minor > 0 for minor in mixed_principal_minors),
        "mixed_witness_induced_coefficient_negative": mixed_induced == -sp.Rational(15, 22),
        "mixed_completion_of_square_exact": effective == mixed_induced * x**2,
        "mixed_effective_curvature_negative": curvature == -sp.Rational(15, 11),
        "cholesky_norm_identity_exact": norm_squared == quadratic_form,
        "quadratic_form_strictly_positive_for_witness": quadratic_form == sp.Rational(15, 11),
        "deliberate_positive_stabilizer_claim_fails": mixed_induced < 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP265",
        "theorem_domain": "any finite real Gaussian mediator vector with positive-definite Hessian K and real linear coupling -x*g^T*S",
        "general_effective_term": "-x^2*g^T*K^-1*g/2",
        "cholesky_sign_certificate": "g^T*K^-1*g = ||L^-1*g||^2 for K=L*L^T",
        "three_mode_diagonal_coefficient": str(induced),
        "mixed_witness": {
            "hessian": [[int(value) for value in mixed_hessian.row(i)] for i in range(2)],
            "coupling": [int(value) for value in mixed_coupling],
            "principal_minors": [str(value) for value in mixed_principal_minors],
            "effective_quadratic_coefficient": str(mixed_induced),
            "effective_curvature": str(curvature),
        },
        "classification": "finite stable Gaussian mediator sectors with arbitrary mixing cannot generate the positive commutator-square stabilizer; their Schur complement is negative semidefinite",
        "smallest_exact_falsifier": "K=[[4,1],[1,3]] and g=(1,2) give the strictly negative coefficient -15/22 despite positive principal minors 4 and 11",
        "remaining_authority_gate": "a direct positive operator, nonlinear mediator interaction, loop/nonperturbative contribution, or constrained auxiliary field whose sign and normalization are source-derived",
        "scope_limit": "does not cover nonlinear mediator potentials, non-Gaussian path integrals, constrained non-propagating fields, or radiative and nonperturbative matching",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp265_gaussian_sector_schur_complement.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
