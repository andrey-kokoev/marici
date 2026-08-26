"""WP400: exact stable one-mediator realization of the one-pole grammar."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    A = sp.symbols("A", real=True)
    c = sp.symbols("c", real=True, nonnegative=True)
    M2 = sp.symbols("M2", positive=True)
    J0, J1 = sp.symbols("J0 J1", real=True)
    potential = (M2+c)*A**2/2-(J0+J1*c)*A
    solution = sp.factor((J0+J1*c)/(M2+c))
    stationary = sp.simplify(sp.diff(potential, A).subs(A, solution))
    curvature = sp.diff(potential, A, 2)
    effective = sp.factor(potential.subs(A, solution))
    a0, a1, b1 = sp.symbols("a0 a1 b1", real=True)
    normalized = sp.factor((a0+a1*c)/(1+b1*c))
    mapping = {a0: J0/M2, a1: J1/M2, b1: 1/M2}
    inverse_mapping = {M2: 1/b1, J0: a0/b1, J1: a1/b1}
    benchmark = {M2: 1, J0: 1, J1: 2}
    benchmark_response = sp.factor(solution.subs(benchmark))
    records = tuple(benchmark_response.subs(c, point) for point in (0, 1, 2, 3))
    checks = {
        "stationary_elimination_exact": stationary == 0,
        "mediator_curvature_positive": curvature.is_positive,
        "effective_potential_exact": sp.simplify(effective+(J0+J1*c)**2/(2*(M2+c))) == 0,
        "response_matches_normalized_one_pole": sp.simplify(solution-normalized.subs(mapping)) == 0,
        "parameter_map_invertible": all(sp.simplify(mapping[key].subs(inverse_mapping)-key) == 0 for key in (a0, a1, b1)),
        "benchmark_matches_wp399": benchmark_response == (2*c+1)/(c+1),
        "benchmark_four_context_records": records == (1, sp.Rational(3, 2), sp.Rational(5, 3), sp.Rational(7, 4)),
        "heavy_mediator_decouples_response": sp.limit(solution, M2, sp.oo) == 0,
        "deleting_tadpole_kills_response": solution.subs({J0: 0, J1: 0}) == 0,
        "context_denominator_never_zero_on_domain": (M2+c).is_positive,
        "mass_only_context_has_constant_numerator": sp.diff(solution.subs(J1, 0)*(M2+c), c) == 0,
        "unlocked_extra_quadratic_context_exits_one_pole_grammar": sp.Poly(M2+c+c**2, c).degree() == 2,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP400",
        "admitted_state_domain": "one real mediator with positive baseline curvature, nonnegative calibrated context shift, and affine source tadpole",
        "faithful_quotient_coordinate": "the projective response direction (1,A_star(c)) mapped into the physical16 response plane",
        "source_authorized_probe_family": "stationary mediator displacement at four calibrated context settings",
        "contextual_partition": "three settings identify the finite source packet (M2,J0,J1); the fourth tests the shared affine mass/tadpole context law",
        "classification": "explicit stable source realization and instrument grammar for WP399, but response identification rather than flavor selection",
        "potential": str(potential),
        "stationary_response": str(solution),
        "effective_potential": str(effective),
        "benchmark_records": [str(value) for value in records],
        "smallest_exact_falsifier": "an independently admitted quadratic context correction to the mediator curvature exits the one-pole family while preserving stability near the calibration domain",
        "remaining_physical_instrument_gate": "identify a real flavor mediator and a calibrated operation that produces the locked affine curvature and tadpole shifts, then measure its withheld displacement without refitting",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp400_one_mediator_response_grammar.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
