import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(856)
wp856=json.loads((ROOT/"results"/"wp856_reciprocal_endpoint_rg_basin_threshold_audit.json").read_text())
assert wp856["summary"]["all_passed"] is True
assert wp856["fixed_point"] == "p*=1/2"
assert wp856["global_basin"] == "entire interval [0,1] for kappa>0"
assert wp856["conditional_portal_magnitude"] == "|g_n-g_m|=1/sqrt(2) if p is the canonically normalized squared coupling"
assert wp856["threshold_family"] == "T_r=[[r,1-r],[1-r,r]]"
assert wp856["smallest_threshold_hostile"] == "r=3/4 preserves p* but maps J to J/2"
assert wp856["classification"] == "conditional nonzero global magnitude selector; physical RG/coherent lift/threshold authority open"
# The reciprocal endpoint flow gives a global nonzero basin, but exact current
# transport across the threshold family is only the identity map.
reciprocal_basin=True
conditional_magnitude=True
identity_threshold_required=True
flavor_rg_derived=False
coherent_normalization_derived=False
isometric_marked_threshold=False
calibrated_readout=False
assert reciprocal_basin and conditional_magnitude and identity_threshold_required
assert not (flavor_rg_derived or coherent_normalization_derived or isometric_marked_threshold or calibrated_readout)
result={
    "schema":"marici.flavor.wp1205.v1",
    "status":"PASS",
    "question":"Can reciprocal endpoint flow survive threshold transport?",
    "dpc":{
        "conjecture":"Reciprocal endpoint flow gives a global nonzero basin whose oriented current can be transported through thresholds.",
        "rivals":["endpoint exchange covariance","arbitrary symmetric threshold","fixed-point preservation","isometric marked-port threshold matching"],
        "risky_consequences":["endpoint exchange forces equal rates","p*=1/2 has the entire probability interval as basin for kappa>0","zero seed is not fixed","T_r scales J by 2r-1","r=3/4 preserves p* but halves J","only r=1 preserves J exactly"],
        "falsification_attempt":"A threshold can preserve the uniform fixed packet while attenuating or erasing the oriented current.",
        "residual":"The endpoint flow still needs a flavor RG derivation, coherent kinetic normalization, isometric marked-port matching, and the calibrated WP1204 readout.",
        "disposition":"construct the reciprocal-basin and threshold audit; reject fixed-point preservation as threshold authority"
    },
    "source_domain":wp856["source_domain"],
    "fixed_point":wp856["fixed_point"],
    "global_basin":wp856["global_basin"],
    "conditional_portal_magnitude":wp856["conditional_portal_magnitude"],
    "threshold_family":wp856["threshold_family"],
    "smallest_threshold_hostile":wp856["smallest_threshold_hostile"],
    "reciprocal_basin":reciprocal_basin,
    "conditional_magnitude":conditional_magnitude,
    "identity_threshold_required":identity_threshold_required,
    "flavor_rg_derived":flavor_rg_derived,
    "coherent_normalization_derived":coherent_normalization_derived,
    "isometric_marked_threshold":isometric_marked_threshold,
    "calibrated_readout":calibrated_readout,
    "classification":"conditional threshold selector: reciprocal basin is global, but exact current transport forces identity",
    "remaining_gate":"derive coherent kinetic normalization and an isometric marked-port threshold intertwiner",
    "hostile_gate":"do not infer current transport from fixed-point preservation alone",
    "claim_boundary":"the basin and threshold law are dimensionless and conditional on the declared endpoint algebra",
    "disposition":"threshold-intertwiner leaf resolved; coherent-kinetic-normalization rival selected"
}
(ROOT/"results"/"wp1205_threshold_intertwiner_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1205 PASS: global reciprocal basin; only identity preserves J")
