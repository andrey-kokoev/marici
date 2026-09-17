#!/usr/bin/env python3
"""Aggregate integrity checks for momentum-twistor NMHV replications."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
artifacts=['six-point-momentum-twistor-r-invariant-identity.json','six-point-nmhv-bcfw-triangulation-independence.json','seven-point-nmhv-bcfw-cyclic-invariance.json','eight-point-nmhv-bcfw-cyclic-invariance.json','nine-point-nmhv-bcfw-cyclic-invariance.json','ten-point-nmhv-bcfw-cyclic-invariance.json','eleven-point-nmhv-bcfw-cyclic-invariance.json','twelve-point-nmhv-bcfw-cyclic-invariance.json']
rows=[];passed=True
for name in artifacts:
 p=ROOT/'research/nima/results'/name;d=json.loads(p.read_text());ok=d['passed'];passed &= ok
 rows.append({'artifact':str(p.relative_to(ROOT)),'passed':ok,'coefficients_checked':d.get('total_grassmann_coefficients_checked',d.get('grassmann_coefficients_checked'))})
out={'schema':'marici.nima.momentum-twistor-nmhv-replication-suite.v1','benchmark':'planar N=4 SYM momentum-twistor R-invariants and BCFW representations','results':rows,'passed':passed,'scope':'Six- through twelve-point exact rational positive-kinematics checks.'}
p=ROOT/'research/nima/results/momentum-twistor-nmhv-replication-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
