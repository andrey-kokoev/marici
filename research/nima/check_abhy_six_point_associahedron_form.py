#!/usr/bin/env python3
"""Exact canonical-form pullback for the three-dimensional ABHY associahedron."""
import json,sys
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
x,y,z=s.symbols('x y z')
c13,c14,c15,c24,c25,c35=s.symbols('c13 c14 c15 c24 c25 c35',positive=True)
X={'X13':x,'X14':y,'X15':z,'X24':c13+y-x,'X25':c13+c14+z-x,
   'X26':c13+c14+c15-x,'X35':c14+c24+z-y,
   'X36':c14+c15+c24+c25-y,'X46':c15+c25+c35-z}
def edge(a,b):return tuple(sorted((a,b)))
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
tris=triangulations(tuple(range(1,7))); coords=(x,y,z); rows=[]; coeff=0; vertices=[]
for tri in tris:
 names=[f'X{a}{b}' for a,b in sorted(tri)]; vals=[X[n] for n in names]
 J=s.det(s.Matrix([[s.diff(v,q) for q in coords] for v in vals])); orient=J # all determinants are +/-1
 coeff += s.simplify(orient*J/s.prod(vals))
 sol=s.solve(vals,coords,dict=True)[0]
 other={k:s.simplify(v.subs(sol)) for k,v in X.items() if k not in names}
 vertices.append({'facets':names,'coordinates':{str(q):str(sol[q]) for q in coords},'other_facets':{k:str(v) for k,v in other.items()}})
 rows.append({'facets':names,'jacobian':str(J),'orientation':str(orient)})
amplitude=sum(1/s.prod(X[f'X{a}{b}'] for a,b in tri) for tri in tris)
loc={str(c):c for c in (c13,c14,c15,c24,c25,c35)}
positive=all(s.sympify(q,locals=loc).is_positive for row in vertices for q in row['other_facets'].values())
checks={'nine_facets':len(X)==9,'fourteen_vertices':len(vertices)==14,'three_facets_per_vertex':all(len(t)==3 for t in tris),'unit_jacobians':all(abs(int(r['jacobian']))==1 for r in rows),'all_other_facets_positive_at_vertices':positive,'canonical_form_equals_amplitude':s.simplify(coeff-amplitude)==0}
report={'schema':'marici.nima.abhy-six-point-associahedron-form.v1','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','object':'six-point kinematic associahedron canonical form'},'embedding':{k:str(v) for k,v in X.items()},'positive_constants':[str(c) for c in loc.values()],'oriented_dlog_vertices':rows,'vertices':vertices,'checks':checks,'passed':all(checks.values()),'scope':'Exact symbolic six-point associahedron pullback in an ABHY affine realization.'}
out=ROOT/'research/nima/results/abhy-six-point-associahedron-form.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks},indent=2));raise SystemExit(0 if report['passed'] else 1)
