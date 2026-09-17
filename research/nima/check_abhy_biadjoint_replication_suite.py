#!/usr/bin/env python3
"""Aggregate integrity check for locally replicated ABHY amplitudes."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
expected={5:(5,5),6:(14,9),7:(42,14),8:(132,20),9:(429,27),10:(1430,35),11:(4862,44),12:(16796,54),13:(58786,65),14:(208012,77)}
words={5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen'}
rows=[]; passed=True
for n,(catalan,channels) in expected.items():
 p=ROOT/f'research/nima/results/abhy-{words[n]}-point-biadjoint-amplitude.json'
 d=json.loads(p.read_text())
 count=d.get('term_count',len(d.get('triangulations',[])))
 listed=len(d.get('physical_channels',[])) if n>5 else n*(n-3)//2
 ok=d['passed'] and count==catalan and listed==channels
 passed &= ok
 rows.append({'multiplicity':n,'artifact':str(p.relative_to(ROOT)),'terms':count,'expected_catalan':math.comb(2*(n-2),n-2)//(n-1),'channels':listed,'expected_channels':n*(n-3)//2,'passed':ok})
out={'schema':'marici.nima.abhy-biadjoint-replication-suite.v1','benchmark':'arXiv:1711.09102 planar tree-level biadjoint amplitudes','multiplicities':[5,6,7,8,9,10,11,12,13,14],'results':rows,'passed':passed,'scope':'Aggregate exact benchmark integrity; no claim for Yang-Mills, gravity, or loops.'}
p=ROOT/'research/nima/results/abhy-biadjoint-replication-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
