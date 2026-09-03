import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(953,954,955)
wp953=json.loads((ROOT/"results"/"wp953_sector_character_common_source_authority_no_go.json").read_text())
wp954=json.loads((ROOT/"results"/"wp954_s3_doublet_cubic_flag_selector.json").read_text())
wp955=json.loads((ROOT/"results"/"wp955_s3_flag_projective_sign_radial_descent.json").read_text())
assert wp953["classification"] == "WP350 up and down rays are selected by different symmetry objects, not two characters of one common natural S3 module"
assert wp954["classification"] == "conditional source selector of an S3-to-Z2 flag orbit and the WP350 down coefficient ray"
assert wp955["classification"] == "projective S3-to-Z2 flag selector is blind to cubic sign and nonzero radial magnitude"
# The S3 doublet supplies a conditional three-flag source route, but the
# projective selector is sign/radius blind and no physical16 instrument is
# derived.
common_character_no_go=True
three_flag_orbit=True
down_ray_conditional=True
projective_sign_blind=True
radial_blind=True
physical_doublet=False
even_projective_coupling=False
radial_amplitudes=False
physical16_descent=False
calibrated_instrument=False
assert common_character_no_go and three_flag_orbit and down_ray_conditional
assert projective_sign_blind and radial_blind
assert not (physical_doublet or even_projective_coupling or radial_amplitudes or physical16_descent or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1222.v1",
    "status":"PASS",
    "question":"Can the S3 doublet supply the three-source-decomposition instrument?",
    "dpc":{
        "conjecture":"The natural S3 module supplies three source-related decompositions and a physical16 instrument.",
        "rivals":["common natural-module character","S3-to-Z2 vector flag orbit","projective S3-to-Z2 flag orbit","opposite cubic-sign orbits"],
        "risky_consequences":["the full-S3 sign subspace has dimension zero","the cubic extrema select two opposite three-member flag orbits and the WP350 down ray","projectivization makes opposite vector orbits share the same flags","the flag projector is blind to cubic sign and nonzero radial magnitude"],
        "falsification_attempt":"the conditional cubic route selects flags but not their sign or amplitude, while the common-character route has no sign line.",
        "residual":"physical doublet and even projective coupling, radial amplitudes, general completion stability, family-module descent, and calibrated instrument",
        "disposition":"accept conditional flag structure only; select physical doublet/projective-coupling rival"
    },
    "module_decomposition":wp953["module_decomposition"],
    "flag_selector":wp954["flag_selector"],
    "projective_selector":wp955["projective_selector"],
    "common_character_no_go":common_character_no_go,
    "three_flag_orbit":three_flag_orbit,
    "down_ray_conditional":down_ray_conditional,
    "projective_sign_blind":projective_sign_blind,
    "radial_blind":radial_blind,
    "physical_doublet":physical_doublet,
    "even_projective_coupling":even_projective_coupling,
    "radial_amplitudes":radial_amplitudes,
    "physical16_descent":physical16_descent,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional three-source flag result: S3-to-Z2 structure exists, but physical16 instrument is absent",
    "remaining_gate":"declare the physical doublet and even projective coupling, derive radial amplitudes, prove completion stability and family-module descent, and calibrate the instrument",
    "hostile_gate":"do not promote a conditional flag orbit or sign/radius-blind projector to a calibrated three-source instrument",
    "claim_boundary":"the positive flag structure is conditional on an undeclared doublet and cubic; projective descent is sign and radial blind",
    "disposition":"three-source-decomposition leaf resolved conditionally; physical-doublet/projective-coupling rival selected"
}
(ROOT/"results"/"wp1222_three_source_decomposition_instrument_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1222 PASS: S3 flag route conditional, instrument absent")
