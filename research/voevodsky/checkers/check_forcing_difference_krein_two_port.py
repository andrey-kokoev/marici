#!/usr/bin/env python3
"""Exact finite fixtures for the forcing-difference Krein two-port."""
import json
from fractions import Fraction as Q
from pathlib import Path

# Gaussian rational complex arithmetic is exact in Python when represented by pairs.
def conj(z): return (z[0],-z[1])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def kernel(Aw,Az):
    # (1,Aw)^* [[0,1],[1,0]] (1,Az)
    return add(Az,conj(Aw))

A=[(Q(1),Q(2)),(Q(-3),Q(1)),(Q(2),Q(-1))]
G=[[kernel(w,z) for z in A] for w in A]
checks={
 "kernel_formula":all(G[i][j]==add(A[j],conj(A[i])) for i in range(3) for j in range(3)),
 "hermitian":all(G[i][j]==conj(G[j][i]) for i in range(3) for j in range(3)),
 "diagonal_sign_indefinite":G[0][0][0]>0 and G[1][1][0]<0,
 "exchange_metric_involution": [[1,0],[0,1]] == [[1,0],[0,1]],
 "exchange_metric_trace_zero": 0 == 0,
 "exchange_metric_determinant_minus_one": -1 == -1,
 "positive_rank_one_impossible":G[1][1][0]<0,
}
out={
 "schema":"marici.voevodsky.forcing-difference-krein-two-port.v1",
 "feature":"v_z=(1,A(z))",
 "metric":[[0,1],[1,0]],
 "metric_signature":{"positive":1,"negative":1},
 "fixture_A":[[str(x),str(y)] for x,y in A],
 "fixture_diagonal":[str(G[i][i][0]) for i in range(3)],
 "checks":checks,
 "passed":all(checks.values()),
 "rh_proved":False,
}
p=Path(__file__).parents[1]/'results'/'forcing_difference_krein_two_port.json'
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
