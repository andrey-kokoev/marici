"""Prepare minimal local evidence payload while forbidding unbound owner send."""
from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parents[1]
source=root/'results/row-attestation-request.json';r=json.loads(source.read_text())
def digest(path):return sha256(path.read_bytes()).hexdigest()
evidence=('results/row-attestation-interface.json','results/bounded-source-directory-discovery.json','results/digest-only-row-packet.json')
payload={'schema':'research.unsent-row-owner-handoff.v1','source_id':r['manifest']['source_id'],'ordered_manifest_sha256':r['manifest_sha256'],'requested_actions':r['requested_capabilities'],'request_sha256':digest(source),'local_evidence':[{'path':p,'sha256':digest(root/p)} for p in evidence],'recipient':None,'source_event_id':None,'source_generation':None,'status':'LOCAL_PREPARED_UNSENDABLE'}
def send_gate(obj,channel=None):
 if obj['recipient'] is None or obj['source_event_id'] is None or obj['source_generation'] is None:raise ValueError('OWNER_ROUTE_UNASSIGNED')
 if channel is None or not channel.get('admitted_for_source'):raise ValueError('AUTHORIZED_CHANNEL_MISSING')
 return 'TEST_ONLY_SEND_FIELDS_MATCH_NOT_SENT'
assert r['requested_owner'] is None and r['owner_event_id'] is None
try:send_gate(payload)
except ValueError as err:assert str(err)=='OWNER_ROUTE_UNASSIGNED'
else:raise AssertionError('unknown owner accepted')
fiction=dict(payload,recipient='fictional',source_event_id='fictional-event',source_generation=1)
try:send_gate(fiction)
except ValueError as err:assert str(err)=='AUTHORIZED_CHANNEL_MISSING'
else:raise AssertionError('invented recipient accepted')
assert len(payload['local_evidence'])==3 and all(len(item['sha256'])==64 for item in payload['local_evidence'])
out=root/'results/unsent-owner-handoff-payload.json';out.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'passed':True,'status':payload['status'],'evidence_hashes':3,'send_gate':'OWNER_ROUTE_UNASSIGNED'}))
