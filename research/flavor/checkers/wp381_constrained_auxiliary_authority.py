"""WP381: exact authority audit for constrained and contour auxiliaries."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    A, B, F, eta = sp.symbols("A B F eta", real=True)
    lam, mu = sp.symbols("lambda mu", positive=True)
    I = sp.I

    complex_exponent = -A**2/(4*lam) + I*A*F
    complex_square = -(A - 2*I*lam*F)**2/(4*lam) - lam*F**2
    real_exponent = -A**2/(4*lam) + A*F
    real_square = -(A - 2*lam*F)**2/(4*lam) + lam*F**2

    constrained = mu*B**2/2 + eta*(B-F)
    constrained_solution = {B: F, eta: -mu*F}
    constrained_effective = sp.factor(constrained.subs(constrained_solution))
    multiplier_hessian = sp.hessian(constrained, (B, eta))
    multiplier_determinant = sp.factor(multiplier_hessian.det())
    constraint_residual = sp.diff(constrained, eta)

    checks = {
        "complex_completion_exact": sp.expand(complex_exponent-complex_square) == 0,
        "complex_contour_generates_positive_potential_penalty": sp.expand(complex_square + (A-2*I*lam*F)**2/(4*lam)) == -lam*F**2,
        "complex_integrand_not_real_for_hostile_point": sp.im(complex_exponent.subs({A: 1, F: 1, lam: 1})) != 0,
        "real_completion_exact": sp.expand(real_exponent-real_square) == 0,
        "real_coupling_has_opposite_effective_exponent": sp.expand(real_square + (A-2*lam*F)**2/(4*lam)) == lam*F**2,
        "constraint_equations_solved": all(sp.simplify(sp.diff(constrained, x).subs(constrained_solution)) == 0 for x in (B, eta)),
        "constraint_substitution_generates_positive_penalty": constrained_effective == mu*F**2/2,
        "constraint_explicitly_contains_shell_residual": constraint_residual == B-F,
        "multiplier_hessian_exact": multiplier_hessian == sp.Matrix([[mu, 1], [1, 0]]),
        "multiplier_hessian_indefinite": multiplier_determinant == -1,
        "deleting_constraint_destroys_positive_matching": (mu*B**2/2).subs(B, 0) == 0,
        "hostile_off_shell_constraint_detected": constraint_residual.subs({B: 0, F: 1}) == -1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP381",
        "admitted_state_domain": "WP378 real shell residual F with either a complex Hubbard-Stratonovich contour or a real Lagrange-multiplier constraint",
        "faithful_quotient_coordinate": "the weak-basis-invariant nondegenerate physical16 residual F",
        "source_authorized_probe_family": "exact square completion, reality audit, constraint elimination, and multiplier-Hessian signature",
        "contextual_partition": "the complex representation separates F through a changed contour experiment; the constrained representation identifies B with F by stipulation",
        "classification": "both constructions can represent a positive penalty, but neither independently derives a flavor selector coefficient or shell",
        "complex_identity": str(complex_square),
        "real_identity": str(real_square),
        "constrained_effective_potential": str(constrained_effective),
        "multiplier_hessian_determinant": str(multiplier_determinant),
        "smallest_exact_falsifier": "at A=F=lambda=1 the complex auxiliary exponent has nonzero imaginary part; the real multiplier alternative has Hessian determinant -1 and embeds B-F directly",
        "remaining_physical_instrument_gate": "derive the integration contour or constraint from admitted source dynamics and independently fix lambda or mu and the invariant residual F before flavor readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp381_constrained_auxiliary_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
