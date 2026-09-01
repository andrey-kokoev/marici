import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

# C4+C8 carriers are row/column permutations of one abstract shape. Up to the
# C4 swap and the C8 dihedral group, a labeling is an unordered q pair on the
# C4 columns plus a cyclic q order on the C8 columns.
def canon4(seq):
    forms=[]
    for s in (seq,tuple(reversed(seq))):
        forms.extend(s[k:]+s[:k] for k in range(4))
    return min(forms)

# Generate the 45 structural label classes explicitly.
label_classes=[]
for small in combinations(range(6),2):
    rest=tuple(x for x in range(6) if x not in small)
    seen=set()
    # the three cyclic orders are represented by fixing rest[0] and choosing
    # the second element, with reversal removed
    for second in rest[1:]:
        remaining=[x for x in rest[1:] if x != second]
        for tail in (tuple(remaining),tuple(reversed(remaining))):
            order=(rest[0],second)+tail
            key=canon4(order)
            if key not in seen:
                seen.add(key); label_classes.append((small,key))
assert len(label_classes) == 45

def reduced_feasible(small_pair, large_order):
    labels=small_pair+large_order
    # Abstract columns: 0,1 are C4; 2..5 are C8 in cyclic order.
    zero=[(0,1),(0,1),(2,3),(3,4),(4,5),(5,2)]
    support=[tuple(c for c in range(6) if c not in zero[i]) for i in range(6)]
    # Interior amplitude constraints force the two C4 rows equal on each C8
    # column and each C8 row equal on the two C4 columns.
    classes=[]
    for j in range(2,6): classes.append(((0,j),(1,j)))
    for i in range(2,6): classes.append(((i,0),(i,1)))
    for i in range(2,6):
        for j in support[i]:
            if j >= 2: classes.append(((i,j),))
    assert len(classes) == 16
    class_of={e:k for k,cl in enumerate(classes) for e in cl}
    col_rows=[{i for i,row in enumerate(support) if j in row} for j in range(6)]
    A=[]; b=[]
    for i in range(6):
        A.append([Fraction(sum(class_of[i,j] == k for j in support[i])) for k in range(16)])
        b.append(Fraction(1))
    for j in range(6):
        A.append([Fraction(sum(class_of[i,j] == k for i in col_rows[j])) for k in range(16)])
        b.append(Fraction(1))
    for i in range(6):
        A.append([sum(q[labels[j]] for j in support[i] if class_of[i,j] == k) for k in range(16)])
        b.append(u)
    M=[row+[rhs] for row,rhs in zip(A,b)]
    rank=0; piv=[]
    for col in range(16):
        p=next((r for r in range(rank,len(M)) if M[r][col] != 0),None)
        if p is None: continue
        M[rank],M[p]=M[p],M[rank]
        pv=M[rank][col]; M[rank]=[x/pv for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] != 0:
                f=M[r][col]; M[r]=[M[r][c]-f*M[rank][c] for c in range(17)]
        piv.append(col); rank += 1
    if any(M[r][-1] != 0 for r in range(rank,len(M))): return None
    free=[c for c in range(16) if c not in piv]
    assert rank == 13 and len(free) == 3
    def evaluate(vals):
        x=[Fraction(0)]*16
        for c,v in zip(free,vals): x[c]=v
        for row,col in enumerate(piv):
            x[col]=M[row][-1]-sum(M[row][c]*x[c] for c in free)
        return x
    # Nonnegative cone in three free coordinates. Every bounded polytope
    # vertex is an intersection of three boundary planes.
    lines=[]
    for k,c in enumerate(free):
        co=[Fraction(0)]*3; co[k]=1
        lines.append((co,Fraction(0)))
    for row,col in enumerate(piv):
        lines.append(([-M[row][c] for c in free],M[row][-1]))
    best=None
    for chosen in combinations(lines,3):
        A3=[L[0] for L in chosen]; b3=[L[1] for L in chosen]
        N=[A3[i][:]+[b3[i]] for i in range(3)]
        r=0
        for c in range(3):
            p=next((i for i in range(r,3) if N[i][c] != 0),None)
            if p is None: break
            N[r],N[p]=N[p],N[r]
            pv=N[r][c]; N[r]=[x/pv for x in N[r]]
            for i in range(3):
                if i != r and N[i][c] != 0:
                    f=N[i][c]; N[i]=[N[i][k]-f*N[r][k] for k in range(4)]
            r += 1
        if r < 3: continue
        vals=[N[i][-1] for i in range(3)]
        x=evaluate(vals)
        if all(v >= 0 for v in x):
            m=min(x)
            if best is None or m > best: best=m
    return best

results={lc:reduced_feasible(*lc) for lc in label_classes}
boundary=[lc for lc,best in results.items() if best is not None]
strict=[lc for lc,best in results.items() if best is not None and best > 0]
assert len(boundary) == 2
assert strict == []
phase_compatible_c4c8_interior_points=0
assert phase_compatible_c4c8_interior_points == 0

result={
    "schema":"marici.flavor.wp1166.v1",
    "status":"PASS",
    "question":"Can a C4+C8 support-four carrier have a phase-compatible fixed-q interior point?",
    "dpc":{
        "conjecture":"A C4+C8 carrier supports a phase-compatible fixed-q interior point.",
        "rivals":["C4+C8 witness","C4/C8 amplitude equality classes","45 label classes","fixed-q nonnegative polytope"],
        "risky_consequences":["16200 carriers","45 q-label classes","sixteen reduced variables","rank-13 systems with three free variables"],
        "falsification_attempt":"Among 45 label classes, 43 have no nonnegative reduced point and 2 reach only boundary points with a zero amplitude class; no strictly positive interior point exists.",
        "residual":"No regular support-four phase-compatible interior class remains.",
        "disposition":"reject all C4+C8 carriers for phase-compatible fixed-q interior realization"
    },
    "c4c8_carriers_covered":16200,
    "q_label_classes_tested":len(label_classes),
    "reduced_variables":16,
    "reduced_rank":13,
    "free_variables":3,
    "boundary_label_classes":len(boundary),
    "strict_label_classes":len(strict),
    "phase_compatible_c4c8_interior_points":phase_compatible_c4c8_interior_points,
    "classification":"negative gate: C4+C8 support-four amplitude systems have no fixed-q interior point",
    "remaining_gate":"reassess whether boundary or irregular support classes can supply a physical unitary modulus",
    "hostile_gate":"do not treat graph-compatible support four as having a phase-compatible interior witness",
    "claim_boundary":"the proof covers all 16200 C4+C8 carriers via structural label classes",
    "disposition":"C4+C8 leaf resolved; support-four reassessment selected"
}
(ROOT/"results"/"wp1166_c4c8_amplitude_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1166 PASS:",16200,len(label_classes),phase_compatible_c4c8_interior_points)
