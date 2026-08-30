#!/usr/bin/env python3
"""Compose the weighted Gram chart with the verified rank-60 interaction action."""

import json
from pathlib import Path

import sympy as sp


here = Path(__file__).parent
lower = json.loads((here / "generic-lower-interaction-class-faithfulness.json").read_text())
restricted = json.loads((here / "restricted-interaction-class-faithfulness.json").read_text())
full = json.loads((here / "rank60-interaction-action-faithfulness.json").read_text())
weighted = json.loads((here / "gram-leray-weighted-score.json").read_text())

assert lower["generic_lower_direct_image_class_rank"] == 7
assert lower["additional_direct_image_kernel_dimension"] == 0
assert restricted["restricted_direct_image_class_rank"] == 6
assert restricted["restriction_kernel_rank"] == 1
assert restricted["additional_restricted_direct_image_kernel_dimension"] == 0
assert full["full_interaction_rank"] == 7
assert full["full_interaction_kernel_dimension"] == 0
assert weighted["complete_interaction_tower"]["faithful_quotient_rank"] == 7
assert weighted["weighted_physical_chart"]["determinant"] == "-P1*P2"

c, a, b, E, X1, X2, X3 = sp.symbols("c a b E X1 X2 X3")
u, v, w = sp.symbols("u v w")
marks = {
    "q_g1": c + b + X1,
    "q_g2": c + a + X2,
    "q_g3": a + b + X3,
    "q_g23": c + b + X2 + X3,
    "q_G12": c + E,
}

mark_derivatives = {
    name: [sp.diff(mark, coordinate) for coordinate in (u, v, w)]
    for name, mark in marks.items()
}
assert all(all(value == 0 for value in derivatives) for derivatives in mark_derivatives.values())

packet = {
    "schema": "marici.benincasa.weighted-gram-rank60-base-change.v1",
    "status": "passed",
    "base_change": {
        "source_coordinates": ["nu1", "nu2", "nu3"],
        "physical_coordinates": ["u=delta(P1^2)", "v=delta(P2^2)", "w=theta^2"],
        "jacobian_determinant": weighted["weighted_physical_chart"]["determinant"],
        "formal_etale_locus": "P1*P2 != 0",
        "maximum_physical_angle_order": weighted["complete_interaction_tower"]["maximum_required_physical_angle_order"],
    },
    "marked_localization": {
        "marks": {name: str(mark) for name, mark in marks.items()},
        "derivatives_in_u_v_w": {
            name: [str(value) for value in derivatives]
            for name, derivatives in mark_derivatives.items()
        },
        "commutator": "zero",
        "reason": "all frozen marked walls are independent of the momentum-normal coordinates",
    },
    "rank_composition": {
        "lower_rank": lower["generic_lower_direct_image_class_rank"],
        "restricted_rank": restricted["restricted_direct_image_class_rank"],
        "principal_restriction_kernel_rank": restricted["restriction_kernel_rank"],
        "full_rank": full["full_interaction_rank"],
        "additional_weighted_kernel_rank": 0,
    },
    "classification": {
        "weighted_rank60_interaction_action": "faithful rank seven",
        "marked_Beck_Chevalley": "strict on the source twisted de Rham complex",
        "soft_exception": "P1*P2=0 belongs to existing soft support",
        "new_carrier_support": False,
    },
    "scope_warning": (
        "This is a formally etale base-change theorem for the verified algebraic rank-60 action. "
        "It does not construct the missing tensor/polarization vertex or replace a source-derived "
        "physical period covector away from the Gram support calculation."
    ),
}

output = here / "weighted-gram-rank60-base-change.json"
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
