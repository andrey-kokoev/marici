"""Compare forced C4 infinity nodes with the source loop-momentum end."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-cycle-triple-points.json"
OUT = ROOT / "research/benincasa/results/four-cycle-physical-infinity-support.json"

packet = json.loads(SOURCE.read_text())
points = [tuple(map(int, key.strip("()").split(", ")))
          for key in packet["projective_y_point_census"]]
physical = (1, 1, 1, 1)


def proportional(x, y):
    pairs = [(a, b) for a, b in zip(x, y) if a or b]
    return all(a*pairs[0][1] == b*pairs[0][0] for a, b in pairs)


assert len(points) == 5
assert not any(proportional(point, physical) for point in points)

result = {
    "schema": "marici.benincasa.four_cycle_physical_infinity_support.v1",
    "source_loop_lengths": "y_i(R,n)=|R n+K_i|",
    "asymptotic_expansion": "y_i=R+n.K_i+O(R^-1)",
    "physical_projective_infinity_point": list(physical),
    "forced_projective_points": [list(p) for p in points],
    "forced_occurrences": sum(packet["projective_y_point_census"].values()),
    "intersection_with_literal_physical_infinity": 0,
    "literal_supported_restriction": "zero",
    "analytic_continuation": "not selected by the frozen positive contour alone",
    "new_carrier_datum": False,
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
