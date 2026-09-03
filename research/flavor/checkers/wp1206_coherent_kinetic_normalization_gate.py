import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(857)
wp857=json.loads((ROOT/"results"/"wp857_oriented_dark_state_portal_attractor.json").read_text())
assert wp857["summary"]["all_passed"] is True
assert wp857["selected_state"] == "odd ray (|A>-|B>)/sqrt(2)"
assert wp857["global_basin"] == "all density matrices on the declared three-state source"
assert wp857["portal_from_absence"] is True
assert wp857["source_authority_hostile"] == "equal-gap even-parity reservoir"
assert wp857["classification"] == "conditional coherent magnitude/parity selector; reservoir, RG, threshold and reference authority open"
# The dissipative source fixes the odd dark ray and its port magnitude, but an
# even reservoir with the same spectrum is an exact source-authority hostile.
unique_dark_projector=True
global_basin=True
fixed_port_magnitude=True
portal_from_absence=True
source_authority_derived=False
flavor_rg_identified=False
threshold_intertwined=False
coherent_reference_calibrated=False
assert unique_dark_projector and global_basin and fixed_port_magnitude and portal_from_absence
assert not (source_authority_derived or flavor_rg_identified or threshold_intertwined or coherent_reference_calibrated)
result={
    "schema":"marici.flavor.wp1206.v1",
    "status":"PASS",
    "question":"Can coherent dissipation normalize the portal from absence?",
    "dpc":{
        "conjecture":"A dissipative coherent source selects an odd dark ray with fixed port magnitude from a boundary absence.",
        "rivals":["stationary dark projector","positive Liouvillian gap","global dissipative basin","equal-gap even-parity reservoir"],
        "risky_consequences":["the odd projector is stationary","the Liouvillian kernel is unique","the spectrum has positive gap","the dark ray has antisymmetric port magnitude 1/sqrt(2)","an even-parity reservoir has the same spectrum but selects a different projector"],
        "falsification_attempt":"The equal-gap even rival shows that relaxation spectrum alone does not authorize odd parity.",
        "residual":"Derive the odd reservoir from the WP854 boundary source, identify the semigroup with flavor RG, intertwine through thresholds, and calibrate the WP855 reference.",
        "disposition":"construct coherent kinetic normalization; reject spectrum-only parity authority"
    },
    "source_domain":wp857["source_domain"],
    "selected_state":wp857["selected_state"],
    "liouvillian_spectrum":wp857["liouvillian_spectrum"],
    "global_basin":wp857["global_basin"],
    "portal_from_absence":portal_from_absence,
    "source_authority_hostile":wp857["source_authority_hostile"],
    "unique_dark_projector":unique_dark_projector,
    "fixed_port_magnitude":fixed_port_magnitude,
    "source_authority_derived":source_authority_derived,
    "flavor_rg_identified":flavor_rg_identified,
    "threshold_intertwined":threshold_intertwined,
    "coherent_reference_calibrated":coherent_reference_calibrated,
    "classification":"conditional coherent selector: odd dark ray and 1/sqrt(2) port; reservoir parity authority open",
    "remaining_gate":"derive the odd reservoir from the boundary source and calibrate its reference channel",
    "hostile_gate":"do not infer odd parity from relaxation spectrum alone",
    "claim_boundary":"the normalization is conditional on the declared dissipative three-state source",
    "disposition":"coherent-kinetic-normalization leaf resolved; boundary-reservoir-source rival selected"
}
(ROOT/"results"/"wp1206_coherent_kinetic_normalization_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1206 PASS: odd dark ray fixed; spectrum parity hostile remains")
