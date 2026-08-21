#!/usr/bin/env python3
"""Audit positive-real poles of all 32 coalesced five-site deck sheets."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import sympy as sp


REPO = Path(__file__).resolve().parents[2]
INPUT = REPO / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUTPUT = REPO / "research/nima/results/five-site-deck-continued-period-poles.json"
RHO = sp.symbols("rho")


def edge_sign(sheet: int, edge: int) -> int:
    return -1 if sheet & (1 << (edge - 1)) else 1


def cut_support(label: str) -> list[int]:
    sites = {int(char) for char in label.removeprefix("g_")}
    return [
        edge
        for edge in range(1, 6)
        if ((edge in sites) != (((edge % 5) + 1) in sites))
    ]


def denominator(label: str, sheet: int) -> sp.Expr:
    if label == "G":
        return sp.Integer(5)
    if label.startswith("G_minus_e"):
        edge = int(label.removeprefix("G_minus_e")[0])
        return 1 + 2 * edge_sign(sheet, edge) * RHO
    assert label.startswith("g_"), label
    size = len(label.removeprefix("g_"))
    slope = sum(edge_sign(sheet, edge) for edge in cut_support(label))
    return size + slope * RHO


def positive_poles(expression: sp.Expr) -> list[dict[str, object]]:
    numerator, denominator_poly = map(sp.factor, sp.cancel(expression).as_numer_denom())
    rows = []
    for factor, denominator_order in sp.factor_list(denominator_poly)[1]:
        polynomial = sp.Poly(factor, RHO)
        if polynomial.degree() != 1:
            continue
        root = -polynomial.nth(0) / polynomial.nth(1)
        if not (root.is_Rational and root > 0):
            continue
        numerator_order = 0
        residual = numerator
        while sp.rem(sp.Poly(residual, RHO), polynomial).is_zero:
            residual = sp.cancel(residual / factor)
            numerator_order += 1
        order = denominator_order - numerator_order
        if order > 0:
            rows.append({"rho": str(root), "order": int(order)})
    return sorted(rows, key=lambda row: sp.Rational(row["rho"]))


def main() -> None:
    packet = json.loads(INPUT.read_text(encoding="utf-8"))["five_cycle"]
    common = packet["common_prefactor"]
    terms = packet["terms"]
    rows = []
    for sheet in range(32):
        common_denominator = sp.prod(denominator(label, sheet) for label in common)
        term_sum = sum(
            1 / sp.prod(denominator(label, sheet) for label in term)
            for term in terms
        )
        integrand = sp.cancel(RHO**2 * term_sum / common_denominator)
        poles = positive_poles(integrand)
        rows.append(
            {
                "sheet": sheet,
                "hamming_weight": sheet.bit_count(),
                "positive_real_poles": poles,
                "positive_ray_regular": not poles,
            }
        )

    regular = [row["sheet"] for row in rows if row["positive_ray_regular"]]
    assert regular == [0]
    assert rows[31]["positive_real_poles"]
    assert all(
        rows[sheet]["positive_ray_regular"] != rows[sheet ^ 31]["positive_ray_regular"]
        or (not rows[sheet]["positive_ray_regular"])
        for sheet in range(32)
    )
    pole_histogram = Counter(
        (pole["rho"], pole["order"])
        for row in rows
        for pole in row["positive_real_poles"]
    )
    result = {
        "schema": "marici.nima.five_site.deck_continued_period_poles.v1",
        "input": str(INPUT.relative_to(REPO)).replace("\\", "/"),
        "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "sheet_count": 32,
        "positive_ray_regular_sheets": regular,
        "positive_ray_singular_sheet_count": 31,
        "pole_histogram": [
            {"rho": rho, "order": int(order), "sheet_count": count}
            for (rho, order), count in sorted(
                pole_histogram.items(), key=lambda item: (sp.Rational(item[0][0]), item[0][1])
            )
        ],
        "rows": rows,
        "conclusion": (
            "Only the source-positive sheet defines an ordinary integral on rho in [0,infinity). "
            "Every nontrivial deck continuation meets an uncancelled positive-real pole, so its "
            "scalar period requires an independently specified contour or i-epsilon continuation."
        ),
        "scope": (
            "Exact characteristic-zero pole audit of the complete 180-term coalesced source "
            "integrand. It does not choose a contour around any pole and therefore does not "
            "assign scalar periods to the 31 continued chambers."
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
                "regular_sheets": regular,
                "singular_sheet_count": 31,
                "distinct_pole_types": len(pole_histogram),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
