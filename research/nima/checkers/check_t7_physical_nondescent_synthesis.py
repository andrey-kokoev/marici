#!/usr/bin/env python3
"""Cross-check the physical five-pole localization data against isolated T7."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[3]
    b = root / "research/benincasa"
    rank = json.loads((b / "five-pole-residue-euler-rank.json").read_text())
    typing = json.loads((b / "physical-g12-residue-localization-typing.json").read_text())
    occupancy_source = (b / "physical_five_pole_residue_occupancy_gate.py").read_text()

    assert rank["five_pole_pre_residue_rank"] == 35
    assert rank["four_mark_residue_rank"] == 20
    assert rank["unmarked_q_G12_residue_rank"] == 9
    assert rank["homogeneous_four_pole_lower_rank"] == 15
    assert rank["homogeneous_four_pole_lower_rank"] + rank["four_mark_residue_rank"] == 35
    assert typing["physical_residue_home"] == "H^2(S_E\\W)"
    assert typing["q_only_nine_master_home"] == "H^2(S_E)"
    assert typing["descent_condition"] == "all localization wall residues vanish"
    assert typing["remaining_wall_residues"] == ["q_g1", "q_g2", "q_g3"]
    assert "physical_residue_class_nonzero\": True" in occupancy_source
    assert "normalized_shared_wall_components_nonzero" in occupancy_source

    inputs = [
        b / "five-pole-residue-euler-rank.json",
        b / "physical-g12-residue-localization-typing.json",
        b / "physical-five-pole-g12-residue.json",
        b / "physical_five_pole_residue_occupancy_gate.py",
    ]
    result = {
        "schema": "marici.nima.t7_physical_nondescent_synthesis.v1",
        "passed": True,
        "physical_five_pole_rank": 35,
        "deletion_rank": 15,
        "physical_four_mark_residue_rank": 20,
        "closed_q_only_rank": 9,
        "physical_home": "H^2(S_E\\W)",
        "closed_T7_home": "H^2(S_E)",
        "wall_residue_descent_condition_met": False,
        "conclusion": "the literal physical q_G12 residue does not descend to isolated closed T7; T7-only UV residuals cannot be interpreted as physical readout deficits",
        "input_sha256": {str(p.relative_to(root)).replace("\\", "/"): hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in inputs},
    }
    output = root / "research/nima/results/t7_physical_nondescent_synthesis.json"
    payload = output.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "physical_descent_to_T7": False,
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
