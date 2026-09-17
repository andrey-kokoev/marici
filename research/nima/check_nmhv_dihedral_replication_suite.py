#!/usr/bin/env python3
"""Aggregate exact dihedral-symmetry checks for planar NMHV tree ratios."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];words={8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve'};rows=[];passed=True
for n,w in words.items():
 gens={}
 for g in ('cyclic','reflection'):
  p=ROOT/f'research/nima/results/{w}-point-nmhv-bcfw-{g}-invariance.json';d=json.loads(p.read_text());gens[g]={'artifact':str(p.relative_to(ROOT)),'coefficients_checked':d['total_grassmann_coefficients_checked'],'passed':d['passed']}
 ok=all(v['passed'] for v in gens.values());passed &= ok;rows.append({'multiplicity':n,'generators':gens,'passed':ok})
out={'schema':'marici.nima.nmhv-dihedral-replication-suite.v1','benchmark':'dihedral invariance of planar N=4 SYM NMHV tree ratio functions','results':rows,'total_exact_coefficient_checks':sum(v['coefficients_checked'] for r in rows for v in r['generators'].values()),'passed':passed,'scope':'Rotation and reflection generators at eight through twelve points, each on three exact positive configurations.'}
p=ROOT/'research/nima/results/nmhv-dihedral-replication-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
