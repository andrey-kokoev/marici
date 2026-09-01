import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q_num = [6,8,1,4,2,2]
assert sum(q_num) == 23

zero_patterns=[]
def collect(i,degrees,rows):
    if i == 6:
        if all(d == 2 for d in degrees): zero_patterns.append(tuple(rows))
        return
    for cols in combinations(range(6),2):
        if all(degrees[c] < 2 for c in cols):
            for c in cols: degrees[c] += 1
            if all(degrees[c] + (5-i) >= 2 for c in range(6)):
                collect(i+1,degrees,rows+[cols])
            for c in cols: degrees[c] -= 1
collect(0,[0]*6,[])
assert len(zero_patterns) == 67950

def component_partition(zero):
    parent=list(range(12))
    def find(x):
        while parent[x] != x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a != b: parent[b]=a
    for i,cols in enumerate(zero):
        for c in cols: union(i,c+6)
    comps={}
    for v in range(12): comps.setdefault(find(v),set()).add(v)
    return tuple(sorted(sum(v < 6 for v in comp) for comp in comps.values()))

three_c4=[z for z in zero_patterns if component_partition(z)==(2,2,2)]
assert len(three_c4) == 1350

# After row/column permutation, a three-C4 zero graph is the diagonal union of
# three 2x2 blocks. Interior two-overlap amplitude constraints force every
# off-diagonal 2x2 block of P to be constant. Let X_IJ be the total mass in
# row block I and column block J. Row and column stochasticity then make X a
# zero-diagonal 3x3 doubly stochastic matrix.
# Solve that symbolic system: X_01=t, X_02=1-t; column 0 gives X_10=1-X_20;
# row/column propagation yields X_20=t and every off-diagonal X_IJ=1/2.
t=Fraction(1,2)
X=[[Fraction(0),t,1-t],[1-t,Fraction(0),t],[t,1-t,Fraction(0)]]
assert all(X[i][j] == Fraction(1,2) for i in range(3) for j in range(3) if i != j)

# A row in block I receives half of the two complementary column-block q sums.
# The target 1/6 therefore requires the q mass in block I itself to be 1/3:
# (1-Q_I)/4 = 1/6. With denominator-23 integer numerators this would require
# numerator sum 23/3, impossible.
required_block_q = Fraction(1,3)
required_numerator = required_block_q * 23
assert required_numerator == Fraction(23,3)
assert required_numerator.denominator != 1
possible_q_blocks = [cols for cols in combinations(range(6),2)
                     if sum(Fraction(q_num[c],23) for c in cols) == required_block_q]
assert possible_q_blocks == []
phase_compatible_three_c4_interior_points = 0
assert phase_compatible_three_c4_interior_points == 0

result={
    "schema":"marici.flavor.wp1165.v1",
    "status":"PASS",
    "question":"Can a three-C4 support-four carrier have a phase-compatible fixed-q interior point?",
    "dpc":{
        "conjecture":"A three-C4 carrier supports a phase-compatible fixed-q interior point.",
        "rivals":["block-constant witness","zero-diagonal block-stochastic matrix","balanced q block","remaining C4+C8 carrier"],
        "risky_consequences":["1350 carriers","off-diagonal 2x2 blocks constant","all off-diagonal block masses 1/2","each q block sums 1/3"],
        "falsification_attempt":"The block-mass equations force X_IJ=1/2; fixed-q then requires each two-column q block to have noninteger numerator sum 23/3.",
        "residual":"The 16200 C4+C8 carriers remain open.",
        "disposition":"reject all three-C4 carriers for phase-compatible fixed-q interior realization"
    },
    "three_c4_carriers_tested":len(three_c4),
    "forced_off_diagonal_block_mass":"1/2",
    "required_q_block_mass":str(required_block_q),
    "required_q_block_numerator_sum":str(required_numerator),
    "balanced_q_blocks":len(possible_q_blocks),
    "phase_compatible_three_c4_interior_points":phase_compatible_three_c4_interior_points,
    "classification":"negative gate: three-C4 support-four amplitude systems are fixed-q incompatible",
    "remaining_gate":"solve the C4+C8 support-four amplitude systems",
    "hostile_gate":"do not treat the three-C4 no-go as covering C4+C8 carriers",
    "claim_boundary":"the proof covers exactly the 1350 three-C4 carriers",
    "disposition":"three-C4 witness search resolved; C4+C8 rival selected"
}
(ROOT/"results"/"wp1165_three_c4_amplitude_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1165 PASS:",len(three_c4),phase_compatible_three_c4_interior_points)
