import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp827=json.loads((ROOT/"results"/"wp827_intrinsic_rg_curvature_anchor_triplet.json").read_text())
wp829=json.loads((ROOT/"results"/"wp829_rg_curvature_scheme_descent_no_go.json").read_text())
wp1191=json.loads((ROOT/"results"/"wp1191_spectral_path_rg_event_gate.json").read_text())
assert wp827["summary"]["all_passed"] is True
assert wp829["summary"]["all_passed"] is True
assert wp1191["conditional_event_selector"] is True
assert wp827["exact_data"]["unit_rate_full_ratio"] == "4*sqrt(3) + 7"
assert wp827["exact_data"]["aspect_germ"]["translation_invariant_event_ratios"] is True
for key in ["beta_normalization_authority","absolute_scale","physical16_descent","common_gain_instrument"]:
    assert wp827["exact_data"]["aspect_germ"][key] is False
assert wp829["classification"]["first_nonfaithful_arrow"] == "physical RG trajectory to chosen coupling-coordinate acceleration jet"
resultant=next(t for t in wp829["tests"] if t["name"]=="new_internal_anchors_are_not_reflection_complements")["evidence"]
assert resultant == "110592"
# WP827 repairs the autonomous translation fiber relationally, while WP829
# shows the repair is not functorial under an admitted running-coupling chart.
translation_fiber_repaired=True
scheme_descent=False
physical_running_observable=False
common_gain_instrument=False
assert translation_fiber_repaired and not (scheme_descent or physical_running_observable or common_gain_instrument)
result={
    "schema":"marici.flavor.wp1192.v1",
    "status":"PASS",
    "question":"Can an intrinsic RG event anchor repair the heteroclinic phase modulus?",
    "dpc":{
        "conjecture":"Curvature extrema of the same RG vector field anchor the portal event.",
        "rivals":["reference-clock anchor","intrinsic curvature triplet","scheme-invariant running observable","common-gain detector"],
        "risky_consequences":["anchors occur at (3±sqrt(3))/6 around 1/2","full ratio is 7+4sqrt(3)","ratio cancels translation and reference scale","admissible scheme change moves the anchors"],
        "falsification_attempt":"WP827 constructs translation-invariant ratios, but WP829's monotone redefinition preserves the physical trajectory while moving coordinate acceleration extrema; reflection failure has resultant 110592.",
        "residual":"A physically normalized running observable, threshold matching, and one common-gain instrument must be derived.",
        "disposition":"construct conditional relative anchor; reject physical anchor authority"
    },
    "anchor_values":wp827["exact_data"]["anchor_values"],
    "one_sided_time_offset":wp827["exact_data"]["one_sided_time_offset"],
    "unit_rate_full_ratio":wp827["exact_data"]["unit_rate_full_ratio"],
    "translation_fiber_repaired":translation_fiber_repaired,
    "scheme_map":wp829["admissible_reparameterization"]["map"],
    "scheme_resultant":resultant,
    "scheme_descent":scheme_descent,
    "physical_running_observable":physical_running_observable,
    "common_gain_instrument":common_gain_instrument,
    "open_gates":[
        "beta_normalization_authority",
        "absolute_scale",
        "physical16_descent",
        "common_gain_instrument",
        "physical_running_observable"
    ],
    "classification":"conditional relative anchor with negative scheme-descent authority",
    "remaining_gate":"derive a physical running observable and matched common-gain instrument",
    "hostile_gate":"do not treat coordinate-curvature ratios as scheme-independent physical anchors",
    "claim_boundary":"the anchor ratio is conditional on the logistic coupling coordinate and unit beta normalization",
    "disposition":"RG-event-anchor leaf resolved; physical-running-observable rival selected"
}
(ROOT/"results"/"wp1192_rg_event_anchor_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1192 PASS:",wp827["exact_data"]["unit_rate_full_ratio"],resultant)
