"""A directory contact is not a trusted row issuer verification endpoint."""
from pathlib import Path
import json
req=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
manifest=req['manifest_sha256'];source=req['manifest']['source_id']
contact={'source_id':source,'contact':'fictional-person@example.invalid','manifest':manifest,'status':'descriptive'}
def classify(entry):
 if entry.get('source_id')!=source or entry.get('manifest')!=manifest:return 'SOURCE_SCOPE_MISMATCH'
 if entry.get('status')!='admitted_verification_endpoint':return 'DESCRIPTIVE_CONTACT_ONLY'
 if not entry.get('trust_root') or not entry.get('verification_endpoint'):return 'TRUST_OR_ENDPOINT_MISSING'
 if entry.get('live_generation') is None or not entry.get('revocation_route'):return 'GENERATION_OR_REVOCATION_MISSING'
 return 'TEST_ONLY_ENDPOINT_SHAPE_COMPLETE_NOT_AUTHORIZED'
assert classify(contact)=='DESCRIPTIVE_CONTACT_ONLY'
endpoint=dict(contact,status='admitted_verification_endpoint',trust_root='fictional-root',verification_endpoint='fictional://verify')
assert classify(endpoint)=='GENERATION_OR_REVOCATION_MISSING'
assert classify(dict(endpoint,trust_root=None))=='TRUST_OR_ENDPOINT_MISSING'
complete=dict(endpoint,live_generation=7,revocation_route='fictional://revoke')
assert classify(complete)=='TEST_ONLY_ENDPOINT_SHAPE_COMPLETE_NOT_AUTHORIZED'
assert classify(dict(complete,manifest='wrong'))=='SOURCE_SCOPE_MISMATCH'
assert req['requested_owner'] is None and req['owner_event_id'] is None
report={'passed':True,'descriptive_contact':'DESCRIPTIVE_CONTACT_ONLY','missing_trust_endpoint':'TRUST_OR_ENDPOINT_MISSING','no_live_generation_or_revocation':'GENERATION_OR_REVOCATION_MISSING','fully_fictional_shape':'TEST_ONLY_ENDPOINT_SHAPE_COMPLETE_NOT_AUTHORIZED','actual_owner':'unassigned; no contact message sent','scope':'Directory interface model, not an admitted live directory entry, usable message address or external trust root.'}
out=Path(__file__).resolve().parents[1]/'results/typed-owner-directory-candidate.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
