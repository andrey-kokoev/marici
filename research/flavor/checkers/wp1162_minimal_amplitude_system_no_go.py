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

def overlap_census(zero):
    zr=[set(x) for x in zero]
    zc=[{i for i,row in enumerate(zr) if j in row} for j in range(6)]
    return (sum(zr[i].isdisjoint(zr[j]) for i in range(6) for j in range(i+1,6)),
            sum(zc[i].isdisjoint(zc[j]) for i in range(6) for j in range(i+1,6)))

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

split_minimal = [z for z in zero_patterns
                 if overlap_census(z) == (9,9) and component_partition(z) == (3,3)]
assert len(split_minimal) == 7200

# In a split minimal carrier, every two-column row overlap is paired with the
# complementary two-row column overlap. For positive entries,
#   P_ia P_ka = P_ib P_kb and P_ia P_ib = P_ka P_kb
# force P_ka=P_ib and P_ia=P_kb. Propagate these equalities, then solve the
# linear fixed-q/doubly-stochastic system in equality classes.
def split_system_consistent(zero):
    support=[tuple(c for c in range(6) if c not in zero[i]) for i in range(6)]
    S=[set(r) for r in support]
    C=[{i for i,row in enumerate(S) if j in row} for j in range(6)]
    edges=[(i,j) for i,row in enumerate(support) for j in row]
    parent={e:e for e in edges}
    def find(x):
        while parent[x] != x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a != b: parent[b]=a
    for i in range(6):
        for k in range(i+1,6):
            common=sorted(S[i] & S[k])
            if len(common) != 2:
                continue
            a,b=common
            assert C[a] & C[b] == {i,k}
            union((k,a),(i,b)); union((i,a),(k,b))
    classes=list({find(e) for e in edges})
    assert len(classes) == 10
    A=[]; b=[]
    for i in range(6):
        A.append([Fraction(sum(find((i,j)) == cl for j in S[i])) for cl in classes]); b.append(Fraction(1))
    for j in range(6):
        A.append([Fraction(sum(find((i,j)) == cl for i in C[j])) for cl in classes]); b.append(Fraction(1))
    for i in range(6):
        A.append([sum(q[j] for j in S[i] if find((i,j)) == cl) for cl in classes]); b.append(u)
    M=[row+[rhs] for row,rhs in zip(A,b)]
    rank=0
    for col in range(len(classes)):
        pivot=next((r for r in range(rank,len(M)) if M[r][col] != 0),None)
        if pivot is None:
            continue
        M[rank],M[pivot]=M[pivot],M[rank]
        pv=M[rank][col]; M[rank]=[x/pv for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] != 0:
                factor=M[r][col]
                M[r]=[M[r][c]-factor*M[rank][c] for c in range(len(classes)+1)]
        rank += 1
    assert rank == 9
    return all(M[r][-1] == 0 for r in range(rank,len(M)))

consistent_split_carriers = sum(1 for z in split_minimal if split_system_consistent(z))
assert consistent_split_carriers == 0

result = {
    "schema":"marici.flavor.wp1162.v1",
    "status":"PASS",
    "question":"Can a split minimal 9+9 support-four carrier satisfy the amplitude system and fixed-q target?",
    "dpc":{
        "conjecture":"A split minimal support-four carrier has a phase-compatible fixed-q interior point.",
        "rivals":["split minimal carrier witness","amplitude equality classes","fixed-q linear consistency","connected minimal carrier"],
        "risky_consequences":["7200 split minimal carriers","ten amplitude equality classes","rank-nine linear system","fixed-q consistency"],
        "falsification_attempt":"Amplitude propagation reduces every split carrier to ten classes; the resulting fixed-q linear system is inconsistent for all 7200.",
        "residual":"43200 connected minimal carriers, 16200 type-10+10 carriers, and 1350 type-12+12 carriers remain open.",
        "disposition":"reject all split minimal 9+9 carriers for fixed-q phase compatibility"
    },
    "split_minimal_carriers_tested":len(split_minimal),
    "amplitude_equality_classes":10,
    "reduced_linear_rank":9,
    "consistent_split_carriers":consistent_split_carriers,
    "residual_carriers":{"connected_9_plus_9":43200,"10_plus_10":16200,"12_plus_12":1350},
    "classification":"negative gate: split minimal support-four amplitude systems are fixed-q inconsistent",
    "remaining_gate":"solve connected minimal and higher-constraint amplitude systems",
    "hostile_gate":"do not treat the split-carrier no-go as excluding connected or higher-constraint support-four carriers",
    "claim_boundary":"the proof covers exactly the 7200 split minimal carriers",
    "disposition":"minimal split amplitude-system leaf resolved; connected-system rival selected"
}

(ROOT/"results"/"wp1162_split_minimal_amplitude_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1162 PASS:",len(split_minimal),consistent_split_carriers)
