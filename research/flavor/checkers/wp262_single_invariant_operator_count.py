"""WP262: exact operator-count theorem for one-coordinate mixing selectors."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    x = sp.symbols("x", positive=True)
    c = sp.symbols("c", nonzero=True)

    monomial_degrees = range(1, 7)
    monomial_derivatives = {n: sp.diff(c * x**n, x) for n in monomial_degrees}
    monomial_interior_roots = {
        n: [root for root in sp.solve(derivative, x) if root.is_positive]
        for n, derivative in monomial_derivatives.items()
    }

    a, b = sp.symbols("a b", positive=True)
    two_operator_potential = -a * x + b * x**2
    two_operator_stationary = sp.solve(sp.diff(two_operator_potential, x), x)[0]

    target = sp.Rational(3, 10)
    required_relation = sp.solve(
        sp.Eq(sp.diff(two_operator_potential, x).subs(x, target), 0), a
    )[0]
    hostile_packets = [
        {"a": sp.Rational(3), "b": sp.Rational(5)},
        {"a": sp.Rational(1), "b": sp.Rational(1)},
    ]
    hostile_points = [sp.simplify(packet["a"] / (2 * packet["b"])) for packet in hostile_packets]

    # Exact weak-basis invariant realization inherited from WP261.
    hu = sp.diag(0, 1)
    hd = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 4)],
                    [sp.Rational(1, 4), sp.Rational(1, 2)]])
    commutator = hu * hd - hd * hu
    invariant = sp.simplify(2 * sp.trace(commutator.T * commutator))
    q = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)],
                   [-sp.Rational(4, 5), sp.Rational(3, 5)]])
    hu_q, hd_q = q * hu * q.T, q * hd * q.T
    commutator_q = hu_q * hd_q - hd_q * hu_q
    invariant_q = sp.simplify(2 * sp.trace(commutator_q.T * commutator_q))

    checks = {
        "all_tested_single_monomials_have_no_positive_stationary_root": all(not roots for roots in monomial_interior_roots.values()),
        "symbolic_monomial_derivatives_nonzero_on_interior": all(sp.factor(value) == n * c * x ** (n - 1) for n, value in monomial_derivatives.items()),
        "two_operator_stationary_point_is_ratio": two_operator_stationary == a / (2 * b),
        "target_three_tenths_requires_a_equals_three_fifths_b": required_relation == sp.Rational(3, 5) * b,
        "hostile_coefficients_select_distinct_points": hostile_points == [target, sp.Rational(1, 2)],
        "mixing_coordinate_is_weak_basis_invariant": invariant_q == invariant,
        "deliberate_one_operator_interior_claim_fails": all(not roots for roots in monomial_interior_roots.values()),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP262",
        "theorem_domain": "single normalized weak-basis-invariant mixing coordinate x in (0,1), with a finite polynomial source potential",
        "single_operator_family": "V_n(x)=c*x^n for nonzero c and integer n>=1",
        "single_operator_derivatives": {str(n): str(value) for n, value in monomial_derivatives.items()},
        "single_operator_interior_stationary_roots": {str(n): [str(root) for root in roots] for n, roots in monomial_interior_roots.items()},
        "minimal_interior_selector": "V(x)=-a*x+b*x^2",
        "stationary_point": str(two_operator_stationary),
        "target_witness": {"x_star": str(target), "required_coefficient_relation": "a=3*b/5"},
        "hostile_selected_points": [str(point) for point in hostile_points],
        "classification": "bounded operator-count theorem: a single nonconstant monomial cannot select interior mixing; the minimal polynomial selector requires a source-authorized relative coefficient",
        "smallest_exact_falsifier": "x*=3/10 forces a=3b/5, while the equally descending choice a=b selects x*=1/2",
        "remaining_physical_instrument_gate": "derive the relative operator coefficient from an independent symmetry, radiative matching, or microscopic source calculation, then supply dynamical substrate and stabilization",
        "scope_limit": "does not exclude a symmetry that independently fixes coefficient ratios, multiple invariant coordinates, nonpolynomial source geometry, or boundary-selected stationary points",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp262_single_invariant_operator_count.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
