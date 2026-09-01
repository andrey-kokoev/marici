import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = [
    [Fraction(1,20), Fraction(31,84), Fraction(61,105), 0, 0, 0],
    [Fraction(59,120), 0, Fraction(2,15), 0, Fraction(3,8), 0],
    [Fraction(11,24), 0, 0, 0, Fraction(13,24), 0],
    [0, Fraction(5,18), 0, Fraction(1,12), 0, Fraction(23,36)],
    [0, Fraction(89,252), Fraction(2,7), 0, 0, Fraction(13,36)],
    [0, 0, 0, Fraction(11,12), Fraction(1,12), 0],
]
P = [[Fraction(x) for x in row] for row in P]

row0_support = {j for j,x in enumerate(P[0]) if x > 0}
row2_support = {j for j,x in enumerate(P[2]) if x > 0}
overlap = sorted(row0_support & row2_support)
assert row0_support == {0,1,2}
assert row2_support == {0,4}
assert overlap == [0]
unique_overlap_product = P[0][0] * P[2][0]
assert unique_overlap_product == Fraction(11,480)
assert unique_overlap_product != 0

# For a unitary lift S with |S_ij|^2=P_ij, rows 0 and 2 must be orthogonal.
# Their support overlap is only column 0, so the inner product is a single
# nonzero product and cannot cancel.
phase_cancellation_terms = len(overlap)
unistochastic_lifts = 0
assert phase_cancellation_terms == 1
assert unistochastic_lifts == 0

# This is a support obstruction, not merely a phase failure.
phase_freedom_can_repair = False
support_graph_admissible = False
assert phase_freedom_can_repair is False
assert support_graph_admissible is False

result = {
    "schema":"marici.flavor.wp1154.v1",
    "status":"PASS",
    "question":"Does the WP1153 support-three witness have a unistochastic lift?",
    "dpc":{
        "conjecture":"The support-three doubly stochastic witness is the modulus of a unitary S-matrix.",
        "rivals":["phase-adjusted lift","support obstruction","alternate support-three witness","nonunitary production map"],
        "risky_consequences":["row orthogonality","single-overlap cancellation impossible","nonzero product 11/480","support graph admissibility"],
        "falsification_attempt":"Rows 0 and 2 overlap only in column 0, so their unitary inner product would be one nonzero term; no phases can cancel it.",
        "residual":"Another support-three pattern may have an admissible support graph.",
        "disposition":"reject the WP1153 witness as unistochastic"
    },
    "blocking_row_pair":[0,2],
    "shared_column":0,
    "unique_overlap_product":str(unique_overlap_product),
    "phase_cancellation_terms":phase_cancellation_terms,
    "phase_freedom_can_repair":phase_freedom_can_repair,
    "support_graph_admissible":support_graph_admissible,
    "unistochastic_lifts":unistochastic_lifts,
    "classification":"negative gate: the first support-three witness is not unistochastic",
    "remaining_gate":"search support-three candidates for unistochastic-admissible support graphs",
    "hostile_gate":"do not treat doubly stochastic support as unitary when a row pair has one shared column",
    "claim_boundary":"the obstruction refutes this witness only, not every support-three pattern",
    "disposition":"unistochastic leaf resolved; support-graph search selected"
}

(ROOT/"results"/"wp1154_unistochastic_witness_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1154 PASS:",unique_overlap_product,unistochastic_lifts)
