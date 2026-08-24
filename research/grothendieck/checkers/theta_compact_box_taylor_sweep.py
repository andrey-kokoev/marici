"""Resumable adaptive sweep for the 64 compact logarithmic boxes."""

import argparse
import json
from pathlib import Path

from theta_compact_box_taylor_interval import D, evaluate_box


ROOT = Path(__file__).parents[1]
SCAN = ROOT / "results" / "theta-outer-schwarzian-scan.json"
OUTPUT = ROOT / "results" / "theta-compact-boxes" / "adaptive-sweep"
LADDER = ((2, 250), (4, 500), (6, 1000))


def run(start, stop, start_tier=0):
    scan = json.loads(SCAN.read_text(encoding="utf-8"))
    boxes = scan["compact_bridge_reconnaissance"][
        "inflated_derivative_box_budget"
    ]["boxes"]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    summary = []
    for index in range(start, min(stop, len(boxes))):
        lo, hi = boxes[index]["interval"]
        certified = False
        attempts = []
        for degree, steps in LADDER[start_tier:]:
            path = OUTPUT / f"box-{index:02d}-d{degree}-s{steps}.json"
            if path.exists():
                result = json.loads(path.read_text(encoding="utf-8"))
            else:
                result = evaluate_box(D(str(lo)), D(str(hi)), steps, degree)
                path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
            attempts.append({
                "degree": degree,
                "steps": steps,
                "lower_bound": result["schwarzian_numerator"][0],
                "certified": result["box_numerator_strictly_positive"],
            })
            if result["box_numerator_strictly_positive"]:
                certified = True
                break
        summary.append({
            "index": index,
            "interval": [lo, hi],
            "certified": certified,
            "attempts": attempts,
        })
        (OUTPUT / f"summary-{start:02d}-{stop:02d}.json").write_text(
            json.dumps(summary, indent=2) + "\n", encoding="utf-8"
        )
        print(index, "certified" if certified else "UNRESOLVED", attempts[-1])
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--stop", type=int, required=True)
    parser.add_argument("--start-tier", type=int, choices=range(len(LADDER)), default=0)
    args = parser.parse_args()
    run(args.start, args.stop, args.start_tier)
