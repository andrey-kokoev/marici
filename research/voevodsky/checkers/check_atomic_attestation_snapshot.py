"""Synthetic atomic epoch binds issuer grant, event and revocation at use time."""
from pathlib import Path
import json
request=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
manifest=request['manifest_sha256']
state={'epoch':7,'generation':2,'revoked':False,'grant':'fictional-grant','event':'fictional-event','manifest':manifest}
def observe(s):return dict(s)
def commit(observation,current):
 if observation['epoch']!=current['epoch']:raise ValueError('ATOMIC_SNAPSHOT_STALE')
 if observation!=current:raise ValueError('INCONSISTENT_SAME_EPOCH')
 if observation['revoked'] or not observation['grant']:raise ValueError('GRANT_REVOKED')
 if observation['manifest']!=manifest or not observation['event']:raise ValueError('EVENT_MANIFEST_MISMATCH')
 return 'TEST_ONLY_SINGLE_EPOCH_FIELDS_MATCH_NOT_AUTHORIZED'
snapshot=observe(state)
assert commit(snapshot,state)=='TEST_ONLY_SINGLE_EPOCH_FIELDS_MATCH_NOT_AUTHORIZED'
revoked=dict(state,epoch=8,revoked=True,grant=None)
try:commit(snapshot,revoked)
except ValueError as err:assert str(err)=='ATOMIC_SNAPSHOT_STALE'
else:raise AssertionError('time-of-use drift accepted')
try:commit(observe(revoked),revoked)
except ValueError as err:assert str(err)=='GRANT_REVOKED'
else:raise AssertionError('revoked grant admitted')
try:commit(snapshot,dict(state,revoked=True))
except ValueError as err:assert str(err)=='INCONSISTENT_SAME_EPOCH'
else:raise AssertionError('same epoch mutation accepted')
report={'passed':True,'lookup_epoch':7,'use_after_revocation_epoch':8,'stale_lookup':'ATOMIC_SNAPSHOT_STALE','revoked_atomic_snapshot':'GRANT_REVOKED','same_epoch_changed_fields':'INCONSISTENT_SAME_EPOCH','untampered_fixture':'TEST_ONLY_SINGLE_EPOCH_FIELDS_MATCH_NOT_AUTHORIZED','scope':'Synthetic compare-at-use atomic epoch model; no actual issuer, signature, lock/transaction implementation, or publisher authority.'}
out=Path(__file__).resolve().parents[1]/'results/atomic-attestation-snapshot.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
