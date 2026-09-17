#!/usr/bin/env python3
"""Exact projectivity check for the five-point planar scattering form."""
import json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
channels=('X13','X14','X24','X25','X35')
# Orientations inherited from the ABHY associahedron pullback in (X13,X14).
terms=[(1,'X13','X14'),(-1,'X13','X35'),(1,'X14','X24'),(1,'X24','X25'),(1,'X25','X35')]
def wedge(a,b):
 if a==b:return None,0
 return ((a,b),1) if a<b else ((b,a),-1)
def form(expanded):
 out=defaultdict(int)
 for sign,a,b in terms:
  choices=((a,b),('L',b),(a,'L'),('L','L')) if expanded else ((a,b),)
  for u,v in choices:
   key,w=wedge(u,v)
   if w:out[key]+=sign*w
 return {k:v for k,v in out.items() if v}
original=form(False);rescaled=form(True);variation={k:rescaled.get(k,0)-original.get(k,0) for k in set(original)|set(rescaled)};variation={k:v for k,v in variation.items() if v}
# Adjacent triangulations differ by one flip and carry the relative signs needed
# for cancellation of all dlog Lambda terms.
checks={'five_cubic_graph_terms':len(terms)==5,'nonzero_scattering_form':len(original)==5,'local_rescaling_variation_zero':not variation,'each_channel_lambda_coefficient_cancels':all(sum(sign*((1 if a==x else 0)-(1 if b==x else 0)) for sign,a,b in terms)==0 for x in channels)}
report={'schema':'marici.nima.abhy-five-point-scattering-form-projectivity.v1','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','result':'projectivity of the planar scattering form'},'form_terms':[{'sign':q[0],'wedge':[f'dlog {q[1]}',f'dlog {q[2]}']} for q in terms],'transformation':'dlog X_a -> dlog X_a + dlog Lambda','original_coefficients':{str(k):v for k,v in original.items()},'variation_coefficients':{str(k):v for k,v in variation.items()},'checks':checks,'passed':all(checks.values()),'scope':'Exact exterior-algebra projectivity check for the five-point planar scattering form.'}
out=ROOT/'research/nima/results/abhy-five-point-scattering-form-projectivity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'variation':report['variation_coefficients']},indent=2));raise SystemExit(0 if report['passed'] else 1)
