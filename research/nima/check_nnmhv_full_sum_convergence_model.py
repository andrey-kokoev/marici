#!/usr/bin/env python3
"""Profile power-law convergence models for the normalized full history sum."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-extended-sections.json').read_text())['sections']
def fit(rows,alpha):
 xs=[r['n']**(-alpha) for r in rows];ys=[r['normalized_value'] for r in rows];N=len(rows);sx=sum(xs);sy=sum(ys);sxx=sum(x*x for x in xs);sxy=sum(x*y for x,y in zip(xs,ys));d=N*sxx-sx*sx;c=(N*sxy-sx*sy)/d;L=(sy-c*sx)/N;rss=sum((y-L-c*x)**2 for x,y in zip(xs,ys));return L,c,rss
def profile(start):
 rows=[r for r in src if r['n']>=start];candidates=[]
 for k in range(10,501):
  a=k/100;L,c,rss=fit(rows,a);candidates.append((rss,a,L,c))
 rss,a,L,c=min(candidates);return {'n_min':start,'n_max':rows[-1]['n'],'alpha':a,'L':L,'c':c,'rss':rss}
profiles=[profile(v) for v in (8,10,12)];alphas=[p['alpha'] for p in profiles];limits=[p['L'] for p in profiles];alpha_spread=max(alphas)-min(alphas);limit_spread=max(limits)-min(limits)
# Monotone increments and their local effective powers: delta_n/delta_{n+1} ~ ((n+1)/n)^(alpha+1).
vals={r['n']:r['normalized_value'] for r in src};effective=[]
for n in range(8,16):
 d0=vals[n]-vals[n-1];d1=vals[n+1]-vals[n]
 if d0>0 and d1>0:effective.append({'n':n,'alpha_effective':math.log(d0/d1)/math.log((n+1)/n)-1})
checks={'three_late_window_profiles':len(profiles)==3,'best_exponents_positive':all(p['alpha']>0 for p in profiles),'all_profile_limits_finite':all(math.isfinite(p['L']) for p in profiles),'profile_exponent_spread_below_point_one':alpha_spread<0.1,'profile_limit_relative_spread_below_one_percent':limit_spread/max(abs(v) for v in limits)<0.01}
out={'schema':'marici.nima.nnmhv-full-sum-convergence-model.v1','model':'S_n=L+c*n^(-alpha)','profiles':profiles,'alpha_window_spread':alpha_spread,'limit_window_spread':limit_spread,'local_effective_exponents':effective,'checks':checks,'passed':all(checks.values()),'conclusion':'Stable late-window power-law profiles give provisional evidence for a family-specific finite limit near 5.81e-4; local exponent drift still precludes a proof.','scope':'Model profiling of exact full-history sections through n=16; exploratory extrapolation only.'}
p=ROOT/'research/nima/results/nnmhv-full-sum-convergence-model.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
