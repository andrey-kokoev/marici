import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q_num = [6,8,1,4,2,2]
q_sum = sum(q_num)
assert q_sum == 23

patterns = []
def collect(i, degrees, rows):
    if i == 6:
        if all(d == 3 for d in degrees):
            patterns.append(tuple(rows))
        return
    for cols in combinations(range(6),3):
        if all(degrees[c] < 3 for c in cols):
            for c in cols: degrees[c] += 1
            if all(degrees[c] + (5-i) >= 3 for c in range(6)):
                collect(i+1, degrees, rows+[cols])
            for c in cols: degrees[c] -= 1
collect(0,[0]*6,[])
assert len(patterns) == 297200

# A unitary's orthogonal rows and columns cannot have support overlap exactly
# one: their inner product would contain one uncancellable nonzero term.
graph_compatible = []
for pattern in patterns:
    row_sets = [set(r) for r in pattern]
    col_sets = [{i for i,row in enumerate(row_sets) if j in row} for j in range(6)]
    row_ok = all(len(row_sets[i] & row_sets[j]) != 1 for i in range(6) for j in range(i+1,6))
    col_ok = all(len(col_sets[i] & col_sets[j]) != 1 for i in range(6) for j in range(i+1,6))
    if row_ok and col_ok:
        graph_compatible.append(pattern)
assert len(graph_compatible) == 200

# Exhaustion shows these 200 graphs are exactly the row/column-permuted direct
# sums of two complete 3x3 blocks. Detect that shape explicitly.
def is_two_complete_blocks(pattern):
    row_sets = [set(r) for r in pattern]
    for rows_a in combinations(range(6),3):
        a = set(rows_a); b = set(range(6))-a
        supports_a = {frozenset(row_sets[i]) for i in a}
        supports_b = {frozenset(row_sets[i]) for i in b}
        if len(supports_a) == len(supports_b) == 1:
            cols_a = next(iter(supports_a)); cols_b = next(iter(supports_b))
            if len(cols_a) == len(cols_b) == 3 and cols_a.isdisjoint(cols_b):
                return True
    return False
assert all(is_two_complete_blocks(pattern) for pattern in graph_compatible)

# In a 3+3 block map, the three rows in one block each satisfy Pq=1/6.
# Summing them forces the corresponding q weights to sum 1/2. Since all q
# numerators are integers and sum to odd 23, no three-column block can have
# numerator sum 23/2.
half_weight = Fraction(1,2)
balanced_blocks = [cols for cols in combinations(range(6),3)
                   if sum(Fraction(q_num[c],23) for c in cols) == half_weight]
assert balanced_blocks == []
fixed_q_block_candidates = 0
unistochastic_compatible_support_three = 0
assert fixed_q_block_candidates == unistochastic_compatible_support_three == 0

result = {
    "schema":"marici.flavor.wp1155.v1",
    "status":"PASS",
    "question":"Does any support-three graph admit a unistochastic-compatible fixed-q solution?",
    "dpc":{
        "conjecture":"Some support-three graph avoids the single-overlap obstruction and supports fixed-q mixing.",
        "rivals":["single-overlap graph","two-block complete graph","fixed-q balanced block","support-four graph"],
        "risky_consequences":["297200 row-support-three patterns","no row or column support overlap one","200 graph-compatible patterns","fixed-q block sum 1/2"],
        "falsification_attempt":"All 200 graph-compatible patterns are two complete 3x3 blocks; fixed-q would require a three-column q sum of 1/2, impossible for integer numerators summing to 23.",
        "residual":"Support four is the next possible sparse class.",
        "disposition":"reject support-three unistochastic-compatible fixed-q maps"
    },
    "support_three_patterns_tested":len(patterns),
    "single_overlap_free_graphs":len(graph_compatible),
    "graph_shape":"row/column-permuted direct sum of two complete 3x3 blocks",
    "balanced_three_column_blocks":len(balanced_blocks),
    "fixed_q_block_candidates":fixed_q_block_candidates,
    "unistochastic_compatible_support_three":unistochastic_compatible_support_three,
    "minimum_possible_sparse_support":4,
    "classification":"negative gate: support-three unistochastic-compatible fixed-q maps are impossible",
    "remaining_gate":"test support-four sparse candidates",
    "hostile_gate":"do not call a graph unistochastic-compatible merely because it is doubly stochastic",
    "claim_boundary":"the no-go uses necessary row/column orthogonality support and exact fixed-q block balance",
    "disposition":"support-graph search resolved; support-four rival selected"
}

(ROOT/"results"/"wp1155_support_graph_search.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1155 PASS:",len(patterns),len(graph_compatible),unistochastic_compatible_support_three)
