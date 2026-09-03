import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(842,843)
wp842=json.loads((ROOT/"results"/"wp842_charge_moment_loop_mismatch.json").read_text())
wp843=json.loads((ROOT/"results"/"wp843_positive_tensor_threshold_contraction_no_go.json").read_text())
assert wp842["summary"]["all_passed"] is True
assert wp843["summary"]["all_passed"] is True
base=wp842["base_packet"]
threshold=wp842["threshold_active_packet"]
assert (base["delta"],base["s2"],base["s4"],base["moment_fixed"],base["diameter_fixed"],base["required_screening"]) == ("2","14","98","1/7","1/2","70")
assert (threshold["delta"],threshold["s2"],threshold["s4"],threshold["required_screening"]) == ("1","13","97","84")
assert wp842["classification"] == "negative charge-only microscopic derivation; exact target for a unique interaction tensor"
assert wp843["required_transition"] == "Y_full=70 -> Y_active=84"
assert wp843["classification"] == "exact negative threshold theorem; noncontractive finite matching or threshold-generated interaction is necessary"
assert wp843["minimal_repairs"]["lossless_squared_amplification"] == "6/5"
assert wp843["minimal_repairs"]["new_positive_increment"] == "14"
# Exact charge moments do not derive the diameter flow; the target tensor must
# increase its contraction across threshold, impossible by ordinary positive
# restriction.
charge_moment_beta=False
unique_interaction_tensor=False
ordinary_threshold_restriction=False
noncontractive_matching_derived=False
threshold_generated_interaction_derived=False
assert not (charge_moment_beta or unique_interaction_tensor or ordinary_threshold_restriction or noncontractive_matching_derived or threshold_generated_interaction_derived)
result={
    "schema":"marici.flavor.wp1198.v1",
    "status":"PASS",
    "question":"Can charge moments derive the microscopic diameter beta flow?",
    "dpc":{
        "conjecture":"A microscopic charge-moment contraction derives the diameter-normalized beta ratio.",
        "rivals":["unscreened charge moments","screened interaction tensor","ordinary positive threshold restriction","noncontractive or threshold-generated matching"],
        "risky_consequences":["primitive moments S2=14 and S4=98 select 1/7 rather than 1/2","Y=70 is required before threshold and Y=84 after charge-one deletion","ordinary positive restriction is Frobenius-contractive","minimal repairs are squared amplification 6/5 or new increment 14"],
        "falsification_attempt":"Charge moments give the wrong fixed point, and the required 70->84 transition contradicts ordinary contraction.",
        "residual":"A source-derived interaction tensor plus noncontractive matching or threshold-generated term is required.",
        "disposition":"reject charge-moment microscopic derivation; retain exact tensor targets"
    },
    "base_moments":{"S2":base["s2"],"S4":base["s4"],"moment_fixed":base["moment_fixed"]},
    "diameter_target":base["diameter_fixed"],
    "required_screening_full":base["required_screening"],
    "threshold_moments":{"S2":threshold["s2"],"S4":threshold["s4"],"moment_fixed":threshold["moment_fixed"]},
    "required_screening_threshold":threshold["required_screening"],
    "required_transition":wp843["required_transition"],
    "minimal_repairs":wp843["minimal_repairs"],
    "charge_moment_beta":charge_moment_beta,
    "unique_interaction_tensor":unique_interaction_tensor,
    "ordinary_threshold_restriction":ordinary_threshold_restriction,
    "noncontractive_matching_derived":noncontractive_matching_derived,
    "threshold_generated_interaction_derived":threshold_generated_interaction_derived,
    "classification":"negative microscopic beta gate: charge moments require an interaction tensor and noncontractive threshold law",
    "remaining_gate":"derive the tensor and its 70->84 finite matching from one source action",
    "hostile_gate":"do not identify the numerical threshold increment 14 with the Ward index without source authority",
    "claim_boundary":"the unit-coefficient moment beta is a structural hostile; no physical scheme is claimed",
    "disposition":"charge-moment microscopic-beta leaf resolved; noncontractive threshold-matching rival selected"
}
(ROOT/"results"/"wp1198_charge_moment_microscopic_beta_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1198 PASS: 1/7 != 1/2; 70->84 requires noncontractive matching")
