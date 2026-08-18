"""Run the certified resonant ranks through the Rust/Symbolica backend."""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPORTER = ROOT / "research/nima/export_gysin_complete_rank_matrix.py"
MANIFEST = ROOT / "research/benincasa/marici-gm/Cargo.toml"
DEFAULT_OUTPUT = ROOT / "research/nima/gysin-complete-resonant-ranks.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--degrees", type=int, nargs="+", default=[15, 17, 28, 30])
    parser.add_argument("--seed", type=lambda value: int(value, 0), default=0x243F6A8885A308D3)
    args = parser.parse_args()
    results = []
    with tempfile.TemporaryDirectory(prefix="marici-gysin-ranks-") as directory:
        temporary = Path(directory)
        for degree in args.degrees:
            matrix = temporary / f"degree-{degree}.bin"
            exported = subprocess.run(
                [
                    "python", str(EXPORTER), "--degree", str(degree),
                    "--output", str(matrix), "--seed", hex(args.seed),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            export_record = json.loads(exported.stdout.strip().splitlines()[-1])
            export_record.pop("output", None)
            solved = subprocess.run(
                [
                    "cargo", "run", "--release", "--quiet",
                    "--manifest-path", str(MANIFEST),
                    "--bin", "gysin_complete_resonant_rank",
                    "--", str(matrix),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            solve_record = json.loads(solved.stdout.strip().splitlines()[-1])
            results.append({"export": export_record, "solve": solve_record})
            print(json.dumps(results[-1], sort_keys=True))
    output = {
        "schema": "marici.nima.gysin_complete_resonant_rank_census.v1",
        "backend": "Symbolica 2.2.0 Matrix<Zp64>::solve",
        "matrix_generator": "research/nima/check_gysin_complete_pole_extension.py",
        "degrees": args.degrees,
        "sampling_seed": args.seed,
        "all_inconsistent": all(item["solve"]["outcome"] == "inconsistent" for item in results),
        "results": results,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
