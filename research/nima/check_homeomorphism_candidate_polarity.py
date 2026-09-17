#!/usr/bin/env python3
"""Exact finite audit of opposite polarity as an antiunitary C2 presentation."""
import json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def conj(z):return complex(z.real,-z.imag)
def D(x):return tuple(conj(z) for z in reversed(x))
def inner(x,y):return sum(conj(a)*b for a,b in zip(x,y))
def norm2(x):return inner(x,x).real
def matstar(A):return tuple(tuple(conj(A[j][i]) for j in range(len(A))) for i in range(len(A[0])))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
vectors=[tuple(complex((s+i)%5-2,(2*s+i)%7-3) for i in range(4)) for s in range(8)]
A=((1+1j,2),(3j,4-1j));B=((2,-1j),(1+2j,3))
endpoint=lambda x:(conj(x[1]),conj(x[0]))
checks={'dagger_involutive':all(D(D(x))==x for x in vectors),'antiunitary_norm':all(norm2(D(x))==norm2(x) for x in vectors),'antiisometry_pairing':all(inner(D(x),D(y))==conj(inner(x,y)) for x,y in itertools.product(vectors,repeat=2)),'product_order_reversed':matstar(mm(A,B))==mm(matstar(B),matstar(A)),'endpoint_swap_conjugation_involutive':all(endpoint(endpoint((x[0],x[-1])))==(x[0],x[-1]) for x in vectors)}
out={'schema':'marici.nima.homeomorphism-candidate-polarity.v1','candidate':'positive and negative minimal generated signed carriers are conjugate-homeomorphic presentations','classification':'exact antiunitary C2 action on signed carriers; positive quotient descent conditional on Douglas acceptance','checks':checks,'passed':all(checks.values()),'axis_effect':'polarity becomes Real/dagger equivariance, not a forgotten ordinary coordinate'}
p=ROOT/'research/nima/results/homeomorphism-candidate-polarity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
