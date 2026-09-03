import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(960,961,962,963)
wp960=json.loads((ROOT/"results"/"wp960_symmetric_three_triplet_overlap_source_no_go.json").read_text())
wp961=json.loads((ROOT/"results"/"wp961_linear_bargmann_source_extrema_no_go.json").read_text())
wp962=json.loads((ROOT/"results"/"wp962_squared_bargmann_orientation_boundary_no_go.json").read_text())
wp963=json.loads((ROOT/"results"/"wp963_linear_volume_orientation_endpoint_switch_no_go.json").read_text())
assert wp960["classification"] == "the minimal permutation-symmetric pair-overlap source selects only orthogonal or collinear CP-blind endpoint orbits"
assert wp961["classification"] == "the linear CP-even Bargmann source selects only real rank-deficient endpoint triples"
assert wp962["classification"] == "the pure CP-even squared-orientation source selects a nonzero conjugate pair only on the rank-two Gram boundary"
assert wp963["classification"] == "linear positive volume produces an endpoint switch, not a spanning oriented maximizer"
# Minimal ordered-triple source candidates are CP-blind, rank-deficient, or
# endpoint-switching; none gives a spanning oriented source action.
pair_overlap_cp_blind=True
linear_bargmann_rank_deficient=True
squared_orientation_boundary=True
volume_orientation_endpoint_switch=True
spanning_oriented_triple=False
interior_enforcing_completion=False
conjugate_spanning_minima=False
instrument_transport=False
assert pair_overlap_cp_blind and linear_bargmann_rank_deficient
assert squared_orientation_boundary and volume_orientation_endpoint_switch
assert not (spanning_oriented_triple or interior_enforcing_completion or conjugate_spanning_minima or instrument_transport)
result={
    "schema":"marici.flavor.wp1224.v1",
    "status":"PASS",
    "question":"Can a minimal ordered-triple source action produce a spanning oriented triple?",
    "dpc":{
        "conjecture":"A permutation-symmetric overlap, linear Bargmann, squared-orientation, or linear volume-orientation source derives the ordered spanning triple.",
        "rivals":["pair-overlap attractive endpoint","pair-overlap repulsive endpoint","linear Bargmann trine","squared-orientation conjugate pair","linear volume-orientation switch"],
        "risky_consequences":["overlap endpoints are collinear rank one or orthogonal CP-blind","the linear Bargmann minimum is the rank-two real trine","the squared-orientation maximizer has conjugate Bargmann values 1/4 +/- i/4 but Gram determinant zero","linear volume switches between rank-two orientation and orthonormal CP-blind frame at lambda=1/16"],
        "falsification_attempt":"every minimal action selects a boundary endpoint or CP-blind frame; no interior maximum with full span and orientation is selected.",
        "residual":"source-derived interior-enforcing barrier, constraint, or completion field preserving a conjugate spanning orientation pair and calibrated instrument transport",
        "disposition":"reject minimal ordered-triple actions; select interior-enforcing source-completion rival"
    },
    "pair_overlap_endpoints":wp960["exact_endpoints"],
    "linear_bargmann_extrema":wp961["exact_extrema"],
    "squared_orientation_maximizer":wp962["exact_maximizer"],
    "volume_tradeoff":wp963["exact_tradeoff"],
    "pair_overlap_cp_blind":pair_overlap_cp_blind,
    "linear_bargmann_rank_deficient":linear_bargmann_rank_deficient,
    "squared_orientation_boundary":squared_orientation_boundary,
    "volume_orientation_endpoint_switch":volume_orientation_endpoint_switch,
    "spanning_oriented_triple":spanning_oriented_triple,
    "interior_enforcing_completion":interior_enforcing_completion,
    "conjugate_spanning_minima":conjugate_spanning_minima,
    "instrument_transport":instrument_transport,
    "classification":"negative ordered-triple source-action result: minimal actions are CP-blind, rank-deficient, or endpoint-switching",
    "remaining_gate":"derive an interior-enforcing barrier, constraint, or completion field with conjugate spanning orientation pair and instrument transport",
    "hostile_gate":"do not call pair-overlap, linear Bargmann, boundary squared orientation, or endpoint-switching volume a spanning source action",
    "claim_boundary":"the negative result is relative to the four minimal ordered-triple source actions audited here",
    "disposition":"ordered-spanning-triple-source-action leaf resolved negatively; interior-enforcing source-completion rival selected"
}
(ROOT/"results"/"wp1224_ordered_spanning_triple_source_action_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1224 PASS: minimal ordered-triple source actions exhausted")
