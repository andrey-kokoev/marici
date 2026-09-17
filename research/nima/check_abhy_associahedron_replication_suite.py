#!/usr/bin/env python3
"""Aggregate integrity check for ABHY kinematic-associahedron replications."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
words={5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
rows=[]; passed=True
for n,w in words.items():
 p=ROOT/f'research/nima/results/abhy-{w}-point-associahedron-form.json';d=json.loads(p.read_text())
 facets=n*(n-3)//2; vertices=math.comb(2*(n-2),n-2)//(n-1); ok=d['passed'] and len(d['embedding'])==facets and len(d['vertices'])==vertices
 passed &= ok;rows.append({'multiplicity':n,'dimension':n-3,'facets':len(d['embedding']),'expected_facets':facets,'vertices':len(d['vertices']),'expected_catalan_vertices':vertices,'canonical_form_check':next(v for k,v in d['checks'].items() if k.startswith('canonical_form_equals_amplitude')),'passed':ok})
out={'schema':'marici.nima.abhy-associahedron-replication-suite.v1','benchmark':'arXiv:1711.09102 kinematic associahedra and canonical forms','multiplicities':list(words),'results':rows,'passed':passed,'scope':'Exact affine positive-geometry checks at multiplicities 5 through 10.'}
p=ROOT/'research/nima/results/abhy-associahedron-replication-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
