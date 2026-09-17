#!/usr/bin/env python3
"""Aggregate exact dihedral-symmetry replication for eight-point NMHV."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
files=['eight-point-nmhv-bcfw-cyclic-invariance.json','eight-point-nmhv-bcfw-reflection-invariance.json']
rows=[]
for f in files:
 d=json.loads((ROOT/'research/nima/results'/f).read_text());rows.append({'artifact':f,'passed':d['passed'],'coefficients_checked':d['total_grassmann_coefficients_checked']})
out={'schema':'marici.nima.eight-point-nmhv-dihedral-replication.v1','benchmark':'dihedral symmetry of the planar eight-point NMHV tree ratio function','generators':{'rotation':'i -> i+1 mod 8','reflection':'i -> 9-i'},'checks':rows,'total_exact_coefficient_checks':sum(r['coefficients_checked'] for r in rows),'passed':all(r['passed'] for r in rows),'scope':'Three exact positive configurations for each dihedral generator.'}
p=ROOT/'research/nima/results/eight-point-nmhv-dihedral-replication.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
