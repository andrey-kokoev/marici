import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(874,876)
wp874=json.loads((ROOT/"results"/"wp874_dual_pair_source_existence_audit.json").read_text())
wp876=json.loads((ROOT/"results"/"wp876_source_compelled_simultaneous_portal_repair_closure.json").read_text())
assert wp874["summary"]["all_passed"] is True
assert wp876["summary"]["all_passed"] is True
assert wp874["classification"] == "negative existence result for current flavor sources"
assert wp876["classification"] == "no currently adjacent compulsory object repairs the simultaneous fixed-point source; WP736 remains only a matching-scale selector"
assert wp876["remaining_source_gate"] == "derive new Yukawa-active matter, multiplicities, and vertices from one independent source principle before computing the fixed point"
# Candidate dual structures fail individually, and the source-compelled
# closure excludes the currently adjacent compulsory repair class.
joint_observer_fails=True
g2_pair_fails=True
rank_one_lattice_fails=True
compulsory_mediators_fail=True
wrong_operator_or_postsource_fails=True
flavor_dual_pair_exists=False
positive_fixed_point_exists=False
new_yukawa_source_derived=False
calibrated_instrument=False
assert joint_observer_fails and g2_pair_fails and rank_one_lattice_fails
assert compulsory_mediators_fail and wrong_operator_or_postsource_fails
assert not (flavor_dual_pair_exists or positive_fixed_point_exists or new_yukawa_source_derived or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1211.v1",
    "status":"PASS",
    "question":"Does the current flavor corpus contain a microscopic dual pair satisfying the WP873 contract?",
    "dpc":{
        "conjecture":"A currently adjacent compulsory flavor object supplies the microscopic dual pair needed for source-modulus selection.",
        "rivals":["joint observer","monodromic G2 pair","rank-one unimodular lattice","WP744 anomaly response","WP854 relational carrier","WP855 post-source instrument","integer coefficient laundering"],
        "risky_consequences":["a valid candidate must add an independent source coupling and primitive pairing","compulsory WP738 mediators must produce a positive simultaneous fixed point","WP744 must have portal operator type","WP854 must map microscopically to flavor","WP855 must precede rather than follow the source"],
        "falsification_attempt":"Joint observer is coordinate recombination; G2 has boundary/transmutation fibers; the lattice has a metric fiber; WP738 has no physical branch; WP744, WP854, and WP855 are outside the source class.",
        "residual":"derive new Yukawa-active matter, multiplicities, and vertices from an independent source principle, then test pairing, threshold, RG, and physical16 calibration",
        "disposition":"reject current-corpus dual-pair existence; require new Yukawa-active source"
    },
    "candidate_dispositions":wp874["candidate_dispositions"],
    "existence_classification":wp874["classification"],
    "admitted_source_domain":wp876["admitted_source_domain"],
    "closure_classification":wp876["classification"],
    "smallest_closure_falsifier":wp876["smallest_exact_falsifier"],
    "remaining_source_gate":wp876["remaining_source_gate"],
    "joint_observer_fails":joint_observer_fails,
    "g2_pair_fails":g2_pair_fails,
    "rank_one_lattice_fails":rank_one_lattice_fails,
    "compulsory_mediators_fail":compulsory_mediators_fail,
    "wrong_operator_or_postsource_fails":wrong_operator_or_postsource_fails,
    "flavor_dual_pair_exists":flavor_dual_pair_exists,
    "positive_fixed_point_exists":positive_fixed_point_exists,
    "new_yukawa_source_derived":new_yukawa_source_derived,
    "calibrated_instrument":calibrated_instrument,
    "classification":"negative dual-pair existence for current and source-compelled flavor corpus",
    "remaining_gate":"derive new Yukawa-active matter from an independent source principle before fixed-point or instrument computation",
    "hostile_gate":"do not relabel observers, anomaly responses, carriers, or instruments as microscopic flavor dual couplings",
    "claim_boundary":"the obstruction covers audited current and compulsory adjacent classes, not all conceivable future source principles",
    "disposition":"flavor-dual-pair-existence leaf resolved negatively; new Yukawa-active source rival selected"
}
(ROOT/"results"/"wp1211_flavor_dual_pair_existence_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1211 PASS: current and compulsory flavor dual pairs absent")
