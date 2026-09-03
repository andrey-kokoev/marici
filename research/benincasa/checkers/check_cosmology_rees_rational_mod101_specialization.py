#!/usr/bin/env python3
"""Verify rational residual basis specializes to the modular quotient."""
import contextlib,io,json,runpy,sys
from fractions import Fraction
from pathlib import Path
P=101;HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_residual_nullspace_basis.py');old=sys.argv;sys.argv=[str(src),'26']
try:
 with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(src))
finally:sys.argv=old
raw=json.loads((HERE.parents[1]/'results/cosmology_rees_rational_residual_nullspace.json').read_text());idx={tuple(x):i for i,x in enumerate(g['labels'])};den=[];rat=[]
for rep in raw['representatives']:
 v={}
 for t in rep:
  q=Fraction(t['coefficient']);den.append(q.denominator);v[idx[tuple(t['input'])]]=q.numerator*pow(q.denominator,-1,P)%P
 rat.append(v)
def added(seed,vs):
 B={};n=sum(g['ins'](B,dict(v)) for v in seed);return sum(g['ins'](B,dict(v)) for v in vs),B
ra,B=added(g['known'],rat);mod_after=sum(g['ins'](B,dict(v)) for v in g['residual']);ma,C=added(g['known'],g['residual']);rat_after=sum(g['ins'](C,dict(v)) for v in rat)
out={'schema':'marici.benincasa.cosmology-rees-rational-mod101-specialization.v1','prime':P,'all_denominators_invertible':all(d%P for d in den),'rational_specialization_added_rank':ra,'modular_basis_added_after_rational':mod_after,'modular_basis_added_rank':ma,'rational_basis_added_after_modular':rat_after,'same_quotient_span':ra==ma==10 and mod_after==rat_after==0};R=HERE.parents[1]/'results';(R/'cosmology_rees_rational_mod101_specialization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
