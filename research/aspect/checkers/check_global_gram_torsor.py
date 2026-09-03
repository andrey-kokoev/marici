"""Exact global Gram factorization and torsor-radical audit."""
from fractions import Fraction as F
from pathlib import Path
import json

def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def mv(a,v):return [sum((a[i][j]*v[j] for j in range(len(v))),F(0)) for i in range(len(a))]
def dot(a,b):return sum((a[i]*b[i] for i in range(len(a))),F(0))
B=[[F(1),0,F(1)],[0,F(1),F(1)]];Q=mm(tr(B),B);v=[F(1),F(1),F(-1)];w=[F(1),0,0]
samples=[[F(1),F(2),F(3)],[F(-1),F(2),0],v]
checks={"torsor_direction_killed_by_route_map":mv(B,v)==[0,0],"torsor_direction_is_joint_radical":mv(Q,v)==[0,0,0],"nonradical_direction_detected":mv(B,w)!=[0,0] and dot(w,mv(Q,w))>0,"gram_identity_on_samples":all(dot(x,mv(Q,x))==dot(mv(B,x),mv(B,x)) for x in samples)}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"Q":[[str(x) for x in r] for r in Q],"conclusion":"one global route map B certifies Q=B*B positive and reduces torsor radical membership to Bv=0"}
out=Path("research/aspect/results/global_gram_torsor.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
