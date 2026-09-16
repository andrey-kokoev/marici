#!/usr/bin/env python3
"""Exact Cl(2,1) audit of the local rotor, endpoint boost, and forced mixed bivector."""
import json
from pathlib import Path


def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(a,b): return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def sub(a,b): return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]
def sc(c,a): return [[c*x for x in row] for row in a]
def eq(a,b): return a==b

I=[[1,0],[0,1]]; Z=[[0,0],[0,0]]
g1=[[1,0],[0,-1]]
g2=[[0,1],[1,0]]
g3=[[0,1],[-1,0]]
B12=mm(g1,g2); B13=mm(g1,g3); B23=mm(g2,g3)
comm=lambda a,b:sub(mm(a,b),mm(b,a))
checks={
 "gamma1_square_plus":eq(mm(g1,g1),I),
 "gamma2_square_plus":eq(mm(g2,g2),I),
 "gamma3_square_minus":eq(mm(g3,g3),sc(-1,I)),
 "pairwise_anticommutation":all(eq(add(mm(a,b),mm(b,a)),Z) for a,b in ((g1,g2),(g1,g3),(g2,g3))),
 "elliptic_bivector_square_minus":eq(mm(B12,B12),sc(-1,I)),
 "hyperbolic_bivector_square_plus":eq(mm(B13,B13),I),
 "forced_mixed_commutator":eq(comm(B12,B13),sc(-2,B23)),
 "mixed_closure_13_23":eq(comm(B13,B23),sc(2,B12)),
 "mixed_closure_23_12":eq(comm(B23,B12),sc(-2,B13)),
}
out={
 "schema":"marici.voevodsky.clifford-endpoint-mixed-channel.v1",
 "signature":"Cl(2,1) irreducible real matrix model",
 "B12":B12,"B13":B13,"B23":B23,
 "checks":checks,
 "passed":all(checks.values()),
 "interpretation":"The elliptic local-current and hyperbolic endpoint generators close only after adjoining the forced B23 mixed Green channel.",
 "claim_boundary":"Exact Clifford algebra only; no physical compression, analytic domain, or positivity claim."
}
path=Path(__file__).resolve().parents[1]/'results/clifford_endpoint_mixed_channel.json'
path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(not out['passed'])
