#!/usr/bin/env python3
"""Aggregate sourced one-loop MHV pre-integration replication results."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
items=[
 ('four-point source conformance','four-point-one-loop-mhv-integrand.json'),
 ('four-point dlog identity','four-point-one-loop-mhv-dlog-identity.json'),
 ('arbitrary-n Kermit count and covariance','arbitrary-n-one-loop-mhv-kermit-covariance.json'),
 ('physical/spurious residue census','one-loop-mhv-kermit-pole-census.json'),
 ('cyclic invariance','one-loop-mhv-kermit-cyclic-invariance.json'),
 ('reflection invariance','one-loop-mhv-kermit-reflection-invariance.json')]
rows=[];passed=True
for label,name in items:
 d=json.loads((R/name).read_text());ok=d.get('passed') is True;passed &= ok
 rows.append({'benchmark':label,'artifact':f'research/nima/results/{name}','schema':d.get('schema'),'passed':ok})
out={'schema':'marici.nima.one-loop-mhv-replication-suite.v1','source':'arXiv:1008.2958 and arXiv:1212.5605 acquired TeX','results':rows,'checks':{'all_dependencies_passed':passed,'preintegration_scope_only':True},'passed':passed,'scope':'Sourced rational and canonical-form results for planar one-loop MHV integrands; no integration, regulator, or infrared-finite observable.'}
p=R/'one-loop-mhv-replication-suite.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
