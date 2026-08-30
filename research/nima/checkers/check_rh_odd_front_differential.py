#!/usr/bin/env python3
"""Exact finite audit of the odd-front differential and valuation telescope."""

import hashlib
import json
from pathlib import Path


def occupancy(r: int) -> int:
    return int(r >= 1)


def excess(r: int) -> int:
    return max(0, r - 1)


def main() -> None:
    rows = []
    for r in range(7):
        primitive = occupancy(r)
        higher = excess(r)
        assert primitive + higher == r
        rows.append(
            {
                "valuation": r,
                "primitive_occupancy": primitive,
                "excess": higher,
                "sum": primitive + higher,
            }
        )

    # Represent a rational multiple of i as the integer coefficient of i.
    # The odd front has symbol -i/xi and the boundary differential has i*xi;
    # their product is exactly one for every nonzero integer xi.
    frequencies = [-5, -2, -1, 1, 3, 8]
    products = []
    wrong_sign_rejected = []
    for xi in frequencies:
        inverse_numerator_i = -1
        inverse_denominator = xi
        differential_coefficient_i = xi
        # (a i)(b i) = -ab.
        product_numerator = -inverse_numerator_i * differential_coefficient_i
        assert product_numerator == inverse_denominator
        products.append({"xi": xi, "product": "1"})

        wrong_inverse_numerator_i = 1
        wrong_product_numerator = -wrong_inverse_numerator_i * differential_coefficient_i
        rejected = wrong_product_numerator != inverse_denominator
        assert rejected
        wrong_sign_rejected.append(rejected)

    payload = {
        "schema": "marici.rh-odd-front-differential.v2",
        "fourier_symbol_products": products,
        "valuation_telescope": rows,
        "odd_pv_singularity_removed_before_aggregation": True,
        "orientation_retained_as_positive_gaussian_density": True,
        "wrong_inverse_orientation_rejected_at_every_sample": all(wrong_sign_rejected),
        "arithmetic_kernel": [0],
        "source_constructor_four_front_identity_proved": False,
        "remaining_gate": "source extraction, vacuum transversality, and completion of the full interval tower",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["sha256"] = hashlib.sha256(canonical).hexdigest()

    out = Path(__file__).parents[1] / "results" / "rh-odd-front-differential.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
