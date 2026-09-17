#!/usr/bin/env python3
"""Aggregate exact covariance checks for momentum-twistor five-brackets."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
items=[('independent supertwistor projectivity','six-point-r-invariant-projectivity.json'),('SL(4) invariance','six-point-r-invariant-sl4-invariance.json'),('GL(4) determinant weight','six-point-r-invariant-gl4-weight.json'),('total antisymmetry','momentum-twistor-five-bracket-antisymmetry.json')]
rows=[];passed=True
for label,name in items:
 d=json.loads((R/name).read_text());ok=d['passed'];passed &= ok;rows.append({'property':label,'artifact':name,'exact_coefficient_checks':d['total_exact_coefficient_checks'],'passed':ok})
out={'schema':'marici.nima.momentum-twistor-covariance-suite.v1','benchmark':'algebraic covariance properties of NMHV momentum-twistor five-brackets','results':rows,'total_exact_coefficient_checks':sum(r['exact_coefficient_checks'] for r in rows),'passed':passed,'scope':'Exact rational tests of projectivity, linear covariance, and permutation behavior.'}
p=R/'momentum-twistor-covariance-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
