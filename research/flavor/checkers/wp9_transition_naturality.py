"""Audit prerequisites for a WP9 hierarchy-flow chart-transition test.

The WP8 ``fiber`` is tolerance-selected: its members need not be exactly the
same weak-basis quotient point.  Consequently this checker may compare loop
readouts and chartwise flows, but it must not manufacture a chart-transition
map or call their difference a naturality obstruction.  Exact physical-point
identity (or an independently derived transition) is a prerequisite.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path


SOURCE = Path("research/flavor/results/wp9_lo_atlas.json")
OUTPUT = Path("research/flavor/results/wp9_transition_naturality.json")
ANGLES = ("alpha", "beta", "gamma")
BASE_TOL = 1.0e-6
FLOW_TOL = 1.0e-3


def circular_distance(left: float, right: float) -> float:
    return abs(math.atan2(math.sin(left - right), math.cos(left - right)))


def pairwise_spread(values: list[float], *, circular: bool = False) -> float:
    distance = circular_distance if circular else lambda a, b: abs(a - b)
    return max(
        (distance(left, right) for i, left in enumerate(values) for right in values[i + 1 :]),
        default=0.0,
    )


def main() -> None:
    packet = json.loads(SOURCE.read_text(encoding="utf-8"))
    groups: dict[float, list[dict]] = defaultdict(list)
    for flow in packet["tau_flows"]:
        groups[float(flow["core"])].append(flow)

    records = []
    for core, flows in sorted(groups.items()):
        if len(flows) < 2:
            continue
        common_tau = sorted(
            set.intersection(
                *(
                    set(flow["flow"]["alpha"]["tau"])
                    for flow in flows
                )
            )
        )
        spreads = {}
        for tau in common_tau:
            channel = {}
            for angle in ANGLES:
                wobble = []
                constants = []
                for flow in flows:
                    series = flow["flow"][angle]
                    index = series["tau"].index(tau)
                    wobble.append(float(series["wobble"][index]))
                    constants.append(float(series["c"][index]))
                channel[angle] = {
                    "wobble_spread": pairwise_spread(wobble),
                    "constant_phase_spread": pairwise_spread(constants, circular=True),
                }
            spreads[str(tau)] = channel

        base_spread = max(
            value
            for channel in spreads.get("1.0", {}).values()
            for value in channel.values()
        )
        later_spread = max(
            (
                value
                for tau, channel in spreads.items()
                if tau != "1.0"
                for fields in channel.values()
                for value in fields.values()
            ),
            default=0.0,
        )
        convergence_states = sorted({bool(flow["converged"]) for flow in flows})
        records.append(
            {
                "core": core,
                "orbits": sorted(flow["orbit"] for flow in flows),
                "common_tau": common_tau,
                "base_spread": base_spread,
                "later_spread": later_spread,
                "base_loop_readout_agrees": base_spread < BASE_TOL,
                "later_flow_readout_agrees": later_spread < FLOW_TOL,
                "mixed_convergence": len(convergence_states) > 1,
                "spreads": spreads,
            }
        )

    mixed = [record for record in records if record["mixed_convergence"]]
    tests = {
        "T1_repeated_cores_share_base_loop_readout": all(
            record["base_loop_readout_agrees"] for record in records
        ),
        "T2_mixed_cores_exist": bool(mixed),
        "T3_mixed_core_later_flow_readouts_diverge": all(
            not record["later_flow_readout_agrees"] for record in mixed
        ),
        "T4_mixed_cores_are_exactly_wp9_pair": {
            round(record["core"], 6) for record in mixed
        }
        == {0.819271, 1.566129},
    }
    output = {
        "schema": "marici.flavor.wp9-transition-naturality.v1",
        "source": str(SOURCE),
        "tolerances": {"base": BASE_TOL, "flow": FLOW_TOL},
        "tests": tests,
        "verdict": (
            "Repeated-core loop readouts agree at tau=1 and diverge later, "
            "but the tolerance-selected points are not certified identical "
            "physical points.  No chart-transition naturality verdict is "
            "typed without an exact quotient identification."
        ),
        "records": records,
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"tests": tests, "mixed": mixed}, indent=2))
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
