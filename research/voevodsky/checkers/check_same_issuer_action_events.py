"""Same issuer/manifest does not automatically union event capabilities."""
from pathlib import Path
import json
r=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text());origin,use=r['requested_capabilities']
issuer='fictional-issuer';manifest=r['manifest_sha256']
events={'e-origin':{'issuer':issuer,'manifest':manifest,'action':origin,'effect':'allow','generation':7},'e-use':{'issuer':issuer,'manifest':manifest,'action':use,'effect':'allow','generation':7},'e-deny-use':{'issuer':issuer,'manifest':manifest,'action':use,'effect':'deny','generation':7}}
def evaluate(ids,policy,epoch):
 if policy is None or epoch!=policy['epoch']:return 'ATOMIC_POLICY_UNAVAILABLE'
 if not set(ids)<=policy['live_events']:return 'EVENT_NOT_LIVE'
 selected=[events[i] for i in ids]
 if len({(e['issuer'],e['manifest'],e['generation']) for e in selected})!=1:return 'SOURCE_BINDING_CONFLICT'
 if any(e['effect']=='deny' and any(f['effect']=='allow' and f['action']==e['action'] for f in selected) for e in selected):return 'CONFLICTING_ACTION_POLICY'
 if not set(ids)<=policy['coexistent_events']:return 'COEXISTENCE_NOT_ADMITTED'
 return ('TEST_ONLY_ACTIONS_NOT_AUTHORIZED',tuple(sorted(e['action'] for e in selected if e['effect']=='allow')))
policy={'epoch':9,'live_events':set(events),'coexistent_events':{'e-origin','e-use'}}
assert evaluate(('e-origin','e-use'),None,9)=='ATOMIC_POLICY_UNAVAILABLE'
assert evaluate(('e-origin','e-use'),policy,9)==('TEST_ONLY_ACTIONS_NOT_AUTHORIZED',tuple(sorted((origin,use))))
assert evaluate(('e-origin','e-deny-use','e-use'),dict(policy,coexistent_events=set(events)),9)=='CONFLICTING_ACTION_POLICY'
assert evaluate(('e-origin','e-use'),dict(policy,live_events={'e-origin'}),9)=='EVENT_NOT_LIVE'
assert evaluate(('e-origin','e-use'),policy,8)=='ATOMIC_POLICY_UNAVAILABLE'
assert evaluate(('e-origin','e-use'),dict(policy,coexistent_events={'e-origin'}),9)=='COEXISTENCE_NOT_ADMITTED'
report={'passed':True,'same_issuer_manifest_without_policy':'ATOMIC_POLICY_UNAVAILABLE','explicit_fictional_coexistence':'TEST_ONLY_ACTIONS_NOT_AUTHORIZED','allow_deny_same_action':'CONFLICTING_ACTION_POLICY','revoked_use_event':'EVENT_NOT_LIVE','stale_epoch':'ATOMIC_POLICY_UNAVAILABLE','scope':'Synthetic event policy fixtures; no signed events, trusted registry or actual owner grant.'}
out=Path(__file__).resolve().parents[1]/'results/same-issuer-action-events.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
