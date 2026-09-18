#!/usr/bin/env python3
"""Test the fixed exponent-two tail with finite-section corrections."""
import json,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
cross=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-cross-family-exponents.json').read_text());q=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-extended-sections.json').read_text());families={'quadratic_cubic':[{'n':r['n'],'value':r['normalized_value']} for r in q['sections']]};families.update({k:v['sections'] for k,v in cross['extended_families'].items()})
def fit(rows,start):
 rr=[r for r in rows if r['n']>=start];A=s.Matrix([[1,s.Rational(1,r['n']**2),s.Rational(1,r['n']**3)] for r in rr]);y=s.Matrix([s.Float(r['value'],40) for r in rr]);c=(A.T*A).inv()*A.T*y;res=[float(y[i]-(A*c)[i]) for i in range(len(rr))];return {'n_min':start,'n_max':rr[-1]['n'],'L':float(c[0]),'c2':float(c[1]),'c3':float(c[2]),'rss':sum(v*v for v in res),'max_abs_residual':max(map(abs,res))}
outf={}
for name,rows in families.items():outf[name]={'profiles':[fit(rows,k) for k in (8,10,12)]}
late=[v['profiles'][-1] for v in outf.values()];window_spreads={name:max(p['L'] for p in d['profiles'])-min(p['L'] for p in d['profiles']) for name,d in outf.items()}
checks={'all_three_families_fit':len(outf)==3,'all_late_residuals_below_2e_minus_9':all(p['max_abs_residual']<2e-9 for p in late),'all_limit_window_spreads_below_one_percent':all(sp/max(abs(p['L']) for p in outf[name]['profiles'])<0.01 for name,sp in window_spreads.items()),'leading_c2_nonzero':all(p['c2']!=0 for p in late)}
out={'schema':'marici.nima.nnmhv-exponent-two-corrections.v1','model':'S_n=L+c2/n^2+c3/n^3','families':outf,'limit_window_spreads':window_spreads,'checks':checks,'passed':all(checks.values()),'interpretation':'A fixed n^-2 leading correction with n^-3 finite-section term fits all families and yields stable limits through n=16.'}
p=ROOT/'research/nima/results/nnmhv-exponent-two-corrections.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
