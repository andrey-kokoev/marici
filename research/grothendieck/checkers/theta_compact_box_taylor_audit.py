"""Audit and consolidate the 64 directed compact Taylor-box certificates."""

import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
RESULTS = ROOT / "results"
BOXES = RESULTS / "theta-compact-boxes"
SWEEP = BOXES / "adaptive-sweep"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


scan = load(RESULTS / "theta-outer-schwarzian-scan.json")
declared = scan["compact_bridge_reconnaissance"][
    "inflated_derivative_box_budget"
]["boxes"]

selected = []
for index, box in enumerate(declared):
    candidates = sorted(SWEEP.glob(f"box-{index:02d}-d*-s*.json"))
    passing = [(path, load(path)) for path in candidates]
    passing = [item for item in passing if item[1]["box_numerator_strictly_positive"]]
    if not passing:
        raise RuntimeError(f"box {index} has no positive directed certificate")
    path, result = passing[0]
    expected = [str(value) for value in box["interval"]]
    actual = result["x_box"]
    # JSON float rendering and Decimal rendering may differ in trailing digits;
    # numeric equality against the declared binary-float endpoints is exact here.
    endpoint_match = all(float(a) == float(e) for a, e in zip(actual, expected))
    if not endpoint_match:
        raise RuntimeError(f"box {index} endpoints disagree: {actual} != {expected}")
    selected.append({
        "index": index,
        "interval": box["interval"],
        "certificate": str(path.relative_to(ROOT)).replace("\\", "/"),
        "degree": result["degree"],
        "simpson_steps": result["simpson_steps"],
        "numerator_enclosure": result["schwarzian_numerator"],
    })

adjacent = all(
    selected[index]["interval"][1] == selected[index + 1]["interval"][0]
    for index in range(len(selected) - 1)
)
closure_path = BOXES / "taylor-x-356.44753572825886-400-d6-s1000.json"
closure = load(closure_path)
closure_positive = closure["box_numerator_strictly_positive"]
closure_overlaps_grid = (
    float(closure["x_box"][0]) <= selected[-1]["interval"][1]
)
closure_reaches_exact_400 = closure["x_box"][1] == "400"
manifest = {
    "declared_interval": [0.25, 400.0],
    "box_count": len(selected),
    "unique_indices": len({item["index"] for item in selected}),
    "exactly_adjacent_declared_float_endpoints": adjacent,
    "all_boxes_strictly_positive": all(
        float(item["numerator_enclosure"][0]) > 0 for item in selected
    ),
    "exact_400_closure_certificate": {
        "certificate": str(closure_path.relative_to(ROOT)).replace("\\", "/"),
        "interval": closure["x_box"],
        "numerator_enclosure": closure["schwarzian_numerator"],
        "strictly_positive": closure_positive,
        "overlaps_terminal_grid_box": closure_overlaps_grid,
        "reaches_exact_decimal_400": closure_reaches_exact_400,
    },
    "smallest_directed_lower_bound": min(
        (item for item in selected),
        key=lambda item: float(item["numerator_enclosure"][0]),
    ),
    "certificates": selected,
    "compact_interval_certified": (
        len(selected) == 64
        and len({item["index"] for item in selected}) == 64
        and adjacent
        and all(float(item["numerator_enclosure"][0]) > 0 for item in selected)
        and closure_positive
        and closure_overlaps_grid
        and closure_reaches_exact_400
    ),
    "rh_proved_or_disproved": False,
}
output = RESULTS / "theta-compact-box-taylor-manifest.json"
output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: value for key, value in manifest.items()
                  if key != "certificates"}, indent=2))
