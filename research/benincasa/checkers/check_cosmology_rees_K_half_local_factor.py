#!/usr/bin/env python3
"""Classify whether the local K divisor permits K^(1/2)=36v times a unit."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from math import comb
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
k,_=g['exact_fiber'](3,6,-3);loc={}
for (i,j),c in k.items():
 for h in range(j+1):loc[(i,h)]=loc.get((i,h),F(0))+c*comb(j,h)*3**(j-h)
loc={e:c for e,c in loc.items() if c};vmin=min(j for i,j in loc);bad={e:c for e,c in loc.items() if e[1]<2};divisible=not bad
unit=loc.get((0,2),F(0)) if divisible else None
H={(2,0):F(1),(0,1):F(-12),(0,2):F(-2)};sq={}
for e,a in H.items():
 for f,b in H.items():sq[(e[0]+f[0],e[1]+f[1])]=sq.get((e[0]+f[0],e[1]+f[1]),F(0))+9*a*b
sq={e:c for e,c in sq.items() if c};assert sq==loc
out={'schema':'marici.benincasa.cosmology-rees-K-half-local-factor.v1','K_local_terms':{str(e):str(c) for e,c in sorted(loc.items())},'minimum_v_exponent':vmin,'divisible_by_v_squared':divisible,'terms_obstructing_v_squared_factor':{str(e):str(c) for e,c in sorted(bad.items())},'exact_square_factorization':'K=9*(u^2-12v-2v^2)^2','square_root_choices':['3*(u^2-12v-2v^2)','-3*(u^2-12v-2v^2)'],'ramified_or_blowup_cover_required':False,'remaining_choice':'a sign branch for K^(1/2), not a ramified extension','exact_residual':'the provisional 36v unit-series model was false, but the complete polynomial is an exact square','passed':True};(R/'cosmology_rees_K_half_local_factor.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
