#!/usr/bin/env python3
"""Test cross-family behavior after little-group normalization."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-kinematic-dependence.json').read_text())
# Same lambda families used by the source experiment.
lf={'quadratic_cubic':lambda j:j*j+j+1,'quadratic_quartic':lambda j:j*j+2*j+2,'cubic_quadratic':lambda j:j**3+j+1}
outfamilies={}
for name,data in src['families'].items():
 bracket=lf[name](3)-lf[name](2) # det((1,f2),(1,f3))
 rows=[{'n':r['n'],'normalized_value':r['value']/bracket**4} for r in data['sections']]
 A=s.Matrix([[1,s.Rational(1,r['n']),s.Rational(1,r['n']**2)] for r in rows[-4:]]);y=s.Matrix([s.Float(r['normalized_value'],30) for r in rows[-4:]]);c=(A.T*A).inv()*A.T*y
 outfamilies[name]={'angle_23':bracket,'sections':rows,'fit_L_plus_a_over_n_plus_b_over_n2':{'L':float(c[0]),'a':float(c[1]),'b':float(c[2])}}
limits=[d['fit_L_plus_a_over_n_plus_b_over_n2']['L'] for d in outfamilies.values()];spread=max(limits)-min(limits);relative_spread=spread/max(abs(v) for v in limits)
checks={'uses_validated_little_group_normalization':all(d['angle_23']!=0 for d in outfamilies.values()),'three_coherent_families_compared':len(outfamilies)==3,'normalized_fits_remain_distinct':relative_spread>0.5,'all_normalized_sections_nonzero':all(r['normalized_value']!=0 for d in outfamilies.values() for r in d['sections'])}
out={'schema':'marici.nima.nnmhv-normalized-full-sum-dependence.v1','observable':'C_23/<23>^4','families':outfamilies,'fitted_limit_absolute_spread':spread,'fitted_limit_relative_spread':relative_spread,'checks':checks,'passed':all(checks.values()),'conclusion':'Little-group normalization removes frame rescaling but not dependence on the coherent kinematic family.','scope':'Derived from exact full-history sections n=6..11; exploratory fits do not prove convergence.'}
p=ROOT/'research/nima/results/nnmhv-normalized-full-sum-dependence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
