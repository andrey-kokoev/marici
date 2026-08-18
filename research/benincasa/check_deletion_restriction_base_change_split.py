"""Check the Euler constraints for the deletion--restriction split."""

import json
from pathlib import Path


path = Path(__file__).with_name("deletion_restriction_base_change_split.json")
data = json.loads(path.read_text(encoding="utf-8"))

g = data["generic"]
h = data["homogeneous"]
d = data["euler_defects"]

assert g["five_pole"] == g["lower"] + g["restricted"] == 60
assert h["five_pole"] == h["lower"] + h["restricted"] == 35
assert d["lower"] == g["lower"] - h["lower"] == 19
assert d["restricted"] == g["restricted"] - h["restricted"] == 6
assert d["five_pole"] == g["five_pole"] - h["five_pole"] == 25
assert d["five_pole"] == d["lower"] + d["restricted"]
assert data["status"] == "necessary Euler-characteristic constraint"

print("PASS: five-pole Euler defect splits as lower 19 plus restricted 6")
