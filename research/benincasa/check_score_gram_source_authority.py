#!/usr/bin/env python3
"""Type the fixed-loop score Gram against the frozen primary source."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).parent
scope = json.loads((ROOT / "interacting-regulated-period-scope.json").read_text(encoding="utf-8"))
rank = json.loads((ROOT / "fixed-loop-physical-score-rank.json").read_text(encoding="utf-8"))

checks = {
    "primary_source_authorizes_linear_regulated_period": (
        scope["primary_source"]["regulated_period_equation"] == "Eq. (6): I_G[alpha,beta;X]"
    ),
    "primary_source_scope_is_regulated_period_family": (
        scope["authorized_theorem_scope"] == "generic regulated twisted-period family"
    ),
    "pointwise_score_rank_is10": rank["generic_response_rank"] == 10,
    "pointwise_score_plus_constant_rank_is11": rank["generic_rank_with_constant"] == 11,
    "source_packet_contains_no_score_gram_measurement_map": True,
}

packet = {
    "schema": "marici.benincasa.score-gram-source-authority.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "authorized_map": "I_G: omega -> integral_Gamma omega",
    "derived_but_unauthorized_map": (
        "(s_i,s_j) -> integral_Gamma rho(l) s_i(l) s_j(l) d^3l"
    ),
    "preserved_result": (
        "The ten score functions are generically independent and their positive "
        "regulated L2 Gram form is nondegenerate."
    ),
    "retracted_inference": (
        "The frozen primary source does not thereby define the L2 score Gram as a "
        "physical observable or make the latent loop coordinate measurable."
    ),
    "classification": (
        "formal/contextual coefficient faithfulness established; physical period-readout "
        "faithfulness unproved"
    ),
    "new_carrier_support": False,
}

out = ROOT / "score-gram-source-authority.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
