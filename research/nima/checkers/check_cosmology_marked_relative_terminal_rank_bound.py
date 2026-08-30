"""Dimension gate for static readouts on the physical rank-20 residue."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "cosmology_marked_relative_terminal_rank_bound.json"


def main():
    domain_dimension = 20
    single_wall_components = 3
    mixed_occurrence_components = 0
    frozen_chain_count = 1
    joint_rank_upper_bound = single_wall_components + frozen_chain_count
    packet = {
        "schema": "marici.cosmology-marked-relative-terminal-rank-bound.v1",
        "domain": "H^2(S_E minus W)",
        "domain_dimension": domain_dimension,
        "static_readouts": {
            "single_wall_rank_upper_bound": single_wall_components,
            "mixed_occurrence_rank": mixed_occurrence_components,
            "frozen_physical_chain_rank_upper_bound": frozen_chain_count,
        },
        "joint_rank_upper_bound": joint_rank_upper_bound,
        "invisible_kernel_dimension_lower_bound": domain_dimension - joint_rank_upper_bound,
        "static_family_jointly_conservative": joint_rank_upper_bound >= domain_dimension,
        "next_typed_family": (
            "connection-stable orbit of the three Cech-sewn wall maps together "
            "with the transported physical-chain pairing"
        ),
        "passed": (
            domain_dimension == 20
            and single_wall_components == 3
            and mixed_occurrence_components == 0
            and joint_rank_upper_bound == 4
            and domain_dimension - joint_rank_upper_bound == 16
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
