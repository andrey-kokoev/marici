#!/usr/bin/env python3
"""Exact finite witness for V stability of the pulled-back multiplier/endpoint graph."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
n=8
a=tuple(i+2 for i in range(n));h1=tuple((-1 if i%2 else 1) for i in range(n));h2=tuple(i+1 for i in range(n))
def mul(x,y):return tuple(u*v for u,v in zip(x,y))
def M(x):return mul(a,x)
def cut(x):return (tuple(-v for v in mul(h1,x)),tuple(-v for v in mul(h2,x)))
def O(x):return (x[0],x[-1])
def D(h,y):return (h[0]*y[0],h[-1]*y[1])
def cutO(y):return (tuple(-v for v in D(h1,y)),tuple(-v for v in D(h2,y)))
def branchmap(fn,branches):return tuple(fn(b) for b in branches)
vectors=[tuple(((s+2)*(i+1))%13-6 for i in range(n)) for s in range(14)]
checks={
 'cut_commutes_with_successor_branchwise':all(branchmap(M,cut(x))==cut(M(x)) for x in vectors),
 'observation_transports_laurent_labels':all(branchmap(O,cut(x))==cutO(O(x)) for x in vectors),
 'observed_successor_after_cut':all(branchmap(O,cut(M(x)))==cutO(O(M(x))) for x in vectors),
 'distinct_branch_marks_retained':h1!=h2 and all(cut(x)[0]!=cut(x)[1] for x in vectors if any(x)),
}
out={'schema':'marici.nima.physical-cut-lo-graph-stability.v1','checks':checks,'theorem':'marked finite cut branches transport multiplier and endpoint graph coordinates by commuting Laurent multipliers and endpoint diagonal matrices','passed':all(checks.values()),'boundary':'transverse marked occurrence carrier with admitted Laurent graph multipliers'}
p=ROOT/'research/nima/results/physical-cut-lo-graph-stability.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
