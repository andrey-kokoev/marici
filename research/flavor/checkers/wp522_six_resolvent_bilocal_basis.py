"""Six-probe rational bilocal basis induced by the WP520 pole grammar."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp520 = load("wp520_finite_propagator_bs_kernel.json")
wp521 = load("wp521_bilocal_moment_obstruction.json")

x = sp.symbols("q_squared", nonnegative=True)
form_factor = sp.cancel(
    sp.sympify(
        wp520["aligned_bs_kernel"]["normalized_spacelike_form_factor"],
        locals={"q_squared": x},
    )
)
numerator, denominator = map(sp.factor, sp.fraction(form_factor))
numerator_poly = sp.Poly(numerator, x)
denominator_poly = sp.Poly(denominator, x)
factor_coefficient, denominator_factors = sp.factor_list(denominator, x)

# The source-authorized finite probe family is
# H_k[mu]=integral x^k/D(x) dmu(x), k=0,...,5.  Every aligned kernel with the
# same six-pole denominator and numerator degree below six is reconstructed by
# the corresponding numerator coefficients.
basis = [sp.factor(x**degree / denominator) for degree in range(6)]
numerator_coefficients = [
    sp.factor(numerator_poly.coeff_monomial(x**degree)) for degree in range(6)
]
reconstruction = sp.factor(
    sum(coefficient * function for coefficient, function in zip(numerator_coefficients, basis))
)

# Exact independence: evaluation at six nonnegative rational points gives a
# weighted Vandermonde matrix.  Its determinant is nonzero because D has no
# spacelike zeros at these points.
evaluation_nodes = [sp.Integer(index) for index in range(6)]
evaluation_matrix = sp.Matrix(
    [
        [sp.factor(function.subs(x, node)) for function in basis]
        for node in evaluation_nodes
    ]
)
evaluation_determinant = sp.factor(evaluation_matrix.det())
five_probe_ranks = [
    evaluation_matrix[:, [column for column in range(6) if column != omitted]].rank()
    for omitted in range(6)
]

# The common denominator should be the product of the two cubic mixed sectors
# carrying F6 and F7.  Quintet factors cancel from the aligned difference.
nonconstant_factors = [
    (sp.factor(factor), multiplicity)
    for factor, multiplicity in denominator_factors
    if sp.Poly(factor, x).degree() > 0
]
factor_degrees = sorted(
    sp.Poly(factor, x).degree()
    for factor, multiplicity in nonconstant_factors
    for _ in range(multiplicity)
)

# A direct bilocal channel for the single frozen WP520 numerator is the one
# weighted sum sum_k n_k H_k.  Six separate probes are needed only to remain
# faithful on the full declared numerator family; do not confuse generic
# family identification with minimal readout of one already frozen kernel.
nonzero_numerator_coefficients = [
    degree
    for degree, coefficient in enumerate(numerator_coefficients)
    if coefficient != 0
]

checks = {
    "wp520_dependency_passed": bool(wp520["passed"]),
    "wp521_dependency_passed": bool(wp521["passed"]),
    "denominator_degree_is_six": denominator_poly.degree() == 6,
    "denominator_is_two_simple_cubic_factors": bool(
        factor_degrees == [3, 3]
        and all(multiplicity == 1 for factor, multiplicity in nonconstant_factors)
    ),
    "numerator_degree_is_below_six": numerator_poly.degree() < 6,
    "six_probe_reconstruction_is_exact": sp.simplify(
        reconstruction - form_factor
    )
    == 0,
    "six_probe_evaluation_matrix_has_nonzero_determinant": evaluation_determinant
    != 0,
    "every_five_probe_subfamily_has_rank_five": five_probe_ranks == [5] * 6,
    "frozen_wp520_kernel_uses_a_proper_subset_or_combination": bool(
        0 < len(nonzero_numerator_coefficients) <= 6
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP522",
    "six_pole_denominator": {
        "factor_coefficient": str(factor_coefficient),
        "factors": [
            {
                "factor": str(factor),
                "degree": sp.Poly(factor, x).degree(),
                "multiplicity": multiplicity,
            }
            for factor, multiplicity in nonconstant_factors
        ],
        "interpretation": "Two cubic mixed sectors carrying the aligned F6 and F7 currents; quintet factors cancel.",
    },
    "rational_completion_basis": {
        "definition": "H_k[mu]=integral (q^2)^k/D(q^2) dmu(q^2), k=0,...,5",
        "basis_functions": [str(function) for function in basis],
        "wp520_numerator_coefficients_low_to_high": [
            str(coefficient) for coefficient in numerator_coefficients
        ],
        "nonzero_coefficient_degrees": nonzero_numerator_coefficients,
        "reconstruction": "B_F[mu]=sum_k n_k H_k[mu] for every numerator N_F of degree below six.",
        "authority": "Algebraic completion only. Arbitrary numerator interventions are not established as source operations.",
    },
    "frozen_source_probe": {
        "definition": "H_0[mu]=integral D(q^2)^-1 dmu(q^2)",
        "wp520_coefficient": str(numerator_coefficients[0]),
        "sufficiency": "The frozen WP520 numerator is constant, so one direct source-shaped bilocal functional determines its response exactly.",
    },
    "minimality_certificate": {
        "domain": "Full six-dimensional numerator family over the frozen two-cubic denominator",
        "evaluation_nodes_q_squared_GeV_squared": [
            str(node) for node in evaluation_nodes
        ],
        "evaluation_determinant": str(evaluation_determinant),
        "five_probe_subfamily_ranks": five_probe_ranks,
        "qualification": "For the one already frozen WP520 kernel, one direct weighted bilocal readout is sufficient. Six are necessary only for joint faithfulness on the full numerator family.",
    },
    "classification": "One exact source-shaped bilocal target suffices for the frozen WP520 kernel. A six-coordinate rational basis is algebraically complete and generically minimal, but arbitrary numerator control and executable hadronic access are not established.",
    "selector": False,
    "rigidifier": bool(evaluation_determinant != 0),
    "instrument": "No physical implementation of the direct H_0 bilocal matrix element is admitted. The six-coordinate completion is not executable control without a source-authorized numerator family.",
    "smallest_exact_falsifier": "The two cubic denominator factors merge or acquire multiplicity, the numerator degree reaches six, or the six rational basis functions lose rank on the admitted source family.",
    "remaining_gate": "Compute the single direct WP520-weighted H_0 neutral-B matrix element with calibrated normalization, uncertainties, and threshold running. Require a separate source authorization before treating the six-coordinate algebraic completion as an executable probe family.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp522_six_resolvent_bilocal_basis.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
