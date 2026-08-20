"""Compare direct and staged triangle-wall reductions at quotient level."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--direct", type=Path, required=True)
    parser.add_argument("--staged", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    direct = json.loads(args.direct.read_text(encoding="utf-8"))["probe_file"]
    staged = json.loads(args.staged.read_text(encoding="utf-8"))["probe_file"]
    if len(direct) != len(staged):
        raise RuntimeError("probe counts differ")
    remainder_equal = [
        left["remainder"] == right["remainder"]
        for left, right in zip(direct, staged)
    ]
    coordinate_equal = [
        left["coordinates"] == right["coordinates"]
        for left, right in zip(direct, staged)
    ]
    result = {
        "schema": "marici.triangle-wall-transition-naturality.v1",
        "probe_count": len(direct),
        "equal_remainder_rows": sum(remainder_equal),
        "different_remainder_indices": [
            index for index, equal in enumerate(remainder_equal) if not equal
        ],
        "equal_coordinate_rows": sum(coordinate_equal),
        "different_coordinate_indices": [
            index for index, equal in enumerate(coordinate_equal) if not equal
        ],
        "quotient_naturality": all(remainder_equal),
        "primitive_witness_naturality": all(coordinate_equal),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
