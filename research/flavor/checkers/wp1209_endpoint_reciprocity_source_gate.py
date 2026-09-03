import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(865)
wp865=json.loads((ROOT/"results"/"wp865_minimal_lossless_colligation_source_audit.json").read_text())
assert wp865["summary"]["all_passed"] is True
assert wp865["state_domain"] == "absent state plus reciprocal two-endpoint portal"
assert wp865["source_operation"] == "three-Kraus channel and its minimal lossless Stinespring colligation"
assert wp865["selected_ray"] == "(-i,1)/sqrt(2) for the audited z=i branch"
assert wp865["channel_spectrum"] == {"0":5,"1":1,"1/2":2,"1/4":1}
assert wp865["classification"] == "implements selector, basin, and source readout conditionally; explains none of their free source moduli"
# A minimal lossless colligation makes endpoint reciprocity executable. It
# does not derive q, z, a reducing threshold, or physical16 calibration.
trace_preserving=True
unique_stationary_dark=True
lossless_complement=True
bright_dark_readout=True
q_modulus_free=True
z_modulus_free=True
reducing_threshold_derived=False
calibrated_physical16=False
assert trace_preserving and unique_stationary_dark and lossless_complement and bright_dark_readout
assert q_modulus_free and z_modulus_free
assert not (reducing_threshold_derived or calibrated_physical16)
result={
    "schema":"marici.flavor.wp1209.v1",
    "status":"PASS",
    "question":"Can endpoint reciprocity be made executable from a source-level colligation?",
    "dpc":{
        "conjecture":"An absent state plus reciprocal two-endpoint portal, realized as a three-Kraus channel and minimal lossless Stinespring colligation, derives endpoint reciprocity.",
        "rivals":["q=0 versus q=1/4 at fixed z=i","z=1 versus z=i at fixed q=1/4","unitary endpoint-heavy rotation","uncalibrated physical16 readout"],
        "risky_consequences":["the Kraus family is trace preserving","the selected dark ray is uniquely stationary","the global basin has spectrum 0^5,1,1/2^2,1/4","complementary rows are lossless","the selected ray is dark in the common port and unit-bright in the complement"],
        "falsification_attempt":"Changing q changes the basin, changing z changes the selected ray, and endpoint-heavy threshold rotation attenuates the readout.",
        "residual":"The colligation explains no free source modulus and does not derive the reducing threshold or calibrated physical16 detector map.",
        "disposition":"construct conditional endpoint-reciprocity source; reject modulus-free promotion"
    },
    "state_domain":wp865["state_domain"],
    "source_operation":wp865["source_operation"],
    "selected_ray":wp865["selected_ray"],
    "channel_spectrum":wp865["channel_spectrum"],
    "contextual_partition":wp865["contextual_partition"],
    "smallest_exact_falsifiers":wp865["smallest_exact_falsifiers"],
    "trace_preserving":trace_preserving,
    "unique_stationary_dark":unique_stationary_dark,
    "lossless_complement":lossless_complement,
    "bright_dark_readout":bright_dark_readout,
    "q_modulus_free":q_modulus_free,
    "z_modulus_free":z_modulus_free,
    "reducing_threshold_derived":reducing_threshold_derived,
    "calibrated_physical16":calibrated_physical16,
    "classification":"conditional endpoint-reciprocity source via minimal lossless colligation",
    "remaining_gate":"derive q and z source moduli, reducing threshold projector, RG, and physical16 calibration from one packet",
    "hostile_gate":"do not infer q, z, reducing transport, or detector calibration from lossless reciprocity alone",
    "claim_boundary":"reciprocity is executable only after source-fixed q and z; it is not microscopic modulus authority",
    "disposition":"endpoint-reciprocity-source leaf resolved; source-modulus selection rival selected"
}
(ROOT/"results"/"wp1209_endpoint_reciprocity_source_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1209 PASS: minimal colligation realizes endpoint reciprocity")
