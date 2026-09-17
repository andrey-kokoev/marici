#!/usr/bin/env python3
"""Exact projectivity of the eleven-point planar scattering 4-form."""
import json,sys
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
N=11;coords=s.symbols('x3:11');C={(i,j):s.Symbol(f'c{i}{j}') for i in range(1,N-1) for j in range(i+2,N)}
def edge(a,b):return tuple(sorted((a,b)))
X={edge(i,i+1):s.Integer(0) for i in range(1,N)};X[(1,N)]=s.Integer(0)
for j,q in zip(range(3,N),coords):X[(1,j)]=q
for i in range(1,N-2):
 for j in range(i+2,N):X[(i+1,j+1)]=s.expand(C[(i,j)]+X[(i,j+1)]+X[(i+1,j)]-X[(i,j)])
@lru_cache(None)
def tris(v):
 if len(v)==3:return (frozenset(),)
 out=set();a,q=v[0],v[-1]
 for k in range(1,len(v)-1):
  b=v[k];L=(frozenset(),) if k+1<3 else tris(v[:k+1]);R=(frozenset(),) if len(v)-k<3 else tris(v[k:]);add=set()
  if k>1:add.add(edge(a,b))
  if k<len(v)-2:add.add(edge(b,q))
  for l in L:
   for r in R:out.add(frozenset(set(l)|set(r)|add))
 return tuple(out)
def wedge(labels):
 if len(set(labels))<len(labels):return None,0
 inv=sum(labels[i]>labels[j] for i in range(len(labels)) for j in range(i+1,len(labels)))
 return tuple(sorted(labels)),(-1)**inv
terms=[]
for t in tris(tuple(range(1,N+1))):
 ds=sorted(t);names=tuple(f'X{a}{b}' for a,b in ds);J=int(s.det(s.Matrix([[s.diff(X[d],q) for q in coords] for d in ds])));terms.append((J,names))
def build(rescaled):
 out=defaultdict(int)
 for orient,names in terms:
  choices=[names]
  if rescaled:choices += [names[:i]+('L',)+names[i+1:] for i in range(N-3)]
  for labels in choices:
   key,sign=wedge(labels)
   if sign:out[key]+=orient*sign
 return {k:v for k,v in out.items() if v}
original=build(False);scaled=build(True);variation={k:scaled.get(k,0)-original.get(k,0) for k in set(original)|set(scaled)};variation={k:v for k,v in variation.items() if v}
checks={'fourthousandeighthundredsixtytwo_cubic_graph_terms':len(terms)==4862,'fortyfour_channels':len([d for d,v in X.items() if v!=0])==44,'unit_graph_orientations':all(abs(o)==1 for o,_ in terms),'nonzero_scattering_form':len(original)==4862,'local_rescaling_variation_zero':not variation}
report={'schema':'marici.nima.abhy-eleven-point-scattering-form-projectivity.v1','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','result':'projectivity of the eleven-point planar scattering form'},'term_count':len(terms),'oriented_terms':[{'sign':o,'channels':list(q)} for o,q in terms],'transformation':'dlog X_a -> dlog X_a + dlog Lambda','variation_coefficients':{str(k):v for k,v in variation.items()},'checks':checks,'passed':all(checks.values()),'scope':'Exact exterior-algebra projectivity check for the eleven-point planar scattering 4-form.'}
out=ROOT/'research/nima/results/abhy-eleven-point-scattering-form-projectivity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'variation_terms':len(variation)},indent=2));raise SystemExit(0 if report['passed'] else 1)
