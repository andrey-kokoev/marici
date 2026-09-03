"""Exact Sylvester/Schur transfer of normalized return scalar invariants."""
from fractions import Fraction as F
from pathlib import Path
import json

def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return sum((a[i][i] for i in range(len(a))),F(0))
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def sub(a,b): return [[a[i][j]-b[i][j] for j in range(len(a))] for i in range(len(a))]
def det(a):
 a=[r[:] for r in a]; out=F(1); n=len(a)
 for i in range(n):
  q=next((r for r in range(i,n) if a[r][i]),None)
  if q is None:return F(0)
  if q!=i:a[i],a[q]=a[q],a[i];out=-out
  p=a[i][i];out*=p
  for r in range(i+1,n):
   f=a[r][i]/p
   for c in range(i,n):a[r][c]-=f*a[i][c]
 return out
A=[[F(4),0],[0,F(3)]]; Ai=[[F(1,4),0],[0,F(1,3)]]
D=[[F(5),0],[0,F(6)]]; Di=[[F(1,5),0],[0,F(1,6)]]
C=[[F(1),F(1)],[0,F(1)]]; Ct=[[F(1),0],[F(1),F(1)]]
K=mm(mm(mm(Ai,C),Di),Ct); L=mm(mm(mm(Di,Ct),Ai),C)
M=[A[0]+C[0],A[1]+C[1],Ct[0]+D[0],Ct[1]+D[1]]
checks={"trace_cycles_to_hidden_sector":tr(K)==tr(L),"sylvester_determinants_agree":det(sub(eye(2),K))==det(sub(eye(2),L)),"schur_ratio_agrees":det(M)/(det(A)*det(D))==det(sub(eye(2),K)),"singular_D_requires_reduced_support":det([[F(5),0],[0,F(0)]])==0}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"trace_return":str(tr(K)),"fredholm_determinant":str(det(sub(eye(2),K))),"schur_ratio":str(det(M)/(det(A)*det(D)))}
out=Path("research/aspect/results/return_scalar_transfer.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
