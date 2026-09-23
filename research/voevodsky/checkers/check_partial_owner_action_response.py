"""Synthetic action response cannot convert origin attestation into proof use."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
payload=json.loads((root/'results/unsent-owner-handoff-payload.json').read_text())
origin,use=payload['requested_actions']
fixture={'request_sha256':payload['request_sha256'],'manifest_sha256':payload['ordered_manifest_sha256'],'generation':7,'issuer':'fictional-only','actions':{origin:'attested',use:'declined'}}
def assess(resp,expected_generation):
 if resp['request_sha256']!=payload['request_sha256'] or resp['manifest_sha256']!=payload['ordered_manifest_sha256']:raise ValueError('RESPONSE_SOURCE_REQUEST_MISMATCH')
 if resp['generation']!=expected_generation:raise ValueError('RESPONSE_GENERATION_MISMATCH')
 if set(resp['actions'])!=set(payload['requested_actions']):raise ValueError('RESPONSE_ACTION_SET_MISMATCH')
 if resp['actions'][origin]!='attested' or resp['actions'][use]!='declined':raise ValueError('RESPONSE_ACTION_VALUES_MISMATCH')
 return {origin:'TEST_ONLY_ORIGIN_CLAIM_NOT_AUTHENTICATED',use:'DECLINED_NO_PROOF_USE'}
assert assess(fixture,7)[use]=='DECLINED_NO_PROOF_USE'
def refuse(change,error):
 try:assess(dict(fixture,**change),7)
 except ValueError as err:assert str(err)==error
 else:raise AssertionError('wrong response accepted')
refuse({'manifest_sha256':'other'},'RESPONSE_SOURCE_REQUEST_MISMATCH')
refuse({'generation':8},'RESPONSE_GENERATION_MISMATCH')
refuse({'actions':{origin:'attested'}},'RESPONSE_ACTION_SET_MISMATCH')
refuse({'actions':{origin:'attested',use:'attested'}},'RESPONSE_ACTION_VALUES_MISMATCH')
assert payload['recipient'] is None
report={'passed':True,'fictional_origin':'TEST_ONLY_ORIGIN_CLAIM_NOT_AUTHENTICATED','fictional_use':'DECLINED_NO_PROOF_USE','wrong_source_request_generation_or_action':'refused','actual_response':'NONE; no owner recipient, signed response or verifier','scope':'Hypothetical action-state partition; cannot treat test-only claim as authenticated owner attestation.'}
out=root/'results/partial-owner-action-response.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
