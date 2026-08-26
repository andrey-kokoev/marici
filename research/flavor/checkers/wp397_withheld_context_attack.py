"""WP397: exact withheld-context attack and bounded-grammar repair."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    c, eps = sp.symbols("c epsilon", real=True, nonzero=True)
    vanishing = sp.expand(c*(c-1)*(c-2))
    base = sp.Matrix([1, 0])
    alternative = sp.Matrix([1, eps*vanishing])
    observed = (0, 1, 2)
    withheld = 3
    alt_withheld = sp.simplify(alternative.subs(c, withheld))
    Kbase = base*base.T
    Kwithheld = alt_withheld*alt_withheld.T
    joint_det = sp.factor((Kbase+Kwithheld).det())
    a0, a1, a2 = sp.symbols("a0 a1 a2", real=True)
    quadratic = a0+a1*c+a2*c**2
    quadratic_solution = sp.solve([quadratic.subs(c, point) for point in observed], (a0, a1, a2), dict=True)
    vandermonde = sp.Matrix([[1, point, point**2] for point in observed])
    checks = {
        "completion_vanishes_at_first_context": vanishing.subs(c, 0) == 0,
        "completion_vanishes_at_second_context": vanishing.subs(c, 1) == 0,
        "completion_vanishes_at_third_context": vanishing.subs(c, 2) == 0,
        "alternative_matches_base_on_all_observed_contexts": all(alternative.subs(c, point) == base for point in observed),
        "withheld_context_rotates_direction": alt_withheld == sp.Matrix([1, 6*eps]),
        "withheld_joint_determinant_positive": joint_det == 36*eps**2,
        "each_context_remains_instantaneously_rank_one": sp.factor((alternative*alternative.T).det()) == 0,
        "completion_has_degree_three": sp.Poly(vanishing, c).degree() == 3,
        "quadratic_vandermonde_invertible": vandermonde.det() == 2,
        "degree_two_zero_completion_forced_trivial": quadratic_solution == [{a0: 0, a1: 0, a2: 0}],
        "deleting_one_context_allows_nonzero_quadratic": (c*(c-1)).subs(c, 0) == 0 and (c*(c-1)).subs(c, 1) == 0 and (c*(c-1)).subs(c, 2) != 0,
        "withheld_falsifier_disappears_when_completion_deleted": joint_det.subs(eps, 0) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP397",
        "admitted_state_domain": "a real context coordinate with three calibrated observed contexts and one withheld context",
        "faithful_quotient_coordinate": "the projective physical16 response direction at each legally parallelized context",
        "source_authorized_probe_family": "context-wise rank tests, cross-context wedge, withheld-context prediction, and a preregistered polynomial-degree grammar",
        "contextual_partition": "the constant and degree-three channel maps agree on all observed contexts and separate at the withheld context; a degree-at-most-two grammar removes this ambiguity",
        "classification": "finite-context no-go without a source complexity bound, plus an exact finite-test repair inside a frozen bounded grammar",
        "vanishing_completion": str(vanishing),
        "withheld_direction": str(alt_withheld),
        "withheld_joint_determinant": str(joint_det),
        "quadratic_vandermonde_determinant": str(vandermonde.det()),
        "smallest_exact_falsifier": "the degree-three completion epsilon*c*(c-1)*(c-2) is invisible at contexts 0,1,2 and produces a nonzero wedge at context 3",
        "remaining_physical_instrument_gate": "derive a bound on allowed context dependence from the source action, reserve at least one executable context, and test its predicted response direction without refitting",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp397_withheld_context_attack.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
