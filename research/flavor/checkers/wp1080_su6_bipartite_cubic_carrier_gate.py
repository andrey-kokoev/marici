import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Branching of 15+2bar6 under SU(3)_A x SU(3)_B x U(1), with
# 6=(3,1)_1+(1,3)_-1.
branches = [
    {"parent": "15", "rep": "(3,3)", "dimA": 3, "dimB": 3, "q": 0, "A_A": 3, "A_B": 3},
    {"parent": "15", "rep": "(bar3,1)", "dimA": 3, "dimB": 1, "q": 2, "A_A": -1, "A_B": 0},
    {"parent": "15", "rep": "(1,bar3)", "dimA": 1, "dimB": 3, "q": -2, "A_A": 0, "A_B": -1},
    {"parent": "bar6a", "rep": "(bar3,1)", "dimA": 3, "dimB": 1, "q": -1, "A_A": -1, "A_B": 0},
    {"parent": "bar6a", "rep": "(1,bar3)", "dimA": 1, "dimB": 3, "q": 1, "A_A": 0, "A_B": -1},
    {"parent": "bar6b", "rep": "(bar3,1)", "dimA": 3, "dimB": 1, "q": -1, "A_A": -1, "A_B": 0},
    {"parent": "bar6b", "rep": "(1,bar3)", "dimA": 1, "dimB": 3, "q": 1, "A_A": 0, "A_B": -1},
]
for b in branches:
    b["dim"] = b["dimA"] * b["dimB"]
assert sum(b["dim"] for b in branches) == 27
assert sum(b["A_A"] for b in branches) == 0
assert sum(b["A_B"] for b in branches) == 0
assert sum(b["dim"] * b["q"] for b in branches) == 0

# The 15 contains a bifundamental cross-block. In an aligned frame its
# coefficient matrix is the rank-three identity, giving a nondegenerate A-B
# pairing.
cross_block = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
def rank(mat):
    m=[[Fraction(x) for x in row] for row in mat]
    rows,cols=len(m),len(m[0]); r=0
    for c in range(cols):
        p=next((i for i in range(r,rows) if m[i][c]),None)
        if p is None: continue
        m[r],m[p]=m[p],m[r]
        pv=m[r][c]; m[r]=[x/pv for x in m[r]]
        for i in range(rows):
            if i!=r and m[i][c]:
                f=m[i][c]; m[i]=[x-f*y for x,y in zip(m[i],m[r])]
        r+=1
    return r
assert rank(cross_block) == 3

# Each SU(3) factor carries the invariant alternating cubic epsilon tensor.
def eps(i,j,k):
    if len({i,j,k}) < 3:
        return 0
    inversions = (i>j) + (i>k) + (j>k)
    return -1 if inversions % 2 else 1
assert eps(1,2,3) == 1
assert eps(2,1,3) == -1
assert eps(1,1,3) == 0

# The A<->B exchange preserves the full branch multiset but swaps the two
# carrier lines; separate orientation of A versus B therefore remains a
# discrete structure to fix.
branch_multiset = sorted((b["rep"], b["q"]) for b in branches)
exchanged = []
for rep,q in branch_multiset:
    if rep == "(bar3,1)":
        exchanged.append(("(1,bar3)", -q))
    elif rep == "(1,bar3)":
        exchanged.append(("(bar3,1)", -q))
    else:
        exchanged.append((rep,q))
assert sorted(exchanged) == branch_multiset

result = {
    "schema": "marici.flavor.wp1080.v1",
    "status": "PASS",
    "question": "Does the SU(6) anomaly family supply Nima's bipartite alignment and alternating cubic carrier signature?",
    "branching_rule": "6=(3,1)_1+(1,3)_-1",
    "branches": branches,
    "anomaly_checks": {
        "cubic_SU3_A": 0,
        "cubic_SU3_B": 0,
        "dimension_weighted_U1": 0,
    },
    "carrier_data": {
        "bifundamental": "(3,3)_0 inside 15",
        "cross_block_rank_in_aligned_frame": rank(cross_block),
        "alternating_carriers": ["epsilon_SU3_A", "epsilon_SU3_B"],
        "epsilon_123": eps(1,2,3),
        "epsilon_213": eps(2,1,3),
    },
    "exchange_fiber": "A<->B preserves the full branch multiset but swaps the two SU3 carrier lines and reverses U(1) charges",
    "nima_signature": {
        "two_three_state_families": True,
        "nondegenerate_pairing": True,
        "alternating_cubic_carriers": True,
        "directed_cross_block": True,
        "temporal_coherence_process": False,
        "ordered_detector_ports": False,
        "calibrated_physical16_descent": False,
    },
    "classification": "conditional SU(3)xSU(3) bipartite carrier constructor: the SU(6) family supplies the group-theoretic alignment/cubic-carrier signature but not temporal coherence, detector ports, production kernel, or physical16 descent",
    "remaining_gate": "derive the temporal coherence process, ordered detector ports, and source production/decay kernel on this bipartite carrier, then descend to physical16",
    "claim_boundary": "representation-level signature only; it does not identify the SU3 factors with generations or select the flux orientation",
    "disposition": "productive: Nima's microscopic search signature now has an exact SU(6) representation candidate rather than only an obstruction",
}

(ROOT / "results" / "wp1080_su6_bipartite_cubic_carrier_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1080 PASS:", len(branches), rank(cross_block), eps(1,2,3), eps(2,1,3))
