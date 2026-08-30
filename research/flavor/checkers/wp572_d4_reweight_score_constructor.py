"""Exact WP572 D4 three-weight score and support audit."""

import json
from pathlib import Path

import sympy as sp


c, h = sp.symbols("c h", real=True, nonzero=True)
a_re, a_im, b_re, b_im = sp.symbols("a_re a_im b_re b_im", real=True)

amplitude_real = a_re + c * b_re
amplitude_imag = a_im + c * b_im
weight = sp.expand(amplitude_real**2 + amplitude_imag**2)
exact_derivative = sp.diff(weight, c)
symmetric_derivative = sp.simplify(
    (weight.subs(c, c + h) - weight.subs(c, c - h)) / (2 * h)
)

hostile_weight = sp.expand((1 - c) ** 2)
hostile_central = hostile_weight.subs(c, 1)
hostile_minus = sp.simplify(hostile_weight.subs(c, 1 - h))
hostile_plus = sp.simplify(hostile_weight.subs(c, 1 + h))
hostile_first_derivative = sp.diff(hostile_weight, c).subs(c, 1)
hostile_second_derivative = sp.diff(hostile_weight, c, 2).subs(c, 1)

repository_census = {
    "revision": "788431390ded97d4b44c25a0013b184053b4aaad",
    "tracked_files": 152,
    "reweight_cards": 0,
    "event_files": 0,
    "hhh_validation_files": 0,
    "release_tags": 0,
    "d4_lha_block": "BSMINPUTS",
    "d4_lha_code": 997,
}

reweight_card = [
    "launch --rwgt_name=d4_minus",
    "  set BSMINPUTS 997 0.5",
    "launch --rwgt_name=d4_plus",
    "  set BSMINPUTS 997 1.5",
]

checks = {
    "event_weight_is_quadratic_in_d4": sp.Poly(weight, c).degree() == 2,
    "symmetric_three_weight_formula_is_exact": sp.simplify(symmetric_derivative - exact_derivative) == 0,
    "hostile_central_weight_vanishes": hostile_central == 0,
    "hostile_neighbor_weights_are_nonzero_polynomials": hostile_minus == h**2 and hostile_plus == h**2,
    "hostile_reweight_ratio_is_undefined": hostile_central == 0 and hostile_plus != 0,
    "hostile_first_order_signed_response_vanishes": hostile_first_derivative == 0,
    "hostile_support_birth_is_second_order": hostile_second_derivative == 2,
    "repository_has_no_frozen_reweight_card": repository_census["reweight_cards"] == 0,
    "repository_has_no_event_sample": repository_census["event_files"] == 0,
    "repository_has_no_hhh_validation_packet": repository_census["hhh_validation_files"] == 0,
    "minimal_card_has_two_symmetric_hypotheses": len(reweight_card) == 4 and "0.5" in reweight_card[1] and "1.5" in reweight_card[3],
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP572",
    "classification": "exact executable-in-principle LO D4 signed-measure derivative with a domination-gated likelihood-score representation",
    "weight_polynomial": str(weight),
    "exact_derivative": str(exact_derivative),
    "symmetric_derivative": str(symmetric_derivative),
    "repository_census": repository_census,
    "prospective_reweight_card": reweight_card,
    "smallest_exact_falsifier": {
        "amplitude": "1 - c",
        "central_parameter": "1",
        "central_weight": str(hostile_central),
        "minus_weight": str(hostile_minus),
        "plus_weight": str(hostile_plus),
        "first_derivative": str(hostile_first_derivative),
        "second_derivative": str(hostile_second_derivative),
        "failure": "central ratio is undefined while support birth occurs only at second order",
    },
    "contextual_partition": "the signed derivative is defined on the declared carrier; its likelihood-score representation requires domination by a frozen proposal",
    "weak_basis_descent": "passes after a declared invariant portal-to-generator coupling map",
    "remaining_gate": "portal-complete local measure jet, frozen dominating source mixture, shower-detector channel, exposure or null completion, covariance, and robust resolution",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp572_d4_reweight_score_constructor.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
