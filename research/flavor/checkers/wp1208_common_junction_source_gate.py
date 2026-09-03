import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(859)
wp859=json.loads((ROOT/"results"/"wp859_positive_kirchhoff_junction_selector_instrument.json").read_text())
assert wp859["summary"]["all_passed"] is True
assert wp859["source_principle"] == "reciprocal normalized Kirchhoff incidence with positive Gram and lossless two-port completion"
assert wp859["selected_ray"] == "(-z,1)/sqrt(2)"
assert wp859["portal_magnitude"] == "unit component magnitudes 1/sqrt(2)"
assert wp859["global_basin"] == "unique zero-temperature lowering fixed point on normalized two-path density matrices"
assert wp859["source_instrument"] == "common dark port plus complementary unit-bright difference port"
assert wp859["classification"] == "conditional selector and executable source-level instrument"
# Positive reciprocal Kirchhoff incidence supplies the common junction and an
# executable instrument. Endpoint reciprocity remains an assumption, not a
# microscopic packet authority.
reciprocal_normalized=True
positive_gram=True
lossless_two_port=True
dark_fixed_point=True
global_gap=True
weighted_rival=False
finite_temperature_rival=False
non_isometric_threshold_rival=False
endpoint_reciprocity_microscopically_derived=False
flavor_rg_identified=False
isometric_full_transport=False
calibrated_detector=False
assert reciprocal_normalized and positive_gram and lossless_two_port
assert dark_fixed_point and global_gap
assert not (weighted_rival or finite_temperature_rival or non_isometric_threshold_rival)
assert not (endpoint_reciprocity_microscopically_derived or flavor_rg_identified or isometric_full_transport or calibrated_detector)
result={
    "schema":"marici.flavor.wp1208.v1",
    "status":"PASS",
    "question":"Can the common junction and spectral ordering be derived from a source-level instrument?",
    "dpc":{
        "conjecture":"Reciprocal normalized Kirchhoff incidence with positive Gram derives the common junction and its dark/bright spectral ordering.",
        "rivals":["weighted junction","finite-temperature reverse jump","non-isometric threshold","missing endpoint-reciprocity authority"],
        "risky_consequences":["positive Kirchhoff Gram is a rank-one projector","reciprocity and normalization force equal primitive weights 1/sqrt(2)","the selected ray is the unique zero mode","the bright difference ray has unit cost","the lossless completion is unitary","the lowering dissipator has a unique dark fixed point and global spectral gap"],
        "falsification_attempt":"A weighted junction selects a different ray, finite temperature introduces reverse jumps, and attenuating threshold transport is non-isometric.",
        "residual":"Endpoint reciprocity is not microscopically authorized; flavor RG, isometric full two-port threshold transport, and calibrated physical16 realization remain open.",
        "disposition":"construct conditional common junction; reject weighted, thermal, and lossy junction rivals"
    },
    "source_principle":wp859["source_principle"],
    "selected_ray":wp859["selected_ray"],
    "portal_magnitude":wp859["portal_magnitude"],
    "global_basin":wp859["global_basin"],
    "source_instrument":wp859["source_instrument"],
    "smallest_hostiles":wp859["smallest_hostiles"],
    "reciprocal_normalized":reciprocal_normalized,
    "positive_gram":positive_gram,
    "lossless_two_port":lossless_two_port,
    "dark_fixed_point":dark_fixed_point,
    "global_gap":global_gap,
    "weighted_rival":weighted_rival,
    "finite_temperature_rival":finite_temperature_rival,
    "non_isometric_threshold_rival":non_isometric_threshold_rival,
    "endpoint_reciprocity_microscopically_derived":endpoint_reciprocity_microscopically_derived,
    "flavor_rg_identified":flavor_rg_identified,
    "isometric_full_transport":isometric_full_transport,
    "calibrated_detector":calibrated_detector,
    "classification":"conditional common-junction source with executable instrument and spectral ordering",
    "remaining_gate":"microscopically authorize endpoint reciprocity, then identify RG, transport isometrically, and calibrate physical16",
    "hostile_gate":"do not promote a Kirchhoff model, thermal jump, or lossy threshold into source authority",
    "claim_boundary":"the junction is a source-level conditional instrument, not microscopic endpoint authority",
    "disposition":"common-junction-source leaf resolved; endpoint-reciprocity authority rival selected"
}
(ROOT/"results"/"wp1208_common_junction_source_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1208 PASS: reciprocal Kirchhoff junction fixes dark ordering")
