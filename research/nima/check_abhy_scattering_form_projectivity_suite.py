#!/usr/bin/env python3
"""Aggregate exact ABHY scattering-form projectivity checks."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];words={5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen'};rows=[];passed=True
for n,w in words.items():
 p=ROOT/f'research/nima/results/abhy-{w}-point-scattering-form-projectivity.json';d=json.loads(p.read_text());ok=d['passed'] and not d['variation_coefficients'];passed &= ok
 rows.append({'multiplicity':n,'form_degree':n-3,'cubic_graph_terms':len(d.get('oriented_terms',d.get('form_terms',[]))),'projective_variation_terms':len(d['variation_coefficients']),'passed':ok})
out={'schema':'marici.nima.abhy-scattering-form-projectivity-suite.v1','benchmark':'arXiv:1711.09102 projective planar scattering forms','results':rows,'passed':passed,'scope':'Exact exterior-algebra checks from five through fourteen points.'}
p=ROOT/'research/nima/results/abhy-scattering-form-projectivity-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
