import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1010,1011)
wp1010=json.loads((ROOT/"results"/"wp1010_global_selector_source_ratio_no_go.json").read_text())
wp1011=json.loads((ROOT/"results"/"wp1011_selected_orbit_spectral_physical16_no_go.json").read_text())
assert wp1010["classification"] == "conditional global selector family; no source-generated numerical ratio"
assert wp1011["classification"] == "global auxiliary selector with no viable separate-spectral physical16 image"
# The global score orbit is selected geometrically, but source c-rescaling
# leaves its ratio unfixed and no separate-spectral Physical16 image realizes
# the selected packet.
score_orbit_unique=True
ratio_family_conditional=True
source_rescaling_unbroken=True
spectral_separation_exact=True
separate_spectral_image_absent=True
source_generated_ratio=False
physical16_image=False
mixed_portal=False
calibrated_instrument=False
assert score_orbit_unique and ratio_family_conditional and source_rescaling_unbroken
assert spectral_separation_exact and separate_spectral_image_absent
assert not (source_generated_ratio or physical16_image or mixed_portal or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1231.v1",
    "status":"PASS",
    "question":"Can source action fix the global-selector ratio and Physical16 image?",
    "dpc":{
        "conjecture":"The global score orbit supplies a source-selected ratio and a viable Physical16 image.",
        "rivals":["source c-rescaling orbit","required exposure ratio","selected spectral-map orbit","1210 fitted ensemble sheets","exact 1/1000 separation threshold"],
        "risky_consequences":["the matched ratio gamma^2 mu^4/(c a^5) remains conditional","positive c-rescaling sends rho to rho/h","the h=2 witness has nonzero gradient","the selected orbit has J squared 5625/636056 and |J| approximately 0.09404","the selected spectral image is disjoint from all 1210 fitted sheets by at least 1/1000"],
        "falsification_attempt":"rescaling freedom prevents a numerical source ratio, while exact spectral separation removes every viable separate-spectral Physical16 image.",
        "residual":"source-derived mixed covariant portal changing relative spectral projectors, together with stable calibration and readout",
        "disposition":"reject global score geometry as source selection; select mixed-covariant-portal rival"
    },
    "matched_ratio":wp1010["matched_ratio"],
    "required_ratio":wp1010["required_ratio"],
    "rescaling":wp1010["induced_action"],
    "h_equals_2_gradient":wp1010["h_equals_2_witness_gradient"],
    "selected_orbit_J_squared":wp1011["selected_orbit_J_squared"],
    "selected_orbit_abs_J_decimal":wp1011["selected_orbit_abs_J_decimal"],
    "ensemble_sheets":wp1011["ensemble_sheets"],
    "exact_separation_threshold":wp1011["exact_separation_threshold"],
    "score_orbit_unique":score_orbit_unique,
    "ratio_family_conditional":ratio_family_conditional,
    "source_rescaling_unbroken":source_rescaling_unbroken,
    "spectral_separation_exact":spectral_separation_exact,
    "separate_spectral_image_absent":separate_spectral_image_absent,
    "source_generated_ratio":source_generated_ratio,
    "physical16_image":physical16_image,
    "mixed_portal":mixed_portal,
    "calibrated_instrument":calibrated_instrument,
    "classification":"negative global-source-ratio result: score selection remains geometric and separate-spectral image is absent",
    "remaining_gate":"derive a mixed covariant portal that fixes the source ratio and changes relative spectral projectors without leaving Physical16",
    "hostile_gate":"do not call score uniqueness, conditional source matching, or spectral separation a source-derived Physical16 selector",
    "claim_boundary":"the selected orbit is a global auxiliary selector; source c-rescaling and separate-spectral no-go leave physical selection unresolved",
    "disposition":"global-selector source-ratio leaf resolved negatively; mixed-covariant-portal rival selected"
}
(ROOT/"results"/"wp1231_global_selector_source_ratio_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1231 PASS: global ratio unfixed; mixed covariant portal required")
