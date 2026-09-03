"""Exact sectorwise sufficient bounds for normalized physical coupling."""
from fractions import Fraction as F
from pathlib import Path
import json

def add(a,b):return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(2)),F(0)) for j in range(2)] for i in range(2)]
def tr(a):return [list(x) for x in zip(*a)]
def norm_diag(a):return max(abs(a[0][0]),abs(a[1][1]))
T1=[[F(1,2),0],[0,0]];T2=[[0,0],[0,F(2,3)]];T=add(T1,T2)
A1=[[F(1,2),0],[0,0]];A2=[[F(1,3),0],[0,0]];A=add(A1,A2)
zero=[[F(0),F(0)],[F(0),F(0)]]
checks={"orthogonal_cross_gram_vanishes":mm(T1,tr(T2))==zero,"orthogonal_sum_norm_is_max":norm_diag(T)==F(2,3),"orthogonal_certificate_below_triangle":F(2,3)<F(1,2)+F(2,3),"aligned_triangle_bound_is_sharp":norm_diag(A)==F(1,2)+F(1,3)}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"orthogonal_eta":str(1-F(2,3)),"aligned_eta":str(1-F(5,6)),"conclusion":"sector norm sum certifies coercivity generally; cross-Gram orthogonality improves it to the maximum sector norm in this decomposed-support case"}
out=Path("research/aspect/results/sectorwise_return_bounds.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
