"""One fictional event digest binds its complete capability set and source scope."""
from hashlib import sha256
from pathlib import Path
import json
r=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
origin,use=r['requested_capabilities']
event={'schema':'synthetic-row-source-event.v1','issuer':'fictional-issuer','event_id':'fictional-event-42','generation':7,'manifest':r['manifest_sha256'],'actions':sorted((origin,use))}
def H(value):return sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
digest=H(event)
def verify(opening,committed):
 if opening is None:raise ValueError('EVENT_BYTES_UNDISCLOSED')
 if set(opening)!=set(event):raise ValueError('EVENT_PARTIALLY_DISCLOSED')
 if H(opening)!=committed:raise ValueError('EVENT_COMMITMENT_MISMATCH')
 return 'TEST_ONLY_EVENT_BYTES_BOUND_NOT_AUTHORIZED'
assert verify(event,digest)=='TEST_ONLY_EVENT_BYTES_BOUND_NOT_AUTHORIZED'
def refuse(opening,code):
 try:verify(opening,digest)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('event substitution accepted')
refuse(None,'EVENT_BYTES_UNDISCLOSED')
refuse({k:v for k,v in event.items() if k!='actions'},'EVENT_PARTIALLY_DISCLOSED')
refuse(dict(event,actions=[origin]),'EVENT_COMMITMENT_MISMATCH')
refuse(dict(event,generation=8),'EVENT_COMMITMENT_MISMATCH')
refuse(dict(event,manifest='other'),'EVENT_COMMITMENT_MISMATCH')
report={'passed':True,'full_synthetic_event':'TEST_ONLY_EVENT_BYTES_BOUND_NOT_AUTHORIZED','missing_or_partial':'refused','changed_actions_generation_or_manifest':'EVENT_COMMITMENT_MISMATCH','single_event_vs_separate_events':'one hash binds set but no issued signature or coexistence proof','actual_status':'owner/event still unassigned, no trusted signer or authorization','scope':'Digest integrity test only; SHA256 bytes do not certify publisher identity, revocation, actual event existence or analytic roles.'}
out=Path(__file__).resolve().parents[1]/'results/single-event-capability-binding.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
