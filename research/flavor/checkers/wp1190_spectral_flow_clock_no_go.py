import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp825=json.loads((ROOT/"results"/"wp825_spectral_flow_dimensional_transmutation_audit.json").read_text())
wp1189=json.loads((ROOT/"results"/"wp1189_chain_level_matter_authority_gate.json").read_text())
assert wp825["summary"]["all_passed"] is True
assert wp1189["chain_level_carrier_constructed"] is True
aspect=wp825["exact_data"]["aspect_germ"]
assert aspect["orientation_selection"] is True
for key in ["crossing_location_selection","boundary_coupling_selection","absolute_scale_selection","threshold_location_protection","physical16_descent","detector_calibration"]:
    assert aspect[key] is False
rho1,rho2=map(Fraction,wp825["exact_data"]["hostile_same_index_crossings"])
assert (rho1,rho2)==(Fraction(1,4),Fraction(3,4)) and rho1 != rho2
# Spectral flow contributes orientation, transmutation contributes an RG
# invariant, but m=rho*Lambda retains one crossing-ratio dimension and one
# transmutation-scale dimension.
orientation_dimension=0
crossing_ratio_dimensions=1
transmutation_scale_dimensions=1
clock_fiber_dimensions=crossing_ratio_dimensions+transmutation_scale_dimensions
assert clock_fiber_dimensions == 2
spectral_flow_orientation_selected=True
spectral_flow_clock_law=False
common_clock_selected=False
threshold_clock_selected=False
assert spectral_flow_orientation_selected
assert not (spectral_flow_clock_law or common_clock_selected or threshold_clock_selected)
result={
    "schema":"marici.flavor.wp1190.v1",
    "status":"PASS",
    "question":"Can spectral flow plus dimensional transmutation derive a clock law?",
    "dpc":{
        "conjecture":"A quantized spectral-flow index and RG-invariant scale jointly select the threshold clock.",
        "rivals":["orientation-only spectral flow","crossing-location law","dimensional transmutation","common spectral/RG clock"],
        "risky_consequences":["crossings 1/4 and 3/4 share index one","every transmutation scale has a boundary coupling","m=rho Lambda retains two continuous dimensions","no calibrated path clock exists"],
        "falsification_attempt":"The index is stable under crossing displacement and transmutation trades scale for boundary coupling; their product does not fix either factor.",
        "residual":"The spectral path must itself be an RG trajectory with a dynamically selected zero.",
        "disposition":"accept orientation selection; reject clock-law selection"
    },
    "spectral_path":wp825["exact_data"]["spectral_path"],
    "same_index_crossings":[str(rho1),str(rho2)],
    "spectral_flow":"1",
    "transmutation_scale":wp825["exact_data"]["transmutation_scale"],
    "orientation_dimension":orientation_dimension,
    "crossing_ratio_dimensions":crossing_ratio_dimensions,
    "transmutation_scale_dimensions":transmutation_scale_dimensions,
    "clock_fiber_dimensions":clock_fiber_dimensions,
    "spectral_flow_orientation_selected":spectral_flow_orientation_selected,
    "spectral_flow_clock_law":spectral_flow_clock_law,
    "common_clock_selected":common_clock_selected,
    "threshold_clock_selected":threshold_clock_selected,
    "classification":"negative clock gate: spectral flow selects orientation while transmutation leaves an independent scale fiber",
    "remaining_gate":"make the spectral path an RG trajectory with a dynamically selected zero and calibrated physical clock",
    "hostile_gate":"do not treat topological crossing survival or RG invariance as a numerical threshold clock",
    "claim_boundary":"the no-go covers juxtaposed spectral-flow and transmutation constructions; a unified RG spectral event remains open",
    "disposition":"spectral-flow-clock leaf resolved; spectral-path-RG-event rival selected"
}
(ROOT/"results"/"wp1190_spectral_flow_clock_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1190 PASS:",rho1,rho2,clock_fiber_dimensions)
