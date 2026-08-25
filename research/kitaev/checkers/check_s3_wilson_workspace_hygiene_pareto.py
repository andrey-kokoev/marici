#!/usr/bin/env python3
"""Exact workspace-footprint versus hygiene Pareto frontier."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SOURCE = K / "results" / "s3-wilson-phase-native-compression.json"
HYGIENE = K / "results" / "s3-wilson-work-ancilla-hygiene.json"
OUT = K / "results" / "s3-wilson-workspace-hygiene-pareto.json"


def exhaustive_frontier(demands: list[int]) -> list[dict]:
    uses = [(gadget, slot) for gadget, demand in enumerate(demands)
            for slot in range(demand)]
    total = len(uses)
    peak = max(demands, default=0)
    frontier = []
    for provisioned in range(peak, total + 1):
        best = None
        witness = None
        # Assign every simultaneous use to a physical block; blocks used by
        # the same gadget must be distinct. A hygiene event is required before
        # every use of a block after its first use because all gadgets overlap
        # on the controlled data block.
        for assignment in itertools.product(range(provisioned), repeat=total):
            valid = True
            offset = 0
            for demand in demands:
                if len(set(assignment[offset:offset + demand])) != demand:
                    valid = False
                    break
                offset += demand
            if not valid or len(set(assignment)) < provisioned:
                continue
            barriers = total - len(set(assignment))
            if best is None or barriers < best:
                best = barriers
                witness = list(assignment)
        assert best == total - provisioned
        frontier.append({
            "provisioned_verified_work_blocks": provisioned,
            "minimum_hygiene_events": best,
            "assignment_witness": witness,
        })
    return frontier


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    hygiene = json.loads(HYGIENE.read_text(encoding="utf-8"))
    controlled = {}
    for label, record in source["controlled"].items():
        demands = [term["clean_ancillas"] for term in record["terms"]
                   if term["clean_ancillas"] > 0]
        total = sum(demands)
        peak = max(demands, default=0)
        frontier = exhaustive_frontier(demands)
        serial_point = frontier[0] if frontier else {
            "provisioned_verified_work_blocks": 0,
            "minimum_hygiene_events": 0,
            "assignment_witness": [],
        }
        assert serial_point["minimum_hygiene_events"] == hygiene["controlled"][label]["minimum_inter_gadget_hygiene_barriers"]
        controlled[label] = {
            "per_gadget_work_block_demands": demands,
            "total_work_block_episodes": total,
            "minimum_simultaneous_work_blocks": peak,
            "pareto_frontier": frontier,
            "law": "minimum_hygiene_events = total_work_block_episodes - provisioned_verified_work_blocks",
        }

    assert controlled["H"]["per_gadget_work_block_demands"] == [1, 1, 1, 2]
    assert [(p["provisioned_verified_work_blocks"], p["minimum_hygiene_events"])
            for p in controlled["H"]["pareto_frontier"]] == [(2, 3), (3, 2), (4, 1), (5, 0)]
    result = {
        "schema": "marici.kitaev.s3-wilson-workspace-hygiene-pareto.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (SOURCE, HYGIENE)
        },
        "controlled": controlled,
        "theorem": "When every work-using gadget overlaps on one data block, each physical work block needs hygiene before every use after its first. For U total work-block episodes and P provisioned verified blocks, exhaustive assignment gives B_min=U-P for peak_demand<=P<=U.",
        "physical_boundary": "The frontier counts verified work-block identities and hygiene events but assigns neither a time nor failure probability to them. It is a schedule-independent resource relation, not a physical optimum.",
        "verdict": "The serial-versus-fresh choice is a complete discrete Pareto line rather than a binary alternative. For controlled H the exact points are (work blocks, hygiene events)=(2,3),(3,2),(4,1),(5,0). Factory and lifecycle costs are still required to choose among them.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
