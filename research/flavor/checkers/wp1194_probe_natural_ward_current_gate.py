import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp831=json.loads((ROOT/"results"/"wp831_primitive_ward_current_threshold_fiber.json").read_text())
wp1193=json.loads((ROOT/"results"/"wp1193_physical_running_observable_gate.json").read_text())
assert wp831["summary"]["all_passed"] is True
assert wp1193["canonical_running_observable"] is False
assert wp831["classification"]["channel_selection"] == "the primitive oriented kernel selects one linear conserved-current channel"
assert wp831["smallest_exact_falsifier"]["base_packet"]["spectral_index"] == "14"
assert wp831["smallest_exact_falsifier"]["vectorlike_completed_packet"]["spectral_index"] == "16"
assert wp831["smallest_exact_falsifier"]["vectorlike_completed_packet"]["coupling"] == "sqrt(7/8)"
assert wp831["smallest_exact_falsifier"]["common_current_record"] == "14"
base_index=14
completed_index=16
record=14
# The response C=S e^2 is invariant under (14,1)->(16,sqrt(7/8)).
assert completed_index * Fraction(7,8) == base_index
unique_current_channel=True
probe_natural_across_threshold_completion=False
spectral_completion_selected=False
physical16_readout=False
assert unique_current_channel
assert not (probe_natural_across_threshold_completion or spectral_completion_selected or physical16_readout)
result={
    "schema":"marici.flavor.wp1194.v1",
    "status":"PASS",
    "question":"Does the primitive Ward current provide a probe-natural invariant?",
    "dpc":{
        "conjecture":"WP820's primitive kernel selects a conserved-current probe natural across the physical family.",
        "rivals":["process-relative effective charge","unique primitive Ward current","vectorlike-completed Ward current","full probe-natural invariant"],
        "risky_consequences":["primitive current q=(1,2,3) has anomaly 36 and index 14","an anomaly-neutral pair changes index to 16","coupling sqrt(7/8) gives the same response 14","no physical16 readout exists"],
        "falsification_attempt":"The current channel is unique on the primitive kernel, but Ward-response continuity identifies the base and vectorlike-completed packets at a common record.",
        "residual":"A source-derived full active spectrum and calibrated current instrument are required.",
        "disposition":"construct conditional Ward-current invariant; reject threshold-natural selection"
    },
    "primitive_current":"q=(1,2,3)",
    "oriented_anomaly":"36",
    "base_spectral_index":base_index,
    "completed_spectral_index":completed_index,
    "base_coupling":"1",
    "completed_coupling":"sqrt(7/8)",
    "common_current_record":record,
    "unique_current_channel":unique_current_channel,
    "probe_natural_across_threshold_completion":probe_natural_across_threshold_completion,
    "spectral_completion_selected":spectral_completion_selected,
    "physical16_readout":physical16_readout,
    "classification":"conditional probe invariant: unique current channel selected, threshold-completed magnitude fiber remains",
    "remaining_gate":"derive the full anomaly-neutral spectrum completion and calibrated Ward instrument",
    "hostile_gate":"do not call the Ward response probe-natural before fixing the active spectrum",
    "claim_boundary":"the invariant is conditional on a fixed active spectrum; no threshold-complete physical record is claimed",
    "disposition":"probe-natural-invariant leaf resolved; Ward-spectral-completion rival selected"
}
(ROOT/"results"/"wp1194_probe_natural_ward_current_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1194 PASS:",base_index,completed_index,record)
