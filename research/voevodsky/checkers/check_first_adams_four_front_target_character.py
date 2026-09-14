#!/usr/bin/env python3
"""Exact Laurent-polynomial audit of the first-Adams four-front target."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/first_adams_four_front_target_character.v1.json';OUT=ROOT/'research/voevodsky/results/first_adams_four_front_target_character.json';D=json.loads(FIX.read_text());poly={e:Q(c) for e,c in zip(D['ordered_exponents'],D['coefficients'])}
def add(a,b):
 o=dict(a)
 for e,c in b.items():o[e]=o.get(e,Q(0))+c
 return {e:c for e,c in o.items() if c}
def neg(a):return {e:-c for e,c in a.items()}
def reciprocal(a):return {-e:c for e,c in a.items()}
def value_one(a):return sum(a.values())
# 2i sin(theta)=z-z^-1 and 2i sin(2theta)=z^2-z^-2.
sine_target=add({1:Q(1),-1:Q(-1)},neg({2:Q(1),-2:Q(-1)}))
# Divide by z-1 using coefficient recurrence, represented with ordinary shifted polynomial z^2*P.
shifted={e+2:c for e,c in poly.items()};quot={0:Q(-1),3:Q(-1)} # (z-1)(-1-z^3)
def mul(a,b):
 o={}
 for e,c in a.items():
  for f,d in b.items():o[e+f]=o.get(e+f,Q(0))+c*d
 return {e:c for e,c in o.items() if c}
checks={'four_coefficients_retained':poly=={-2:Q(1),-1:Q(-1),1:Q(1),2:Q(-1)},'equals_odd_sine_character':poly==sine_target,'reciprocal_odd':reciprocal(poly)==neg(poly),'wall_cancellation_at_z_one':value_one(poly)==0,'wall_factor_exact':mul({1:Q(1),0:Q(-1)},quot)==shifted,'outer_fronts_present':poly[-2]!=0 and poly[2]!=0,'three_front_truncation_rejected':len(poly)==4,'source_identity_not_promoted':D['disposition']['source_constructor_identity'].startswith('not yet evaluated')}
out={'schema':'marici.voevodsky.first-adams-four-front-target-character-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'laurent_coefficients':{str(e):str(c) for e,c in sorted(poly.items())},'reciprocal_coefficients':{str(e):str(c) for e,c in sorted(reciprocal(poly).items())},'value_at_wall_z_1':str(value_one(poly)),'shifted_wall_quotient_coefficients':{str(e):str(c) for e,c in sorted(quot.items())}},'disposition':'The required boundary target is the unique retained four-front Laurent character with the frozen coefficients. It is reciprocal-odd and wall-killed. The source constructor must still be shown to land exactly in this span with no orthogonal remainder.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_first_adams_four_front_target_character.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/D['source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
