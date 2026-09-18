#!/usr/bin/env python3
"""Test whether the 1/n grade is absent in the full-history asymptotics."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
cross=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-cross-family-exponents.json').read_text());q=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-extended-sections.json').read_text());families={'quadratic_cubic':[{'n':r['n'],'value':r['normalized_value']} for r in q['sections']]};families.update({k:v['sections'] for k,v in cross['extended_families'].items()})
def fit(rows,start):
 rr=[r for r in rows if r['n']>=start];A=s.Matrix([[1,s.Rational(1,r['n']),s.Rational(1,r['n']**2),s.Rational(1,r['n']**3)] for r in rr]);y=s.Matrix([s.Float(r['value'],40) for r in rr]);c=(A.T*A).inv()*A.T*y;res=[float(y[i]-(A*c)[i]) for i in range(len(rr))];return {'n_min':start,'L':float(c[0]),'c1':float(c[1]),'c2':float(c[2]),'c3':float(c[3]),'rss':sum(v*v for v in res),'grade1_fraction_at_n16':abs(float(c[1])/16)/abs(float(c[0]))}
outf={name:{'profiles':[fit(rows,k) for k in (8,9,10)]} for name,rows in families.items()}
# A genuine exact selection rule would return c1=0 stably as the window moves.
late=[d['profiles'][-1] for d in outf.values()];checks={'fits_all_families':len(outf)==3,'grade_one_not_numerically_zero':all(abs(p['c1'])>1e-8 for p in late),'grade_one_coefficients_window_dependent':all(max(p['c1'] for p in d['profiles'])-min(p['c1'] for p in d['profiles'])>1e-7 for d in outf.values())}
out={'schema':'marici.nima.nnmhv-grade-one-selection.v1','model':'S_n=c0+c1/n+c2/n^2+c3/n^3','families':outf,'checks':checks,'passed':all(checks.values()),'conclusion':'Finite sections do not independently establish c1=0: unconstrained fits assign a nonzero, window-dependent c1 that can absorb omitted higher grades. The zero-grade-one claim requires an analytic selection rule or longer data.'}
p=ROOT/'research/nima/results/nnmhv-grade-one-selection.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
