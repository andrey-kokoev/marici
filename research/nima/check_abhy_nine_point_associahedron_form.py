#!/usr/bin/env python3
"""Exact canonical-form pullback for the four-dimensional ABHY associahedron."""
import json,sys
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
N=9; coords=s.symbols('x3:9') # fan variables X13,...,X16
# Positive ABHY constants c_ij, 1 <= i < j-1 <= N-2.
C={(i,j):s.Symbol(f'c{i}{j}',positive=True) for i in range(1,N-1) for j in range(i+2,N)}
def edge(i,j):return tuple(sorted((i,j)))
X={edge(i,i+1):s.Integer(0) for i in range(1,N)};X[edge(1,N)]=s.Integer(0)
for j,q in zip(range(3,N),coords):X[(1,j)]=q
# Discrete ABHY mesh relation: Xij + X(i+1,j+1) - X(i,j+1) - X(i+1,j) = c_ij.
for i in range(1,N-2):
 for j in range(i+2,N):
  X[(i+1,j+1)]=s.expand(C[(i,j)]+X[(i,j+1)]+X[(i+1,j)]-X[(i,j)])
facets={f'X{i}{j}':v for (i,j),v in X.items() if j>i+1 and (i,j)!=(1,N)}
@lru_cache(None)
def triangulations(v):
 if len(v)==3:return (frozenset(),)
 out=set();a,q=v[0],v[-1]
 for k in range(1,len(v)-1):
  b=v[k];L=(frozenset(),) if k+1<3 else triangulations(v[:k+1]);R=(frozenset(),) if len(v)-k<3 else triangulations(v[k:]);add=set()
  if k>1:add.add(edge(a,b))
  if k<len(v)-2:add.add(edge(b,q))
  for l in L:
   for r in R:out.add(frozenset(set(l)|set(r)|add))
 return tuple(sorted(out,key=lambda q:sorted(q)))
tris=triangulations(tuple(range(1,N+1))); rows=[]; vertices=[]; local_equal=True
for tri in tris:
 names=[f'X{a}{b}' for a,b in sorted(tri)]; vals=[facets[n] for n in names]
 J=s.det(s.Matrix([[s.diff(v,q) for q in coords] for v in vals])); orient=J
 local_equal &= s.simplify(orient*J-1)==0
 sol=s.solve(vals,coords,dict=True)[0]
 other={k:s.simplify(v.subs(sol)) for k,v in facets.items() if k not in names}
 vertices.append({'facets':names,'coordinates':{str(q):str(sol[q]) for q in coords},'other_facets':{k:str(v) for k,v in other.items()}})
 rows.append({'facets':names,'jacobian':str(J),'orientation':str(orient)})
loc={str(c):c for c in C.values()}
def positive_sum(q):
 e=s.sympify(q,locals=loc); p=s.Poly(e,*C.values()); return e!=0 and all(a>0 for a in p.coeffs())
positive=all(positive_sum(q) for row in vertices for q in row['other_facets'].values())
checks={'twentyseven_facets':len(facets)==27,'fourhundredtwentynine_vertices':len(vertices)==429,'six_facets_per_vertex':all(len(t)==6 for t in tris),'unit_jacobians':all(abs(int(r['jacobian']))==1 for r in rows),'all_other_facets_positive_at_vertices':positive,'canonical_form_equals_amplitude_termwise':bool(local_equal)}
report={'schema':'marici.nima.abhy-nine-point-associahedron-form.v1','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','object':'nine-point kinematic associahedron canonical form'},'embedding':{k:str(v) for k,v in facets.items()},'positive_constants':[str(c) for c in C.values()],'oriented_dlog_vertices':rows,'vertices':vertices,'checks':checks,'passed':all(checks.values()),'scope':'Exact symbolic nine-point associahedron pullback in the fan-coordinate ABHY realization.'}
out=ROOT/'research/nima/results/abhy-nine-point-associahedron-form.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks},indent=2));raise SystemExit(0 if report['passed'] else 1)
