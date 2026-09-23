"""Independent finite operator evidence gate; never accepts a self-asserted role map."""
from pathlib import Path
import importlib.util,hashlib,json
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky'
source=V/'checkers/check_degree_four_reciprocal_waldhausen_realization.py'
spec=importlib.util.spec_from_file_location('historical_fixture',source);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
assert h.out['all_exact']
source_digest=hashlib.sha256(source.read_bytes()).hexdigest()
# A candidate is checked only against independently loaded historical data;
# self-reported grade arrays or a claimed owner grant have no admission path.
def check(packet):
 if set(packet)!={'fixture_digest','edges','role_to_polyhedral','base_map','source_authority'}:return 'malformed'
 if packet['fixture_digest']!=source_digest:return 'stale_fixture'
 edges=packet['edges']
 if len(edges)!=4:return 'missing_edges'
 for i,(candidate,actual) in enumerate(zip(edges,h.Fplus)):
  if candidate!=[[str(actual[r,c]) for c in range(actual.cols)] for r in range(actual.rows)]:return 'operator_mismatch'
  if actual.rows-actual.rank()!=[1,0,1,0][i] or actual.cols-actual.rank()!=[0,1,0,1][i]:return 'historical_defect_mismatch'
 if packet['role_to_polyhedral'] is None or packet['base_map'] is None:return 'missing_typed_map'
 # No authoritative role/edge-to-Farkas source functor has been admitted.
 # An arbitrary string here must never be treated as a credential.
 return 'unverified_owner_role_map'
valid_edges=[[[str(a[r,c]) for c in range(a.cols)] for r in range(a.rows)] for a in h.Fplus]
base={'fixture_digest':source_digest,'edges':valid_edges,'role_to_polyhedral':None,'base_map':None,'source_authority':None}
assert check(base)=='missing_typed_map'
assert check({**base,'fixture_digest':'foreign'})=='stale_fixture'
wrong=json.loads(json.dumps(valid_edges));wrong[0][0][0]='9'
assert check({**base,'edges':wrong})=='operator_mismatch'
assert check({**base,'role_to_polyhedral':'S=T0,A=T1,C=T2,G=T3','base_map':'B=b_z','source_authority':'self-certified'})=='unverified_owner_role_map'
report={'passed':True,'historical_fixture_sha256':source_digest,'verified_edge_shapes':[list(x.shape) for x in h.Fplus],'refusals':['stale-fixture','operator-mismatch','missing-map','self-certified-owner-map'],'acceptance_status':'no owner-derived role functor present; finite historical edges alone do not give a cross-category map','scope':'Local verifier boundary for trusted historical finite matrices; owner role/base derivation, closed analytic completion and actual Farkas-chain functor still missing.'}
(V/'results/analytic-adapter-verifier-contract.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='historical_fixture_sha256'},indent=2))
