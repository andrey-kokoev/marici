"""Check the replicated source-cyclicity certificate for the relative union."""

import json
from pathlib import Path


path = Path(__file__).with_name("unsplit-relative-horizontal-saturation.json")
data = json.loads(path.read_text(encoding="utf-8"))

assert data["marks"] == ["g1", "g2", "g3", "g23", "g31"]
assert len(data["runs"]) == 3
for run in data["runs"]:
    assert run["first_jet_rank"] == 3
    assert run["horizontal_saturation_rank"] == run["relative_dimension"] == 21

print("PASS: unsplit source horizontally saturates the rank-21 relative union")
