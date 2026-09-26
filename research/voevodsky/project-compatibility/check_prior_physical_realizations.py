"""Read-only recovery audit of existing Benincasa evidence; writes only our receipt."""
from pathlib import Path
import hashlib,importlib.util,json,sys
import sympy as sp
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];B=ROOT/'research/benincasa'
names=['source-to-observer-transfer-goal-audit.md','spectral-gaussian-source-to-observer-complex.json','source-authorized-renormalization-provenance.md','source-authorized-renormalization-completion.json','check_source_authorized_renormalization_completion.py','three-site-uv-finiteness.json','fixed-loop-physical-score-rank.json','check_fixed_loop_physical_score_rank.py','action-level-renormalization-source-bridge.md','finite-q-tensor-vertex-ports.json']
paths=[B/n for n in names]+[Path(__file__)]
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes()
spec=importlib.util.spec_from_file_location('prior_fixed_cycle_score_audit',B/'check_fixed_loop_physical_score_rank.py')
module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
old=sys.dont_write_bytecode;sys.dont_write_bytecode=True
try:spec.loader.exec_module(module)
finally:sys.dont_write_bytecode=old
runs=[module.run_packet(32003,(3,4,5)),module.run_packet(32009,(4,13,15))]
load=lambda n:json.loads((B/n).read_text(encoding='utf-8'))
spectral=load('spectral-gaussian-source-to-observer-complex.json')
D=sp.Matrix(spectral['maps']['direct_score'])
assert D.det()==-6 and D.inv()*D==sp.eye(3)
# This tests the actual retained direct-score matrix, not an invented tensor transfer.
assert D.det()**2==spectral['coefficient_compatibility']['elliptic_rank2_tensor_determinant']
assert D.det()**12==spectral['coefficient_compatibility']['marked_relative_rank12_tensor_determinant']
finite=load('source-authorized-renormalization-completion.json');uv=load('three-site-uv-finiteness.json')
assert finite['source_authorized_finite_maps']==['ev_epsilon=0']
assert finite['renormalized_readout_rank']==7
assert uv['common_dimension_strip']=='2 < Re(d) < 4'
assert 2<3<4
assert before==hashes()
report={'passed':True,'owner_sources_unchanged':True,'source_sha256':before,
 'fresh_score_runs':[{'prime':r['prime'],'energies':r['energies'],'response_rank':r['response_rank'],'rank_with_constant':r['rank_with_constant']} for r in runs],
 'fresh_direct_score_determinant':int(D.det()),'fresh_direct_score_inverse':[[str(v) for v in row] for row in D.inv().tolist()],
 'historical_finite_map':finite['source_authorized_finite_maps'],
 'scope':'Recomputed two modular score ranks and exact direct-score matrix invariants. Historical analytic convergence, source authority, full tensor transfer and physical completion are not independently re-proved by this audit. No owner outputs rewritten.'}
(HERE/'prior-physical-realizations.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
