"""Bounded conjunction of checked local obligations versus absent analytic role map."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky/results'
def load(name):return json.loads((V/name).read_text())
local={'source_contract':load('relational-continuation-ports.json'),
       'operation_square':load('unified-local-laws-verification.json'),
       'section':load('whole-section-comparison.json'),
       'resource':load('integrated-local-continuation-verification.json'),
       'cost':load('scoped-cost-ledger-verification.json'),
       'provider_menu':load('fixed-menu-provider-bundles-verification.json'),
       'sensitivity':load('bundle-cost-sensitivity-verification.json')}
assert all(x['passed'] for x in local.values())
root=load('integrated-local-continuation.json')['root']
assert root==load('unified-local-laws.json')['source_binding']==load('fixed-menu-provider-bundles.json')['migration_binding']==load('scoped-cost-ledger.json')['migration_binding']
assert local['operation_square']['refined_public_optimum']==local['resource']['verified_refined_public_optimum']=='3/4'
assert local['section']['direct_equals_staged'] and local['provider_menu']['minimum_receipt_bytes']==3658
assert local['sensitivity']['independent_threshold']=='180'
assert local['cost']['receipt_subtotal_bytes']==3838
assert local['source_contract']['state_count']==638
analytic=load('analytic-interval-defect-profile.json')
assert analytic['passed'] and len(analytic['intervals'])==10
assert analytic['intervals'][0]['interval']==[0,1] and analytic['intervals'][0]['cokernel']==1
# The finite protocol and rank-one migration do NOT share a source carrier.
# Their presence in one ledger is not a natural transformation between them.
obstruction={'first_missing_map':'source-derived S,A,C,G role-labelled closed edge/domain/base assignment to polyhedral constraint/provider objects',
 'noncollapse_test':'preserve ten graded interval kernel/cokernel profiles and reciprocal mates; first edge cokernel dimension one cannot map to acyclic simplex-face cone',
 'coupled_protocol_status':'separate 638-state carrier; no coercion into rank-one migration source',
 'analytic_identification':'withheld'}
paths=[V/(name+'.json') for name in ('relational-continuation-ports','unified-local-laws-verification','whole-section-comparison','integrated-local-continuation-verification','scoped-cost-ledger-verification','fixed-menu-provider-bundles-verification','bundle-cost-sensitivity-verification','analytic-interval-defect-profile')]
bindings={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
report={'passed':True,'local_status':'scoped_checked_conjunction_not_single_universal_source_theory','rank_one_migration_binding':root,'independent_protocol_states':638,'public_optimum':'3/4','whole_section_routes_agree':True,'finite_receipt_minimum':3658,'cost_delta_threshold':180,'total_cost':'unavailable','analytical_status':obstruction,'bindings':bindings,'scope':'Conjunction of existing bounded checks plus binding checks; does not rerun owning verifiers or construct cross-sector realization.'}
(V/'integrated-architecture-boundary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('bindings','rank_one_migration_binding')},indent=2))
