"""Exact audit: self-adjoint return turns one-way triangularity into reduction."""
from fractions import Fraction as F
from pathlib import Path
import json

Pplus=[[F(1),0],[0,F(0)]]
Pminus=[[F(0),0],[0,F(1)]]
C=[[F(1),F(1)],[0,F(1)]]
Ct=[[F(1),0],[F(1),F(1)]]
K=[[F(2),F(1)],[F(1),F(1)]]
Z=[[F(0),0],[0,F(0)]]

def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(2)),F(0)) for j in range(2)] for i in range(2)]
def tr(a): return [list(x) for x in zip(*a)]
forward=mm(mm(Pminus,K),Pplus)
reverse=mm(mm(Pplus,K),Pminus)
C_preserves_flag=mm(mm(Pminus,C),Pplus)==Z
checks={
 "C_preserves_declared_one_step_flag":C_preserves_flag,
 "K_equals_C_Cstar":K==mm(C,Ct),
 "K_is_positive":K[0][0]>=0 and K[1][1]>=0 and K[0][0]*K[1][1]-K[0][1]*K[1][0]>=0,
 "schur_return_recreates_reverse_grade_path":forward!=Z,
 "selfadjoint_offdiagonal_blocks_are_adjoint_pair":reverse==tr(forward),
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"K":[[str(x) for x in row] for row in K],"Pminus_K_Pplus":[[str(x) for x in row] for row in forward],"conclusion":"filtration preservation by C does not survive C D^-1 C*; for self-adjoint K, one-way triangularity forces both off-diagonal blocks to vanish"}
out=Path("research/aspect/results/selfadjoint_return_filtration.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
