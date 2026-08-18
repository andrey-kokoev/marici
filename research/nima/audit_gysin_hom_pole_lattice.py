"""Exact factor audit of the Gysin Hom operator and extension cocycle."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research/benincasa"))
from check_gysin_occurrence_covariance import (  # noqa: E402
    clean_poly,
    poly_from_terms,
    valuation,
)

INPUT = ROOT / "research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
OUTPUT = ROOT / "research/nima/gysin-hom-pole-lattice-audit.json"


def source_factors(prime: int):
    half = pow(2, prime - 2, prime)
    quarter = pow(4, prime - 2, prime)
    one = {(0, 0): 1}
    y = {(1, 0): half, (0, 1): half, (0, 0): prime - 1}

    def combine(*terms):
        result = {}
        for scale, polynomial in terms:
            for exponent, coefficient in polynomial.items():
                result[exponent] = (result.get(exponent, 0) + scale * coefficient) % prime
        return clean_poly(result, prime)

    declared = [
        ("u", {(1, 0): 1}),
        ("v", {(0, 1): 1}),
        ("y", y),
        ("1-y", combine((1, one), (-1, y))),
        ("1+y", combine((1, one), (1, y))),
        ("v-u", {(0, 1): 1, (1, 0): prime - 1}),
        ("y-u^2", combine((1, y), (-1, {(2, 0): 1}))),
        ("y+u^2", combine((1, y), (1, {(2, 0): 1}))),
        ("P6", clean_poly({
            (0, 0): 1, (1, 0): -1, (0, 1): -1,
            (0, 2): quarter, (1, 1): half, (2, 0): -7 * quarter,
            (2, 1): 1, (3, 0): 1, (3, 1): -1, (4, 0): 1,
        }, prime)),
    ]
    residual = [
        ("u-2", {(1, 0): 1, (0, 0): prime - 2}),
        ("v-2", {(0, 1): 1, (0, 0): prime - 2}),
        ("u^2+1", {(2, 0): 1, (0, 0): 1}),
    ]
    return declared, residual


def in_hom_operator(item: dict) -> bool:
    row, column = item["row"], item["col"]
    return (
        (row < 2 and column < 2)
        or (row >= 2 and column >= 2)
        or (row >= 2 and column < 2)
    )


def main() -> None:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    declared, residual = source_factors(prime)
    factors = declared + residual
    maxima = {name: 0 for name, _ in factors}
    entries = []
    for item in payload["entries"]:
        if not in_hom_operator(item):
            continue
        numerator = poly_from_terms(item["fit"]["numerator"], prime)
        remainder = poly_from_terms(item["fit"]["denominator"], prime)
        net = {}
        raw_denominator = {}
        numerator_orders = {}
        for name, factor in factors:
            denominator_order, remainder = valuation(remainder, factor, prime)
            numerator_order, _ = valuation(numerator, factor, prime)
            order = max(denominator_order - numerator_order, 0)
            raw_denominator[name] = denominator_order
            numerator_orders[name] = numerator_order
            net[name] = order
            maxima[name] = max(maxima[name], order)
        residual_is_unit = not remainder or all(exponent == (0, 0) for exponent in remainder)
        entries.append({
            "axis": item["axis"],
            "row": item["row"],
            "col": item["col"],
            "block": (
                "T" if item["row"] < 2 else
                "E" if item["col"] >= 2 else
                "C"
            ),
            "raw_denominator_orders": raw_denominator,
            "numerator_orders": numerator_orders,
            "net_pole_orders": net,
            "residual_is_unit": residual_is_unit,
            "residual_terms": [[du, dv, coefficient] for (du, dv), coefficient in sorted(remainder.items())],
        })
    result = {
        "schema": "marici.nima.gysin_hom_pole_lattice_audit.v1",
        "prime": prime,
        "connection_source": str(INPUT.relative_to(ROOT)).replace("\\", "/"),
        "audited_blocks": ["A_T", "A_E", "C"],
        "declared_factor_order": [name for name, _ in declared],
        "additional_factor_order": [name for name, _ in residual],
        "complete_factor_order": list(maxima),
        "componentwise_maximum": [maxima[name] for name in maxima],
        "componentwise_maximum_by_name": maxima,
        "all_residual_denominators_units": all(item["residual_is_unit"] for item in entries),
        "entries": entries,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "entry_count": len(entries),
        "componentwise_maximum": result["componentwise_maximum"],
        "all_residual_denominators_units": result["all_residual_denominators_units"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
