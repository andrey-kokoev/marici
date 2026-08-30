"""WP380: exact local envelope-sign theorem for stable nonlinear mediators."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    F = sp.symbols("F", real=True)
    h1, h2 = sp.symbols("h1 h2", positive=True)
    g1, g2 = sp.symbols("g1 g2", real=True)
    k = sp.symbols("k", real=True)
    H, G = sp.diag(h1, h2), sp.Matrix([g1, g2])
    schur = sp.factor(k - (G.T * H.inv() * G)[0])
    induced = sp.factor(schur.subs(k, 0))
    solution = -H.inv() * G * F
    A = sp.Matrix(sp.symbols("A1 A2", real=True))
    potential = (A.T * H * A)[0] / 2 + F * (G.T * A)[0] + k * F**2 / 2
    effective = sp.factor(potential.subs(dict(zip(A, solution))))
    a, m2, lam, g = sp.symbols("a m2 lambda g", real=True)
    nonlinear = m2*a**2/2 + lam*a**4/4 + g*a*F
    nh = sp.hessian(nonlinear, (a, F)).subs({a: 0, F: 0})
    nonlinear_schur = sp.factor(nh[1, 1] - nh[1, 0]*nh[0, 0]**-1*nh[0, 1])
    a_prime = sp.factor(-sp.diff(nonlinear, a, F).subs({a: 0, F: 0}) / sp.diff(nonlinear, a, 2).subs({a: 0, F: 0}))
    threshold = sp.factor((G.T * H.inv() * G)[0])
    benchmark = {h1: 2, h2: 3, g1: 1, g2: 2}
    benchmark_threshold = sp.factor(threshold.subs(benchmark))
    checks = {
        "stationary_solution_exact": sp.simplify(H*solution + G*F) == sp.zeros(2, 1),
        "effective_curvature_is_schur_complement": sp.expand(2*effective/F**2 - schur) == 0,
        "contact_free_formula_exact": sp.simplify(induced + g1**2/h1 + g2**2/h2) == 0,
        "contact_free_curvature_nonpositive": induced.is_nonpositive,
        "coupled_benchmark_strictly_negative": induced.subs(benchmark).is_negative,
        "nonlinear_vacuum_hessian_exact": nh == sp.Matrix([[m2, g], [g, 0]]),
        "quartic_drops_out_locally": not nonlinear_schur.has(lam),
        "nonlinear_envelope_curvature_negative": nonlinear_schur == -g**2/m2,
        "implicit_response_exact": a_prime == -g/m2,
        "direct_contact_threshold_exact": sp.simplify(schur.subs(k, threshold)) == 0,
        "benchmark_threshold_exact": benchmark_threshold == sp.Rational(11, 6),
        "subthreshold_contact_fails": schur.subs(benchmark).subs(k, 1).is_negative,
        "superthreshold_contact_positive": schur.subs(benchmark).subs(k, 2).is_positive,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP380",
        "admitted_state_domain": "smooth real mediator potentials near a stationary vacuum with positive mediator Hessian",
        "faithful_quotient_coordinate": "WP378 real nondegenerate physical16 shell residual F",
        "source_authorized_probe_family": "local stationary elimination and exact Hessian Schur complement",
        "contextual_partition": "coupling-kernel directions have zero induced curvature; coupled directions have negative induced curvature",
        "classification": "local no-go for a positive shell penalty from stable classical mediator minimization without an independent positive direct contact",
        "general_effective_curvature": str(schur),
        "contact_free_induced_curvature": str(induced),
        "nonlinear_quartic_effective_curvature": str(nonlinear_schur),
        "direct_contact_threshold": str(threshold),
        "benchmark_threshold": str(benchmark_threshold),
        "smallest_exact_falsifier": "a stable nonlinear mediator has local envelope curvature -g^2/m2, independent of quartic stabilization",
        "remaining_physical_instrument_gate": "derive a positive direct flavor contact above the Schur threshold, or a source mechanism outside stable classical minimization",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp380_stable_mediator_envelope_sign.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
