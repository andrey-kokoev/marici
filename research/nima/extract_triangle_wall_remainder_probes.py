"""Extract sparse remainder rows from a captured triangle-wall reducer result."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    packet = json.loads(args.input.read_text(encoding="utf-8"))
    probes = packet["probe_file"]
    lines = [
        ",".join(f"{column}:{value}" for column, value in probe["remainder"])
        for probe in probes
    ]
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "schema": "marici.triangle-wall-remainder-probes.v1",
                "probe_count": len(lines),
                "nonzero_remainders": sum(bool(line) for line in lines),
                "term_count": sum(len(probe["remainder"]) for probe in probes),
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
