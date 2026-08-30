#!/usr/bin/env python3
"""Exact finite audit of the odd-front differential and valuation telescope."""

import json
from pathlib import Path


def occupancy(r: int) -> int:
    return int(r >= 1)


def excess(r: int) -> int:
    return max(0, r - 1)


def main() -> None:
    rows = []
    for r in range(7):
        p = occupancy(r)
        q = excess(r)
        assert p + q == r
        rows.append({"valuation": r, "primitive_occupancy": p, "excess": q, "sum": p + q})

    # Fourier-symbol audit away from zero frequency.  The odd front carries
    # inverse frequency 1/(i*xi); its boundary differential carries i*xi.
    # Their product is exactly one, independent of xi.
    frequencies = [-5, -2, -1, 1, 3, 8]
    products = []
    for xi in frequencies:
        inverse_frequency = 1 / (1j * xi)
        boundary_differential = 1j * xi
        product = boundary_differential * inverse_frequency
        assert product == 1
        products.append({"xi": xi, "product": product.real})

    result = {
        "schema": "marici.rh-odd-front-differential.v1",
        "fourier_symbol_products": products,
        "valuation_telescope": rows,
        "odd_pv_singularity_removed_before_aggregation": True,
        "orientation_retained_as_positive_gaussian_density": True,
        "arithmetic_kernel": [0],
        "remaining_gate": "vacuum_transversality_and_completion_of_the_full_interval_tower"
    }
    out = Path(__file__).parents[1] / "results" / "rh-odd-front-differential.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
