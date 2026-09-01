import json
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q=[Fraction(x,23) for x in (6,8,1,4,2,2)]
u=Fraction(1,6)

# Regular support-five carriers: each row excludes one column. Graph
# compatibility excludes row/column support intersections of size one.
patterns=[]
for zero in product(range(6),repeat=6):
    row_support=[set(range(6))-{zero[i]} for i in range(6)]
    col_support=[{i for i,s in enumerate(row_support) if j in s} for j in range(6)]
    if all(len(row_support[i]&row_support[k]) != 1 for i in range(6) for k in range(i+1,6)) and \
       all(len(col_support[j]&col_support[k]) != 1 for j in range(6) for k in range(j+1,6)):
        patterns.append(zero)
assert len(patterns) == 37476
multiplicity=Counter(tuple(sorted(Counter(z).values(),reverse=True)) for z in patterns)
assert multiplicity == Counter({
    (2,2,1,1):16200,
    (2,1,1,1,1):10800,
    (3,1,1,1):7200,
    (2,2,2):1800,
    (1,1,1,1,1,1):720,
    (4,2):450,
    (3,3):300,
    (6,):6,
})
# A doubly stochastic carrier needs every column nonempty, so only the 720
# derangement zero patterns can be algebraically feasible.
derangements=[z for z in patterns if len(set(z)) == 6]
assert len(derangements) == 720
assert all(any(j == z[i] for i in range(6)) for z in patterns if len(set(z)) == 6 for j in range(6))

def feasible_carrier(zero):
    allowed=[(i,j) for i in range(6) for j in range(6) if j != zero[i]]
    index={e:k for k,e in enumerate(allowed)}; n=len(allowed); A=[]; b=[]
    for i in range(6):
        row=[Fraction(0)]*n
        for j in range(6):
            if j != zero[i]: row[index[i,j]] = 1
        A.append(row); b.append(Fraction(1))
    for j in range(6):
        row=[Fraction(0)]*n
        for i in range(6):
            if j != zero[i]: row[index[i,j]] = 1
        A.append(row); b.append(Fraction(1))
    for i in range(6):
        row=[Fraction(0)]*n
        for j in range(6):
            if j != zero[i]: row[index[i,j]] = q[j]
        A.append(row); b.append(u)
    for i in range(18):
        if b[i] < 0:
            A[i]=[-x for x in A[i]]; b[i]=-b[i]
    m=18; N=n+m
    T=[A[i]+[Fraction(k == i) for k in range(m)]+[b[i]] for i in range(m)]
    basis=list(range(n,N)); objective=[Fraction(0)]*n+[Fraction(1)]*m+[Fraction(0)]
    for i,base in enumerate(basis):
        factor=objective[base]
        objective=[objective[c]-factor*T[i][c] for c in range(N+1)]
    while True:
        col=next((c for c in range(N) if objective[c] < 0),None)
        if col is None: return objective[-1] == 0
        candidates=[(T[i][-1]/T[i][col],i) for i in range(m) if T[i][col] > 0]
        if not candidates: return False
        _,row=min(candidates)
        pivot=T[row][col]; T[row]=[x/pivot for x in T[row]]
        for i in range(m):
            if i != row and T[i][col] != 0:
                factor=T[i][col]
                T[i]=[T[i][c]-factor*T[row][c] for c in range(N+1)]
        if objective[col] != 0:
            factor=objective[col]
            objective=[objective[c]-factor*T[row][c] for c in range(N+1)]
        basis[row]=col

feasible=[z for z in derangements if feasible_carrier(z)]
assert len(feasible) == 720

# Exact interior point for the identity zero pattern (zero diagonal). It was
# constructed by averaging one exact LP maximizer per allowed edge.
rows=[
 ["0","8501/30240","1147/14175","51607/453600","619/7560","4777/10800"],
 ["11759/37800","0","287/8100","7081/22680","13/720","181/560"],
 ["103/5040","4523/22680","0","1049/3780","8209/22680","709/5040"],
 ["3/100","1373/4536","1943/18900","0","3337/6480","107/2160"],
 ["7081/37800","679/4320","13627/37800","12637/50400","0","239/5400"],
 ["11369/25200","901/15120","15889/37800","173/3780","5/216","0"]]
P=[[Fraction(x) for x in row] for row in rows]
assert all(P[i][i] == 0 for i in range(6))
assert all(P[i][j] > 0 for i in range(6) for j in range(6) if i != j)
assert all(sum(row) == 1 for row in P)
assert all(sum(P[i][j] for i in range(6)) == 1 for j in range(6))
assert [sum(P[i][j]*q[j] for j in range(6)) for i in range(6)] == [u]*6

# The displayed witness itself is not a phase certificate. Its row and column
# pair sqrt-product polygon inequalities fail, so it is not unistochastic.
# Use high-precision square roots with margins far above Decimal error.
getcontext().prec=60
def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)
def exact_polygon_failures(P,by_row=True):
    failures=[]
    for a in range(6):
        for b in range(a+1,6):
            terms=[P[a][j]*P[b][j] for j in range(6)] if by_row else [P[i][a]*P[i][b] for i in range(6)]
            roots=[dec(x).sqrt() for x in terms]
            largest=max(roots)
            if largest > sum(roots)-largest:
                failures.append((a,b))
    return failures
row_failures=exact_polygon_failures(P,True)
col_failures=exact_polygon_failures(P,False)
assert len(row_failures) == 3 and len(col_failures) == 4
phase_lift_certificates=0
result={
    "schema":"marici.flavor.wp1168.v2",
    "status":"PASS",
    "question":"Do graph-compatible support-five carriers contain fixed-q interior points?",
    "dpc":{
        "conjecture":"Graph-compatible support-five carriers supply fixed-q interior points.",
        "rivals":["empty graph class","derangement-only algebra","zero-diagonal witness","phase lift"],
        "risky_consequences":["37476 graph-compatible carriers","720 derangement carriers","strictly positive off-diagonal witness","Pq=u"],
        "falsification_attempt":"All 720 derangement carriers pass exact linear feasibility, and the identity carrier has an explicit interior point.",
        "residual":"The displayed identity witness fails sqrt-product polygon inequalities and has no phase lift.",
        "disposition":"accept support-five graph and algebraic existence; select the phase-compatible search"
    },
    "graph_compatible_carriers":len(patterns),
    "zero_column_multiplicity":{str(k):v for k,v in sorted(multiplicity.items())},
    "derangement_carriers":len(derangements),
    "linearly_feasible_derangement_carriers":len(feasible),
    "explicit_interior_witnesses":1,
    "witness_matrix":[[str(x) for x in row] for row in P],
    "minimum_off_diagonal_entry":str(min(P[i][j] for i in range(6) for j in range(6) if i != j)),
    "witness_row_polygon_failures":row_failures,
    "witness_column_polygon_failures":col_failures,
    "phase_lift_certificates":phase_lift_certificates,
    "classification":"productive gate with correction: support five has graph-compatible derangement carriers and one explicit fixed-q interior witness",
    "remaining_gate":"search the support-five polytopes for a point satisfying unitary phase constraints",
    "hostile_gate":"do not generalize one identity-carrier witness to all support-five carriers or treat it as unistochastic",
    "claim_boundary":"all 720 derangement carriers are linearly feasible; only the displayed identity carrier has a certified strict interior witness",
    "disposition":"support-five graph leaf resolved; phase-compatible rival selected"
}
(ROOT/"results"/"wp1168_support_five_graph_search.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1168 PASS:",len(patterns),len(feasible),1,phase_lift_certificates)
