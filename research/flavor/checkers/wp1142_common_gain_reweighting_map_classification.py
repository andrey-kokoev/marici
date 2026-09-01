import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
r = [Fraction(1,4)] * 6
gain = Fraction(3,2)
u = [value / gain for value in r]
assert u == [Fraction(1,6)] * 6

U = [[Fraction(1,6)] * 6 for _ in range(6)]
p_plus = [Fraction(5,24), Fraction(1,8), Fraction(5,36), Fraction(7,36), Fraction(1,6), Fraction(1,6)]
p_minus = [Fraction(1,8), Fraction(5,24), Fraction(7,36), Fraction(5,36), Fraction(1,6), Fraction(1,6)]
R2 = [p_plus] + [p_minus] * 5

def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(6)) for i in range(6)]

def rank(A):
    rows = [list(row) for row in A]
    rank_value = 0
    col = 0
    while col < 6 and rank_value < 6:
        pivot = next((i for i in range(rank_value,6) if rows[i][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        rows[rank_value], rows[pivot] = rows[pivot], rows[rank_value]
        pv = rows[rank_value][col]
        rows[rank_value] = [v / pv for v in rows[rank_value]]
        for i in range(6):
            if i != rank_value and rows[i][col] != 0:
                factor = rows[i][col]
                rows[i] = [rows[i][j] - factor * rows[rank_value][j] for j in range(6)]
        rank_value += 1
        col += 1
    return rank_value

assert all(sum(row) == 1 for row in U)
assert all(sum(row) == 1 for row in R2)
assert all(value >= 0 for row in R2 for value in row)
assert matvec(U,q) == u
assert matvec(R2,q) == u
assert rank(U) == 1
assert rank(R2) == 2

# After dividing by the common gain, the constraint is Mq=u. Hence every
# solution is M=U+A with A1=0 and Aq=0. Before positivity, each row has a
# four-dimensional perturbation space, so the unconstrained affine dimension
# is 24. Positivity cuts out a convex polytope but does not restore uniqueness.
row_perturbation_dimension = 4
unconstrained_affine_dimension = 6 * row_perturbation_dimension
assert unconstrained_affine_dimension == 24

concentrated_source = [Fraction(1)] + [Fraction(0)] * 5
rank1_image = matvec(U, concentrated_source)
rank2_image = matvec(R2, concentrated_source)
assert rank1_image == [Fraction(1,6)] * 6
assert rank2_image != rank1_image

result = {
    "schema": "marici.flavor.wp1142.v1",
    "status": "PASS",
    "question": "Do q, r, and common gain 3/2 uniquely classify the reweighting map?",
    "dpc": {
        "conjecture": "The common-gain constraint uniquely selects complete uniform mixing.",
        "rivals": [
            "rank-one complete mixing",
            "rank-two stochastic map",
            "unique source-compatible map",
            "underdetermined convex map polytope"
        ],
        "risky_consequences": [
            "Mq=r/g=u",
            "row-stochastic nonnegative M",
            "rank-one and rank-two exact solutions",
            "different responses to a concentrated hostile source"
        ],
        "falsification_attempt": "A rank-two stochastic matrix maps q to u and distinguishes a concentrated source, so q and r do not uniquely select U.",
        "residual": "Physical production/decay locality may select a map inside the convex polytope.",
        "disposition": "reject uniqueness of complete mixing and classify the executable map family"
    },
    "source_q": [str(x) for x in q],
    "target_r": [str(x) for x in r],
    "gain": str(gain),
    "normalized_target_u": [str(x) for x in u],
    "rank_one_map": {"rank": rank(U), "row": [str(x) for x in U[0]]},
    "rank_two_example": {
        "rank": rank(R2),
        "row_plus": [str(x) for x in p_plus],
        "row_minus": [str(x) for x in p_minus],
        "concentrated_source_image": [str(x) for x in rank2_image]
    },
    "solution_space": {
        "form": "M=U+A, with A1=0 and Aq=0",
        "unconstrained_affine_dimension": unconstrained_affine_dimension,
        "nonnegative_subset": "convex polytope",
        "unique": False
    },
    "classification": "classification gate: common gain fixes only Mq=u, not the production kernel",
    "remaining_gate": "test rank-two/localized candidates against physical production locality",
    "hostile_gate": "do not treat complete mixing as unique merely because it is the rank-one solution",
    "claim_boundary": "the algebraic map family is exact; physical selection remains open",
    "disposition": "common-gain map classification resolved; rank-two rival selected",
}

(ROOT / "results" / "wp1142_common_gain_reweighting_map_classification.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1142 PASS:", rank(U), rank(R2), unconstrained_affine_dimension)
