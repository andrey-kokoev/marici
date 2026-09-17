#!/usr/bin/env python3
"""Test the naive four-chart model using four pairwise-compatible fixed ear channels."""
import json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def C(m):return math.comb(2*m,m)//(m+1) if m>=0 else 0
rows=[]
for n in range(10,101):
 full=C(n-2);singles=4*C(n-3);pairs=6*C(n-4);triples=4*C(n-5);quad=C(n-6);union=singles-pairs+triples-quad
 ratio=Fraction(union,full);uncovered=Fraction(full-union,full)
 rows.append({'n':n,'full':full,'union':union,'union_ratio':float(ratio),'uncovered_ratio':float(uncovered),'single_sum_excess':float(Fraction(singles-full,full))})
limit=Fraction(175,256);checks={'union_never_covers_full_module':all(x['union']<x['full'] for x in rows),'n100_near_175_over_256':abs(rows[-1]['union_ratio']-float(limit))<.01,'uncovered_does_not_vanish':rows[-1]['uncovered_ratio']>.30}
out={'schema':'marici.nima.four-fixed-ear-cech-cover.v1','range':[10,100],'formula':'|union_i E_i|=4 C_(n-3)-6 C_(n-4)+4 C_(n-5)-C_(n-6) for four pairwise-compatible ears.','asymptotic_union_ratio':'175/256','asymptotic_uncovered_ratio':'81/256','sample_rows':rows[:3]+rows[23:26]+rows[-3:],'checks':checks,'passed':all(checks.values()),'consequence':'The four chart projections cannot be four fixed ear/forced-channel submodules. Their Cech union misses asymptotically 81/256 of all triangulations.'}
p=ROOT/'research/nima/results/four-fixed-ear-cech-cover.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'formula':out['formula'],'limit':out['asymptotic_union_ratio'],'n33':rows[23],'n100':rows[-1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
