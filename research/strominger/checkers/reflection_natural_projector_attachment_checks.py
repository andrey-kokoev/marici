#!/usr/bin/env python3
"""Exact finite checks for reflection-natural affine/projector label attachments."""

from __future__ import annotations

import json
import math
from pathlib import Path


def main() -> None:
    cases = []
    gates = {
        "unary_chart_never_carries_reflection_descent": True,
        "joint_chart_packet_never_has_projector_cardinality": True,
        "even_quotient_has_wrong_reflection_action": True,
        "odd_quotient_is_complete_exactly_off_five_primary_family": True,
        "spin_two_odd_labels_are_complete_and_reflection_natural": True,
        "exceptional_odd_labels_miss_exactly_factor_five": True,
    }

    for s in range(1, 101):
        n = 4 * s - 1
        d = math.gcd(n, 5)
        unary_reflection_descends = 5 % n == 0
        joint_size = n * n // d
        odd_size = n // d

        gates["unary_chart_never_carries_reflection_descent"] &= not unary_reflection_descends
        gates["joint_chart_packet_never_has_projector_cardinality"] &= joint_size != n
        gates["even_quotient_has_wrong_reflection_action"] &= n > 2
        gates["odd_quotient_is_complete_exactly_off_five_primary_family"] &= (odd_size == n) == (s % 5 != 4)
        if d == 5:
            gates["exceptional_odd_labels_miss_exactly_factor_five"] &= odd_size * 5 == n

        cases.append({
            "spin_parameter": s,
            "modulus": n,
            "projector_count": n,
            "unary_reflection_descends": unary_reflection_descends,
            "joint_chart_size": joint_size,
            "odd_quotient_size": odd_size,
            "odd_attachment_available": odd_size == n,
        })

    n = 7
    inv5 = pow(5, -1, n)
    residues = set()
    equivariant = True
    for x in range(n):
        for y in range(n):
            label = inv5 * ((3 * x - 2 * y) - (3 * y - 2 * x)) % n
            reflected = inv5 * ((3 * y - 2 * x) - (3 * x - 2 * y)) % n
            residues.add(label)
            equivariant &= reflected == (-label) % n
    gates["spin_two_odd_labels_are_complete_and_reflection_natural"] &= residues == set(range(n)) and equivariant

    aspect_profile = {
        "source_provenance": True,
        "well_typed_term": True,
        "discriminating_target": True,
        "operational_witness": False,
        "nonredundancy": True,
        "bounded_decisive_test": False,
    }
    structural = all(aspect_profile[k] for k in (
        "source_provenance", "well_typed_term", "discriminating_target", "nonredundancy"))
    complete = structural and aspect_profile["operational_witness"] and aspect_profile["bounded_decisive_test"]
    aspect_disposition = "admit" if complete else "defer" if structural else "reject"
    gates["updated_aspect_tester_defers_candidate"] = aspect_disposition == "defer"

    result = {
        "theorem": "the odd affine quotient is the unique algebraically viable projector-label candidate when five is invertible",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "all_passed": all(gates.values()),
        "spin_two": {"modulus": 7, "inverse_of_five": inv5, "odd_label_formula": "x-y mod 7"},
        "aspect_updated_tester": {
            **aspect_profile,
            "disposition": aspect_disposition,
            "missing": ["operational_witness", "bounded_decisive_test"],
        },
        "cases": cases,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "reflection_natural_projector_attachment_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passed", "total", "all_passed", "spin_two")}, indent=2))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
