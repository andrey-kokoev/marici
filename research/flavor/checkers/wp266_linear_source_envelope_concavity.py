"""WP266: exact local and finite envelope-concavity audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    # General differentiable one-mediator envelope at a stable stationary point.
    hessian, source_gradient = sp.symbols("hessian source_gradient", positive=True)
    envelope_curvature = -source_gradient**2 / hessian

    # Non-Gaussian exact witness U=s^2/2+s^4/4, G=s at x=0.
    s, x = sp.symbols("s x", real=True)
    potential = s**2 / 2 + s**4 / 4 - x * s
    stationarity = sp.diff(potential, s)
    local_hessian = sp.diff(potential, s, 2).subs({s: 0, x: 0})
    local_source_gradient = sp.diff(s, s)
    local_envelope_curvature = sp.simplify(-local_source_gradient**2 / local_hessian)

    # Exact nondifferentiable finite-mediator envelope: min of three affine
    # source branches. Midpoint concavity is checked across all rational pairs.
    branches = [lambda z: -z, lambda z: sp.Rational(1, 4), lambda z: z]
    grid = [sp.Rational(-1), sp.Rational(-1, 2), sp.Rational(0), sp.Rational(1, 2), sp.Rational(1)]

    def envelope(z):
        return min(branch(z) for branch in branches)

    midpoint_residuals = []
    for left in grid:
        for right in grid:
            midpoint = (left + right) / 2
            midpoint_residuals.append(sp.simplify(envelope(midpoint) - (envelope(left) + envelope(right)) / 2))

    # A positive stabilizer violates concavity directly.
    positive_stabilizer = x**2
    convex_midpoint_residual = sp.simplify(
        positive_stabilizer.subs(x, 0)
        - (positive_stabilizer.subs(x, -1) + positive_stabilizer.subs(x, 1)) / 2
    )

    checks = {
        "general_stable_envelope_curvature_nonpositive": envelope_curvature.is_negative,
        "non_gaussian_stationary_point_exact": stationarity.subs({s: 0, x: 0}) == 0,
        "non_gaussian_local_hessian_positive": local_hessian == 1,
        "non_gaussian_envelope_curvature_negative": local_envelope_curvature == -1,
        "finite_branch_envelope_midpoint_concave": all(residual >= 0 for residual in midpoint_residuals),
        "positive_x_squared_stabilizer_is_not_concave": convex_midpoint_residual == -1,
        "deliberate_linear_source_positive_curvature_claim_fails": envelope_curvature < 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP266",
        "theorem_domain": "stable mediator sectors eliminated by minimization from V(S,x)=U(S)-x*G(S), including nonlinear U and finite competing branches",
        "global_certificate": "the pointwise infimum over S of affine functions U(S)-x*G(S) is concave in x",
        "local_certificate": "F''(x)=-grad(G)^T*H^-1*grad(G)<=0 at a stable differentiable stationary branch",
        "symbolic_one_mode_curvature": str(envelope_curvature),
        "non_gaussian_witness": {
            "potential": "s^2/2+s^4/4-x*s",
            "stationary_point": "s=0 at x=0",
            "mediator_hessian": str(local_hessian),
            "effective_curvature": str(local_envelope_curvature),
        },
        "finite_branch_midpoint_residuals_exact": sorted({str(value) for value in midpoint_residuals}),
        "positive_stabilizer_midpoint_residual_exact": str(convex_midpoint_residual),
        "classification": "any stable mediator sector coupled linearly to the invariant produces a concave effective envelope and cannot generate the positive curvature required for an interior mixing minimum",
        "smallest_exact_falsifier": "the nonlinear stable potential s^2/2+s^4/4-x*s has effective curvature -1 at x=s=0; x^2 instead has midpoint concavity residual -1",
        "remaining_authority_gate": "introduce and independently derive direct nonlinear x-dependence, a constrained non-minimizing operation, nonequilibrium dynamics, or quantum corrections not representable as this stable linear-source envelope",
        "scope_limit": "does not cover direct x^2 source operators, nonlinear dependence on x in mediator couplings, metastable branch selection without global minimization, or genuinely nonequilibrium/complex effective actions",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp266_linear_source_envelope_concavity.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
