"""Export an authoritative complete-pole splitting matrix for Rust/Symbolica."""

from __future__ import annotations

import argparse
import json
import struct
from pathlib import Path

import check_gysin_complete_pole_extension as checker


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--degree", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=lambda value: int(value, 0), default=0x243F6A8885A308D3)
    args = parser.parse_args()
    payload = json.loads(checker.DEFAULT_INPUT.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    entries = {(item["axis"], item["row"], item["col"]): item["fit"] for item in payload["entries"]}
    declared, additional = checker.source_factors(prime)
    matrix, unknowns, accepted = checker.census(
        entries,
        declared + additional,
        prime,
        checker.COMPLETE_VECTOR,
        args.degree,
        args.seed,
        return_matrix=True,
    )
    rows = len(matrix)
    columns = unknowns + 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("wb") as stream:
        stream.write(b"MGSRANK1")
        stream.write(struct.pack("<QQQQQ", prime, rows, columns, unknowns, args.degree))
        for row in matrix:
            stream.write(struct.pack(f"<{columns}Q", *row))
    print(json.dumps({
        "degree": args.degree,
        "prime": prime,
        "rows": rows,
        "columns": columns,
        "unknowns": unknowns,
        "sample_points": accepted,
        "output": str(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
