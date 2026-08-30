#!/usr/bin/env python3
"""Show that equal Koszul rank data can carry different labelled support."""

import json
from math import gcd
from pathlib import Path


# Each affine form is ((a,b) coefficients, (x,y,z) constant coefficients).
FORMS = {
    "g1": ((0, 1), (0, -1, -1)),
    "g2": ((1, 0), (-1, 0, -1)),
    "g3": ((1, 1), (0, 0, 1)),
    "g12": ((1, 1), (1, 1, 0)),
    "g23": ((0, 1), (-1, 0, 0)),
    "g31": ((1, 0), (0, -1, 0)),
}

PACKETS = {
    "vertex_triple": ("g1", "g2", "g3"),
    "complementary_triple": ("g23", "g31", "g12"),
}


def rank2(columns):
    return 2 if any(
        left[0] * right[1] - left[1] * right[0]
        for i, left in enumerate(columns)
        for right in columns[i + 1:]
    ) else 1


def primitive(vector):
    divisor = 0
    for value in vector:
        divisor = gcd(divisor, abs(value))
    vector = tuple(value // divisor for value in vector)
    first = next(value for value in vector if value)
    return tuple(-value for value in vector) if first < 0 else vector


def support(packet):
    # Both packets have the source-labelled relation third - second - first.
    constants = [FORMS[label][1] for label in packet]
    raw = tuple(constants[2][i] - constants[1][i] - constants[0][i] for i in range(3))
    return raw, primitive(raw)


def main():
    records = {}
    for name, packet in PACKETS.items():
        columns = [FORMS[label][0] for label in packet]
        raw, reduced = support(packet)
        records[name] = {
            "labels": list(packet),
            "marked_count": 3,
            "incidence_rank": rank2(columns),
            "incidence_nullity": 3 - rank2(columns),
            "primitive_kernel_coordinates": [-1, -1, 1],
            "raw_external_support_coefficients_xyz": list(raw),
            "primitive_external_support_coefficients_xyz": list(reduced),
        }

    left, right = records.values()
    checks = {
        "same_abstract_marked_count": left["marked_count"] == right["marked_count"] == 3,
        "same_abstract_incidence_rank": left["incidence_rank"] == right["incidence_rank"] == 2,
        "same_abstract_nullity": left["incidence_nullity"] == right["incidence_nullity"] == 1,
        "same_abstract_kernel_coordinates": left["primitive_kernel_coordinates"] == right["primitive_kernel_coordinates"],
        "different_labelled_support_divisors": left["primitive_external_support_coefficients_xyz"] != right["primitive_external_support_coefficients_xyz"],
        "expected_vertex_support": left["primitive_external_support_coefficients_xyz"] == [1, 1, 3],
        "expected_complementary_support": right["primitive_external_support_coefficients_xyz"] == [1, 1, 0],
    }
    result = {
        "schema": "marici.equal-rank-occurrence-support-discriminator.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "packets": records,
        "conclusion": "abstract Koszul rank data agrees, but occurrence-labelled affine incidence distinguishes support x+y+3z from x+y",
        "checks": checks,
    }
    output = Path(__file__).with_name("equal-rank-occurrence-support-discriminator.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
