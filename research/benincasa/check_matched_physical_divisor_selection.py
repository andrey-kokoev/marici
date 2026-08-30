#!/usr/bin/env python3
"""Matched visible/invisible divisor test on the weighted X1-soft current."""

import json
from pathlib import Path


def main():
    # Source-derived exceptional current: Gamma_xi=[-1,1], oriented increasingly.
    endpoints = (-1, 1)
    boundary_coefficients = {-1: -1, 1: 1}

    # After removing the common X1 normal:
    # q_g1/X1 = xi+1, while q_g23|_{X1=0}=2p with p>0.
    q_g1_values = {xi: xi + 1 for xi in endpoints}
    p = 1  # Any positive p has the same support incidence.
    q_g23_values = {xi: 2 * p for xi in endpoints}

    g1_zeros = [xi for xi, value in q_g1_values.items() if value == 0]
    g23_zeros = [xi for xi, value in q_g23_values.items() if value == 0]
    g1_pairing = sum(boundary_coefficients[xi] for xi in g1_zeros)
    g23_pairing = sum(boundary_coefficients[xi] for xi in g23_zeros)

    checks = {
        "same_oriented_chain_used_for_both_divisors": endpoints == (-1, 1),
        "q_g1_is_negative_endpoint_support": g1_zeros == [-1],
        "q_g1_boundary_pairing_is_nonzero": g1_pairing == -1,
        "q_g23_is_a_unit_on_the_exceptional_chain": g23_zeros == [],
        "q_g23_boundary_pairing_is_zero": g23_pairing == 0,
    }
    result = {
        "schema": "marici.matched-physical-divisor-selection.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_chart": "weighted X1-soft q_G12 residue current",
        "physical_chain": "Gamma_xi=[-1,1] with boundary [1]-[-1]",
        "visible_packet": {
            "divisor": "q_g1",
            "exceptional_equation": "xi+1",
            "boundary_support": [-1],
            "oriented_chain_pairing": g1_pairing,
        },
        "invisible_packet": {
            "divisor": "q_g23",
            "exceptional_equation": "2p",
            "condition": "p>0",
            "boundary_support": [],
            "oriented_chain_pairing": g23_pairing,
        },
        "selection_law": "the same source-derived boundary map selects the marked divisor met by the physical chain and kills the divisor that is a unit on that chain",
        "checks": checks,
    }
    output = Path(__file__).with_name("matched-physical-divisor-selection.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
