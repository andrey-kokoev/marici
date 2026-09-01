import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

# Enumerate all row-support-two patterns with every column support two. Any
# support-at-most-two doubly stochastic solution must have this support shape,
# because no q_j equals u, so support one cannot satisfy Pq=u.
patterns = []
def collect(i, degrees, rows):
    if i == 6:
        if all(d == 2 for d in degrees):
            patterns.append(tuple(rows))
        return
    for cols in combinations(range(6),2):
        if all(degrees[c] < 2 for c in cols):
            for c in cols: degrees[c] += 1
            if all(degrees[c] + (5-i) >= 2 for c in range(6)):
                collect(i+1, degrees, rows+[cols])
            for c in cols: degrees[c] -= 1
collect(0,[0]*6,[])
assert len(patterns) == 67950

def consistent(pattern):
    edges = [(i,j) for i,cols in enumerate(pattern) for j in cols]
    m = len(edges)
    equations = []
    for i in range(6):
        equations.append(([Fraction(r == i) for r,c in edges], Fraction(1)))
    for j in range(6):
        equations.append(([Fraction(c == j) for r,c in edges], Fraction(1)))
    for i in range(6):
        equations.append(([q[c] if r == i else Fraction(0) for r,c in edges], u))
    A = [row+[b] for row,b in equations]
    rank = 0
    for col in range(m):
        pivot = next((r for r in range(rank,len(A)) if A[r][col] != 0), None)
        if pivot is None:
            continue
        A[rank],A[pivot] = A[pivot],A[rank]
        pv = A[rank][col]
        A[rank] = [x/pv for x in A[rank]]
        for r in range(len(A)):
            if r != rank and A[r][col] != 0:
                factor = A[r][col]
                A[r] = [A[r][c] - factor*A[rank][c] for c in range(m+1)]
        rank += 1
    return all(A[r][m] == 0 for r in range(rank,len(A)))

consistent_support_two = 0
for pattern in patterns:
    if consistent(pattern):
        consistent_support_two += 1
assert consistent_support_two == 0

# Full support survives through the uniform doubly stochastic map J6/6.
J = [[Fraction(1,6)]*6 for _ in range(6)]
assert all(sum(row) == 1 for row in J)
assert all(sum(J[i][j] for i in range(6)) == 1 for j in range(6))
assert [sum(J[i][j]*q[j] for j in range(6)) for i in range(6)] == [u]*6

result = {
    "schema":"marici.flavor.wp1152.v1",
    "status":"PASS",
    "question":"Does a sparse support-at-most-two doubly stochastic fixed-q S-matrix modulus survive?",
    "dpc":{
        "conjecture":"A sparse support-two unitary-modulus map satisfies the fixed-q target.",
        "rivals":["support-one map","support-two doubly stochastic map","full-support uniform map","support-three candidate"],
        "risky_consequences":["row and column sums one","Pq=u","every row and column support exactly two","all 67950 support patterns checked"],
        "falsification_attempt":"Every support pattern is linearly inconsistent with the target; support one is impossible because no q_j=1/6. J6/6 survives with full support.",
        "residual":"A support-three or denser doubly stochastic candidate may exist.",
        "disposition":"reject sparse support-two unitary-modulus maps and select the support-three question"
    },
    "support_one_maps":0,
    "support_two_patterns_tested":len(patterns),
    "consistent_support_two_patterns":consistent_support_two,
    "full_support_solution":"J6/6",
    "minimal_known_support":6,
    "minimal_possible_support_lower_bound":3,
    "classification":"negative gate: sparse support-two doubly stochastic maps are impossible for this fixed q",
    "remaining_gate":"decide whether support three admits a fixed-q doubly stochastic solution",
    "hostile_gate":"do not call the full-support J6/6 map sparse or localized",
    "claim_boundary":"the support-two obstruction is exact; support three remains open",
    "disposition":"doubly stochastic support leaf resolved; support-three rival selected"
}

(ROOT/"results"/"wp1152_doubly_stochastic_support_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1152 PASS:",len(patterns),consistent_support_two)
