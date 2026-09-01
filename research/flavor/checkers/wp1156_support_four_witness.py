import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

# Add edge (0,4)=1/16 to the WP1153 support-three witness and rebalance the
# active nullspace exactly. This yields a maximum-row-support-four witness.
P = [
    [Fraction(3,80), Fraction(31,84), Fraction(223,420), 0, Fraction(1,16), 0],
    [Fraction(121,240), 0, Fraction(11,60), 0, Fraction(5,16), 0],
    [Fraction(11,24), 0, 0, 0, Fraction(13,24), 0],
    [0, Fraction(5,18), 0, Fraction(1,12), 0, Fraction(23,36)],
    [0, Fraction(89,252), Fraction(2,7), 0, 0, Fraction(13,36)],
    [0, 0, 0, Fraction(11,12), Fraction(1,12), 0],
]

assert all(all(x >= 0 for x in row) for row in P)
assert all(sum(row) == 1 for row in P)
assert all(sum(P[i][j] for i in range(6)) == 1 for j in range(6))
assert [sum(P[i][j]*q[j] for j in range(6)) for i in range(6)] == [u]*6
row_support = [sum(x > 0 for x in row) for row in P]
col_support = [sum(P[i][j] > 0 for i in range(6)) for j in range(6)]
assert row_support == [4,3,2,3,3,2]
assert col_support == [3,3,3,2,4,2]
assert max(row_support) == 4
assert sum(row_support) == 17

# The witness still fails the necessary unitary support test: rows 0 and 3
# share exactly column 1, so their inner product has one uncancellable term.
row_sets = [frozenset(j for j,x in enumerate(row) if x > 0) for row in P]
single_overlap_pairs = [(i,j,sorted(row_sets[i] & row_sets[j]))
                        for i in range(6) for j in range(i+1,6)
                        if len(row_sets[i] & row_sets[j]) == 1]
assert (0,3,[1]) in single_overlap_pairs
unistochastic_graph_compatible = not single_overlap_pairs
assert unistochastic_graph_compatible is False

result = {
    "schema":"marici.flavor.wp1156.v1",
    "status":"PASS",
    "question":"Does a sparse maximum-row-support-four fixed-q doubly stochastic map exist?",
    "dpc":{
        "conjecture":"A support-four algebraic witness exists after the support-three graph exclusion.",
        "rivals":["support-three witness","support-four perturbation","unistochastic-compatible graph","nonunitary map"],
        "risky_consequences":["nonnegative entries","row and column sums one","Pq=u","maximum row support four"],
        "falsification_attempt":"The added edge (0,4) is rebalanced exactly and passes all four algebraic tests.",
        "residual":"The witness has a single-overlap row pair and is not unistochastic-compatible.",
        "disposition":"accept support-four algebraic existence and select the support-four graph search"
    },
    "witness_matrix":[[str(x) for x in row] for row in P],
    "row_support":row_support,
    "column_support":col_support,
    "maximum_row_support":max(row_support),
    "nonzero_entries":sum(row_support),
    "single_overlap_pairs":single_overlap_pairs,
    "unistochastic_graph_compatible":unistochastic_graph_compatible,
    "classification":"productive algebraic gate: support-four fixed-q doubly stochastic maps exist",
    "remaining_gate":"search support-four graphs for unitary orthogonality compatibility",
    "hostile_gate":"do not treat this support-four doubly stochastic witness as unistochastic",
    "claim_boundary":"existence is algebraic only; the displayed witness is graph-incompatible with unitarity",
    "disposition":"support-four leaf resolved; support-four graph-search rival selected"
}

(ROOT/"results"/"wp1156_support_four_witness.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1156 PASS:",max(row_support),sum(row_support),len(single_overlap_pairs))
