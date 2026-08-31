"""Denominator gate for the triple-incidence p-normal primitive.

The previous primitive H_p=p*q1*dq2 lived in the cleared numerator carrier.
This checker tests whether the actual logarithmic denominator carrier supplies a
one-form primitive for p*dq1^dq2/(q1*q2*q3), with q3=q1+q2+p and without 1/p.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = ROOT / "research" / "voevodsky" / "results" / "cosmology_log_denominator_primitive_gate.json"


def load(name: str) -> dict:
    return json.loads((NIMA_RESULTS / name).read_text(encoding="utf-8"))


def monomials(x: sp.Symbol, y: sp.Symbol, degree: int) -> list[sp.Expr]:
    return [x**i * y**j for i in range(degree + 1) for j in range(degree + 1 - i)]


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    row_count = len(rows)
    col_count = len(rows[0])
    for col in range(col_count):
        pivot = next((r for r in range(rank, row_count) if rows[r][col] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, prime)
        rows[rank] = [(value * inv) % prime for value in rows[rank]]
        for r in range(row_count):
            if r == rank:
                continue
            factor = rows[r][col] % prime
            if factor:
                rows[r] = [(a - factor * b) % prime for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def bounded_rational_ansatz(depth: int, numerator_degree: int, prime: int) -> dict:
    """Test A=P/D^depth, B=Q/D^depth after p=1 over F_prime."""
    x, y = sp.symbols("x y")
    z = x + y + 1
    d = x * y * z
    mons = monomials(x, y, numerator_degree)
    a_unknowns = sp.symbols(f"a0:{len(mons)}")
    b_unknowns = sp.symbols(f"b0:{len(mons)}")
    p_num = sum(coeff * mon for coeff, mon in zip(a_unknowns, mons))
    q_num = sum(coeff * mon for coeff, mon in zip(b_unknowns, mons))
    a_form = p_num / d**depth
    b_form = q_num / d**depth
    residual = sp.together(sp.diff(b_form, x) - sp.diff(a_form, y) - 1 / d)
    numerator = sp.Poly(sp.expand(sp.together(residual * d ** (depth + 1))), x, y)
    equations = []
    for coeff in numerator.coeffs():
        poly = sp.Poly(coeff, *(a_unknowns + b_unknowns))
        equations.append([int(c) for c in poly.coeffs()])
    unknown_count = len(a_unknowns) + len(b_unknowns)

    # Convert sparse coefficient polys into aligned rows plus the constant term.
    monomial_keys = [(1,) + tuple(0 for _ in range(unknown_count))]
    monomial_keys += [tuple(1 if i == j else 0 for i in range(unknown_count)) for j in range(unknown_count)]
    rows = []
    augmented = []
    variables = a_unknowns + b_unknowns
    for coeff in numerator.coeffs():
        poly = sp.Poly(coeff, *variables)
        row = [0] * unknown_count
        constant = 0
        for powers, value in poly.terms():
            value_int = int(value)
            if sum(powers) == 0:
                constant = value_int
            elif sum(powers) == 1:
                row[powers.index(1)] = value_int
            else:
                raise AssertionError("nonlinear ansatz equation")
        rows.append(row)
        augmented.append(row + [-constant])

    coefficient_rank = rank_mod_prime(rows, prime)
    augmented_rank = rank_mod_prime(augmented, prime)
    return {
        "depth": depth,
        "numerator_degree": numerator_degree,
        "unknowns": unknown_count,
        "equations": len(rows),
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "solution_exists": coefficient_rank == augmented_rank,
    }


def main() -> None:
    log_identity = load("cosmology_triple_incidence_logarithmic_identity.json")
    primitive = json.loads((ROOT / "research" / "voevodsky" / "results" / "cosmology_minimal_bulk_face_primitive.json").read_text(encoding="utf-8"))

    assert log_identity["local_wall_model"] == "q3=q1+q2+p"
    assert log_identity["cleared_identity"].endswith("=p*dq1^dq2")
    assert primitive["dH_equals_p_Xi"] is True
    assert primitive["ambient_division_by_p"] is False

    # Logarithmic denominator carrier: alpha_i=dlog(q_i), omega_ij=alpha_i^alpha_j.
    # d(alpha_i)=0, so no logarithmic one-form with coefficient constants has
    # differential p*eta.  The nonzero class is the circuit combination in H^2
    # of the generic three-line complement; it disappears only after the p=0
    # Orlik--Solomon specialization relation is imposed.
    log_complex = {
        "degree_1_basis": ["dlog(q1)", "dlog(q2)", "dlog(q3)"],
        "degree_2_basis": ["omega12", "omega13", "omega23"],
        "d_degree_1_to_degree_2": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        "target": "p*eta=omega12-omega13+omega23",
        "log_one_form_primitive_exists": False,
    }

    bounded_tests = {}
    for prime in (101, 103):
        prime_tests = []
        for depth in (1, 2):
            test = bounded_rational_ansatz(depth=depth, numerator_degree=2 * depth, prime=prime)
            assert test["solution_exists"] is False
            prime_tests.append(test)
        bounded_tests[str(prime)] = prime_tests

    result = {
        "schema": "marici.voevodsky.cosmology-log-denominator-primitive-gate.v1",
        "status": "finite_denominator_gate_no_go_for_log_and_bounded_rational_primitives",
        "source_normal": "p=x+y+3*z",
        "denominator_carrier": "R[q1^-1,q2^-1,q3^-1] with q3=q1+q2+p",
        "eta": "dq1^dq2/(q1*q2*q3)",
        "cleared_numerator_primitive_retained_as_prior_result": "H_p=p*q1*dq2 gives dH_p=p*dq1^dq2 before denominators",
        "log_complex": log_complex,
        "bounded_rational_ansatz_tests": bounded_tests,
        "ambient_division_by_p": False,
        "ideal_dual_evaluation_applied": False,
        "tautological_circuit_quotient_used": False,
        "all_soft_Z3_used_as_coefficient": False,
        "inferred_from_identity_monodromy": False,
        "global_contour_or_physical_period_constructed": False,
        "first_missing_enlargement": "Cech localization or resolved/Rees exceptional face generator; the pure logarithmic denominator complex has a closed non-exact top circuit class",
        "conclusion": "The cleared numerator primitive does not lift to a logarithmic one-form primitive for p*eta. In the logarithmic denominator carrier, degree-one log generators are closed and p*eta is the nonzero generic circuit class. A bounded rational search with pole depth 1 and 2 and numerator degree up to twice the depth is inconsistent over F_101 and F_103. The denominator gate therefore blocks the candidate until a Cech or resolved/Rees face enlargement supplies a source-derived primitive.",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
