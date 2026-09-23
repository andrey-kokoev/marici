"""Synthetic grant scope must bind entire row source and permitted action."""
from hashlib import sha256
from pathlib import Path
import json
request=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
manifest=request['manifest']
def digest(m):return sha256(json.dumps(m,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert digest(manifest)==request['manifest_sha256']
grant={'issuer':'fictional-test-only','source_id':manifest['source_id'],'manifest_sha256':digest(manifest),'dimension':2,'action':'attest-primitive-row-origin','event_id':'fictional-event'}
def check(m,g,action):
 if m['source_id']!=g['source_id']:raise ValueError('SOURCE_ID_MISMATCH')
 if m['dimension']!=g['dimension']:raise ValueError('DIMENSION_SCOPE_MISMATCH')
 if digest(m)!=g['manifest_sha256']:raise ValueError('ORDERED_ROW_SCOPE_MISMATCH')
 if g['action']!=action:raise ValueError('ACTION_SCOPE_MISMATCH')
 return 'TEST_ONLY_SCOPE_MATCH_NOT_AUTHORIZED'
assert check(manifest,grant,'attest-primitive-row-origin')=='TEST_ONLY_SCOPE_MATCH_NOT_AUTHORIZED'
def expect(m,g,action,code):
 try:check(m,g,action)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('scope escape admitted')
expect(dict(manifest,dimension=3),grant,grant['action'],'DIMENSION_SCOPE_MISMATCH')
expect(dict(manifest,ordered_primitive_rows=manifest['ordered_primitive_rows'][:3]),grant,grant['action'],'ORDERED_ROW_SCOPE_MISMATCH')
expect(dict(manifest,ordered_primitive_rows=list(reversed(manifest['ordered_primitive_rows']))),grant,grant['action'],'ORDERED_ROW_SCOPE_MISMATCH')
expect(manifest,grant,'authorize-future-source-rooted-proof-use','ACTION_SCOPE_MISMATCH')
report={'passed':True,'same_source_label_different_dimension':'DIMENSION_SCOPE_MISMATCH','same_label_row_subset_or_reorder':'ORDERED_ROW_SCOPE_MISMATCH','same_manifest_different_capability':'ACTION_SCOPE_MISMATCH','exact_fictional_scope':'TEST_ONLY_SCOPE_MATCH_NOT_AUTHORIZED','real_request':'owner unassigned; no signed grant or admitted trust root','scope':'Local negative test of exact source/action scoping, not real issuer attestation, signature verification, publication or analytic role correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/row-source-grant-scope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
