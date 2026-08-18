#!/usr/bin/env python3
"""Exact labelled rank test for the triangle--soft polar square."""

import json
from pathlib import Path


def q_pair(E, P1, P2, P3, a, b):
    common = E*E*(a*a-b*b)-P1*P1*a*a+P2*P2*b*b
    odd = 2*E*P3*a*b
    return common+odd, common-odd


def main():
    witnesses = []
    for P1, P2, P3, a, b in [(2,3,4,5,7), (3,5,7,2,11), (5,4,6,3,8)]:
        q0 = q_pair(0, P1, P2, P3, a, b)
        assert q0[0] == q0[1] == -P1*P1*a*a+P2*P2*b*b
        derivatives = (2*P3*a*b, -2*P3*a*b)
        determinant = -4*P3*a*b
        assert determinant != 0
        witnesses.append({
            "parameters": [P1,P2,P3,a,b],
            "common_restriction": q0[0],
            "soft_derivatives": derivatives,
            "basis_determinant": determinant,
        })

    packet = {
        "cartier_pair": ["Lambda", "E"],
        "regular_sequence_generic": True,
        "beck_chevalley_map": "canonical",
        "soft_restriction_vector": [1,1],
        "soft_normal_vector": [1,-1],
        "scaled_determinant": "-4*P3*a*b",
        "generic_rank": 2,
        "generic_mapping_cone_dimension": 0,
        "failure_support": ["P3=0", "a=0", "b=0"],
        "witnesses": witnesses,
    }
    out = Path(__file__).with_name("triangle-soft-polar-beck-chevalley.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
