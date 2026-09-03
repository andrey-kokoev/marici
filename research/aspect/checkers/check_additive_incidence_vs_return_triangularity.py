"""Exact independence hostile: even-odd incidence does not force return triangularity."""
from fractions import Fraction as F
from pathlib import Path
import json

I=[[F(1),0],[0,F(1)]]
Z=[[F(0),0],[0,F(0)]]
P=I; Kplus=I; Kminus=I; M=I
R=[[F(0),F(1)],[F(1),F(0)]]
Pplus=[[F(1),0],[0,F(0)]]
Pminus=[[F(0),0],[0,F(1)]]

def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b): return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
incidence_residual=sub(mm(Kminus,P),mm(M,Kplus))
reverse_block=mm(mm(Pminus,R),Pplus)
checks={
 "normalized_even_odd_incidence_square_closes":incidence_residual==Z,
 "return_has_nonzero_reverse_block":reverse_block!=Z,
 "return_is_unitary_involution":mm(R,R)==I,
 "incidence_and_return_are_logically_independent":incidence_residual==Z and reverse_block!=Z,
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only; scalar 2pi i absorbed into typed multiplier","checks":checks,"incidence_residual":[[str(x) for x in row] for row in incidence_residual],"reverse_block":[[str(x) for x in row] for row in reverse_block],"conclusion":"the additive Fourier differentiation square constrains parity incidence but imposes no reverse-triangularity law on an independent Green return"}
out=Path("research/aspect/results/additive_incidence_vs_return_triangularity.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
