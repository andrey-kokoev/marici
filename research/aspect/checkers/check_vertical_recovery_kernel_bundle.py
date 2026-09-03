"""Exact rational audit of the vertical recovery-kernel bundle."""
from fractions import Fraction as F
from pathlib import Path
import json


def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]


def sub(a,b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mv(a,x):
    return [sum((a[i][k]*x[k] for k in range(len(x))),F(0)) for i in range(len(a))]


Id2=[[F(1),F(0)],[F(0),F(1)]]
records=[]
all_checks=[]
for s in [F(-2),F(0),F(3,2)]:
    I=[[F(1)],[s]]
    R=[[F(1),F(0)]]
    P=mm(I,R)
    Q=sub(Id2,P)
    dark=[F(0),F(1)]
    checks={
        "left_inverse":mm(R,I)==[[F(1)]],
        "P_is_projection":mm(P,P)==P,
        "Q_is_projection":mm(Q,Q)==Q,
        "Q_range_is_recovery_dark":mv(R,mv(Q,dark))==[F(0)],
        "Q_fixes_kernel_generator":mv(Q,dark)==dark,
        "P_plus_Q_is_identity":[[P[i][j]+Q[i][j] for j in range(2)] for i in range(2)]==Id2,
    }
    all_checks.extend(checks.values())
    records.append({"s":str(s),"I":[[str(v) for v in row] for row in I],"R":[[str(v) for v in row] for row in R],"Q":[[str(v) for v in row] for row in Q],"checks":checks})
result={
    "status":"pass" if all(all_checks) else "fail",
    "arithmetic":"fractions.Fraction only",
    "theorem":"Q_s=Id-I_s R_s is a projection with range ker R_s when R_s I_s=Id",
    "records":records,
    "hostile":"A proposed vertical auxiliary vector with nonzero R_s image is outside the maximal recovery-dark bundle.",
}
out=Path("research/aspect/results/vertical_recovery_kernel_bundle.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
