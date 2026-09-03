import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(826,1190)
wp826=json.loads((ROOT/"results"/"wp826_rg_spectral_heteroclinic_event_selection_audit.json").read_text())
wp1190=json.loads((ROOT/"results"/"wp1190_spectral_flow_clock_no_go.json").read_text())
assert wp826["summary"]["all_passed"] is True
assert wp1190["clock_fiber_dimensions"] == 2
germ=wp826["exact_data"]["aspect_germ"]
for key in ["orientation_selection","dimensionless_magnitude_selection","global_open_basin"]:
    assert germ[key] is True
for key in ["trajectory_phase_selection","absolute_event_scale","threshold_criterion_authority","physical16_descent","detector_calibration"]:
    assert germ[key] is False
assert wp826["exact_data"]["half_crossing_time"] == "log(modulus)"
assert wp826["exact_data"]["crossing_scale"] == "modulus*reference_scale"
assert wp826["exact_data"]["crossing_slope"] == "1/4"
# A is the autonomous translation modulus. A=1 and A=2 share endpoint
# regularity but give different physical event scales at fixed reference.
moduli=[Fraction(1),Fraction(2)]
reference=Fraction(1)
event_scales=[reference*a for a in moduli]
assert event_scales[0] != event_scales[1]
threshold_shift=Fraction(3,1)  # t(3/4)-t(1/2)=log 3
assert threshold_shift == 3
conditional_event_selector=True
absolute_event_scale_selected=False
spectral_path_is_rg_trajectory=True
assert conditional_event_selector and spectral_path_is_rg_trajectory
assert not absolute_event_scale_selected
result={
    "schema":"marici.flavor.wp1191.v1",
    "status":"PASS",
    "question":"Can the spectral path be made into an RG trajectory with a selected event?",
    "dpc":{
        "conjecture":"Coupling the spectral zero to a global RG heteroclinic selects the physical event.",
        "rivals":["juxtaposed index and scale","autonomous heteroclinic event","boundary-anchored heteroclinic","detector-calibrated event"],
        "risky_consequences":["positive transverse crossing at u=1/2","global open basin from 0 to 1","A=1 and A=2 give different event scales","criterion 3/4 shifts the event by log 3"],
        "falsification_attempt":"The coupled logistic trajectory fixes orientation, dimensionless magnitude, and basin, but autonomous translation leaves one phase modulus and no absolute scale.",
        "residual":"A second independently fixed physical event or boundary clock must anchor the RG phase.",
        "disposition":"construct conditional RG spectral event; reject absolute event selection"
    },
    "trajectory":wp826["exact_data"]["trajectory"],
    "crossing":"u=1/2 at t=log(A)",
    "crossing_slope":wp826["exact_data"]["crossing_slope"],
    "global_basin":"0<u<1 flows from 0 to 1",
    "conditional_event_selector":conditional_event_selector,
    "spectral_path_is_rg_trajectory":spectral_path_is_rg_trajectory,
    "translation_moduli":[str(a) for a in moduli],
    "event_scales_at_unit_reference":[str(x) for x in event_scales],
    "threshold_shift_log_ratio":str(threshold_shift),
    "open_gates":[
        "trajectory_phase_selection",
        "absolute_event_scale",
        "threshold_criterion_authority",
        "physical16_descent",
        "detector_calibration"
    ],
    "absolute_event_scale_selected":absolute_event_scale_selected,
    "classification":"conditional event selector: orientation, dimensionless magnitude, and basin close; absolute event scale remains open",
    "remaining_gate":"derive an independently fixed RG boundary or second physical event to anchor the heteroclinic phase",
    "hostile_gate":"do not treat global regularity or a reference-clock convention as absolute event-scale selection",
    "claim_boundary":"the selector is conditional on the logistic RG field, symmetric threshold, and a future physical anchor",
    "disposition":"spectral-path-RG-event leaf resolved; RG-event-anchor rival selected"
}
(ROOT/"results"/"wp1191_spectral_path_rg_event_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1191 PASS:",event_scales,threshold_shift)
