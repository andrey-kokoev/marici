"""Exact rational audit of equivariant zero-trace projection and defects."""
from fractions import Fraction as F
from pathlib import Path
import json


def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]

def add(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def neg(a): return [[-v for v in row] for row in a]
def sub(a,b): return add(a,neg(b))
def zero(a): return all(v==0 for row in a for v in row)

Id=[[F(1),0],[0,F(1)]]
T=[[F(1),0]]
P=[[F(1)],[0]]
A=sub(Id,mm(P,T))
UE=[[F(1)]]
Ugood=[[F(1),0],[0,F(-1)]]
Ubad=[[0,F(1)],[F(1),0]]

def audit(U):
    delta_P=sub(mm(U,P),mm(P,UE))
    delta_T=sub(mm(UE,T),mm(T,U))
    comm=sub(mm(U,A),mm(A,U))
    predicted=neg(add(mm(delta_P,T),mm(P,delta_T)))
    return {"commutes":zero(comm),"residual_identity":comm==predicted,"residual_nonzero":not zero(comm)}

good=audit(Ugood); bad=audit(Ubad)
checks={
    "A_is_idempotent":mm(A,A)==A,
    "T_A_is_zero":zero(mm(T,A)),
    "A_projects_onto_kernel_T":A==[[0,0],[0,F(1)]],
    "typed_intertwiners_give_equivariance":good["commutes"] and good["residual_identity"],
    "defect_formula_holds_in_hostile":bad["residual_identity"],
    "failed_intertwiner_produces_nonzero_residual":bad["residual_nonzero"],
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"formula":"U_H A-A U_H=-delta_P T-P delta_T","good":good,"hostile":bad}
out=Path("research/aspect/results/equivariant_zero_trace_projection.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
