"""Exact source-derived controllability and observability Gramian pairing."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp520 = load("wp520_finite_propagator_bs_kernel.json")
wp555 = load("wp555_realization_invariant_conditioning.json")

z = sp.symbols("z")
kernel = sp.sympify(
    wp520["aligned_bs_kernel"]["exact_witness_rational_function"],
    locals={"z": z},
)
_, denominator = sp.fraction(kernel)
denominator = sp.expand(denominator / sp.LC(sp.Poly(denominator, z)))
coefficients = sp.Poly(denominator, z).all_coeffs()
degree = sp.degree(denominator, z)

A = sp.zeros(degree)
for row in range(degree - 1):
    A[row, row + 1] = 1
for column, coefficient in enumerate(reversed(coefficients[1:])):
    A[degree - 1, column] = -coefficient
B = sp.zeros(degree, 1)
B[degree - 1, 0] = 1

# Solve the output row from the exact transfer function rather than inserting
# numerator coordinates by hand.
c_symbols = sp.symbols("c0:6")
c_trial = sp.Matrix([c_symbols])
transfer_trial = sp.together((c_trial * (z * sp.eye(degree) - A).inv() * B)[0])
transfer_equations = sp.Poly(
    sp.fraction(sp.together(transfer_trial - kernel))[0], z
).all_coeffs()
c_solution = sp.solve(transfer_equations, c_symbols, dict=True)[0]
c = sp.Matrix([[c_solution[value] for value in c_symbols]])

controllability = sp.Matrix.hstack(*[(A**power) * B for power in range(degree)])
observability = sp.Matrix.vstack(*[c * (A**power) for power in range(degree)])


def solve_lyapunov(rhs, transpose_left=False):
    variables = sp.symbols("x0:36")
    matrix = sp.Matrix(6, 6, variables)
    equation = (
        A.T * matrix + matrix * A - rhs
        if transpose_left
        else A * matrix + matrix * A.T - rhs
    )
    solution = next(iter(sp.linsolve(list(equation), variables)))
    return sp.Matrix(6, 6, solution)


Wc = solve_lyapunov(B * B.T)
Wo = solve_lyapunov(c.T * c, transpose_left=True)
Wc_minors = [sp.factor(Wc[:size, :size].det()) for size in range(1, 7)]
Wo_minors = [sp.factor(Wo[:size, :size].det()) for size in range(1, 7)]

T = sp.diag(2, 3, 5, 7, 11, 13)
A_prime = T * A * T.inv()
B_prime = T * B
c_prime = c * T.inv()
Wc_prime = T * Wc * T.T
Wo_prime = T.inv().T * Wo * T.inv()

metric = Wc.inv()
metric_prime = Wc_prime.inv()
metric_covariance = sp.simplify(metric_prime - T.inv().T * metric * T.inv())
hankel_original = Wc * Wo
hankel_prime = Wc_prime * Wo_prime
hankel_similarity = sp.simplify(hankel_prime - T * hankel_original * T.inv())

checks = {
    "dependencies_passed": bool(wp555["passed"]),
    "degree_six_realization": degree == 6,
    "exact_transfer_output_row_is_derived": sp.simplify(
        (c * (z * sp.eye(degree) - A).inv() * B)[0] - kernel
    )
    == 0,
    "realization_is_controllable": controllability.rank() == 6,
    "realization_is_observable": observability.rank() == 6,
    "controllability_gramian_is_positive_definite": all(
        value > 0 for value in Wc_minors
    ),
    "observability_gramian_is_positive_definite": all(
        value > 0 for value in Wo_minors
    ),
    "source_metric_transforms_covariantly": metric_covariance == sp.zeros(6),
    "hankel_product_is_similarity_covariant": hankel_similarity == sp.zeros(6),
    "pairing_selects_no_proper_subspace": Wc.rank() == Wo.rank() == 6,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP556",
    "domain": "The minimal degree-six companion realization of the frozen WP520 aligned b-s source resolvent.",
    "realization": {
        "state_dimension": int(degree),
        "input_dimension": B.cols,
        "output_dimension": c.rows,
        "output_row": [str(value) for value in c],
        "controllability_rank": int(controllability.rank()),
        "observability_rank": int(observability.rank()),
    },
    "positive_pairing": {
        "controllability_gramian_rank": int(Wc.rank()),
        "observability_gramian_rank": int(Wo.rank()),
        "controllability_leading_minor_signs": [int(sp.sign(value)) for value in Wc_minors],
        "observability_leading_minor_signs": [int(sp.sign(value)) for value in Wo_minors],
        "source_metric": "G_source=W_c^-1",
        "metric_transport": "G_source_prime=T^-T G_source T^-1",
        "hankel_spectrum": "eigenvalues of W_c W_o, invariant under realization similarity",
    },
    "selector_test": {
        "selected_subspace_dimension": int(Wc.rank()),
        "ambient_state_dimension": int(degree),
        "proper_subspace_selected": bool(Wc.rank() < degree),
        "conclusion": "The positive pairing weights all six minimal directions and selects no proper subspace or distinguished point.",
    },
    "classification": "Source-generated invariant positive geometry and presentation rigidifier; neither numerical selector nor physically executed probe.",
    "selector": bool(Wc.rank() < degree),
    "rigidifier": bool(Wc.rank() == degree),
    "instrument": "No admitted flavor operation implements the auxiliary inverse-mass-squared-time impulse experiment whose infinite-horizon response defines the Gramians.",
    "smallest_exact_falsifier": "Both exact Gramians have rank six and positive leading principal minors, so the proposed pairing has no null direction and selects no proper subspace.",
    "remaining_gate": "Derive a physical preparation, evolution parameter, and detector realizing the Gramian pairing, or replace it by another source-derived metric with an admitted instrument; then combine it with measured WP542 covariance. Selection still requires an independent transverse source law.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp556_source_gramian_pairing.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
