"""Check the exact singleton-face contribution to the lower rank loss."""

import json
from pathlib import Path


path = Path(__file__).with_name("homogeneous_lower_single_face_census.json")
data = json.loads(path.read_text(encoding="utf-8"))

generic = data["generic_proper_grades"]
homogeneous = data["homogeneous_proper_grades"]
losses = [g - h for g, h in zip(generic, homogeneous)]

assert data["homogeneous_closed_ranks"] == [7, 8, 8, 8, 11]
assert losses == data["single_face_losses"] == [0, 4, 4, 4, 1]
assert sum(losses) == data["single_face_loss_total"] == 13
assert data["full_lower_euler_loss"] - sum(losses) == data["unresolved_higher_support_loss"] == 6
assert data["scope"].startswith("empty and singleton faces only")
assert data["frontier_superseded_by"] == [706, 707]

print("PASS: singleton faces account for 13 of the lower Euler loss 19")
