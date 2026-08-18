"""Validate the typing gate for the remaining Gauss--Manin base-change test."""

import json
from pathlib import Path


path = Path(__file__).with_name("derived_pushforward_base_change_contract.json")
data = json.loads(path.read_text(encoding="utf-8"))

assert data["entry"] == 701
assert data["status"] == "acceptance-contract-only"
assert data["frozen_input"]["labels"] == [
    "nu_1*nu_2",
    "nu_1*nu_3",
    "nu_2*nu_3",
]
assert data["closed_elementary_square"]["result"] == "strictly_commutative"
assert "Rpi_*" in data["open_square"]["upper_route"]
assert "Rpi_hom,*" in data["open_square"]["lower_route"]
assert set(data["accepted_outcomes"]) == {"strict", "homotopy", "obstructed", "untyped"}
assert len(data["typing_requirements"]) == 6
assert len(data["inadmissible_inferences"]) == 5
assert data["Q_gate"]["open_only_after"].startswith("beta_GM is typed")

print("PASS: derived pushforward/base-change acceptance contract is internally typed")
