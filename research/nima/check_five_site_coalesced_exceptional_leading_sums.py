#!/usr/bin/env python3
"""Compute all coalesced exceptional leading sums over exact rationals."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
INPUT = REPO / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUTPUT = (
    REPO
    / "research/nima/results/five-site-coalesced-exceptional-leading-sums.json"
)


def cut_support(label: str) -> list[int]:
    sites = {int(char) for char in label.removeprefix("g_")}
    return [
        edge
        for edge in range(1, 6)
        if ((edge in sites) != (((edge % 5) + 1) in sites))
    ]


def denominator_leading(label: str, sheet: int) -> tuple[int, Fraction]:
    if label == "G":
        return 0, Fraction(1, 5)
    if label.startswith("G_minus_e"):
        edge = int(label.removeprefix("G_minus_e")[0]) - 1
        sign = 1 if sheet & (1 << edge) == 0 else -1
        return 1, Fraction(1, 2 * sign)

    cut = cut_support(label)
    signs = [1 if sheet & (1 << (edge - 1)) == 0 else -1 for edge in cut]
    radial_constant = sum(signs)
    if radial_constant:
        return 1, Fraction(1, radial_constant)
    return 0, Fraction(1, len(label.removeprefix("g_")))


def main() -> None:
    packet = json.loads(INPUT.read_text(encoding="utf-8"))["five_cycle"]
    common = packet["common_prefactor"]
    terms = packet["terms"]
    rows = []

    for sheet in range(32):
        term_data = []
        for term in terms:
            order = 0
            coefficient = Fraction(1)
            for label in common + term:
                shift, factor = denominator_leading(label, sheet)
                order += shift
                coefficient *= factor
            term_data.append((order, coefficient))

        order = min(value for value, _ in term_data)
        leading = sum(
            coefficient
            for value, coefficient in term_data
            if value == order
        )
        assert leading
        rows.append(
            {
                "sheet": sheet,
                "tau_order": order,
                "minimal_term_count": sum(value == order for value, _ in term_data),
                "leading_coefficient": f"{leading.numerator}/{leading.denominator}",
            }
        )

    assert Counter(row["tau_order"] for row in rows) == Counter({2: 10, 4: 20, 9: 2})
    assert rows[31]["leading_coefficient"] == "-9/128"
    assert rows[0]["leading_coefficient"] == "9/128"
    assert all(
        Fraction(rows[sheet]["leading_coefficient"])
        == Fraction(rows[sheet ^ 31]["leading_coefficient"])
        * (-1 if rows[sheet]["tau_order"] % 2 else 1)
        for sheet in range(32)
    )

    result = {
        "schema": "marici.nima.five_site.coalesced_exceptional_leading_sums.v1",
        "input": str(INPUT.relative_to(REPO)).replace("\\", "/"),
        "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "sheet_count": 32,
        "all_complete_leading_sums_nonzero": True,
        "termwise_orders_survive_complete_source_sum": True,
        "order_histogram": {
            str(order): count
            for order, count in sorted(Counter(row["tau_order"] for row in rows).items())
        },
        "distinct_leading_coefficients": sorted(
            {row["leading_coefficient"] for row in rows}
        ),
        "global_complement_character_verified": True,
        "rows": rows,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(json.dumps({
        "sha256": digest,
        "order_histogram": result["order_histogram"],
        "all_complete_leading_sums_nonzero": True,
        "distinct_leading_coefficients": result["distinct_leading_coefficients"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
