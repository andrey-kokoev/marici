import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

# Exact support-three witness found by enumerating row support-three patterns.
rows = [
    [Fraction(1,20), Fraction(31,84), Fraction(61,105), 0, 0, 0],
    [Fraction(59,120), 0, Fraction(2,15), 0, Fraction(3,8), 0],
    [Fraction(11,24), 0, 0, 0, Fraction(13,24), 0],
    [0, Fraction(5,18), 0, Fraction(1,12), 0, Fraction(23,36)],
    [0, Fraction(89,252), Fraction(2,7), 0, 0, Fraction(13,36)],
    [0, 0, 0, Fraction(11,12), Fraction(1,12), 0],
]
P = [[Fraction(x) for x in row] for row in rows]

assert all(all(x >= 0 for x in row) for row in P)
assert all(sum(row) == 1 for row in P)
assert all(sum(P[i][j] for i in range(6)) == 1 for j in range(6))
assert [sum(P[i][j]*q[j] for j in range(6)) for i in range(6)] == [u]*6
row_support = [sum(x > 0 for x in row) for row in P]
col_support = [sum(P[i][j] > 0 for i in range(6)) for j in range(6)]
assert row_support == [3,3,2,3,3,2]
assert col_support == [3,3,3,2,3,2]
assert max(row_support) == 3

# The pattern occurred at ordinal 2232 in the checker enumeration. Its
# existence refutes a support-three no-go, but double stochasticity alone does
# not prove that P is |S|^2 for a unitary S.
unistochastic_certificate = 0
physical_production_maps = 0
locality_certificates = 0
assert unistochastic_certificate == physical_production_maps == locality_certificates == 0

result = {
    "schema":"marici.flavor.wp1153.v1",
    "status":"PASS",
    "question":"Do support-three doubly stochastic fixed-q maps exist?",
    "dpc":{
        "conjecture":"Support-three doubly stochastic fixed-q maps exist after the support-two no-go.",
        "rivals":["support-two map","support-three algebraic witness","unistochastic lift","physical production locality"],
        "risky_consequences":["nonnegative entries","row and column sums one","Pq=u","maximum row support three"],
        "falsification_attempt":"An exact witness passes all four tests, refuting a support-three no-go.",
        "residual":"The witness still needs a unistochastic lift, production maps, and locality certificates.",
        "disposition":"accept support-three algebraic existence; select the unistochastic gate"
    },
    "witness_pattern_zero_based":[[0,1,2],[0,2,4],[0,3,4],[1,3,5],[1,2,5],[3,4,5]],
    "witness_matrix":[[str(x) for x in row] for row in P],
    "row_support":row_support,
    "column_support":col_support,
    "maximum_row_support":max(row_support),
    "row_sums_one":True,
    "column_sums_one":True,
    "target_rows":str(u),
    "unistochastic_certificate":unistochastic_certificate,
    "physical_production_maps":physical_production_maps,
    "locality_certificates":locality_certificates,
    "classification":"productive algebraic gate: support-three fixed-q doubly stochastic maps exist",
    "remaining_gate":"test whether the witness is unistochastic and physically local",
    "hostile_gate":"do not treat double stochasticity as unitarity or source locality",
    "claim_boundary":"existence is exact algebra; unitary and physical realization remain open",
    "disposition":"support-three leaf resolved; unistochastic rival selected"
}

(ROOT/"results"/"wp1153_support_three_witness.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1153 PASS:",max(row_support),unistochastic_certificate)
