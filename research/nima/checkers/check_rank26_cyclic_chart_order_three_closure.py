#!/usr/bin/env python3
"""Verify the genuine three-cycle of physical residue-chart quotient maps."""
from __future__ import annotations
import contextlib,importlib,io,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3];BEN=ROOT/"research"/"benincasa";NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(NCHK)]
with contextlib.redirect_stdout(io.StringIO()):
    base=importlib.import_module("physical_four_mark_residue_twisted_derham")
    charts=importlib.import_module("g12_g31_residue_chart_transition")
    prior=importlib.import_module("check_rank26_physical_annihilator_chart_transport")
P=base.PRIME;HALF=(-pow(2,P-2,P))%P
OUT=ROOT/"research"/"nima"/"results"/f"rank26_cyclic_chart_order_three_closure_p{P}.json"
base.reduce_row=prior.reduce_complete

CYCLE={"g1":"g2","g2":"g3","g3":"g1","g23":"g31","g31":"g12","g12":"g23"}
N0=("g1","g2","g3","g23","g31")
N1=tuple(CYCLE[n] for n in N0)
N2=tuple(CYCLE[n] for n in N1)

def fiber1(x,y,z):
    k,q=base.fiber_data(y,z,x)
    return k,{CYCLE[n]:poly for n,poly in q.items()}

def fiber2(x,y,z):
    k,q=base.fiber_data(z,x,y)
    return k,{CYCLE[CYCLE[n]]:poly for n,poly in q.items()}

def transition(source,target):
    tpos={c:i for i,c in enumerate(target["free_low"])};T=[[0]*26 for _ in range(26)]
    for j,c in enumerate(source["free_low"]):
      label=source["ordered_columns"][c]
      red=prior.reduce_complete({target["columns"][label]:1},target["pivots"])
      for tc,v in red.items():
       if tc in tpos:T[tpos[tc]][j]=v
    return T

def identity_defect(M):return sum(M[i][j]!=(1 if i==j else 0) for i in range(26) for j in range(26))
def rank(M):return prior.rank([{i:v for i,v in enumerate(row) if v} for row in M])

def main():
    charts.GAMMA=HALF;charts.AMBIENT=14;charts.CUTOFF=7;charts.K_DEPTH=3
    p0=charts.presentation(base.fiber_data,(2,3,4),N0)
    p1=charts.presentation(fiber1,(4,2,3),N1)
    p2=charts.presentation(fiber2,(3,4,2),N2)
    T01=transition(p0,p1);T12=transition(p1,p2);T20=transition(p2,p0)
    product=prior.matmul(T20,prior.matmul(T12,T01))
    payload={"schema":"marici.rank26-cyclic-chart-order-three-closure.v1","prime":P,"gamma":"-1/2","k_pole_depth":3,"cycle":["G12@(2,3,4)","G23@(4,2,3)","G31@(3,4,2)","G12@(2,3,4)"],"mark_orders":[N0,N1,N2],"transition_ranks":[rank(T01),rank(T12),rank(T20)],"order_three_identity_defect":identity_defect(product),"passed":all(rank(T)==26 for T in (T01,T12,T20)) and identity_defect(product)==0}
    OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");print(json.dumps(payload,indent=2))
    if not payload["passed"]:raise SystemExit(1)
if __name__=="__main__":main()
