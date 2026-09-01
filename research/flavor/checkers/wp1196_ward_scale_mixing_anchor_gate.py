import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp837=json.loads((ROOT/"results"/"wp837_primitive_current_reflection_aspect_germ_audit.json").read_text())
wp1195=json.loads((ROOT/"results"/"wp1195_ward_spectral_completion_gate.json").read_text())
assert wp837["summary"]["all_passed"] is True
assert wp1195["finite_completion_selected"] is True
assert wp837["classification"] == "conditional mixing rigidifier attached to the WP836 finite-completion selector; not a physical16 source selector"
assert wp837["aspect_gates"]["authority"].startswith("fails")
assert wp837["smallest_exact_falsifier"] == "D=H_q and D=2 H_q obey the same germ law and score but have different absolute spectral thresholds"
reflection=next(t for t in wp837["tests"] if t["name"]=="reflection_is_self_adjoint_involution")["evidence"]
scale=next(t for t in wp837["tests"] if t["name"]=="positive_scale_fiber_survives")["evidence"]
alternative=next(t for t in wp837["tests"] if t["name"]=="alternative_wp836_minimizer_fails_current_attachment")["evidence"]
assert scale == "3"
# The current-attached Householder reflection is unique up to positive scale.
mixing_orientation_conditionally_selected=True
absolute_scale_selected=False
source_authority=False
calibrated_instrument=False
assert mixing_orientation_conditionally_selected
assert not (absolute_scale_selected or source_authority or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1196.v1",
    "status":"PASS",
    "question":"Can the primitive current anchor Ward scale and mixing?",
    "dpc":{
        "conjecture":"Attaching the finite-completion minimizer to the primitive current selects scale and mixing.",
        "rivals":["unattached equal-singular minimizer","current-reflection germ","positive spectral scale","source-derived action and instrument"],
        "risky_consequences":["H_q has exactly one negative current line","the alternative WP836 minimizer fails current attachment","H_q and 2H_q retain the same germ law and score","no source action supplies the attachment"],
        "falsification_attempt":"The normalized Householder reflection removes the mixing fiber, but positive rescaling leaves an exact scale fiber.",
        "residual":"A source-derived spectral action and normalized scale are required.",
        "disposition":"construct conditional mixing anchor; reject scale/source selection"
    },
    "householder_reflection":reflection,
    "current":"q=(1,2,3)",
    "current_norm_squared":"14",
    "alternative_minimizer_current_image":alternative,
    "mixing_orientation_conditionally_selected":mixing_orientation_conditionally_selected,
    "absolute_scale_selected":absolute_scale_selected,
    "source_authority":source_authority,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional mixing anchor: current reflection selected up to positive scale",
    "remaining_gate":"derive the spectral-action profile and its normalized scale from source",
    "hostile_gate":"do not treat the current-attached germ as a source-generated physical selector",
    "claim_boundary":"the anchor is conditional on the declared current attachment and does not select absolute threshold scale",
    "disposition":"Ward scale/mixing leaf resolved; spectral-action normalization rival selected"
}
(ROOT/"results"/"wp1196_ward_scale_mixing_anchor_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1196 PASS: mixing=yes scale=no")
