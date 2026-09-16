#!/usr/bin/env python3
"""Exact rational model of the proposed source/endpoint/crossing Weyl reservoir."""
from fractions import Fraction as F
import json
from pathlib import Path

def tr(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def sub(A,B): return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(c,A): return [[c*x for x in a] for a in A]
def diag(xs): return [[xs[i] if i==j else F(0) for j in range(len(xs))] for i in range(len(xs))]
def serial(A): return [[str(x) for x in row] for row in A]

# History eigenchannels and three distinct ports: source, fixed endpoint, moving crossing.
D=diag([F(-2),F(1),F(4)])
J=[[F(1),F(1),F(1)], [F(1),F(2),F(1)], [F(1),F(0),F(-1)]]
z,w=F(0),F(3)
Rz=diag([1/(D[i][i]-z) for i in range(3)])
Rw=diag([1/(D[i][i]-w) for i in range(3)])
MZ=mm(mm(tr(J),Rz),J); MW=mm(mm(tr(J),Rw),J)
rhs=scale(z-w,mm(mm(mm(tr(J),Rw),Rz),J))
res=sub(sub(MZ,MW),rhs)
zero=all(x==0 for row in res for x in row)
# Third port is independent of the first two.
det=(J[0][0]*(J[1][1]*J[2][2]-J[1][2]*J[2][1])
     -J[0][1]*(J[1][0]*J[2][2]-J[1][2]*J[2][0])
     +J[0][2]*(J[1][0]*J[2][1]-J[1][1]*J[2][0]))
checks={"weyl_resolvent_identity_exact":zero,"three_ports_independent":det!=0,"moving_port_cross_entries_retained":MZ[2][0]!=0 and MZ[2][1]!=0}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.three-port-moving-index-weyl-identity.v1",
 "ports":["source_incidence","fixed_endpoint","moving_real_boundary_evaluation"],
 "identity":"M(z)-M(w)=(z-w) J^T R(w)R(z)J",
 "D":serial(D),"J":serial(J),"M_z":serial(MZ),"M_w":serial(MW),"residual":serial(res),
 "checks":checks,"passed":True,
 "analytical_interpretation":"The moving index current can be retained as an independent Weyl port while sharing one Green identity with source and fixed endpoint channels.",
 "claim_boundary":"Exact finite-dimensional architecture only; actual-Tate moving evaluation continuity and identification remain to be proved."
}
path=Path(__file__).parents[1]/"results"/"three_port_moving_index_weyl_identity.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
