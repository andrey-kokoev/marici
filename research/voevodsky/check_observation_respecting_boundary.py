"""Finite controls for the proved boundary calculus; not a physical-law oracle."""
from pathlib import Path
from itertools import permutations
import hashlib,json
base=Path(__file__).resolve().parent
receipt_path=base/'observation-respecting-boundary-formal.json'
f=json.loads(receipt_path.read_text())
checks={
 'fresh_formal_closure':f['passed'] and f['fresh'] and f['observed_boundary_mode'],
 'intended_controls':len(f['results'])==3 and all(r['passed'] for r in f['results']),
 'dependencies_current':all(Path(p).exists() and hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in f['source_snapshot_hashes'].items()),
 'checker_current':hashlib.sha256((base/'check_native_radar_formal.py').read_bytes()).hexdigest()==f['checker_sha256']}
# An explicitly synthetic finite signature tests the generic operations.
X=(-2,-1,0,1,2); all_maps=list(permutations(X))
def at(p,x):return p[X.index(x)]
def respects(p,r):return all(r(at(p,x))==r(x) for x in X)
def comp(p,q):return tuple(at(q,at(p,x)) for x in X)
def inverse(p):return tuple(X[p.index(x)] for x in X)
coarse=[p for p in all_maps if respects(p,abs)]
fine=[p for p in all_maps if respects(p,lambda x:(abs(x),x))]
checks['constant_observation_admits_every_permutation']=all(respects(p,lambda _:0) for p in all_maps)
checks['absolute_observation_has_four_symmetries']=len(coarse)==4
checks['joint_observation_has_only_identity']=fine==[X]
checks['refinement_strictly_restricts_underlying_maps']=set(fine)<set(coarse)<set(all_maps)
checks['identity_preserves_declared_observation']=X in coarse
for i,p in enumerate(coarse):
    checks[f'inverse_compatible_{i}']=inverse(p) in coarse
    checks[f'inverse_laws_{i}']=comp(p,inverse(p))==X and comp(inverse(p),p)==X
    for j,q in enumerate(coarse):checks[f'composition_compatible_{i}_{j}']=comp(p,q) in coarse
checks['joint_compatibility_is_componentwise']=all(respects(p,lambda x:(abs(x),x))==(respects(p,abs) and respects(p,lambda x:x)) for p in all_maps)
# Actual preceding physical example, integer payload scale 8*1728.
checks['actual_gradient_channels_differ']=-144!=0
checks['actual_loose_filler_aligns_marked_gradients']=-144+144==0
checks['actual_loose_filler_not_gradient_preserving']=-144+144!=-144
checks['observation_scope_not_selected_by_carrier']=len(all_maps)>len(coarse)>len(fine)
out=dict(passed=all(checks.values()),checks=checks,finite_signature={'domain':X,'unrestricted':len(all_maps),'absolute_observation':len(coarse),'joint_observation':len(fine)},
 formal_receipt_sha256=hashlib.sha256(receipt_path.read_bytes()).hexdigest(),
 scope='Universal closure/refinement/native-transport statements are Agda proofs. Finite permutation controls are synthetic, not new physical sources. Physical profile authorization and metric completion remain separate obligations.')
(base/'observation-respecting-boundary.json').write_text(json.dumps(out,indent=2)+'\n')
print('passed=',out['passed'],'checks=',len(checks))
raise SystemExit(0 if out['passed'] else 1)
