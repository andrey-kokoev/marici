import json
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

def rref(A,b,n):
    M=[row[:] + [rhs] for row,rhs in zip(A,b)]
    rank=0; piv=[]
    for col in range(n):
        p=next((r for r in range(rank,len(M)) if M[r][col] != 0),None)
        if p is None: continue
        M[rank],M[p]=M[p],M[rank]
        pv=M[rank][col]; M[rank]=[x/pv for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] != 0:
                f=M[r][col]; M[r]=[M[r][c]-f*M[rank][c] for c in range(n+1)]
        piv.append(col); rank += 1
    if any(M[r][-1] != 0 for r in range(rank,len(M))): return None
    return M[:rank],piv,[c for c in range(n) if c not in piv]

def boundary_point(A,b,n):
    solved=rref(A,b,n)
    if solved is None: return None
    M,piv,free=solved
    def evaluate(vals):
        x=[Fraction(0)]*n
        for c,v in zip(free,vals): x[c]=v
        for row,col in enumerate(piv):
            x[col]=M[row][-1]-sum(M[row][c]*x[c] for c in free)
        return x
    lines=[]
    for k,c in enumerate(free):
        co=[Fraction(0)]*len(free); co[k]=1
        lines.append((co,Fraction(0)))
    for row,col in enumerate(piv):
        lines.append(([-M[row][c] for c in free],M[row][-1]))
    candidates=[tuple(Fraction(0) for _ in free)]
    for chosen in combinations(lines,len(free)):
        A0=[L[0] for L in chosen]; b0=[L[1] for L in chosen]
        sol=rref(A0,b0,len(free))
        if sol is None: continue
        N,pv,fr=sol
        if len(pv) == len(free): candidates.append(tuple(N[r][-1] for r in range(len(free))))
    feasible=[evaluate(vals) for vals in candidates]
    feasible=[x for x in feasible if all(v >= 0 for v in x)]
    if not feasible: return None
    return max(feasible,key=min)

def single_overlaps(P):
    rows=[{j for j,x in enumerate(row) if x > 0} for row in P]
    cols=[{i for i in range(6) if P[i][j] > 0} for j in range(6)]
    row_hits=[(i,k,sorted(rows[i]&rows[k])) for i in range(6) for k in range(i+1,6) if len(rows[i]&rows[k]) == 1]
    col_hits=[(i,k,sorted(cols[i]&cols[k])) for i in range(6) for k in range(i+1,6) if len(cols[i]&cols[k]) == 1]
    return row_hits,col_hits

inventory=[]
# WP1153 irregular support-three witness.
R=[{0,1,2},{0,2,4},{0,3,4},{1,3,5},{1,2,5},{3,4,5}]
row_hits=[(i,k) for i in range(6) for k in range(i+1,6) if len(R[i]&R[k]) == 1]
assert len(row_hits) == 6
inventory.append({"id":"wp1153_irregular_support_three","unitary":False,"reason":"six single-overlap row pairs"})

# WP1158 boundary support-four point.
P1158=[
 [0,0,0,Fraction(11,12),Fraction(1,12),0],
 [0,Fraction(11,36),0,0,Fraction(7,18),Fraction(11,36)],
 [Fraction(5,12),0,0,Fraction(1,12),Fraction(1,2),0],
 [0,Fraction(11,36),0,0,0,Fraction(25,36)],
 [Fraction(1,60),Fraction(7,18),Fraction(17,30),0,Fraction(1,36),0],
 [Fraction(17,30),0,Fraction(13,30),0,0,0]]
rh,ch=single_overlaps(P1158)
assert len(rh) == 5 and len(ch) == 5
inventory.append({"id":"wp1158_boundary_support_four","unitary":False,"reason":"single-overlap rows and columns"})

# WP1163 connected-minimal boundary points: 12 antipodal classes.
def canon(order):
    forms=[]
    for s in (order,tuple(reversed(order))): forms.extend(s[k:]+s[:k] for k in range(6))
    return min(forms)
orders=sorted({canon(p) for p in permutations(range(6))})
zero=[(i,(i-1)%6) for i in range(6)]
support=[tuple(c for c in range(6) if c not in zero[i]) for i in range(6)]
def ant(e): return min(e,((e[0]+3)%6,(e[1]+3)%6))
reps=sorted({ant((i,j)) for i,row in enumerate(support) for j in row})
groups=[[e for i,row in enumerate(support) for j in row for e in [(i,j)] if ant(e)==r] for r in reps]
col_rows=[{i for i,row in enumerate(support) if j in row} for j in range(6)]
boundary=[]
for order in orders:
    A=[]; b=[]
    for i in range(6):
        A.append([Fraction(sum(reps.index(ant((i,j))) == k for j in support[i])) for k in range(12)]); b.append(Fraction(1))
    for j in range(6):
        A.append([Fraction(sum(reps.index(ant((i,j))) == k for i in col_rows[j])) for k in range(12)]); b.append(Fraction(1))
    for i in range(6):
        A.append([sum(q[order[j]] for j in support[i] if reps.index(ant((i,j))) == k) for k in range(12)]); b.append(u)
    x=boundary_point(A,b,12)
    if x is not None: boundary.append((order,x))
