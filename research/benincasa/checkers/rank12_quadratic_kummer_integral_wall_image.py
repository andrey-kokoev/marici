"""Primitivity of the integral Kummer generator in the two-wall lattice."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/rank12-quadratic-kummer-integral-wall-image.json"

# Represent a+b*r, r^2=2, as (a,b).
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x): return (-x[0], -x[1])
def norm(x): return x[0] * x[0] - 2 * x[1] * x[1]

wall_image = [(1, 1), (0, -1), (-1, -1), (0, 0)]
assert norm(wall_image[0]) == -1  # 1+r is a unit.
assert add(wall_image[0], wall_image[2]) == (0, 0)

packet = {
    "schema": "marici.benincasa.rank12_quadratic_kummer_integral_wall_image.v1",
    "integer_ring": "Z[sqrt(2)]",
    "primitive_kummer_generator": "kappa=sqrt(2)*k",
    "integral_wall_image": ["1+sqrt(2)", "-sqrt(2)", "-1-sqrt(2)", "0"],
    "unit_coordinate": "1+sqrt(2)",
    "unit_norm": -1,
    "wall_image_saturated": True,
    "top_residue": 0,
    "additional_lattice_index": 1,
    "physical_activation_selected": False,
    "interpretation": "The sole index-two defect is intrinsic to the source Kummer eigenline. Its integral two-wall Cousin image is primitive and introduces no further extension.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
