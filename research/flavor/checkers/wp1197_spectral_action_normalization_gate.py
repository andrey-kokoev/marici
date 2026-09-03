import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(839,840,841)
wp839=json.loads((ROOT/"results"/"wp839_spectral_action_coefficient_fiber.json").read_text())
wp840=json.loads((ROOT/"results"/"wp840_reciprocal_spectral_self_duality_normalization_fiber.json").read_text())
wp841=json.loads((ROOT/"results"/"wp841_charge_diameter_normalized_global_portal_flow.json").read_text())
assert wp839["summary"]["all_passed"] is True
assert wp840["summary"]["all_passed"] is True
assert wp841["summary"]["all_passed"] is True
assert wp839["hostile_packets"]["A"]["m_squared"] == "1"
assert wp839["hostile_packets"]["B"]["m_squared"] == "2"
assert wp839["hostile_packets"]["A"]["portal"] == "1/sqrt(2)"
assert wp839["hostile_packets"]["B"]["portal"] == "1/sqrt(3)"
assert wp839["first_nonfaithful_arrow"] == "fixed finite spectral packet -> choice of spectral-action profile and moment ratio"
assert wp840["classification"] == "conditional relative-scale selector; absolute scale and coupling normalization remain unselected"
assert wp840["hostile_pair"]["eta_2"]["x_star"] == "1/2"
assert wp840["hostile_pair"]["eta_3"]["x_star"] == "1/3"
assert wp841["prediction"]["x_star"] == "1/2"
assert wp841["prediction"]["portal"] == "1/sqrt(2)"
assert wp841["prediction"]["basin"] == "entire positive x half-line"
assert wp841["smallest_threshold_falsifier"] == "decouple charge 1: active diameter 2->1 and selected x 1/2->1"
# The primitive charge diameter normalizes a candidate global flow, but the
# microscopic beta ratio is not derived; the threshold deletion moves x.
microscopic_action_profile=False
absolute_scale=False
coupling_normalization=False
invariant_candidate_normalization=True
threshold_survival=False
assert invariant_candidate_normalization
assert not (microscopic_action_profile or absolute_scale or coupling_normalization or threshold_survival)
result={
    "schema":"marici.flavor.wp1197.v1",
    "status":"PASS",
    "question":"Can spectral-action normalization select the source scale?",
    "dpc":{
        "conjecture":"A source-normalized spectral action selects the Ward scale and portal flow.",
        "rivals":["polynomial spectral action","reciprocal self-duality","charge-diameter beta flow","microscopic interaction-tensor flow"],
        "risky_consequences":["polynomial packets select squared scales 1 and 2 and portals 1/sqrt(2), 1/sqrt(3)","reciprocity selects ratios but not absolute scale or eta","charge diameter gives x*=1/2 and global positive basin","charge-1 decoupling moves x* to 1"],
        "falsification_attempt":"Polynomial coefficients, reciprocal normalization, and threshold deletion all change the selected physical coordinate or scale.",
        "residual":"A microscopic interaction tensor must derive the diameter beta ratio and survive finite threshold matching.",
        "disposition":"construct a charge-diameter candidate; reject source-complete spectral normalization"
    },
    "polynomial_stationary_law":wp839["stationary_law"],
    "polynomial_scale_fiber":["1","2"],
    "reciprocal_action":wp840["reciprocal_action"],
    "reciprocal_normalization_fiber":["eta=2 -> x*=1/2","eta=3 -> x*=1/3"],
    "charge_diameter":wp841["source_invariant"],
    "candidate_beta":wp841["candidate_beta"],
    "selected_coordinate":wp841["prediction"]["x_star"],
    "selected_portal":wp841["prediction"]["portal"],
    "global_basin":wp841["prediction"]["basin"],
    "lyapunov_identity":wp841["lyapunov_identity"],
    "threshold_falsifier":wp841["smallest_threshold_falsifier"],
    "invariant_candidate_normalization":invariant_candidate_normalization,
    "microscopic_action_profile":microscopic_action_profile,
    "absolute_scale":absolute_scale,
    "coupling_normalization":coupling_normalization,
    "threshold_survival":threshold_survival,
    "classification":"conditional spectral normalization: invariant charge-diameter flow selected; microscopic beta authority absent",
    "remaining_gate":"derive the charge-moment interaction tensor and finite threshold matching",
    "hostile_gate":"do not treat diameter normalization as microscopic beta authority",
    "claim_boundary":"the selected x*=1/2 flow is a candidate beta constructor, not a derived microscopic action",
    "disposition":"spectral-action normalization leaf resolved; charge-moment microscopic-beta rival selected"
}
(ROOT/"results"/"wp1197_spectral_action_normalization_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1197 PASS: x*=1/2; microscopic beta open")
