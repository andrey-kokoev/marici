#!/usr/bin/env python3
"""Audit divisor geometry governing a pole-level residue functional."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
_,q=g['exact_fiber'](3,6,-3);q1,q2,q3,q23,q31=q
def add(*ps):
 o={}
 for p in ps:
  for k,v in p.items():o[k]=o.get(k,F(0))+v
 return {k:v for k,v in o.items() if v}
assert q1==q23 and add(q1,q2,{k:-v for k,v in q3.items()})=={}
def ev(p,x,y):return sum(c*x**i*y**j for (i,j),c in p.items())
triple=[ev(p,0,3) for p in (q1,q2,q3)];assert triple==[0,0,0] and ev(q31,0,3)==-6
out={'schema':'marici.benincasa.cosmology-rees-cech-localization-geometry.v1','source_point':[3,6,-3],'divisor_identities':['q1=q23=Y-3','q2=X','q3=q1+q2=X+Y-3','q31=X-6'],'intersection_0_3':{'vanishing':['q1','q2','q3','q23'],'nonvanishing':{'q31':-6}},'normal_crossing':False,'exact_residual':'the pole list contains a duplicate divisor and a dependent triple intersection in two variables','consequence':'a functional cannot be specified as an unqualified simple common residue; it needs an ordered iterated residue, a blowup/Čech representative, or an equivalent source-derived cycle, and compatibility among those choices','canonical_functional_constructed':False,'acceptance_test':'choose a typed Čech representative or resolution, compute the induced functional on every pole-level shift, and prove independence from presentation before testing tau','passed':True};(R/'cosmology_rees_cech_localization_geometry.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
