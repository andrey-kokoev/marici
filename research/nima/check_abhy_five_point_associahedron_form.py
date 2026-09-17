#!/usr/bin/env python3
"""Exact pullback of the ABHY five-point associahedron canonical form."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
x,y=s.symbols('x y')
c13,c14,c24=s.symbols('c13 c14 c24', positive=True)
X={
 'X13':x,
 'X14':y,
 'X24':c13+y-x,
 'X25':c13+c14-x,
 'X35':c14+c24-y,
}
triangles=[('X13','X14'),('X13','X35'),('X14','X24'),('X24','X25'),('X25','X35')]
# Orient each vertex dlog wedge so its pullback has positive dx wedge dy.
forms=[]
for a,b in triangles:
 J=s.det(s.Matrix([[s.diff(X[a],x),s.diff(X[a],y)],[s.diff(X[b],x),s.diff(X[b],y)]]))
 sign=1 if J==1 else -1
 forms.append({'channels':[a,b],'orientation':sign,'jacobian':str(J),'coefficient':sign*J/(X[a]*X[b])})
pullback=s.factor(sum(f['coefficient'] for f in forms))
amplitude=s.factor(sum(1/(X[a]*X[b]) for a,b in triangles))
# Vertices are intersections of adjacent facets in cyclic order; positivity of
# constants makes all other facet values nonnegative there.
vertices=[]; facet_order=['X13','X14','X24','X25','X35']
# Actual compatible pairs, i.e. the five vertices of the pentagon.
for a,b in triangles:
 sol=s.solve([X[a],X[b]],[x,y],dict=True)[0]
 others={k:s.simplify(v.subs(sol)) for k,v in X.items() if k not in (a,b)}
 vertices.append({'facets':[a,b],'x':str(sol[x]),'y':str(sol[y]),'other_facets':{k:str(v) for k,v in others.items()}})
checks={
 'five_facets':len(X)==5,
 'five_vertices':len(vertices)==5,
 'abhy_linear_relations':s.simplify(X['X24']-(c13+y-x))==0 and s.simplify(X['X25']-(c13+c14-x))==0 and s.simplify(X['X35']-(c14+c24-y))==0,
 'unit_oriented_jacobians':all(s.simplify(f['orientation']*s.sympify(f['jacobian']))==1 for f in forms),
 'all_other_facets_positive_at_vertices':all(s.sympify(q,locals={'c13':c13,'c14':c14,'c24':c24}).is_positive for row in vertices for q in row['other_facets'].values()),
 'canonical_form_equals_amplitude':s.simplify(pullback-amplitude)==0,
}
report={'schema':'marici.nima.abhy-five-point-associahedron-form.v1','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','object':'five-point kinematic associahedron canonical form'},'embedding':{k:str(v) for k,v in X.items()},'positive_constants':['c13','c14','c24'],'oriented_dlog_vertices':[{k:v for k,v in f.items() if k!='coefficient'} for f in forms],'vertices':vertices,'pullback_coefficient':str(pullback),'amplitude_coefficient':str(amplitude),'checks':checks,'passed':all(checks.values()),'scope':'Exact symbolic five-point associahedron pullback in one ABHY affine realization.'}
out=ROOT/'research/nima/results/abhy-five-point-associahedron-form.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'pullback':str(pullback)},indent=2));raise SystemExit(0 if report['passed'] else 1)
