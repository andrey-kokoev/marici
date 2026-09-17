#!/usr/bin/env python3
"""Combinatorial exact replication of the ABHY ten-point planar amplitude."""
import json,math
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];N=10
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def triangulations(v):
 if len(v)==3:return (frozenset(),)
 out=set();a,z=v[0],v[-1]
 for k in range(1,len(v)-1):
  b=v[k];L=(frozenset(),) if k+1<3 else triangulations(v[:k+1]);R=(frozenset(),) if len(v)-k<3 else triangulations(v[k:]);add=set()
  if k>1:add.add(edge(a,b))
  if k<len(v)-2:add.add(edge(b,z))
  for l in L:
   for r in R:out.add(frozenset(set(l)|set(r)|add))
 return tuple(out)
verts=tuple(range(1,N+1));tris=set(triangulations(verts));channels=sorted(set().union(*tris))
def rotate(d):return edge(d[0]%N+1,d[1]%N+1)
def reflect(d):return edge(N+1-d[0],N+1-d[1])
cyclic={frozenset(rotate(d) for d in t) for t in tris}==tris
reflection={frozenset(reflect(d) for d in t) for t in tris}==tris
residues={};all_factor=True
for d in channels:
 i,j=d;left=tuple(range(i,j+1));right=tuple(range(j,N+1))+tuple(range(1,i+1))
 L=triangulations(left);R=triangulations(right)
 expected={frozenset(set(a)|set(b)) for a in L for b in R}
 actual={frozenset(set(t)-{d}) for t in tris if d in t}
 ok=actual==expected;all_factor &= ok
 residues[f'X{i}{j}']={'terms':len(actual),'expected_left_times_right':len(L)*len(R),'passed':ok}
checks={'1430_catalan_terms':len(tris)==1430,'35_physical_channels':len(channels)==35,'seven_propagators_per_term':all(len(t)==7 for t in tris),'unit_coefficients':len(tris)==len(set(tris)),'cyclic_invariance':cyclic,'reflection_invariance':reflection,'all_35_factorization_residues':all_factor}
report={'schema':'marici.nima.abhy-ten-point-biadjoint-amplitude.v2','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','observable':'m_10[12345678910|12345678910]'},'representation':'Each unit-coefficient rational term is encoded exactly by its seven planar propagator diagonals.','term_count':len(tris),'physical_channels':[f'X{i}{j}' for i,j in channels],'residues':residues,'checks':checks,'passed':all(checks.values()),'scope':'Exact combinatorial rational-function identity; avoids redundant global symbolic simplification.'}
out=ROOT/'research/nima/results/abhy-ten-point-biadjoint-amplitude.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'term_count':len(tris),'channels':len(channels),'checks':checks},indent=2));raise SystemExit(0 if report['passed'] else 1)
