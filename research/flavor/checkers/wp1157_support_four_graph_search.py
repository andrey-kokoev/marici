import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The zero complement of a row/column support-four pattern is a row/column
# support-two pattern. Enumerating the zero patterns is therefore exhaustive.
zero_patterns = []
def collect(i, degrees, rows):
    if i == 6:
        if all(d == 2 for d in degrees):
            zero_patterns.append(tuple(rows))
        return
    for cols in combinations(range(6),2):
        if all(degrees[c] < 2 for c in cols):
            for c in cols: degrees[c] += 1
            if all(degrees[c] + (5-i) >= 2 for c in range(6)):
                collect(i+1, degrees, rows+[cols])
            for c in cols: degrees[c] -= 1
collect(0,[0]*6,[])
assert len(zero_patterns) == 67950

support_four_patterns = []
single_overlap_free = 0
for zero_pattern in zero_patterns:
    support = tuple(tuple(c for c in range(6) if c not in zero_pattern[i]) for i in range(6))
    row_sets = [set(r) for r in support]
    col_sets = [{i for i,row in enumerate(row_sets) if j in row} for j in range(6)]
    assert all(len(r) == 4 for r in row_sets)
    assert all(len(c) == 4 for c in col_sets)
    # If zero row sets have size two, support overlap is 6-|Z_i union Z_j|,
    # hence 2, 3, or 4 and never 1. The same applies to columns.
    assert all(len(row_sets[i] & row_sets[j]) != 1 for i in range(6) for j in range(i+1,6))
    assert all(len(col_sets[i] & col_sets[j]) != 1 for i in range(6) for j in range(i+1,6))
    single_overlap_free += 1
    support_four_patterns.append(support)

assert single_overlap_free == len(support_four_patterns) == 67950
# Graph compatibility is necessary, not sufficient. This gate does not claim a
# nonnegative fixed-q solution or a phase lift.
fixed_q_polytope_witnesses = 0
phase_lifts = 0
assert fixed_q_polytope_witnesses == phase_lifts == 0

result = {
    "schema":"marici.flavor.wp1157.v1",
    "status":"PASS",
    "question":"Are support-four graphs free of the single-overlap unistochastic obstruction?",
    "dpc":{
        "conjecture":"Support four is the first support class whose regular graphs all pass the single-overlap test.",
        "rivals":["support-three two-block graph","support-four complement graph","fixed-q polytope point","phase lift"],
        "risky_consequences":["67950 zero-complement patterns","row and column support four","no support overlap one","remaining polytope and phase tests"],
        "falsification_attempt":"Every support-four regular graph has row and column support overlaps of size 2, 3, or 4, never 1.",
        "residual":"No nonnegative fixed-q witness or phase lift is established by graph compatibility alone.",
        "disposition":"accept support-four graph compatibility and select the support-four polytope test"
    },
    "support_four_patterns_tested":len(support_four_patterns),
    "single_overlap_free_graphs":single_overlap_free,
    "complement_characterization":"each zero pattern is a 2-regular bipartite graph on 6+6 vertices",
    "allowed_overlap_sizes":[2,3,4],
    "fixed_q_polytope_witnesses":fixed_q_polytope_witnesses,
    "phase_lifts":phase_lifts,
    "classification":"productive graph gate: support-four is the first single-overlap-free sparse class",
    "remaining_gate":"test nonnegative fixed-q polytope points on support-four graphs",
    "hostile_gate":"do not treat graph compatibility as a unistochastic or fixed-q witness",
    "claim_boundary":"the result is a necessary support condition only",
    "disposition":"support-four graph search resolved; support-four polytope rival selected"
}

(ROOT/"results"/"wp1157_support_four_graph_search.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1157 PASS:",len(support_four_patterns),single_overlap_free)
