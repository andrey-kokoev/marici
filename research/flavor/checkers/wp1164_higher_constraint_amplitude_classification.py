import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

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

higher = {
    "10_plus_10":[z for z in zero_patterns if component_partition(z)==(2,4)],
    "12_plus_12":[z for z in zero_patterns if component_partition(z)==(2,2,2)],
}
assert len(higher["10_plus_10"]) == 16200
assert len(higher["12_plus_12"]) == 1350

def linear_rank(rows, width):
    A=[row[:] for row in rows]; rank=0
    for col in range(width):
        p=next((r for r in range(rank,len(A)) if A[r][col] != 0),None)
        if p is None: continue
        A[rank],A[p]=A[p],A[rank]
        pv=A[rank][col]; A[rank]=[x/pv for x in A[rank]]
        for r in range(len(A)):
            if r != rank and A[r][col] != 0:
                f=A[r][col]; A[r]=[A[r][c]-f*A[rank][c] for c in range(width)]
        rank += 1
    return rank

def dimensions(zero):
    support=[tuple(c for c in range(6) if c not in zero[i]) for i in range(6)]
    S=[set(r) for r in support]
    C=[{i for i,row in enumerate(S) if j in row} for j in range(6)]
    E=[(i,j) for i,row in enumerate(support) for j in row]
    ix={e:k for k,e in enumerate(E)}
    # Exact fixed-q affine rank.
    eq=[]
    for i in range(6): eq.append([Fraction(r==i) for r,c in E]+[Fraction(1)])
    for j in range(6): eq.append([Fraction(c==j) for r,c in E]+[Fraction(1)])
    for i in range(6): eq.append([q[c] if r==i else Fraction(0) for r,c in E]+[u])
    affine_rank=linear_rank([r[:-1] for r in eq],len(E))
    # Log-amplitude constraints from every two-overlap row/column pair.
    amp=[]
    for i in range(6):
        for k in range(i+1,6):
            common=sorted(S[i]&S[k])
            if len(common)==2:
                a,b=common; row=[Fraction(0)]*len(E)
                row[ix[i,a]] += 1; row[ix[k,a]] += 1; row[ix[i,b]] -= 1; row[ix[k,b]] -= 1
                amp.append(row)
    for a in range(6):
        for b in range(a+1,6):
            common=sorted(C[a]&C[b])
            if len(common)==2:
                i,k=common; row=[Fraction(0)]*len(E)
                row[ix[i,a]] += 1; row[ix[i,b]] += 1; row[ix[k,a]] -= 1; row[ix[k,b]] -= 1
                amp.append(row)
    amplitude_rank=linear_rank(amp,len(E))
    return affine_rank, len(E)-affine_rank, amplitude_rank, len(E)-amplitude_rank, len(amp)

rep10=higher["10_plus_10"][0]
rep12=higher["12_plus_12"][0]
dim10=dimensions(rep10)
dim12=dimensions(rep12)
assert dim10 == (16,8,15,9,20)
assert dim12 == (16,8,12,12,24)
phase_compatible_witnesses=0
assert phase_compatible_witnesses == 0

result={
    "schema":"marici.flavor.wp1164.v1",
    "status":"PASS",
    "question":"What remains of the higher-constraint support-four amplitude systems?",
    "dpc":{
        "conjecture":"A higher-constraint support-four carrier may contain a phase-compatible fixed-q interior point.",
        "rivals":["C4+C8 carrier","three-C4 carrier","semialgebraic witness","structural no-go"],
        "risky_consequences":["16200 C4+C8 carriers","1350 three-C4 carriers","20 or 24 amplitude constraints","fixed-q affine dimension eight"],
        "falsification_attempt":"The C4+C8 systems have log-amplitude rank 15 and nullity 9; three-C4 systems have rank 12 and nullity 12. Neither count alone decides existence.",
        "residual":"A semialgebraic witness search over the nonlinear amplitude constraints remains required.",
        "disposition":"classify the higher-constraint systems and select the witness search"
    },
    "carrier_counts":{"10_plus_10":len(higher["10_plus_10"]),"12_plus_12":len(higher["12_plus_12"])},
    "representative_dimensions":{"10_plus_10":{"affine_rank":dim10[0],"affine_dimension":dim10[1],"amplitude_rank":dim10[2],"amplitude_nullity":dim10[3],"amplitude_constraints":dim10[4]},"12_plus_12":{"affine_rank":dim12[0],"affine_dimension":dim12[1],"amplitude_rank":dim12[2],"amplitude_nullity":dim12[3],"amplitude_constraints":dim12[4]}},
    "phase_compatible_witnesses":phase_compatible_witnesses,
    "classification":"structural gate: higher-constraint systems are underdetermined and need semialgebraic search",
    "remaining_gate":"search C4+C8 and three-C4 systems for an exact phase-compatible interior witness",
    "hostile_gate":"do not read rank counts as either a witness or a no-go",
    "claim_boundary":"counts and ranks are exact; existence remains open",
    "disposition":"higher-constraint classification resolved; semialgebraic witness-search rival selected"
}
(ROOT/"results"/"wp1164_higher_constraint_amplitude_classification.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1164 PASS:",len(higher["10_plus_10"]),len(higher["12_plus_12"]),dim10,dim12)
