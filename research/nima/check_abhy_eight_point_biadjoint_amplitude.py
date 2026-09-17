#!/usr/bin/env python3
"""Exact ABHY eight-point planar biadjoint amplitude replication."""
import itertools,json,sys
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as sp
N=8

def edge(a,b): return tuple(sorted((a,b)))
def boundary(vertices): return {edge(vertices[i],vertices[(i+1)%len(vertices)]) for i in range(len(vertices))}
@lru_cache(None)
def triangulations(vertices):
 vertices=tuple(vertices); n=len(vertices)
 if n==3:return (frozenset(),)
 out=set(); a,z=vertices[0],vertices[-1]
 for k in range(1,n-1):
  b=vertices[k]; left=vertices[:k+1]; right=vertices[k:]
  L=(frozenset(),) if len(left)<3 else triangulations(left)
  R=(frozenset(),) if len(right)<3 else triangulations(right)
  added=set()
  if k>1: added.add(edge(a,b))
  if k<n-2: added.add(edge(b,z))
  for l in L:
   for r in R: out.add(frozenset(set(l)|set(r)|added))
 return tuple(sorted(out,key=lambda s:sorted(s)))

def var(d): return sp.Symbol(f'X{d[0]}{d[1]}')
def amplitude(vertices):
 ts=triangulations(tuple(vertices))
 return sp.Add(*(sp.prod(1/var(d) for d in t) for t in ts)),ts
verts=tuple(range(1,N+1)); m8,tris=amplitude(verts)
diagonals=sorted(set().union(*tris)); terms=sp.Add.make_args(sp.expand(m8))
# Dihedral actions on planar channels.
def rotate(d): return edge(d[0]%N+1,d[1]%N+1)
def reflect(d): return edge(N+1-d[0],N+1-d[1])
rho={var(d):var(rotate(d)) for d in diagonals}; sigma={var(d):var(reflect(d)) for d in diagonals}
cyclic_ok=sp.simplify(m8.xreplace(rho)-m8)==0
reflection_ok=sp.simplify(m8.xreplace(sigma)-m8)==0
# Each of nine physical poles factors into amplitudes of the two polygons cut by it.
residues={}; residue_ok=True
for i,j in diagonals:
 side1=tuple(range(i,j+1)); side2=tuple(range(j,N+1))+tuple(range(1,i+1))
 a1,_=amplitude(side1); a2,_=amplitude(side2); expected=sp.expand(a1*a2)
 x=var((i,j)); got=sp.simplify(sp.limit(x*m8,x,0)); ok=sp.simplify(got-expected)==0
 residue_ok &= ok
 residues[str(x)]={'left_vertices':list(side1),'right_vertices':list(side2),'computed':str(got),'expected_product':str(expected),'passed':bool(ok)}
report={'schema':'marici.nima.abhy-eight-point-biadjoint-amplitude.v1','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','observable':'m_8[12345678|12345678]'},'convention':'overall coupling and sign stripped; X_ij are planar propagator variables','formula':str(m8),'term_count':len(terms),'physical_channels':[str(var(d)) for d in diagonals],'checks':{'onehundredthirtytwo_catalan_terms':len(terms)==132,'twenty_physical_channels':len(diagonals)==20,'cyclic_invariance':bool(cyclic_ok),'reflection_invariance':bool(reflection_ok),'all_twenty_factorization_residues':bool(residue_ok)},'residues':residues,'passed':bool(len(terms)==132 and len(diagonals)==20 and cyclic_ok and reflection_ok and residue_ok),'scope':'Exact symbolic replication of the tree-level eight-point planar biadjoint scalar benchmark.'}
out=ROOT/'research/nima/results/abhy-eight-point-biadjoint-amplitude.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':report['passed'],'term_count':len(terms),'channels':len(diagonals),'checks':report['checks']},indent=2));raise SystemExit(0 if report['passed'] else 1)
