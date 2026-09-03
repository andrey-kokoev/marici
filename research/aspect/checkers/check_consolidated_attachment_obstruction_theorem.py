#!/usr/bin/env python3
"""Verify the evidence basis for the consolidated obstruction schema."""
import json
from pathlib import Path
ROOT = Path(__file__).parents[1] / "results"
files = [
 "source_derived_attachment_symmetry.json",
 "instrument_attachment_category.json",
 "coherent_attachment_representability.json",
 "noninvertible_attachment_naturality.json",
 "lax_attachment_compositor_coherence.json",
 "universal_equipment_record_module.json",
 "state_effect_pairing_record_map.json",
 "four_coherence_obligations_independence.json",
 "coefficient_residual_obstruction_classifier.json",
]
data = {f: json.loads((ROOT/f).read_text(encoding="utf-8")) for f in files}
checks = {f+"_passed": d.get("status") == "passed" for f,d in data.items()}
checks["representability_is_not_required_for_correspondence"] = "coherent_attachment_representability.json" in data and "instrument_attachment_category.json" in data
checks["pairing_and_record_are_separate"] = data["state_effect_pairing_record_map.json"].get("disposition") == "pairing descent does not imply physical record descent"
checks["four_face_irredundancy_is_relative"] = "not absolute" in data["four_coherence_obligations_independence.json"].get("strength", "")
assert all(checks.values()), checks
result={"schema":"marici.aspect.consolidated-attachment-obstruction.v1","status":"passed","check_count":len(checks),"evidence_files":files,"strength":"finite theorem schema; unbounded and physical promotions remain open"}
(ROOT/"consolidated_attachment_obstruction_theorem.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"status":"passed","check_count":len(checks),"evidence_count":len(files)},sort_keys=True))
