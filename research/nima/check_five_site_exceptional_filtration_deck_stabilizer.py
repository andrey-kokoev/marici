#!/usr/bin/env python3
"""Audit which five-site deck translations preserve the exceptional filtration."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
INPUT = REPO / "research/benincasa/results/five-site-two-normal-rees.json"
OUTPUT = (
    REPO
    / "research/nima/results/five-site-exceptional-filtration-deck-stabilizer.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    packet = json.loads(INPUT.read_text(encoding="utf-8"))
    orders = {
        int(row["sheet"]): int(row["tau_vanishing_order"])
        for row in packet["tau_sheet_orders"]
    }
    assert set(orders) == set(range(32))
    assert Counter(orders.values()) == Counter({2: 10, 4: 20, 9: 2})

    translations = []
    stabilizer = []
    for mask in range(32):
        transitions = Counter((orders[sheet], orders[sheet ^ mask]) for sheet in range(32))
        preserves = all(source == target for source, target in transitions)
        if preserves:
            stabilizer.append(mask)
        translations.append(
            {
                "mask": mask,
                "preserves_filtration": preserves,
                "transition_counts": [
                    {"source_order": source, "target_order": target, "count": count}
                    for (source, target), count in sorted(transitions.items())
                ],
            }
        )

    assert stabilizer == [0, 31]
    assert all(orders[sheet] == orders[sheet ^ 31] for sheet in range(32))
    assert any(
        source != target
        for row in translations
        if row["mask"] not in stabilizer
        for source, target in (
            (cell["source_order"], cell["target_order"])
            for cell in row["transition_counts"]
        )
    )

    result = {
        "schema": "marici.nima.five_site.exceptional_filtration_deck_stabilizer.v1",
        "input": str(INPUT.relative_to(REPO)).replace("\\", "/"),
        "input_sha256": sha256(INPUT),
        "deck_group": "(Z/2)^5 acting by sheet XOR",
        "order_histogram": {
            str(order): count for order, count in sorted(Counter(orders.values()).items())
        },
        "filtration_stabilizer": stabilizer,
        "filtration_stabilizer_description": "{identity, global complement}",
        "full_deck_action_preserves_unspecialized_pairing": True,
        "full_deck_action_preserves_exceptional_filtration": False,
        "global_complement_preserves_exceptional_filtration": True,
        "interpretation": (
            "The tau-Cartier associated grading retains only global complement as "
            "an honest deck symmetry. Other sheet translations are filtered "
            "correspondences that mix orders 2, 4, and 9."
        ),
        "translations": translations,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "order_histogram",
        "filtration_stabilizer",
        "full_deck_action_preserves_exceptional_filtration",
        "global_complement_preserves_exceptional_filtration",
    )}, sort_keys=True))


if __name__ == "__main__":
    main()
