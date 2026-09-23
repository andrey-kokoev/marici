"""Delivery/receipt are not issuer attestations; actual route stays unsent."""
from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parents[1]
payload=json.loads((root/'results/unsent-owner-handoff-payload.json').read_text())
def H(obj):return sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
request_digest=H(payload)
def step(state,action,route=None,receipt=None,verifier=None):
 if action=='send':
  if state!='prepared' or route is None or not route.get('admitted_for_source'):raise ValueError('AUTHORIZED_ROUTE_MISSING')
  return 'sent'
 if action=='deliver' and state=='sent':return 'delivered'
 if action=='receive' and state=='delivered':
  if receipt is None or receipt.get('payload_digest')!=request_digest:raise ValueError('RECEIPT_REQUEST_MISMATCH')
  return 'received_not_attested'
 if action=='attest' and state=='received_not_attested':
  if verifier is None:raise ValueError('OWNER_ATTESTATION_VERIFIER_MISSING')
  raise ValueError('REAL_TRUST_ROOT_NOT_AVAILABLE')
 if action=='reject' and state in ('sent','delivered','received_not_attested'):return 'rejected'
 raise ValueError('INVALID_STATE_TRANSITION')
try:step('prepared','send')
except ValueError as err:assert str(err)=='AUTHORIZED_ROUTE_MISSING'
else:raise AssertionError('actual payload sent')
route={'admitted_for_source':True,'fictional':True};s=step('prepared','send',route);s=step(s,'deliver');s=step(s,'receive',receipt={'payload_digest':request_digest})
assert s=='received_not_attested'
try:step(s,'attest')
except ValueError as err:assert str(err)=='OWNER_ATTESTATION_VERIFIER_MISSING'
else:raise AssertionError('receipt promoted to attestation')
assert step(s,'reject')=='rejected'
try:step('delivered','receive',receipt={'payload_digest':'different'})
except ValueError as err:assert str(err)=='RECEIPT_REQUEST_MISMATCH'
else:raise AssertionError('foreign receipt accepted')
report={'passed':True,'actual_prepared_to_send':'AUTHORIZED_ROUTE_MISSING','fictional_received':'received_not_attested','foreign_receipt':'RECEIPT_REQUEST_MISMATCH','receipt_to_attested':'OWNER_ATTESTATION_VERIFIER_MISSING','explicit_rejection':'rejected','scope':'Synthetic state machine only. No real owner message, delivery, receipt or attestation occurred; graph admission not truth.'}
out=root/'results/handoff-ack-states.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
