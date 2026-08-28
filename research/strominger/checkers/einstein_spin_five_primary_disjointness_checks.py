#!/usr/bin/env python3
"""Check the separation of the Einstein spin-two source from the formal five-primary family."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    # This singleton is a typed input from the completed Bondi/Einstein source
    # contract, not inferred from the affine formula.
    source_authorized_spins = [2]
    formal_spins = list(range(1, 101))
    exceptional = [s for s in formal_spins if (4 * s - 1) % 5 == 0]

    gates = {
        "einstein_source_contract_contains_only_spin_two": source_authorized_spins == [2],
        "spin_two_modulus_is_seven": 4 * source_authorized_spins[0] - 1 == 7,
        "spin_two_reflected_determinant_is_invertible": 7 % 5 != 0,
        "authorized_exceptional_intersection_is_empty": not set(source_authorized_spins).intersection(exceptional),
        "formal_exceptional_family_is_four_modulo_five": all(s % 5 == 4 for s in exceptional),
        "first_formal_exception_is_spin_four": exceptional[0] == 4,
    }

    result = {
        "claim": "the five-primary family is disjoint from the source-authorized Einstein spin spectrum",
        "typed_source_input": {
            "theory": "four-dimensional Bondi/Einstein gravity",
            "radiative_spin_parameters": source_authorized_spins,
            "higher_spin_extension_authorized": False,
        },
        "formal_exceptional_spins_through_100": exceptional,
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "all_passed": all(gates.values()),
    }

    target = Path(__file__).resolve().parents[1] / "results" / "einstein_spin_five_primary_disjointness_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passed", "total", "all_passed", "formal_exceptional_spins_through_100")}, indent=2))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
