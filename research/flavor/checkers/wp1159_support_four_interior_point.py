import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)
zero_carrier = [(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)]
carrier = [tuple(c for c in range(6) if c not in zero_carrier[i]) for i in range(6)]

# Exact interior point obtained by maximizing the minimum carrier entry in the
# fixed-q doubly stochastic polytope; t=1/42 is the optimum certificate used
# by the construction, and every carrier entry is at least t.
P = [
    [0, 0, Fraction(1,42), Fraction(13,14), Fraction(1,42), Fraction(1,42)],
    [0, Fraction(25,84), 0, Fraction(1,42), Fraction(97,252), Fraction(37,126)],
    [Fraction(25,56), 0, 0, Fraction(1,42), Fraction(85,168), Fraction(1,42)],
    [Fraction(1,42), Fraction(37,126), Fraction(1,42), 0, 0, Fraction(83,126)],
    [Fraction(1,42), Fraction(1325,3528), Fraction(101,196), 0, Fraction(43,504), 0],
    [Fraction(85,168), Fraction(13,392), Fraction(257,588), Fraction(1,42), 0, 0],
]

assert all(P[i][j] > 0 for i,row in enumerate(carrier) for j in row)
assert all(P[i][j] == 0 for i in range(6) for j in range(6) if j not in carrier[i])
assert all(sum(row) == 1 for row in P)
assert all(sum(P[i][j] for i in range(6)) == 1 for j in range(6))
assert [sum(P[i][j]*q[j] for j in range(6)) for i in range(6)] == [u]*6
assert min(x for row in P for x in row if x > 0) == Fraction(1,42)
assert [sum(x > 0 for x in row) for row in P] == [4]*6
assert [sum(P[i][j] > 0 for i in range(6)) for j in range(6)] == [4]*6
assert all((P[i][j] > 0) == (j in carrier[i]) for i in range(6) for j in range(6))

# Carrier and matrix are single-overlap free, satisfying the necessary support
# condition for a unitary modulus. No phase lift is asserted here.
row_sets = [frozenset(j for j,x in enumerate(row) if x > 0) for row in P]
col_sets = [frozenset(i for i in range(6) if P[i][j] > 0) for j in range(6)]
assert all(len(row_sets[i] & row_sets[j]) != 1 for i in range(6) for j in range(i+1,6))
assert all(len(col_sets[i] & col_sets[j]) != 1 for i in range(6) for j in range(i+1,6))
phase_lift_certificates = 0
assert phase_lift_certificates == 0

result = {
    "schema":"marici.flavor.wp1159.v1",
    "status":"PASS",
    "question":"Does the support-four carrier have an interior fixed-q doubly stochastic point?",
    "dpc":{
        "conjecture":"The support-four carrier polytope has a point with every allowed edge positive.",
        "rivals":["boundary-only polytope","interior algebraic point","phase lift","physical production map"],
        "risky_consequences":["all 24 carrier entries positive","minimum entry 1/42","row and column sums one","Pq=u"],
        "falsification_attempt":"The exact rational matrix passes every algebraic test and realizes exact row/column support four.",
        "residual":"A unitary phase lift and physical production map remain unestablished.",
        "disposition":"accept interior algebraic existence and select the phase-lift test"
    },
    "zero_carrier_pattern":[list(x) for x in zero_carrier],
    "witness_matrix":[[str(x) for x in row] for row in P],
    "minimum_positive_entry":"1/42",
    "row_support":[4]*6,
    "column_support":[4]*6,
    "positive_entries":24,
    "single_overlap_free":True,
    "phase_lift_certificates":phase_lift_certificates,
    "classification":"productive algebraic gate: exact support-four fixed-q doubly stochastic maps exist",
    "remaining_gate":"test whether this exact support-four modulus has a unitary phase lift",
    "hostile_gate":"do not treat the interior doubly stochastic point as unitary or physical",
    "claim_boundary":"the witness is exact algebra only; unistochasticity remains open",
    "disposition":"support-four interior leaf resolved; phase-lift rival selected"
}

(ROOT/"results"/"wp1159_support_four_interior_point.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1159 PASS:",min(x for row in P for x in row if x > 0),phase_lift_certificates)
