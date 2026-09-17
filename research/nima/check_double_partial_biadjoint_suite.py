#!/usr/bin/env python3
"""Aggregate finite certificates supporting the arbitrary-n double-partial proof."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results';items=['double-partial-biadjoint-common-trees.json','double-partial-biadjoint-factorization.json'];rows=[];passed=True
for name in items:
 d=json.loads((R/name).read_text());ok=d['passed'];passed &= ok;rows.append({'artifact':name,'schema':d['schema'],'passed':ok})
proof=ROOT/'research/nima/arbitrary-n-double-partial-biadjoint-proof.md';checks={'proof_present':proof.is_file() and proof.stat().st_size>0,'finite_certificates_pass':passed};out={'schema':'marici.nima.double-partial-biadjoint-suite.v1','arbitrary_n_proof':str(proof.relative_to(ROOT)),'finite_certificates':rows,'checks':checks,'passed':all(checks.values()),'scope':'Arbitrary-n cut/glue proof with finite exact implementation checks through n=9.'}
p=R/'double-partial-biadjoint-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
