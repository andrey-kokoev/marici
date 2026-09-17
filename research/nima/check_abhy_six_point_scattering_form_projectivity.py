#!/usr/bin/env python3
"""Exact projectivity of the six-point planar scattering 3-form."""
import json,sys
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
x,y,z=s.symbols('x y z');c13,c14,c15,c24,c25,c35=s.symbols('c13 c14 c15 c24 c25 c35')
X={'X13':x,'X14':y,'X15':z,'X24':c13+y-x,'X25':c13+c14+z-x,'X26':c13+c14+c15-x,'X35':c14+c24+z-y,'X36':c14+c15+c24+c25-y,'X46':c15+c25+c35-z}
def edge(a,b):return tuple(sorted((a,b)))
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
for t in tris(tuple(range(1,7))):
 names=tuple(f'X{a}{b}' for a,b in sorted(t));J=int(s.det(s.Matrix([[s.diff(X[n],q) for q in (x,y,z)] for n in names])))
 terms.append((J,names))
def build(rescaled):
 out=defaultdict(int)
 for orient,names in terms:
  choices=[names]
  if rescaled:
   choices += [names[:i]+('L',)+names[i+1:] for i in range(3)]
  for labels in choices:
   key,sign=wedge(labels)
   if sign:out[key]+=orient*sign
 return {k:v for k,v in out.items() if v}
original=build(False);scaled=build(True);variation={k:scaled.get(k,0)-original.get(k,0) for k in set(original)|set(scaled)};variation={k:v for k,v in variation.items() if v}
checks={'fourteen_cubic_graph_terms':len(terms)==14,'nine_channels':len(X)==9,'unit_graph_orientations':all(abs(q[0])==1 for q in terms),'nonzero_scattering_form':len(original)==14,'local_rescaling_variation_zero':not variation}
report={'schema':'marici.nima.abhy-six-point-scattering-form-projectivity.v1','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','result':'projectivity of the six-point planar scattering form'},'term_count':len(terms),'channel_count':len(X),'oriented_terms':[{'sign':o,'channels':list(q)} for o,q in terms],'transformation':'dlog X_a -> dlog X_a + dlog Lambda','variation_coefficients':{str(k):v for k,v in variation.items()},'checks':checks,'passed':all(checks.values()),'scope':'Exact exterior-algebra projectivity check for the six-point planar scattering 3-form.'}
out=ROOT/'research/nima/results/abhy-six-point-scattering-form-projectivity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'variation_terms':len(variation)},indent=2));raise SystemExit(0 if report['passed'] else 1)