assert len(boundary) == 2 and all(min(x) == 0 for _,x in boundary)
for order,x in boundary:
    P=[[Fraction(0)]*6 for _ in range(6)]
    for cl,v in zip(groups,x):
        for i,j in cl: P[i][j]=v
    rh,ch=single_overlaps(P)
    assert rh and ch
    inventory.append({"id":"wp1163_connected_boundary","unitary":False,"reason":"single-overlap rows and columns"})

# WP1166 C4+C8 boundary points: 45 q-label structural classes.
def canon4(seq):
    forms=[]
    for s in (seq,tuple(reversed(seq))): forms.extend(s[k:]+s[:k] for k in range(4))
    return min(forms)
label_classes=[]
for small in combinations(range(6),2):
    rest=tuple(x for x in range(6) if x not in small); seen=set()
    for second in rest[1:]:
        rem=[x for x in rest[1:] if x != second]
        for tail in (tuple(rem),tuple(reversed(rem))):
            key=canon4((rest[0],second)+tail)
            if key not in seen: seen.add(key); label_classes.append((small,key))
assert len(label_classes) == 45
zero=[(0,1),(0,1),(2,3),(3,4),(4,5),(5,2)]
support=[tuple(c for c in range(6) if c not in zero[i]) for i in range(6)]
groups=[[(0,j),(1,j)] for j in range(2,6)] + [[(i,0),(i,1)] for i in range(2,6)]
groups += [[(i,j)] for i in range(2,6) for j in support[i] if j >= 2]
assert len(groups) == 16
class_of={e:k for k,cl in enumerate(groups) for e in cl}
col_rows=[{i for i,row in enumerate(support) if j in row} for j in range(6)]
boundary=[]
for small,large in label_classes:
    labels=small+large; A=[]; b=[]
    for i in range(6):
        A.append([Fraction(sum(class_of[i,j] == k for j in support[i])) for k in range(16)]); b.append(Fraction(1))
    for j in range(6):
        A.append([Fraction(sum(class_of[i,j] == k for i in col_rows[j])) for k in range(16)]); b.append(Fraction(1))
    for i in range(6):
        A.append([sum(q[labels[j]] for j in support[i] if class_of[i,j] == k) for k in range(16)]); b.append(u)
    x=boundary_point(A,b,16)
    if x is not None: boundary.append(((small,large),x))
assert len(boundary) == 2 and all(min(x) == 0 for _,x in boundary)
for lc,x in boundary:
    P=[[Fraction(0)]*6 for _ in range(6)]
    for cl,v in zip(groups,x):
        for i,j in cl: P[i][j]=v
    rh,ch=single_overlaps(P)
    assert rh and ch
    inventory.append({"id":"wp1166_c4c8_boundary","unitary":False,"reason":"single-overlap rows and columns"})

assert len(inventory) == 6
assert all(item["unitary"] is False for item in inventory)
result={
    "schema":"marici.flavor.wp1167.v1",
    "status":"PASS",
    "question":"Can the known boundary or irregular fixed-q candidates be unistochastic?",
    "dpc":{
        "conjecture":"A boundary or irregular support candidate supplies a unistochastic modulus after regular support four was excluded.",
        "rivals":["irregular support-three witness","disconnected boundary point","connected boundary points","C4+C8 boundary points"],
        "risky_consequences":["six exact candidates","boundary class collapse","single-overlap unitary obstruction"],
        "falsification_attempt":"All six candidates have a single-overlap pair and therefore cannot be the squared modulus of a unitary.",
        "residual":"No known boundary or irregular candidate remains; support-five sparse search is the next executable rival.",
        "disposition":"reject the current boundary and irregular inventory"
    },
    "candidates_tested":len(inventory),
    "unistochastic_candidates":0,
    "inventory":inventory,
    "classification":"negative gate: current boundary and irregular fixed-q candidates are not unistochastic",
    "remaining_gate":"search graph-compatible support-five carriers and their amplitude systems",
    "hostile_gate":"do not treat an exact fixed-q boundary point as a unitary modulus",
    "claim_boundary":"the result rejects the six known candidates but does not yet enumerate all irregular supports",
    "disposition":"boundary leaf resolved; support-five rival selected"
}
(ROOT/"results"/"wp1167_boundary_unistochastic_inventory.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1167 PASS:",len(inventory),0)
