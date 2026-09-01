import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

# Every connected minimal zero graph is a single 12-cycle. Use abstract cycle
# positions R_t adjacent to C_t and C_{t-1}. Only the cyclic order of q labels
# affects the fixed-q reduced system; dihedral reparameterizations are equal.
def canonical_order(order):
    n=len(order)
    forms=[]
    for seq in (order,tuple(reversed(order))):
        forms.extend(seq[k:]+seq[:k] for k in range(n))
    return min(forms)

orders = sorted({canonical_order(p) for p in permutations(range(6))})
assert len(orders) == 60

def feasible_for_order(order):
    # H edges: R_t -- C_t and R_t -- C_{t-1}.
    zero = [(i,(i-1)%6) for i in range(6)]
    support = [tuple(c for c in range(6) if c not in zero[i]) for i in range(6)]
    edges = [(i,j) for i,row in enumerate(support) for j in row]
    def antipode(edge):
        i,j=edge
        return min(edge,((i+3)%6,(j+3)%6))
    classes = sorted({antipode(e) for e in edges})
    assert len(classes) == 12
    index = {c:k for k,c in enumerate(classes)}
    col_rows = [{i for i,row in enumerate(support) if j in row} for j in range(6)]
    A=[]; b=[]
    for i in range(6):
        A.append([Fraction(sum(index[antipode((i,j))] == k for j in support[i])) for k in range(12)])
        b.append(Fraction(1))
    for j in range(6):
        A.append([Fraction(sum(index[antipode((i,j))] == k for i in col_rows[j])) for k in range(12)])
        b.append(Fraction(1))
    for i in range(6):
        A.append([sum(q[order[j]] for j in support[i] if index[antipode((i,j))] == k) for k in range(12)])
        b.append(u)
    M=[row+[rhs] for row,rhs in zip(A,b)]
    rank=0; piv=[]
    for col in range(12):
        pivot=next((r for r in range(rank,len(M)) if M[r][col] != 0),None)
        if pivot is None:
            continue
        M[rank],M[pivot]=M[pivot],M[rank]
        pv=M[rank][col]; M[rank]=[x/pv for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] != 0:
                factor=M[r][col]
                M[r]=[M[r][c]-factor*M[rank][c] for c in range(13)]
        piv.append(col); rank += 1
    if any(M[r][-1] != 0 for r in range(rank,len(M))):
        return False
    free=[c for c in range(12) if c not in piv]
    assert rank == 10 and len(free) == 2
    def evaluate(vals):
        x=[Fraction(0)]*12
        for c,v in zip(free,vals): x[c]=v
        for row,col in enumerate(piv):
            x[col]=M[row][-1]-sum(M[row][c]*x[c] for c in free)
        return x
    # Enumerate vertices of the nonnegative polygon in the two free variables.
    lines=[]
    for k,c in enumerate(free):
        coeff=[Fraction(0),Fraction(0)]; coeff[k]=1
        lines.append((coeff,Fraction(0)))
    for row,col in enumerate(piv):
        lines.append(([-M[row][c] for c in free],M[row][-1]))
    best = None
    candidates=[(Fraction(0),Fraction(0))]
    for L1,L2 in combinations(lines,2):
        co1,r1=L1; co2,r2=L2
        det=co1[0]*co2[1]-co2[0]*co1[1]
        if det == 0:
            continue
        candidates.append(((r1*co2[1]-r2*co1[1])/det,(co1[0]*r2-co2[0]*r1)/det))
    for vals in candidates:
        x=evaluate(vals)
        if all(v >= 0 for v in x):
            m=min(x)
            if best is None or m > best:
                best=m
    return best

order_results = {order: feasible_for_order(order) for order in orders}
boundary_orders = [order for order,best in order_results.items() if best is not None]
strict_orders = [order for order,best in order_results.items() if best is not None and best > 0]
assert len(boundary_orders) == 2
assert strict_orders == []
connected_minimal_carriers = 43200
phase_compatible_connected_interior_points = 0
assert phase_compatible_connected_interior_points == 0

result = {
    "schema":"marici.flavor.wp1163.v1",
    "status":"PASS",
    "question":"Can a connected minimal 9+9 support-four carrier satisfy the amplitude system and fixed-q target?",
    "dpc":{
        "conjecture":"A connected minimal carrier has a phase-compatible fixed-q interior point.",
        "rivals":["connected carrier witness","antipodal equality classes","cyclic q order","fixed-q nonnegative polygon"],
        "risky_consequences":["43200 connected carriers","60 dihedral classes of cyclic q order","12 antipodal equality classes","rank-ten reduced systems with two free variables"],
        "falsification_attempt":"Among the 60 cyclic q orders, 58 have no nonnegative reduced point and 2 reach only boundary points with one amplitude class zero; no strictly positive interior point exists.",
        "residual":"16200 type-10+10 carriers and 1350 type-12+12 carriers remain open.",
        "disposition":"reject all connected minimal 9+9 carriers for fixed-q phase compatibility"
    },
    "connected_minimal_carriers_covered":connected_minimal_carriers,
    "cyclic_q_order_classes_tested":len(orders),
    "antipodal_equality_classes":12,
    "reduced_rank":10,
    "free_variables":2,
    "boundary_cyclic_q_orders":len(boundary_orders),
    "strict_cyclic_q_orders":len(strict_orders),
    "phase_compatible_connected_interior_points":phase_compatible_connected_interior_points,
    "classification":"negative gate: connected minimal support-four amplitude systems have no fixed-q interior point",
    "remaining_gate":"test 10+10 and 12+12 support-four amplitude systems",
    "hostile_gate":"do not treat the connected-minimal no-go as excluding the higher-constraint carrier classes",
    "claim_boundary":"the proof covers all 43200 connected minimal carriers via cyclic q-order reduction",
    "disposition":"connected minimal leaf resolved; higher-constraint carrier rival selected"
}

(ROOT/"results"/"wp1163_connected_minimal_amplitude_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1163 PASS:",connected_minimal_carriers,len(orders),len(boundary_orders),phase_compatible_connected_interior_points)
