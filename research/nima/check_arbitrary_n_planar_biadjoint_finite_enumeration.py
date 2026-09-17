#!/usr/bin/env python3
"""Finite exhaustive instances of the arbitrary-n triangulation proof schema."""
import json,math
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def enum(v):
 if len(v)<=3:return (frozenset(),)
 out=set();a,z=v[0],v[-1]
 for k in range(1,len(v)-1):
  b=v[k];L=enum(v[:k+1]) if k+1>=3 else (frozenset(),);R=enum(v[k:]) if len(v)-k>=3 else (frozenset(),);add=set()
  if k>1:add.add(edge(a,b))
  if k<len(v)-2:add.add(edge(b,z))
  for l in L:
   for r in R:out.add(frozenset(set(l)|set(r)|add))
 return tuple(out)
rows=[];passed=True
for n in range(3,15):
 V=tuple(range(1,n+1));T=set(enum(V));want=math.comb(2*(n-2),n-2)//(n-1);channels=sorted(set().union(*T)) if n>3 else [];factor=True
 for d in channels:
  i,j=d;L=enum(tuple(range(i,j+1)));R=enum(tuple(range(j,n+1))+tuple(range(1,i+1)));actual={frozenset(set(t)-{d}) for t in T if d in t};expected={frozenset(set(a)|set(b)) for a in L for b in R};factor &= actual==expected
 ok=len(T)==want and all(len(t)==n-3 for t in T) and factor;passed &= ok;rows.append({'n':n,'triangulations':len(T),'catalan':want,'channels':len(channels),'all_channel_factorizations':factor,'passed':ok})
out={'schema':'marici.nima.arbitrary-n-planar-biadjoint-finite-enumeration.v1','proof_role':'For each supplied finite n, recursively enumerate the finite triangulation set and exhaust every channel. The accompanying mathematical induction proves the recursion for arbitrary n; this bounded run is regression evidence, not the logical source of universal quantification.','enumerated_range':[3,14],'results':rows,'passed':passed}
p=ROOT/'research/nima/results/arbitrary-n-planar-biadjoint-finite-enumeration.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':passed,'range':[3,14],'total_triangulations':sum(r['triangulations'] for r in rows),'largest':rows[-1]},indent=2));raise SystemExit(0 if passed else 1)
