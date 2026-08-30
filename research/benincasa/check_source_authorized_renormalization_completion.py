#!/usr/bin/env python3
"""Completion audit for source-authorized three-site finite renormalization."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(name: str) -> dict:
    with (ROOT / name).open(encoding="utf-8") as stream:
        return json.load(stream)


source = load("renormalization-source-identifiability.json")
contact = load("rank7-local-contact-quotient.json")
finiteness = load("three-site-uv-finiteness.json")
regulated = load("interacting-contextual-faithfulness-completion.json")
physical = load("fixed-loop-physical-score-rank.json")

checks = {
    "source_omissions_identified": source.get("status") == "source_underidentified",
    "local_contact_quotient_preserves_rank7": (
        contact.get("status") == "passed"
        and contact.get("rank7_contact_quotient_rank") == 7
    ),
    "frozen_graph_is_uv_finite": finiteness.get("status") == "passed",
    "graph_local_counterterm_space_is_zero": (
        finiteness.get("graph_local_uv_counterterm_space", {}).get("dimension") == 0
    ),
    "authorized_map_is_epsilon_zero_evaluation": (
        finiteness.get("source_authorized_finite_map")
        == "ordinary evaluation at epsilon=0"
    ),
    "authorized_map_preserves_rank7": (
        finiteness.get("rank_after_source_authorized_map") == 7
    ),
    "regulated_observer_was_faithful": (
        regulated.get("status") == "passed"
        and physical.get("regulated_physical_score_kernel_on_source_quotient") == 0
    ),
    "no_new_carrier_support": all(
        packet.get("new_carrier_support") is False
        for packet in (source, contact, finiteness)
    ),
}

packet = {
    "schema": "marici.benincasa.source-authorized-renormalization-completion.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "admissible_graph_local_counterterm_space": {
        "dimension": 0,
        "generators": [],
    },
    "source_authorized_finite_maps": ["ev_epsilon=0"],
    "genuine_graph_local_scheme_group": "trivial",
    "induced_rank7_map": "identity",
    "renormalized_readout_rank": 7,
    "contextual_faithfulness": "scheme-independent within the frozen graph-local source",
    "action_level_boundary": (
        "A larger theory may supply inherited local counterterms. The frozen source "
        "does not specify their coefficients, but locality places them in the "
        "loop-independent contact port, whose intersection with R7 is zero."
    ),
    "classification": "physical readout layer; no Carrier modification",
    "new_carrier_support": False,
    "evidence": [
        "renormalization-source-identifiability.json",
        "rank7-local-contact-quotient.json",
        "three-site-uv-finiteness.json",
        "interacting-contextual-faithfulness-completion.json",
        "fixed-loop-physical-score-rank.json",
    ],
}

output = ROOT / "source-authorized-renormalization-completion.json"
output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
