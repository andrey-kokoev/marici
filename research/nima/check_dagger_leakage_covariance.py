#!/usr/bin/env python3
"""Exact finite witness for dagger covariance of centered-cutoff leakage."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
n=9
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(n)] for i in range(n)]
I=[[int(i==j) for j in range(n)] for i in range(n)]
# q is cyclic shift, dagger is reflection j -> -j, so D q D = q^{-1}.
q=[[int(i==(j+1)%n) for j in range(n)] for i in range(n)]
qi=[[int(i==(j-1)%n) for j in range(n)] for i in range(n)]
D=[[int(i==(-j)%n) for j in range(n)] for i in range(n)]
def P(rad):return [[int(i==j and min(i,n-i)<=rad) for j in range(n)] for i in range(n)]
def leak(Q,Px):return mm(mm(Px,Q),sub(I,Px))
PX=P(1);PY=P(2);A=leak(q,PX);Amate=leak(qi,PX)
shell=add(mm(mm(PX,qi),sub(PY,PX)),mm(mm(PX,qi),sub(I,PY)))
checks={'dagger_involution':mm(D,D)==I,'centered_cutoff_dagger_invariant':mm(mm(D,PX),D)==PX,'chart_arrow_reversed':mm(mm(D,q),D)==qi,'leakage_maps_to_reverse_leakage':mm(mm(D,A),D)==Amate,'dagger_mate_shell_cocycle':Amate==shell,'leakage_nonzero':any(any(x for x in row) for row in A)}
out={'schema':'marici.nima.dagger-leakage-covariance.v1','checks':checks,'identity':'D A_X^q D^-1 = A_X^(q^dagger)','passed':all(checks.values()),'scope':'centered dagger-invariant cutoffs and chart-dagger covariance on retained graph'}
p=ROOT/'research/nima/results/dagger-leakage-covariance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
