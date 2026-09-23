"""Synthetic freshness gate: same row hash and event label do not migrate grants."""
from pathlib import Path
import json
request=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
rowhash=request['manifest_sha256']
fixture={'issuer':'fictional-issuer-ONLY-TEST','event_id':'fictional-e-17','manifest_sha256':rowhash,'generation':1,'revocation_epoch':3}
current={'issuer':fixture['issuer'],'live_generation':2,'revocation_epoch':4,'event_generation':{'fictional-e-17':1},'revoked_generations':{1}}
def gate(claim,registry):
 if claim['manifest_sha256']!=rowhash:raise ValueError('MANIFEST_MISMATCH')
 if claim['issuer']!=registry['issuer']:raise ValueError('ISSUER_MISMATCH')
 if claim['generation']!=registry['live_generation']:raise ValueError('SUPERSEDED_GENERATION')
 if registry['event_generation'].get(claim['event_id'])!=claim['generation']:raise ValueError('EVENT_GENERATION_REPLAY')
 if claim['generation'] in registry['revoked_generations'] or claim['revocation_epoch']!=registry['revocation_epoch']:raise ValueError('REVOCATION_VIEW_STALE')
 return 'TEST_ONLY_FRESHNESS_FIELDS_MATCH; NOT_AUTHORIZED'
try:gate(fixture,current)
except ValueError as err:assert str(err)=='SUPERSEDED_GENERATION'
else:raise AssertionError('stale generation admitted')
rebound=dict(fixture,generation=2,revocation_epoch=4)
try:gate(rebound,current)
except ValueError as err:assert str(err)=='EVENT_GENERATION_REPLAY'
else:raise AssertionError('event replay admitted')
new_event=dict(rebound,event_id='fictional-e-18')
new_registry=dict(current,event_generation={**current['event_generation'],'fictional-e-18':2})
assert gate(new_event,new_registry)=='TEST_ONLY_FRESHNESS_FIELDS_MATCH; NOT_AUTHORIZED'
try:gate(dict(new_event,revocation_epoch=3),new_registry)
except ValueError as err:assert str(err)=='REVOCATION_VIEW_STALE'
else:raise AssertionError('stale revocation view admitted')
report={'passed':True,'old_signed_label_same_manifest':'SUPERSEDED_GENERATION','rewritten_generation_old_event':'EVENT_GENERATION_REPLAY','stale_revocation_snapshot':'REVOCATION_VIEW_STALE','fictional_new_generation_new_event':'TEST_ONLY_FRESHNESS_FIELDS_MATCH; NOT_AUTHORIZED','actual_request':'no owner/event; no trusted registry, key, signature or revocation channel','scope':'Synthetic freshness predicate, not signature validation or issuer designation; no real source publication.'}
out=Path(__file__).resolve().parents[1]/'results/hypothetical-attestation-generation-replay.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
