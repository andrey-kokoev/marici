"""Aggregate independent source-Laurent sign replications."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"
PACKETS = (
    RESULTS / "marked_extension_source_laurent_lead_prime3921.json",
    RESULTS / "marked_extension_source_laurent_lead_prime3951_v5.json",
    RESULTS / "marked_extension_source_laurent_lead_prime3951_v7.json",
)
RESULT = RESULTS / "marked_extension_source_laurent_lead.json"


def main() -> None:
    packets = [json.loads(path.read_text(encoding="utf-8")) for path in PACKETS]
    assert all(packet["status"] == "pass" for packet in packets)
    assert all(packet["held_out_polynomial_identity"] for packet in packets)
    assert all(packet["target_fixed"] for packet in packets)
    assert {packet["target_rational_reconstruction"] for packet in packets} == {"-1/8"}
    assert {packet["rank"] for packet in packets} == {655}
    assert len({packet["prime"] for packet in packets}) == 2
    assert len({packet["v"] for packet in packets}) == 2
    output = {
        "schema": "marici.benincasa.marked_extension_source_laurent_replication.v1",
        "status": "pass",
        "target": packets[0]["target"],
        "target_rational_reconstruction": "-1/8",
        "primes": sorted({packet["prime"] for packet in packets}),
        "generic_v_fibers": sorted({packet["v"] for packet in packets}),
        "ranks": sorted({packet["rank"] for packet in packets}),
        "replications": [path.name for path in PACKETS],
        "scope": "source-direct modular Laurent theorem; characteristic-zero universal identity remains a separate claim",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
