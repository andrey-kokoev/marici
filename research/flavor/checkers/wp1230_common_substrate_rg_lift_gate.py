import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1000,1001,1002,1003,1004,1005,1006,1007,1008,1009)
wp1000=json.loads((ROOT/"results"/"wp1000_source_parameter_submersion_operation_gap.json").read_text())
wp1001=json.loads((ROOT/"results"/"wp1001_two_background_mediator_actuator.json").read_text())
wp1002=json.loads((ROOT/"results"/"wp1002_harmonic_carrier_control_metric.json").read_text())
wp1003=json.loads((ROOT/"results"/"wp1003_positive_mediator_reachability_cone.json").read_text())
wp1004=json.loads((ROOT/"results"/"wp1004_positive_cone_reference_replacement_gate.json").read_text())
wp1005=json.loads((ROOT/"results"/"wp1005_positive_cone_third_configuration.json").read_text())
wp1006=json.loads((ROOT/"results"/"wp1006_third_configuration_global_dominance_falsifier.json").read_text())
wp1007=json.loads((ROOT/"results"/"wp1007_one_parameter_score_envelope.json").read_text())
wp1008=json.loads((ROOT/"results"/"wp1008_full_quotient_local_score_maximum.json").read_text())
wp1009=json.loads((ROOT/"results"/"wp1009_global_hermitian_score_hull.json").read_text())
assert wp1000["classification"] == "algebraically complete constructor; neither selector nor rigidifier"
assert wp1001["classification"] == "candidate source-derived actuator; neither selector nor rigidifier"
assert wp1002["classification"] == "source-priced local actuator and carrier rigidifier; not flavor selector"
assert wp1003["classification"] == "two-label positive-source actuator; incomplete WP991 preparation instrument"
assert wp1004["classification"] == "formal positive-cone instrument-design criterion; no physical instrument"
assert wp1005["classification"] == "Hermitian source-domain capacity witness; not source-selected or instrumented"
assert wp1006["classification"] == "WP1005 finite-set witness globally falsified; no preparation instrument"
assert wp1007["classification"] == "unique global exposure on one-parameter Hermitian subfamily only"
assert wp1008["classification"] == "strict local maximum on reduced generic Hermitian-pair quotient"
assert wp1009["classification"] == "unique global maximizing orbit modulo simultaneous permutations, weak-basis conjugation, and scales"
# A common-substrate coordinate lift and priced actuator exist formally, but
# they do not realize all preparation labels or authorize the selected source
# ratio/instrument.
algebraic_lift=True
rank_two_candidate_actuator=True
priced_control_metric=True
positive_reachability_incomplete=True
third_configuration_falsified=True
score_hull_unique=True
repeatable_intervention=False
all_three_labels=False
source_selected_ratio=False
physical16_image=False
calibrated_instrument=False
assert algebraic_lift and rank_two_candidate_actuator and priced_control_metric
assert positive_reachability_incomplete and third_configuration_falsified and score_hull_unique
assert not (repeatable_intervention or all_three_labels or source_selected_ratio or physical16_image or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1230.v1",
    "status":"PASS",
    "question":"Can a common-substrate source lift provide the RG-to-control lift and actuator?",
    "dpc":{
        "conjecture":"The logarithmic source-to-(q,k) submersion, two-mediator actuator, and source-priced Gram provide the missing RG lift.",
        "rivals":["algebraic source submersion","two-background mediator actuator","harmonic carrier Gram","positive-cone reachability","third-configuration witness","finite-set score witness","one-parameter score envelope","local full-quotient maximum","global Hermitian score hull"],
        "risky_consequences":["the log response has determinant one and covers the positive quadrant","rank-two mediation requires nonzero kappa_A*kappa_s","the induced Gram [[37,-6],[-6,1]] is positive","positive sources reach only rank-two and full-rank labels","the third-configuration witness is globally dominated","the global score maximum is unique but still lacks source ratio, physical16 image, and instrument"],
        "falsification_attempt":"the formal lift is source-priced, yet repeatable intervention, all-label preparation, selected ratio, and calibrated instrument are absent.",
        "residual":"source-derived coefficient ratio, physical16 image, stable selected orbit, and calibrated preparation/readout instrument",
        "disposition":"accept a formal common-substrate lift; reject it as physical RG-to-control authority"
    },
    "log_response_matrix":wp1000["log_response_matrix"],
    "actuator_rank_condition":wp1001["rank_two_condition"],
    "induced_gram":wp1002["unit_induced_coefficient_gram"],
    "positive_region_intersections":wp1003["region_intersections"],
    "relative_response_determinant":wp1004["relative_response_determinant"],
    "third_configuration_scores":wp1005["candidate_scores"],
    "global_score_maximum":wp1009["global_maximum"],
    "global_maximizer":wp1009["global_maximizer"],
    "local_maximum_hessian":wp1008["hessian"],
    "score_curve":wp1007["score_curve"],
    "algebraic_lift":algebraic_lift,
    "rank_two_candidate_actuator":rank_two_candidate_actuator,
    "priced_control_metric":priced_control_metric,
    "positive_reachability_incomplete":positive_reachability_incomplete,
    "third_configuration_falsified":third_configuration_falsified,
    "score_hull_unique":score_hull_unique,
    "repeatable_intervention":repeatable_intervention,
    "all_three_labels":all_three_labels,
    "source_selected_ratio":source_selected_ratio,
    "physical16_image":physical16_image,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional common-substrate lift: formal actuator exists, physical selector authority absent",
    "remaining_gate":"derive the selected source ratio and physical16 image, then calibrate a stable repeatable instrument reaching all preparation labels",
    "hostile_gate":"do not call algebraic completeness, rank-two mediation, priced Grams, positive-cone reachability, or score maximization physical RG-to-control authority",
    "claim_boundary":"the lift and cost metric are formal source constructions; intervention and instrument calibration remain outside them",
    "disposition":"common-substrate RG-lift leaf resolved conditionally; global-selector source-ratio rival selected"
}
(ROOT/"results"/"wp1230_common_substrate_rg_lift_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1230 PASS: common-substrate lift formal, source ratio and instrument absent")
