#!/usr/bin/env python3
"""Exact finite witness for shell leakage coherence after multiplier/observation transport."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
pos=(-3,-2,-1,1,2,3);n=len(pos)
# Same exact Fourier permutation used by the source Q/D hostile fixture.
out_of=tuple((j-2)%n for j in range(n))
def F(x):
 y=[0]*n
 for j,v in enumerate(x):y[out_of[j]]+=v
 return y
def P(x,r):return [v if abs(pos[i])<r else 0 for i,v in enumerate(x)]
def sub(x,y):return [a-b for a,b in zip(x,y)]
def add(x,y):return [a+b for a,b in zip(x,y)]
def A(x,r):return P(F(sub(x,P(x,r))),r)
def shell(x,r,s):return P(F(sub(P(x,s),P(x,r))),r)
def transported_tail(x,r,s):return P(F(sub(x,P(x,s))),r)
m=(2,-1,3,4,-2,1)
def M(x):return [m[i]*x[i] for i in range(n)]
def O(x):return (x[2],x[3])
vectors=[[1 if mask&(1<<i) else -1 for i in range(n)] for mask in range(1<<n)]
checks={
 'shell_cocycle_after_multiplier':all(A(M(x),2)==add(shell(M(x),2,3),transported_tail(M(x),2,3)) for x in vectors),
 'shell_cocycle_after_observation':all(O(A(M(x),2))==O(add(shell(M(x),2,3),transported_tail(M(x),2,3))) for x in vectors),
 'nonzero_lax_cell_retained':any(any(A(M(x),2)) for x in vectors),
}
out={'schema':'marici.nima.qdlo-leakage-transport.v1','checks':checks,'theorem':'Fourier leakage shell additivity survives admitted multiplier and retained-observation transport while remaining nonzero','passed':all(checks.values()),'boundary':'finite exact witness accompanying the Q/D graph estimate; no strict finite-cutoff commutation claimed'}
p=ROOT/'research/nima/results/qdlo-leakage-transport.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
