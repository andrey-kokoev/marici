#!/usr/bin/env python3
"""Ideal cross-port conjunction sharing for faithful D(S3) Wilson families."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SOURCE = K / "results" / "s3-faithful-family-resource-selection.json"
OUT = K / "results" / "s3-cross-port-conjunction-sharing.json"


def family_vector(source: dict, family: str) -> dict:
    cs = ccz = 0
    conjunction_episodes = set()
    uses = {}
    for label in family:
        for power in source["ports"][label]["controlled_powers"]:
            for term in power["terms"]:
                degree = term["mask"].bit_count()
                coefficient = term["coefficient_mod8"]
                data_mask = term["mask"] & 0b111
                ladder = 0
                primitive = None
                if degree >= 2 and coefficient in {2, 6}:
                    cs += 1
                    ladder = degree - 2
                    primitive = "CS"
                elif degree >= 3 and coefficient == 4:
                    ccz += 1
                    ladder = degree - 3
                    primitive = "CCZ"
                if ladder:
                    if data_mask.bit_count() == 2:
                        conjunction_episodes.add(("pair", data_mask))
                    elif data_mask == 0b111:
                        # Choose pair 011 as the common first ladder level.
                        # It is already required independently in every
                        # faithful family. A degree-four CS then extends it to
                        # the triple predicate; a degree-four CCZ needs only
                        # the base pair.
                        conjunction_episodes.add(("pair", 0b011))
                        if coefficient in {2, 6}:
                            conjunction_episodes.add(("triple", 0b111))
                    else:
                        raise AssertionError((data_mask, ladder))
                if ladder:
                    key = f"{data_mask:03b}"
                    uses.setdefault(key, []).append({"port": label, "power": power["power"],
                                                     "primitive": primitive, "coefficient_mod8": coefficient})
    shared_pairs = len(conjunction_episodes)
    return {
        "shared_primitive_vector": [cs, ccz, shared_pairs, shared_pairs],
        "coordinates": ["CS_or_CSdagger", "CCZ", "shared_Toffoli_pair", "shared_work_episode"],
        "shared_data_conjunction_levels": [
            {"kind": kind, "data_mask": f"{mask:03b}"}
            for kind, mask in sorted(conjunction_episodes)
        ],
        "uses_by_shared_data_predicate": uses,
        "T_count_upper_bound": 3 * cs + 7 * ccz + 14 * shared_pairs,
    }


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    families = {family: family_vector(source, family) for family in source["families"]}
    assert all(record["shared_primitive_vector"][2:] == [4, 4]
               for record in families.values())
    assert families["CDFG"]["shared_primitive_vector"] == [13, 14, 4, 4]
    assert families["CDFG"]["T_count_upper_bound"] == 193
    differences = {
        family: [value - base for value, base in zip(
            record["shared_primitive_vector"], families["CDFG"]["shared_primitive_vector"])]
        for family, record in families.items() if family != "CDFG"
    }
    assert all(all(value >= 0 for value in difference) for difference in differences.values())
    old = source["families"]["CDFG"]
    result = {
        "schema": "marici.kitaev.s3-cross-port-conjunction-sharing.v1",
        "input_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "families": families,
        "CDFG_difference_table": differences,
        "CDFG_compression": {
            "T_upper_bound_before": old["T_count_upper_bound_for_controlled_powers_1_and_2"],
            "T_upper_bound_after": families["CDFG"]["T_count_upper_bound"],
            "work_episodes_before": old["total_work_block_episodes"],
            "shared_work_episodes_after": 4,
        },
        "fault_boundary": "Keeping a computed data predicate live across multiple port and power contacts can propagate one persistent predicate fault into several pointer blocks or repeatedly into one pointer block. Algebraic sharing is exact, but one-fault-safe sharing requires a new contact-order and hygiene audit; the five-episode count is not yet an exRec resource count.",
        "verdict": "Ideal cross-port predicate sharing compresses every family to four conjunction episodes: three pair predicates and one triple extension reusing a pair. CDFG improves from 361T to a 193T upper bound and from 16 to four ideal shared work episodes, while remaining componentwise minimal. The family selection survives this structural compiler change, but the shared-predicate fault contract is unresolved.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
