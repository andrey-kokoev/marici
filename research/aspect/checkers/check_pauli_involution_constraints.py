"""Exact rational audit of grade-parity and grade-exchange conjugations."""
from fractions import Fraction as F
from pathlib import Path
import json

def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(2)),F(0)) for j in range(2)] for i in range(2)]
def conj_by(s,k):return mm(mm(s,k),s)
a=F(1,2);x=F(1,4);z=F(1,5)
K=[[a+z,x],[x,a-z]]
Z=[[F(1),0],[0,F(-1)]];X=[[0,F(1)],[F(1),0]]
Kz=conj_by(Z,K);Kx=conj_by(X,K)
parity_expected=[[a+z,-x],[-x,a-z]]
exchange_expected=[[a-z,x],[x,a+z]]
K_no_x=[[a+z,0],[0,a-z]]
K_no_z=[[a,x],[x,a]]
checks={"grade_parity_flips_only_X":Kz==parity_expected,"grade_exchange_flips_only_Z":Kx==exchange_expected,"grade_parity_invariance_allows_Z":conj_by(Z,K_no_x)==K_no_x,"grade_exchange_invariance_allows_X":conj_by(X,K_no_z)==K_no_z,"both_invariances_leave_only_scalar":conj_by(Z,[[a,0],[0,a]])==[[a,0],[0,a]] and conj_by(X,[[a,0],[0,a]])==[[a,0],[0,a]]}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"conclusion":"grade-parity invariance forces x=0; grade-exchange invariance forces z=0 but preserves the reciprocal cross-grade X channel"}
out=Path("research/aspect/results/pauli_involution_constraints.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
