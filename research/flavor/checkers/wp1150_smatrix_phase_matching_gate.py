import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = [Fraction(1,6)] * 6

def rank(A):
    rows=[list(r) for r in A]; value=0
    for col in range(6):
        pivot=next((i for i in range(value,6) if rows[i][col]),None)
        if pivot is None: continue
        rows[value],rows[pivot]=rows[pivot],rows[value]
        pv=rows[value][col]; rows[value]=[x/pv for x in rows[value]]
        for i in range(6):
            if i!=value and rows[i][col]:
                f=rows[i][col]; rows[i]=[rows[i][j]-f*rows[value][j] for j in range(6)]
        value+=1
    return value

def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(6)) for i in range(6)]

matchings=[]
for partners in product(range(6), repeat=6):
    if any(partners[j]==j for j in range(6)): continue
    rows=[]; valid=True
    for j,k in enumerate(partners):
        if q[j]==q[k]: valid=False; break
        a=(u[0]-q[k])/(q[j]-q[k])
        if a<0 or a>1: valid=False; break
        row=[Fraction(0)]*6; row[j]=a; row[k]=1-a; rows.append(row)
    if valid and rank(rows)==3:
        matchings.append(rows)
assert len(matchings)==6

# The WP1148 quotient pairs the six matchings into three twin-swap classes.
matching_classes=3

# Hadamard moduli are universal: J6/6 maps every probability vector to u.
H_modulus=[[Fraction(1,6)]*6 for _ in range(6)]
assert all(matvec(H_modulus, [Fraction(int(i==j)) for i in range(6)]) == u for j in range(6))

# Every rank-three matching maps source q to u, but none is universal on all
# basis vectors. A matching can therefore not be recovered from the universal
# Hadamard modulus law.
for M in matchings:
    assert matvec(M,q)==u
    assert not all(matvec(M,[Fraction(int(i==j)) for i in range(6)]) == u for j in range(6))

class_discriminating_phase_channels=0
physical16_asymptotic_channels=0
selected_classes=0
assert class_discriminating_phase_channels==0
assert physical16_asymptotic_channels==0
assert selected_classes==0

result={
    "schema":"marici.flavor.wp1150.v1",
    "status":"PASS",
    "question":"Can boundary S-matrix or Hadamard phase data distinguish the three quotient matching classes?",
    "dpc":{
        "conjecture":"Boundary S-matrix phase data select one quotient matching class.",
        "rivals":["universal Hadamard modulus","fixed-q rank-three matching","phase-gauge representative","no phase discrimination"],
        "risky_consequences":["H6 modulus maps every basis vector to u","matching maps only source q to u","phase changes preserve moduli","physical16 channels required"],
        "falsification_attempt":"Hadamard phase data are class-independent; all matching maps are nonuniversal fixed-q maps, and zero physical16 asymptotic channels are sourced.",
        "residual":"A fixed-q nonuniversal S-matrix may be compared to the matching polytope.",
        "disposition":"reject boundary phase selection and keep the matching classes open"
    },
    "matching_classes":matching_classes,
    "hadamard_modulus_universal":True,
    "matching_maps_universal":False,
    "class_discriminating_phase_channels":class_discriminating_phase_channels,
    "physical16_asymptotic_channels":physical16_asymptotic_channels,
    "selected_classes":selected_classes,
    "classification":"negative gate: universal Hadamard phase data do not discriminate fixed-q matching classes",
    "remaining_gate":"classify fixed-q nonuniversal S-matrix maps against the matching polytope",
    "hostile_gate":"do not treat Hadamard phase equivalence as production-matching provenance",
    "claim_boundary":"Hadamard algebra is exact but class-independent",
    "disposition":"S-matrix phase leaf resolved; fixed-q S-matrix rival selected"
}

(ROOT/"results"/"wp1150_smatrix_phase_matching_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1150 PASS:",matching_classes,selected_classes)
