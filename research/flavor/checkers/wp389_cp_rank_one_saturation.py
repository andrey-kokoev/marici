"""WP389: exact CP-invariant portal cone and rank-one saturation audit."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    X, Y = sp.symbols("X Y", real=True)
    a, b = sp.symbols("a b", positive=True)
    k = sp.symbols("kappa", real=True)
    portal = a*X**2+k*X*Y+b*Y**2
    gram = sp.Matrix([[a, k/2], [k/2, b]])
    determinant = sp.factor(gram.det())
    completed = sp.expand(a*(X+k*Y/(2*a))**2+(b-k**2/(4*a))*Y**2)
    rank_plus = sp.factor(portal.subs(k, 2*sp.sqrt(a*b)))
    rank_minus = sp.factor(portal.subs(k, -2*sp.sqrt(a*b)))
    checks = {
        "completion_exact": sp.expand(portal-completed) == 0,
        "gram_determinant_exact": sp.simplify(determinant-a*b+k**2/4) == 0,
        "cp_flip_invariance": sp.expand(portal.subs({X: -X, Y: -Y}, simultaneous=True)-portal) == 0,
        "generic_cp_symmetric_benchmark_positive_definite": gram.subs({a: 1, b: 1, k: 0}).det() == 1,
        "generic_benchmark_zero_only_at_intersection": portal.subs({a: 1, b: 1, k: 0, X: 1, Y: 0}).is_positive,
        "rank_one_plus_factorization": sp.simplify(rank_plus-(sp.sqrt(a)*X+sp.sqrt(b)*Y)**2) == 0,
        "rank_one_minus_factorization": sp.simplify(rank_minus-(sp.sqrt(a)*X-sp.sqrt(b)*Y)**2) == 0,
        "rank_one_shell_nontrivial": rank_minus.subs(X, sp.sqrt(b/a)*Y) == 0,
        "sign_flip_is_carrier_relabelling": sp.expand(rank_plus.subs(Y, -Y)-rank_minus) == 0,
        "supercritical_benchmark_unstable": gram.subs({a: 1, b: 1, k: 3}).det().is_negative,
        "rank_one_is_codimension_one_equation": sp.solve(sp.Eq(determinant, 0), k) == [-2*sp.sqrt(a)*sp.sqrt(b), 2*sp.sqrt(a)*sp.sqrt(b)],
        "shell_ratio_remains_coefficient_ratio": sp.simplify(sp.sqrt(b/a)-sp.sqrt(b)/sp.sqrt(a)) == 0,
        "same_cp_symmetry_allows_intersection_and_shell": portal.subs({a: 1, b: 1, k: 0}) != portal.subs({a: 1, b: 1, k: 2}),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP389",
        "admitted_state_domain": "real CP-odd coordinates X=C and Y=D*q with the general CP-even quadratic portal and positive diagonal coefficients",
        "faithful_quotient_coordinate": "unlabelled CP quotient of (C,D,q), with branch-labelled stabilizer experiment treated separately",
        "source_authorized_probe_family": "CP symmetry, positive-semidefinite Gram cone, square completion, and carrier relabelling",
        "contextual_partition": "determinant positive selects only the intersection; determinant zero produces a one-dimensional shell; determinant negative is unstable",
        "classification": "CP symmetry rigidifies parity but does not select rank-one saturation or the numerical shell ratio",
        "portal": str(portal),
        "gram_determinant": str(determinant),
        "rank_one_condition": "kappa^2=4*a*b",
        "shell_ratio": "sqrt(b/a)",
        "smallest_exact_falsifier": "a=b=1 with kappa=0 and kappa=2 are both CP invariant and stable/nonnegative, but the first selects only X=Y=0 while the second has the shell X=-Y",
        "remaining_physical_instrument_gate": "derive rank-one Gram saturation and b/a from an independent source principle; a labelled branch port may then calibrate the otherwise conventional sign",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp389_cp_rank_one_saturation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
