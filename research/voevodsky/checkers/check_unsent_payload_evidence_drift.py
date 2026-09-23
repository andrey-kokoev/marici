"""Detect changed referenced evidence without mutating the frozen payload."""
from hashlib import sha256
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
payload=json.loads((root/'results/unsent-owner-handoff-payload.json').read_text())
request=root/'results/row-attestation-request.json'
def H(b):return sha256(b).hexdigest()
def verify(request_bytes,evidence):
 if H(request_bytes)!=payload['request_sha256']:raise ValueError('FROZEN_REQUEST_DRIFT')
 for item in payload['local_evidence']:
  if item['path'] not in evidence or H(evidence[item['path']])!=item['sha256']:raise ValueError('EVIDENCE_DIGEST_DRIFT')
 return 'LOCAL_REFERENCES_CURRENT_STILL_UNSENDABLE'
current={item['path']:(root/item['path']).read_bytes() for item in payload['local_evidence']}
assert verify(request.read_bytes(),current)=='LOCAL_REFERENCES_CURRENT_STILL_UNSENDABLE'
changed=dict(current);first=payload['local_evidence'][0]['path'];changed[first]=changed[first]+b'\n'
try:verify(request.read_bytes(),changed)
except ValueError as err:assert str(err)=='EVIDENCE_DIGEST_DRIFT'
else:raise AssertionError('evidence edit unnoticed')
try:verify(request.read_bytes()+b'\n',current)
except ValueError as err:assert str(err)=='FROZEN_REQUEST_DRIFT'
else:raise AssertionError('request edit unnoticed')
assert payload['recipient'] is None and payload['status']=='LOCAL_PREPARED_UNSENDABLE'
report={'passed':True,'current_references':'LOCAL_REFERENCES_CURRENT_STILL_UNSENDABLE','simulated_one_byte_evidence_edit':'EVIDENCE_DIGEST_DRIFT','simulated_request_edit':'FROZEN_REQUEST_DRIFT','physical_files_mutated':False,'send_status':'OWNER_ROUTE_UNASSIGNED','scope':'Local file integrity at check time, not authenticity, authorized route, immutable storage, atomic file snapshot or actual owner communication.'}
out=root/'results/unsent-payload-evidence-drift.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
