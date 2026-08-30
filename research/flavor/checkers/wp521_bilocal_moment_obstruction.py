"""Finite-moment obstruction for the WP520 bilocal hadronic interface."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp511 = load("wp511_neutral_b_current_instrument.json")
wp519 = load("wp519_wet_matching_domain_audit.json")
wp520 = load("wp520_finite_propagator_bs_kernel.json")

x = sp.symbols("q_squared", nonnegative=True)
form_factor = sp.cancel(
    sp.sympify(
        wp520["aligned_bs_kernel"]["normalized_spacelike_form_factor"],
        locals={"q_squared": x},
    )
)
numerator, denominator = sp.fraction(form_factor)
reduced_denominator_degree = sp.Poly(denominator, x).degree()


def moments(nodes, weights, maximum_degree):
    return [
        sp.factor(sum(weight * node**degree for node, weight in zip(nodes, weights)))
        for degree in range(maximum_degree + 1)
    ]


# On the positive normalized subclass of possible momentum measures supported
# on x=q^2 in [0,1] GeV^2, construct two measures sharing moments 0..N.
# Alternating binomial weights annihilate every polynomial of degree <=N.
# A small symmetric perturbation of the uniform measure keeps both measures
# strictly positive.
hostile_pairs = []
for maximum_moment in range(7):
    order = maximum_moment + 1
    nodes = [sp.Rational(index, order) for index in range(order + 1)]
    null_weights = [
        (-1) ** index * sp.binomial(order, index)
        for index in range(order + 1)
    ]
    base_weight = sp.Rational(1, order + 1)
    epsilon = sp.Rational(
        1,
        2 * (order + 1) * max(abs(weight) for weight in null_weights),
    )
    weights_plus = [
        sp.factor(base_weight + epsilon * weight) for weight in null_weights
    ]
    weights_minus = [
        sp.factor(base_weight - epsilon * weight) for weight in null_weights
    ]
    moments_plus = moments(nodes, weights_plus, maximum_moment)
    moments_minus = moments(nodes, weights_minus, maximum_moment)
    response_plus = sp.factor(
        sum(weight * form_factor.subs(x, node) for node, weight in zip(nodes, weights_plus))
    )
    response_minus = sp.factor(
        sum(weight * form_factor.subs(x, node) for node, weight in zip(nodes, weights_minus))
    )
    response_difference = sp.factor(response_plus - response_minus)
    hostile_pairs.append(
        {
            "matched_through_moment": maximum_moment,
            "nodes_q_squared_GeV_squared": [str(node) for node in nodes],
            "weights_plus": [str(weight) for weight in weights_plus],
            "weights_minus": [str(weight) for weight in weights_minus],
            "matched_moments": [str(value) for value in moments_plus],
            "moments_match_exactly": moments_plus == moments_minus,
            "minimum_weight": str(min(weights_plus + weights_minus)),
            "response_plus": str(response_plus),
            "response_minus": str(response_minus),
            "response_difference": str(response_difference),
            "response_difference_numeric": float(sp.N(response_difference, 30)),
        }
    )

# If integration against F were determined by moments 0..N for every positive
# measure on an interval, F would have to lie in the polynomial span of those
# moment functions.  The reduced WP520 kernel has a nonconstant denominator,
# so it is not in any finite polynomial span.
checks = {
    "wp511_dependency_passed": bool(wp511["passed"]),
    "wp519_dependency_passed": bool(wp519["passed"]),
    "wp520_dependency_passed": bool(wp520["passed"]),
    "form_factor_is_reduced_rational": sp.gcd(
        sp.Poly(numerator, x), sp.Poly(denominator, x)
    ).degree()
    == 0,
    "reduced_denominator_is_nonconstant": reduced_denominator_degree > 0,
    "all_hostile_measures_are_strictly_positive": bool(
        all(sp.Rational(pair["minimum_weight"]) > 0 for pair in hostile_pairs)
    ),
    "all_declared_moments_match_exactly": bool(
        all(pair["moments_match_exactly"] for pair in hostile_pairs)
    ),
    "all_finite_examples_have_distinct_bilocal_response": bool(
        all(sp.sympify(pair["response_difference"]) != 0 for pair in hostile_pairs)
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP521",
    "bilocal_response_contract": {
        "response": "B[mu]=integral F(q^2) dmu(q^2)",
        "measure_domain": "Hostile positive normalized subclass on 0<=q^2<=1 GeV^2; positivity is a restriction for the counterexample, not an assertion about the full neutral-B bilocal matrix element.",
        "local_wet_information": "Only moment zero, integral dmu=1, after factoring the contact matrix element.",
        "exact_form_factor": str(form_factor),
        "reduced_denominator_degree": reduced_denominator_degree,
    },
    "hostile_equal_moment_pairs": hostile_pairs,
    "general_obstruction": "Because the reduced WP520 form factor is rational with nonconstant denominator, it is not in any finite polynomial moment span. Therefore no finite tower of ordinary q^2 moments determines its convolution for every admitted measure.",
    "classification": "Exact nonfaithfulness theorem for local and finite-moment hadronic summaries. A direct bilocal functional or a source-authorized complete representation is required.",
    "selector": False,
    "rigidifier": False,
    "instrument": "WP511 supplies the local contact normalization only. No calibrated bilocal momentum functional is currently attached.",
    "smallest_exact_falsifier": "The N=0 pair consists of two positive normalized measures with the same contact normalization and unequal WP520 response. The N=1 pair additionally shares the first q^2 moment and remains unequal.",
    "remaining_gate": "Supply a calibrated bilocal neutral-B matrix element or an independently justified complete basis with controlled truncation error; finite moments without such an error contract cannot restore faithfulness.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp521_bilocal_moment_obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
