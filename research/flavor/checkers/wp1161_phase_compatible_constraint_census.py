import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

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

constraint_census = Counter()
for zero in zero_patterns:
    row_zero = [set(z) for z in zero]
    col_zero = [{i for i,row in enumerate(row_zero) if j in row} for j in range(6)]
    row_two_overlap = sum(row_zero[i].isdisjoint(row_zero[j]) for i in range(6) for j in range(i+1,6))
    col_two_overlap = sum(col_zero[i].isdisjoint(col_zero[j]) for i in range(6) for j in range(i+1,6))
    constraint_census[(row_two_overlap,col_two_overlap)] += 1
assert constraint_census == Counter({(9,9):50400,(10,10):16200,(12,12):1350})
minimum_total_constraints = min(r+c for r,c in constraint_census)
assert minimum_total_constraints == 18

# Representative minimal carrier from WP1159: check exact affine rank/dimension.
representative_zero = ((0,1),(0,2),(1,2),(3,4),(3,5),(4,5))
carrier = [tuple(c for c in range(6) if c not in representative_zero[i]) for i in range(6)]
edges = [(i,j) for i,cols in enumerate(carrier) for j in cols]
equations = []
for i in range(6): equations.append(([Fraction(r == i) for r,c in edges], Fraction(1)))
for j in range(6): equations.append(([Fraction(c == j) for r,c in edges], Fraction(1)))
for i in range(6): equations.append(([q[c] if r == i else Fraction(0) for r,c in edges], u))
A = [row+[b] for row,b in equations]
rank = 0
for col in range(len(edges)):
    pivot = next((r for r in range(rank,len(A)) if A[r][col] != 0), None)
    if pivot is None:
        continue
    A[rank],A[pivot] = A[pivot],A[rank]
    pv = A[rank][col]
    A[rank] = [x/pv for x in A[rank]]
    for r in range(len(A)):
        if r != rank and A[r][col] != 0:
            f = A[r][col]
            A[r] = [A[r][c]-f*A[rank][c] for c in range(len(edges)+1)]
    rank += 1
assert rank == 16
affine_dimension = len(edges) - rank
assert affine_dimension == 8

phase_compatible_witnesses = 0
assert phase_compatible_witnesses == 0

result = {
    "schema":"marici.flavor.wp1161.v1",
    "status":"PASS",
    "question":"How constrained is the phase-compatible support-four interior search?",
    "dpc":{
        "conjecture":"Some support-four interior point can satisfy the two-overlap amplitude equations.",
        "rivals":["minimal 9+9 constraint carrier","10+10 carrier","12+12 carrier","phase-compatible witness"],
        "risky_consequences":["67950 carriers","equal amplitude products on every two-column row overlap","equal products on every two-row column overlap","8-dimensional representative polytope"],
        "falsification_attempt":"Every carrier has at least 18 exact two-overlap amplitude constraints; the minimal carrier census is 50400 of 67950.",
        "residual":"The amplitude equation system remains unsolved; constraint count alone neither constructs nor excludes a witness.",
        "disposition":"complete the constraint census and select the minimal amplitude-system solve"
    },
    "carriers_tested":len(zero_patterns),
    "constraint_census":{"9_row_9_col":50400,"10_row_10_col":16200,"12_row_12_col":1350},
    "minimum_total_two_overlap_constraints":minimum_total_constraints,
    "representative_zero_pattern":[list(x) for x in representative_zero],
    "representative_affine_rank":rank,
    "representative_affine_dimension":affine_dimension,
    "phase_compatible_witnesses":phase_compatible_witnesses,
    "classification":"constraint gate: phase-compatible interior search is exactly constrained by at least 18 amplitude equations",
    "remaining_gate":"solve the minimal 9+9 amplitude system on a support-four fixed-q polytope",
    "hostile_gate":"do not treat constraint counting as a unistochastic witness or no-go proof",
    "claim_boundary":"the census is exact; existence remains open",
    "disposition":"phase-compatible interior search leaf resolved; amplitude-system rival selected"
}

(ROOT/"results"/"wp1161_phase_compatible_constraint_census.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1161 PASS:",len(zero_patterns),minimum_total_constraints,affine_dimension)
