#!/usr/bin/env python3
"""Aggregate integrity check for NMHV spurious-boundary cancellation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
items=[(6,'six',3),(7,'seven',8),(8,'eight',15),(9,'nine',24)];rows=[];passed=True
for n,w,count in items:
 p=ROOT/f'research/nima/results/{w}-point-nmhv-all-spurious-poles.json';d=json.loads(p.read_text());ok=d['passed'] and len(d['runs'])==count and all(r['failure_count']==0 and r['nonzero_individual_residues']>0 for r in d['runs']);passed &= ok
 rows.append({'multiplicity':n,'spurious_divisors':len(d['runs']),'expected':count,'grassmann_residues_checked':d['total_grassmann_residues_checked'],'passed':ok})
out={'schema':'marici.nima.nmhv-spurious-boundary-replication-suite.v1','benchmark':'cancellation of internal BCFW/amplituhedron boundaries','results':rows,'total_residue_checks':sum(r['grassmann_residues_checked'] for r in rows),'passed':passed,'scope':'Complete shared nonphysical codimension-one divisor census for the standard NMHV BCFW sums at six through nine points.'}
p=ROOT/'research/nima/results/nmhv-spurious-boundary-replication-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
