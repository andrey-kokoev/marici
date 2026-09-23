"""Local least-privilege model: primitive-row origin != future proof-use grant."""
from pathlib import Path
import json
request=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
origin,use=request['requested_capabilities']
assert origin=='attest-primitive-row-origin' and use=='authorize-future-source-rooted-proof-use'
manifest=request['manifest_sha256']
def authorize(grant,action,revoked=frozenset()):
 if grant.get('manifest')!=manifest:raise ValueError('MANIFEST_SCOPE_MISMATCH')
 if action not in grant['capabilities']:raise ValueError('CAPABILITY_NOT_GRANTED')
 if action in revoked:raise ValueError('CAPABILITY_REVOKED')
 return 'TEST_ONLY_ACTION_SCOPE_MATCH_NOT_AUTHORIZED'
base={'issuer':'fictional-test-issuer','manifest':manifest,'event':'fictional-test-event','capabilities':frozenset((origin,))}
assert authorize(base,origin)=='TEST_ONLY_ACTION_SCOPE_MATCH_NOT_AUTHORIZED'
try:authorize(base,use)
except ValueError as err:assert str(err)=='CAPABILITY_NOT_GRANTED'
else:raise AssertionError('origin escalated to proof use')
combined=dict(base,capabilities=frozenset((origin,use)))
assert authorize(combined,use)=='TEST_ONLY_ACTION_SCOPE_MATCH_NOT_AUTHORIZED'
try:authorize(combined,use,frozenset((use,)))
except ValueError as err:assert str(err)=='CAPABILITY_REVOKED'
else:raise AssertionError('revoked proof use admitted')
assert authorize(combined,origin,frozenset((use,)))=='TEST_ONLY_ACTION_SCOPE_MATCH_NOT_AUTHORIZED'
try:authorize(dict(combined,manifest='wrong'),origin)
except ValueError as err:assert str(err)=='MANIFEST_SCOPE_MISMATCH'
else:raise AssertionError('foreign manifest admitted')
report={'passed':True,'origin_only_to_use':'CAPABILITY_NOT_GRANTED','combined_grant':'TEST_ONLY_ACTION_SCOPE_MATCH_NOT_AUTHORIZED','use_only_revocation':'CAPABILITY_REVOKED without revoking origin','different_manifest':'MANIFEST_SCOPE_MISMATCH','real_owner_request':'requested_owner and owner_event_id unassigned; zero live grants','scope':'Synthetic set-inclusion lattice, no signed issuer, actual revocation channel or publication authority; analytic roles not mapped.'}
out=Path(__file__).resolve().parents[1]/'results/source-capability-lattice.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
