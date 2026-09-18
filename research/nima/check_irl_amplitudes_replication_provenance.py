#!/usr/bin/env python3
"""Materialize source/result digests for the amplitude replication suites."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];manifest=json.loads((ROOT/'research/nima/results/irl-amplitudes-replication-manifest.json').read_text())
files=[]
for row,checker in zip(manifest['benchmark_families'],manifest['suite_checkers']):
 for role,path in [('checker',checker),('result',row['artifact'])]:
  p=ROOT/path;data=p.read_bytes();files.append({'family':row['benchmark_family'],'role':role,'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
checks={'manifest_passed':manifest['passed'],'family_count_matches_manifest':len(manifest['benchmark_families'])==manifest['family_count'],'two_files_per_family':len(files)==2*manifest['family_count'],'all_nonempty':all(r['bytes']>0 for r in files),'all_digests_unique':len({r['sha256'] for r in files})==len(files)}
out={'schema':'marici.nima.irl-amplitudes-replication-provenance.v1','manifest_schema':manifest['schema'],'files':files,'checks':checks,'passed':all(checks.values()),'scope':'Content-addressed snapshot of top-level suite sources and result artifacts; leaf artifacts remain referenced through their suites.'}
p=ROOT/'research/nima/results/irl-amplitudes-replication-provenance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'families':manifest['family_count'],'files_hashed':len(files),'checks':checks},indent=2));raise SystemExit(0 if out['passed'] else 1)
