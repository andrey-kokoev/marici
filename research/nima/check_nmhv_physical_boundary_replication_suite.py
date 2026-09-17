#!/usr/bin/env python3
"""Aggregate physical-boundary survival checks for NMHV BCFW sums."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];items=[(6,'six',9),(7,'seven',14),(8,'eight',20),(9,'nine',27)];rows=[];passed=True
for n,w,want in items:
 p=ROOT/f'research/nima/results/{w}-point-nmhv-physical-pole-survival.json';d=json.loads(p.read_text());ok=d['passed'] and len(d['runs'])==want and all(r['nonzero_total_residue_components']>0 for r in d['runs']);passed &= ok
 rows.append({'multiplicity':n,'physical_poles':len(d['runs']),'expected_planar_channels':n*(n-3)//2,'residues_checked':d['total_grassmann_residues_checked'],'passed':ok})
out={'schema':'marici.nima.nmhv-physical-boundary-replication-suite.v1','benchmark':'survival of physical amplituhedron boundaries after summing BCFW cells','results':rows,'total_residue_checks':sum(r['residues_checked'] for r in rows),'passed':passed,'scope':'Exact nonvanishing residue census at six through nine points; normalized factorization is not asserted.'}
p=ROOT/'research/nima/results/nmhv-physical-boundary-replication-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
