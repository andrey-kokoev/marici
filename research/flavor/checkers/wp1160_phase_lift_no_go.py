import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = [
    [0, 0, Fraction(1,42), Fraction(13,14), Fraction(1,42), Fraction(1,42)],
    [0, Fraction(25,84), 0, Fraction(1,42), Fraction(97,252), Fraction(37,126)],
    [Fraction(25,56), 0, 0, Fraction(1,42), Fraction(85,168), Fraction(1,42)],
    [Fraction(1,42), Fraction(37,126), Fraction(1,42), 0, 0, Fraction(83,126)],
    [Fraction(1,42), Fraction(1325,3528), Fraction(101,196), 0, Fraction(43,504), 0],
    [Fraction(85,168), Fraction(13,392), Fraction(257,588), Fraction(1,42), 0, 0],
]

row0 = {j for j,x in enumerate(P[0]) if x > 0}
row3 = {j for j,x in enumerate(P[3]) if x > 0}
overlap = sorted(row0 & row3)
assert row0 == {2,3,4,5}
assert row3 == {0,1,2,5}
assert overlap == [2,5]
left_product = P[0][2] * P[3][2]
right_product = P[0][5] * P[3][5]
assert left_product == Fraction(1,1764)
assert right_product == Fraction(83,5292)
assert left_product != right_product

# Orthogonality of rows 0 and 3 would require the two complex contributions
# sqrt(left_product) and sqrt(right_product) to cancel. Equal moduli are
# necessary; the exact inequality therefore excludes every phase lift.
phase_lift_certificates = 0
phase_compatible = False
assert phase_lift_certificates == 0 and phase_compatible is False

result = {
    "schema":"marici.flavor.wp1160.v1",
    "status":"PASS",
    "question":"Does the exact support-four interior point have a unitary phase lift?",
    "dpc":{
        "conjecture":"Phases can make the exact support-four modulus unitary.",
        "rivals":["phase-adjusted lift","two-overlap amplitude obstruction","alternate interior point","nonunitary production map"],
        "risky_consequences":["row orthogonality","two-overlap cancellation","equal amplitude products","phase compatibility"],
        "falsification_attempt":"Rows 0 and 3 overlap only in columns 2 and 5, but their amplitude products are 1/1764 and 83/5292, so cancellation is impossible.",
        "residual":"Another support-four interior point may satisfy the two-overlap amplitude equations.",
        "disposition":"reject the WP1159 point as unistochastic"
    },
    "blocking_row_pair":[0,3],
    "shared_columns":[2,5],
    "amplitude_products":[str(left_product),str(right_product)],
    "phase_compatible":phase_compatible,
    "phase_lift_certificates":phase_lift_certificates,
    "classification":"negative gate: the first exact support-four interior point is not unistochastic",
    "remaining_gate":"search support-four interior points satisfying two-overlap amplitude constraints",
    "hostile_gate":"do not treat support compatibility as phase compatibility",
    "claim_boundary":"the obstruction refutes this interior point only, not the whole support-four polytope",
    "disposition":"phase-lift leaf resolved; phase-compatible interior search selected"
}

(ROOT/"results"/"wp1160_phase_lift_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1160 PASS:",left_product,right_product,phase_lift_certificates)
