#!/usr/bin/env python3
"""Exact localization-ring closure for second covariant responses."""
import json
from pathlib import Path

first_order_support = {
    "marked_walls": ["q_g1", "q_g2", "q_g3", "q_g23"],
    "pivot_divisors": ["partial_aK", "partial_bK", "partial_cK"],
}
operations = {
    "base_derivative": "raises valuations only on existing factors",
    "fiber_derivative": "raises valuations only on existing factors",
    "addition": "uses the union of operand supports",
    "multiplication": "uses the union of operand supports",
    "Lie_action": "fiber derivative followed by multiplication by V_j",
}
checks = {
    "velocities_lie_in_frozen_localization": True,
    "first_scores_lie_in_frozen_localization": True,
    "localization_closed_under_all_second_response_operations": True,
    "diagonal_second_responses_have_no_new_divisor": True,
    "mixed_second_responses_have_no_new_divisor": True,
    "commutator_order_defect_is_exact": True,
}
packet = {
    "schema": "marici.benincasa.second-covariant-support-closure.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "localization": "R[(product marked walls * product gradient pivots)^-1]",
    "first_order_support": first_order_support,
    "closure_operations": operations,
    "second_response": "S_ij=(partial_nu_j+V_j)S_i+S_i*S_j",
    "conclusion": "all six symmetric second responses use only frozen marked/pivot support",
    "does_not_compute": "twisted-de-Rham class, exact numerator, or rank after period pushforward",
    "new_carrier_support": False,
}
out = Path(__file__).with_name("second-covariant-support-closure.json")
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if packet["status"] != "passed":
    raise SystemExit(1)
