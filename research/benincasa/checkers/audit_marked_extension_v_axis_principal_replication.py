#!/usr/bin/env python3
"""Aggregate source-direct v-axis Laurent replications."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"
INPUTS = [
    RESULTS / "marked_extension_source_laurent_v_axis_v5.json",
    RESULTS / "marked_extension_source_laurent_v_axis_v7.json",
]
OUTPUT = RESULTS / "marked_extension_source_laurent_v_axis_replication.json"


def main() -> None:
    packets = [json.loads(path.read_text(encoding="utf-8")) for path in INPUTS]
    assert {packet["v"] for packet in packets} == {5, 7}
    assert {packet["rank"] for packet in packets} == {655}
    assert all(packet["held_out_polynomial_identity"] for packet in packets)
    assert all(packet["derivative_axis"] == "v" for packet in packets)
    assert all(not packet["target_fixed"] for packet in packets)
    zero = [["0", "0", "0"]] * 3
    assert all(packet["fixed_u_minus_1_matrix"][1:] == zero for packet in packets)
    assert all(packet["fixed_u_minus_1_matrix"][0] == [None, None, None] for packet in packets)
    assert all(
        packet["fixed_u_minus_2_matrix"] == [["0", "0", "0"]] * 4
        for packet in packets
    )

    output = {
        "schema": "marici.benincasa.marked_extension_source_laurent_v_axis_replication.v1",
        "status": "pass",
        "primes": sorted({packet["prime"] for packet in packets}),
        "generic_v_fibers": sorted({packet["v"] for packet in packets}),
        "ranks": sorted({packet["rank"] for packet in packets}),
        "source_result": {
            "u_minus_2_block": "zero",
            "u_minus_1_rows_e7_e8_e9": "zero",
            "u_minus_1_e6_row": "unfixed in all three quotient columns",
        },
        "candidate_e6_q0_value": "1/(4*v*(v-2))",
        "candidate_status": "one triangular splitting choice, not a fixed principal coordinate",
        "consequence": "the quotient Beck-Chevalley observer has no canonical principal lift through B_v into the final four-master block",
        "new_carrier_datum": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
