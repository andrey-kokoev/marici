"""Exact finite audit of observational quotient plus integral primitivity."""
from fractions import Fraction as Fq
from math import gcd
from pathlib import Path
import json

F=[[1,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,1,1]]
S=[[-2 if i==j else 0 for j in range(6)] for i in range(6)]
N=[[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]]
d=[1]*6

def mv(a,v): return [sum(Fq(x)*Fq(y) for x,y in zip(row,v)) for row in a]
def mm(a,b): return [[sum(Fq(a[i][k])*Fq(b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a): return [list(x) for x in zip(*a)]
Fd=mv(F,d)
FS=mm(F,S)
checks={
 "three_invisible_pair_difference_directions":all(mv(F,n)==[0,0,0] for n in N),
 "transport_preserves_invisible_subspace":all(mv(F,mv(S,n))==[0,0,0] for n in N),
 "transport_adds_no_observational_resolution":FS==[[-2*x for x in row] for row in F],
 "forgotten_boundary_is_nonprimitive":gcd(*[abs(int(x)) for x in Fd])==2,
 "sheet_parity_not_strictly_unitary_standard_metric":mm(transpose(S),S)!=[[1 if i==j else 0 for j in range(6)] for i in range(6)],
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"observational_quotient_dimension":3,"invisible_dimension":3,"forgotten_boundary":[str(x) for x in Fd],"forgotten_boundary_content":2,"conclusion":"the rational identity quotient merges occurrence pairs, while integral coherence requires marked primitive-lattice data; transports constrain invariance but do not define distinguishability by their kernels"}
out=Path("research/aspect/results/finite_coherence_identity_quotient.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
