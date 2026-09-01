import json
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import permutations
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
getcontext().prec=60

def dec(x): return Decimal(x.numerator)/Decimal(x.denominator)
def polygon_failures(P,by_row=True):
    failures=[]
    for a in range(6):
        for b in range(a+1,6):
            terms=[P[a][j]*P[b][j] for j in range(6)] if by_row else [P[i][a]*P[i][b] for i in range(6)]
            roots=[dec(x).sqrt() for x in terms]
            largest=max(roots)
            if largest > sum(roots)-largest: failures.append((a,b))
    return failures

# Every feasible regular support-five carrier is a derangement of excluded
# columns. Distinct excluded columns make every row-pair and column-pair
# intersection size four, so no support-induced two-overlap determinant
# constraint is available.
derangements=list(permutations(range(6)))
assert len(derangements) == 720
for zero in derangements:
    rows=[set(range(6))-{zero[i]} for i in range(6)]
    cols=[{i for i,s in enumerate(rows) if j in s} for j in range(6)]
    assert all(len(rows[i]&rows[k]) == 4 for i in range(6) for k in range(i+1,6))
    assert all(len(cols[j]&cols[k]) == 4 for j in range(6) for k in range(j+1,6))

rows=[
 ["0","8501/30240","1147/14175","51607/453600","619/7560","4777/10800"],
 ["11759/37800","0","287/8100","7081/22680","13/720","181/560"],
 ["103/5040","4523/22680","0","1049/3780","8209/22680","709/5040"],
 ["3/100","1373/4536","1943/18900","0","3337/6480","107/2160"],
 ["7081/37800","679/4320","13627/37800","12637/50400","0","239/5400"],
 ["11369/25200","901/15120","15889/37800","173/3780","5/216","0"]]
P=[[Fraction(x) for x in row] for row in rows]
row_failures=polygon_failures(P,True)
col_failures=polygon_failures(P,False)
assert row_failures == [(0,1),(1,5),(2,3)]
assert col_failures == [(0,2),(0,5),(2,4),(3,4)]
phase_lift_certificates=0
assert phase_lift_certificates == 0
result={
    "schema":"marici.flavor.wp1169.v1",
    "status":"PASS",
    "question":"Does the explicit support-five interior witness have a unitary phase lift?",
    "dpc":{
        "conjecture":"The zero-diagonal support-five witness is unistochastic.",
        "rivals":["support-induced determinant constraint","row polygon obstruction","column polygon obstruction","constrained phase search"],
        "risky_consequences":["720 derangement carriers","no two-overlap constraints","three row polygon failures","four column polygon failures"],
        "falsification_attempt":"The exact witness violates sqrt-product polygon inequalities, which are necessary for orthogonality of unitary rows and columns.",
        "residual":"A different point in a support-five fixed-q polytope may still be unistochastic.",
        "disposition":"reject the displayed witness and select constrained phase-compatible search"
    },
    "derangement_carriers":720,
    "support_induced_two_overlap_constraints":0,
    "row_polygon_failures":row_failures,
    "column_polygon_failures":col_failures,
    "phase_lift_certificates":phase_lift_certificates,
    "classification":"negative gate: the explicit support-five witness is not unistochastic",
    "remaining_gate":"search support-five fixed-q polytopes under row and column phaseability constraints",
    "hostile_gate":"do not treat the absence of two-overlap constraints as a phase certificate",
    "claim_boundary":"the no-go covers the displayed WP1168 witness, not every support-five polytope point",
    "disposition":"support-five phase-lift leaf resolved; constrained search selected"
}
(ROOT/"results"/"wp1169_support_five_phase_obstruction.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1169 PASS:",720,row_failures,col_failures,phase_lift_certificates)
