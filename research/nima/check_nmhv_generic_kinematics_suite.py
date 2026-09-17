#!/usr/bin/env python3
"""Aggregate NMHV identity checks away from moment-curve kinematics."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
items=[('six-term identity','six-term-r-invariant-identity-generic-kinematics.json'),('seven-point cyclic invariance','seven-point-nmhv-cyclic-generic-kinematics.json'),('seven-point reflection invariance','seven-point-nmhv-reflection-generic-kinematics.json'),('eight-point cyclic invariance','eight-point-nmhv-cyclic-generic-kinematics.json'),('eight-point reflection invariance','eight-point-nmhv-reflection-generic-kinematics.json'),('nine-point cyclic invariance','nine-point-nmhv-cyclic-generic-kinematics.json'),('nine-point reflection invariance','nine-point-nmhv-reflection-generic-kinematics.json'),('ten-point cyclic invariance','ten-point-nmhv-cyclic-generic-kinematics.json'),('ten-point reflection invariance','ten-point-nmhv-reflection-generic-kinematics.json')]
rows=[];passed=True
for label,name in items:
 d=json.loads((R/name).read_text());ok=d['passed'];passed &= ok;rows.append({'benchmark':label,'artifact':name,'exact_coefficient_checks':d['total_exact_coefficient_checks'],'passed':ok})
out={'schema':'marici.nima.nmhv-generic-kinematics-suite.v1','benchmark':'NMHV momentum-twistor identities on generic rational data','results':rows,'total_exact_coefficient_checks':sum(r['exact_coefficient_checks'] for r in rows),'passed':passed,'scope':'Generic denominator-regular rational matrices, complementing positive moment-curve tests.'}
p=R/'nmhv-generic-kinematics-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
