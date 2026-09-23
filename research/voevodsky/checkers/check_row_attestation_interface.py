"""Fail-closed proposal interface, never an attestation issuance or signature verifier."""
from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parents[3]
request=json.loads((root/'research/voevodsky/results/row-attestation-request.json').read_text())
def digest(manifest):return sha256(json.dumps(manifest,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert digest(request['manifest'])==request['manifest_sha256']
def verify(disclosure,claim,independent_grant,signature_verifier=None):
 if digest(disclosure)!=request['manifest_sha256']:raise ValueError('ROW_MANIFEST_MISMATCH')
 if not claim or not claim.get('issuer') or not claim.get('source_event_id'):raise ValueError('ISSUER_OR_EVENT_UNASSIGNED')
 if independent_grant is None:raise ValueError('INDEPENDENT_ISSUER_GRANT_MISSING')
 if independent_grant.get('issuer')!=claim['issuer'] or independent_grant.get('source_id')!=request['manifest']['source_id']:raise ValueError('ISSUER_SCOPE_MISMATCH')
 if not claim.get('generation') or claim['generation']!=independent_grant.get('generation') or independent_grant.get('revocation_route') is None:raise ValueError('GENERATION_OR_REVOCATION_MISSING')
 if claim.get('manifest_sha256')!=request['manifest_sha256'] or claim.get('source_event_id')!=independent_grant.get('source_event_id'):raise ValueError('EVENT_MANIFEST_BINDING_MISMATCH')
 if signature_verifier is None:raise ValueError('CRYPTOGRAPHIC_VERIFIER_UNAVAILABLE')
 raise ValueError('EXTERNAL_TRUST_ROOT_NOT_ADMITTED')
def expect(code,disclosure,claim,grant):
 try:verify(disclosure,claim,grant)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('unauthenticated claim accepted')
base={'issuer':'fictional-issuer-test-only','source_event_id':'fictional-event-test-only','generation':'test-generation','manifest_sha256':request['manifest_sha256']}
grant={'issuer':base['issuer'],'source_id':request['manifest']['source_id'],'source_event_id':base['source_event_id'],'generation':base['generation'],'revocation_route':'test-only-route'}
expect('ISSUER_OR_EVENT_UNASSIGNED',request['manifest'],{'issuer':request['requested_owner'],'source_event_id':request['owner_event_id']},None)
expect('INDEPENDENT_ISSUER_GRANT_MISSING',request['manifest'],dict(base,issuer='marici.Voevodsky'),None)
expect('ROW_MANIFEST_MISMATCH',dict(request['manifest'],dimension=3),base,grant)
expect('ISSUER_SCOPE_MISMATCH',request['manifest'],base,dict(grant,issuer='other'))
expect('GENERATION_OR_REVOCATION_MISSING',request['manifest'],base,dict(grant,generation='stale'))
expect('EVENT_MANIFEST_BINDING_MISMATCH',request['manifest'],base,dict(grant,source_event_id='different'))
expect('CRYPTOGRAPHIC_VERIFIER_UNAVAILABLE',request['manifest'],base,grant)
report={'passed':True,'actual_request':'ISSUER_OR_EVENT_UNASSIGNED','graph_actor_self_claim':'INDEPENDENT_ISSUER_GRANT_MISSING','wrong_manifest_scope_generation_or_event':'refused','fully_synthetic_fields':'CRYPTOGRAPHIC_VERIFIER_UNAVAILABLE','authorization_result':'NO_REAL_GRANT','scope':'Interface design only; fictional fields are test fixtures, no source owner contact, signature verification, revocation check, graph truth certification or analytic roles.'}
out=Path(__file__).resolve().parents[1]/'results/row-attestation-interface.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
