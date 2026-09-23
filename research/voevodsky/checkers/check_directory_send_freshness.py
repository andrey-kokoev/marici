"""Cached fictional row-owner endpoint cannot authorize send after rotation."""
from pathlib import Path
import json
r=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
old={'source':r['manifest']['source_id'],'manifest':r['manifest_sha256'],'epoch':5,'endpoint':'fictional://old','trust_root':'fictional-key-5','generation':1,'revoked':False}
def gate(cached,live):
 if cached['epoch']!=live['epoch']:raise ValueError('DIRECTORY_SNAPSHOT_STALE')
 if cached!=live:raise ValueError('SAME_EPOCH_BINDING_CHANGED')
 if live['revoked']:raise ValueError('DIRECTORY_ENTRY_REVOKED')
 if live['source']!=r['manifest']['source_id'] or live['manifest']!=r['manifest_sha256']:raise ValueError('ROW_SOURCE_SCOPE_MISMATCH')
 return 'TEST_ONLY_ENDPOINT_FRESH_NOT_AUTHORIZED_TO_SEND'
rotated=dict(old,epoch=6,endpoint='fictional://new',trust_root='fictional-key-6',generation=2)
for live,expected in ((rotated,'DIRECTORY_SNAPSHOT_STALE'),(dict(old,endpoint='fictional://moved'),'SAME_EPOCH_BINDING_CHANGED')):
 try:gate(old,live)
 except ValueError as err:assert str(err)==expected
 else:raise AssertionError('stale endpoint accepted')
try:gate(dict(rotated,revoked=True),dict(rotated,revoked=True))
except ValueError as err:assert str(err)=='DIRECTORY_ENTRY_REVOKED'
else:raise AssertionError('revoked endpoint accepted')
assert gate(rotated,rotated)=='TEST_ONLY_ENDPOINT_FRESH_NOT_AUTHORIZED_TO_SEND'
assert r['requested_owner'] is None and r['owner_event_id'] is None
report={'passed':True,'cached_endpoint_after_rotation':'DIRECTORY_SNAPSHOT_STALE','same_epoch_binding_mutation':'SAME_EPOCH_BINDING_CHANGED','revoked_fresh_entry':'DIRECTORY_ENTRY_REVOKED','fictional_current_entry':'TEST_ONLY_ENDPOINT_FRESH_NOT_AUTHORIZED_TO_SEND','real_handoff':'NO_AUTHENTICATED_OWNER_RECIPIENT; no message sent','scope':'Synthetic directory compare-at-send; no trust-root signature verification or actual source issuer admission.'}
out=Path(__file__).resolve().parents[1]/'results/directory-send-freshness.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
