#!/usr/bin/env python3
"""Long-window fixed-grade asymptotics of the normalized full history sum."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-long-numeric-grade-selection.json').read_text());outf={}
for name,data in src['families'].items():
 rows=data['long_sections'];A=s.Matrix([[1,s.Rational(1,r['n']**2),s.Rational(1,r['n']**3)] for r in rows]);y=s.Matrix([s.Float(r['value'],40) for r in rows]);c=(A.T*A).inv()*A.T*y;L,c2,c3=map(float,c);scaled=[{'n':r['n'],'n2_times_L_minus_S':r['n']**2*(L-r['value'])} for r in rows];res=[float(y[i]-(A*c)[i]) for i in range(len(rows))];outf[name]={'L':L,'c2':c2,'c3':c3,'scaled_tail':scaled,'max_abs_residual':max(map(abs,res)),'late_scaled_over_minus_c2':scaled[-1]['n2_times_L_minus_S']/(-c2)}
checks={'three_family_limits':len(outf)==3,'all_residuals_below_1e_minus_8':all(v['max_abs_residual']<1e-8 for v in outf.values()),'scaled_tails_approach_minus_c2':all(abs(v['late_scaled_over_minus_c2']-1)<0.1 for v in outf.values()),'all_limits_positive':all(v['L']>0 for v in outf.values())}
out={'schema':'marici.nima.nnmhv-long-exponent-two-limit.v1','model':'S_n=L+c2/n^2+c3/n^3','families':outf,'checks':checks,'passed':all(checks.values()),'meaning':'n^2(L-S_n) tends to -c2, while shell flux has leading coefficient -2*c2 at degree n^-3.'};p=ROOT/'research/nima/results/nnmhv-long-exponent-two-limit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
