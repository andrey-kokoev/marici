import json
from pathlib import Path


def dot(row, column):
    return sum(a * b for a, b in zip(row, column))


U_x = (1, -1)
evans = (1, 1)
moving = (1, -1)
defect = tuple(e - m for e, m in zip(evans, moving))

moving_margin = dot(moving, U_x)
fixed_readout = dot(evans, U_x)
defect_value = dot(defect, U_x)
sharp_rho = abs(defect_value) / moving_margin

assert moving_margin == 2
assert fixed_readout == 0
assert defect_value == -2
assert sharp_rho == 1

result = {
    "fixture": {
        "transported_state": U_x,
        "fixed_observer": evans,
        "moving_observer": moving,
        "observer_defect": defect,
    },
    "moving_margin": moving_margin,
    "fixed_readout": fixed_readout,
    "defect_value": defect_value,
    "sharp_relative_constant": sharp_rho,
    "strict_gap_passes": sharp_rho < 1,
    "conclusion": "rho < 1 transfers positivity; rho = 1 permits exact cancellation",
}

output = Path(__file__).parents[1] / "results" / "rh-observer-comparison-gap.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

