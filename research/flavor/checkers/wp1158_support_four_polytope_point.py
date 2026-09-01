import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

# A graph-compatible support-four carrier, written as the complement of a
# support-two zero pattern. The displayed P is a boundary point of that
# carrier's fixed-q polytope.
zero_carrier = [(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)]
carrier = [tuple(c for c in range(6) if c not in zero_carrier[i]) for i in range(6)]
P = [
    [0, 0, 0, Fraction(11,12), Fraction(1,12), 0],
    [0, Fraction(11,36), 0, 0, Fraction(7,18), Fraction(11,36)],
    [Fraction(5,12), 0, 0, Fraction(1,12), Fraction(1,2), 0],
    [0, Fraction(11,36), 0, 0, 0, Fraction(25,36)],
    [Fraction(1,60), Fraction(7,18), Fraction(17,30), 0, Fraction(1,36), 0],
    [Fraction(17,30), 0, Fraction(13,30), 0, 0, 0],
]

carrier_sets = [set(r) for r in carrier]
assert [len(r) for r in carrier] == [4]*6
assert all(j in carrier_sets[i] or P[i][j] == 0 for i in range(6) for j in range(6))
assert all(sum(P[i][j] > 0 for i in range(6)) <= 4 for j in range(6))
assert all(all(x >= 0 for x in row) for row in P)
assert all(sum(row) == 1 for row in P)
assert all(sum(P[i][j] for i in range(6)) == 1 for j in range(6))
assert [sum(P[i][j]*q[j] for j in range(6)) for i in range(6)] == [u]*6

# The carrier is single-overlap free by the WP1157 zero-complement argument.
carrier_cols = [{i for i,row in enumerate(carrier_sets) if j in row} for j in range(6)]
assert all(len(carrier_sets[i] & carrier_sets[j]) != 1 for i in range(6) for j in range(i+1,6))
assert all(len(carrier_cols[i] & carrier_cols[j]) != 1 for i in range(6) for j in range(i+1,6))

allowed_edges = sum(len(r) for r in carrier)
positive_entries = sum(x > 0 for row in P for x in row)
boundary_zeros = allowed_edges - positive_entries
assert (allowed_edges,positive_entries,boundary_zeros) == (24,16,8)
row_support = [sum(x > 0 for x in row) for row in P]
col_support = [sum(P[i][j] > 0 for i in range(6)) for j in range(6)]
assert row_support == [2,3,3,2,4,2]
assert col_support == [3,3,2,2,4,2]

# Carrier compatibility is not an interior witness or phase certificate.
interior_support_four_point = False
phase_lift_certificate = 0
assert interior_support_four_point is False and phase_lift_certificate == 0

result = {
    "schema":"marici.flavor.wp1158.v1",
    "status":"PASS",
    "question":"Does a graph-compatible support-four carrier contain a fixed-q doubly stochastic point?",
    "dpc":{
        "conjecture":"A single-overlap-free support-four carrier contains a fixed-q doubly stochastic point.",
        "rivals":["empty carrier polytope","boundary polytope point","interior support-four point","phase lift"],
        "risky_consequences":["carrier row support four","nonnegative entries","row and column sums one","Pq=u"],
        "falsification_attempt":"An exact rational boundary point passes all algebraic tests on the carrier.",
        "residual":"Eight carrier edges are zero, so an exact support-four interior point and phase lift remain open.",
        "disposition":"accept carrier-polytope existence and select the interior-point test"
    },
    "zero_carrier_pattern":[list(x) for x in zero_carrier],
    "carrier_row_support":[len(r) for r in carrier],
    "witness_matrix":[[str(x) for x in row] for row in P],
    "allowed_edges":allowed_edges,
    "positive_entries":positive_entries,
    "boundary_zeros":boundary_zeros,
    "row_support":row_support,
    "column_support":col_support,
    "single_overlap_free_carrier":True,
    "interior_support_four_point":interior_support_four_point,
    "phase_lift_certificate":phase_lift_certificate,
    "classification":"productive polytope gate: a support-four carrier has an exact fixed-q boundary point",
    "remaining_gate":"find an interior point with all 24 carrier edges positive, then test phase lift",
    "hostile_gate":"do not call the boundary point an exact support-four or unistochastic witness",
    "claim_boundary":"the result proves polytope nonemptiness on a carrier, not full-support-four realization",
    "disposition":"support-four polytope leaf resolved; interior-point rival selected"
}

(ROOT/"results"/"wp1158_support_four_polytope_point.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1158 PASS:",allowed_edges,positive_entries,boundary_zeros)
