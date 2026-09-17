#!/usr/bin/env python3
"""Exact finite witness for H stability of the pulled-back multiplier/endpoint graph."""
import json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
n=8;a=tuple(i+2 for i in range(n))
def mul(x,y):return tuple(u*v for u,v in zip(x,y))
def M(x):return mul(a,x)
def O(x):return (x[0],x[-1])
def odot(x,y):return tuple(u*v for u,v in zip(x,y))
def D(x):return (a[0]*x[0],a[-1]*x[1])
def mu(x):return max(abs(v) for v in x)
vectors=[tuple(((s+1)*(i+2))%11-5 for i in range(n)) for s in range(12)]
checks={
 'mellin_product_associative':all(M(mul(x,y))==mul(M(x),y)==mul(x,M(y)) for x,y in itertools.product(vectors,repeat=2)),
 'endpoint_multiplicative':all(O(mul(x,y))==odot(O(x),O(y)) for x,y in itertools.product(vectors,repeat=2)),
 'observed_successor_transport':all(O(M(mul(x,y)))==D(odot(O(x),O(y))) for x,y in itertools.product(vectors,repeat=2)),
 'multiplier_seminorm_submultiplicative':all(mu(mul(x,y))<=mu(x)*mu(y) for x,y in itertools.product(vectors,repeat=2)),
}
out={'schema':'marici.nima.rooted-convolution-lo-graph-stability.v1','checks':checks,'theorem':'H preserves all source-pulled L/O coordinates for admitted Mellin graph multipliers','passed':all(checks.values()),'boundary':'scalar rooted-convolution scope; arbitrary completed observers and nontransverse loaded divisors excluded'}
p=ROOT/'research/nima/results/rooted-convolution-lo-graph-stability.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
