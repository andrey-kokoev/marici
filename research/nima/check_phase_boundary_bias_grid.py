#!/usr/bin/env python3
"""Resolve degree shift from boundary-growth bias on the 4x4 transition grid."""
import contextlib,io,json,runpy,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
env={'__file__':str(ROOT/'research/nima/check_nnmhv_long_numeric_grade_selection.py')};code=(ROOT/'research/nima/check_nnmhv_long_numeric_grade_selection.py').read_text().replace("raise SystemExit(0 if out['passed'] else 1)","")
with contextlib.redirect_stdout(io.StringIO()):exec(compile(code,env['__file__'],'exec'),env)
value,terminal=env['value'],env['terminal_shell'];poly=lambda d,j:j**d+(d+1)*j+1;rows=[]
for p in range(1,5):
 for q in range(1,5):
  lf=lambda j,p=p:poly(p,j);tf=lambda j,q=q:poly(q,j);n=64;v=value(n,lf,tf);inc=v-value(n-1,lf,tf);ins,_=terminal(n,lf,tf);omega=(inc-ins-ins)/inc;rho=math.atanh(max(-.999999999,min(.999999999,omega)));rows.append({'p':p,'q':q,'delta':q-p,'total_degree':p+q,'omega':omega,'rapidity':rho})
def fit(features):
 A=s.Matrix([[s.Float(f(r),30) for f in features] for r in rows]);y=s.Matrix([s.Float(r['rapidity'],30) for r in rows]);c=(A.T*A).inv()*A.T*y;res=[float(y[i]-(A*c)[i]) for i in range(len(rows))];return [float(v) for v in c],sum(v*v for v in res),max(map(abs,res))
c1,rss1,m1=fit((lambda r:1,lambda r:r['delta']));c2,rss2,m2=fit((lambda r:1,lambda r:r['delta'],lambda r:r['total_degree']));c3,rss3,m3=fit((lambda r:1,lambda r:r['delta'],lambda r:r['total_degree'],lambda r:r['p']*r['q']))
checks={'all_sixteen_transitions':len(rows)==16,'total_degree_reduces_residual':rss2<rss1,'interaction_degree_reduces_residual_further':rss3<rss2,'boundary_bias_is_not_constant':m1>0.1}
out={'schema':'marici.nima.phase-boundary-bias-grid.v1','n':64,'rows':rows,'models':{'delta_only':{'coefficients':c1,'rss':rss1,'max_residual':m1},'delta_plus_total':{'coefficients':c2,'rss':rss2,'max_residual':m2},'delta_total_product':{'coefficients':c3,'rss':rss3,'max_residual':m3}},'checks':checks,'passed':all(checks.values()),'scope':'Double-precision 4x4 polynomial-degree grid at cutoff 64.'};p=ROOT/'research/nima/results/phase-boundary-bias-grid.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
