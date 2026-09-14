#!/usr/bin/env python3
"""Freeze the Del Pezzo entrance and partition later Voevodsky artifacts as holdout."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
origin=R/'research/voevodsky/results/global_del_pezzo_double_cover.json'
statement=R/'research/voevodsky/the_cayley_menger_determinant_supplies_the_global_del_pezzo_surface.md'
data=json.loads(origin.read_text()); cutoff=origin.stat().st_mtime_ns
assert data['passed'] and data['next']=="identify the invariant rank-three E7 sublattice and express the source support plane in the same marking"
def record(p):
 b=p.read_bytes();return {'path':p.relative_to(R).as_posix(),'mtime_ns':p.stat().st_mtime_ns,'sha256':hashlib.sha256(b).hexdigest()}
# The theorem is a contemporaneous restatement even though its write follows the JSON.
entrance=[record(origin),record(statement)]
all_results=sorted((R/'research/voevodsky/results').glob('*.json'),key=lambda p:(p.stat().st_mtime_ns,p.name))
holdout=[record(p) for p in all_results if p.stat().st_mtime_ns>cutoff and p!=origin]
first=[h['path'] for h in holdout[:12]]
out={'schema':'marici.conjecture-replay.del-pezzo-entrance-freeze.v1','cutoff':{'artifact':origin.relative_to(R).as_posix(),'mtime_ns':cutoff,'sha256':entrance[0]['sha256']},'entrance_artifacts':entrance,'established':{'surface':data['surface'],'global_involutions':data['global_involutions'],'E7_eigen_multiplicities':data['fixed_locus_r_a']['E7_eigen_multiplicities'],'next':data['next']},'policy_information_rule':'entrance plus artifacts at or before cutoff; theorem is a contemporaneous restatement','holdout_result_count':len(holdout),'first_holdout_results':first,'holdout_manifest':holdout,'checks':{'origin_passed':data['passed'],'cutoff_precedes_every_holdout':all(h['mtime_ns']>cutoff for h in holdout),'origin_excluded_from_holdout':all(h['path']!=entrance[0]['path'] for h in holdout),'first_expected_holdout':'research/voevodsky/results/reflection_elliptic_pencil.json' in first},'passed':True}
assert all(out['checks'].values());dest=R/'research/conjecture_replay/results/del_pezzo_entrance_freeze.json';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'cutoff':cutoff,'holdout_results':len(holdout),'first':first[:5]}))
