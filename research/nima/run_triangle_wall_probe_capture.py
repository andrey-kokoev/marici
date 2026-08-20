"""Run the Rust triangle-wall reducer and durably capture its JSON output."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exe", type=Path, required=True)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args, forwarded = parser.parse_known_args()

    command = [str(args.exe), str(args.packet), *forwarded]
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(completed.stdout)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "schema": "marici.triangle-wall-probe-capture.v1",
                "command": command,
                "captured_schema": payload.get("schema"),
                "probe_count": payload.get("probe_count"),
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
