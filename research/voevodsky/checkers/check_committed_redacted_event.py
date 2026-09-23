"""Opaque event commitment links a chain but cannot replay a hidden occurrence."""
from hashlib import sha256
from pathlib import Path
import json
context=('square-synthetic-v1','W','trace-slot-1')
def commit(ctx,event_id,nonce):return sha256(repr(('event-occurrence-v1',ctx,event_id,nonce)).encode()).hexdigest()
event='w#alpha';nonce='test-private-nonce-77';c=commit(context,event,nonce)
left={'target_event_commitment':c,'target_role':'W','manifest':context[0]}
right={'source_event_commitment':c,'source_role':'W','manifest':context[0]}
assert left['target_event_commitment']==right['source_event_commitment']
def verify_opening(ctx,id_value,salt,digest):
 if id_value is None or salt is None:raise ValueError('UNVERIFIABLE_TRACE')
 if commit(ctx,id_value,salt)!=digest:raise ValueError('COMMITMENT_OPENING_MISMATCH')
 return id_value
try:verify_opening(context,None,None,c)
except ValueError as err:assert str(err)=='UNVERIFIABLE_TRACE'
else:raise AssertionError('opaque commitment replayed')
assert verify_opening(context,event,nonce,c)==event
for ctx,id_value,salt in ((context,'w#beta',nonce),(context,event,'wrong'),(('other-manifest','W','trace-slot-1'),event,nonce)):
 try:verify_opening(ctx,id_value,salt,c)
 except ValueError as err:assert str(err)=='COMMITMENT_OPENING_MISMATCH'
 else:raise AssertionError('wrong opening accepted')
# Even a valid opening does not authenticate source/effect issuer.
def verify_effect_issuer(attestation):
 if attestation is None:raise ValueError('EFFECT_ATTESTATION_MISSING')
try:verify_effect_issuer(None)
except ValueError as err:assert str(err)=='EFFECT_ATTESTATION_MISSING'
else:raise AssertionError('issuer invented')
report={'passed':True,'same_commitment_links_adjacent_record_fields':True,'without_opening':'UNVERIFIABLE_TRACE','correct_opening':'locally checked exact occurrence ID','wrong_id_salt_or_context':'COMMITMENT_OPENING_MISMATCH','effect_issuer_without_attestation':'EFFECT_ATTESTATION_MISSING','scope':'SHA256 domain-separated synthetic commitment with secret-nonce premise; equality of digests is not occurrence disclosure, real effect authentication or row-owner grant.'}
out=Path(__file__).resolve().parents[1]/'results/committed-redacted-event.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
