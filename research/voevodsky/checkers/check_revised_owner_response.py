"""Synthetic revised grant needs explicit predecessor, not merely later graph time."""
from pathlib import Path
import json
p=json.loads((Path(__file__).resolve().parents[1]/'results/unsent-owner-handoff-payload.json').read_text())
use='authorize-future-source-rooted-proof-use'
prior={'event':'fictional-denial-7','decision':'decline','action':use,'request':p['request_sha256'],'manifest':p['ordered_manifest_sha256'],'generation':7,'epoch':8}
later={'event':'fictional-revision-8','supersedes':prior['event'],'decision':'allow','action':use,'request':prior['request'],'manifest':prior['manifest'],'generation':7,'epoch':9,'graph_order':101}
registry={'live_epoch':9,'live_generation':7,'revoked':False}
def assess(old,new,state):
 if new.get('supersedes')!=old['event']:raise ValueError('MISSING_EXPLICIT_REVISION_EDGE')
 if new['request']!=old['request'] or new['manifest']!=old['manifest'] or new['action']!=old['action']:raise ValueError('REVISION_SCOPE_MISMATCH')
 if new['generation']!=old['generation'] or new['generation']!=state['live_generation'] or new['epoch']!=state['live_epoch']:raise ValueError('REVISION_SNAPSHOT_STALE')
 if state['revoked']:raise ValueError('REVISION_REVOKED')
 return 'TEST_ONLY_REVISION_CHAIN_NOT_AUTHORIZED'
assert assess(prior,later,registry)=='TEST_ONLY_REVISION_CHAIN_NOT_AUTHORIZED'
def reject(mod,state,code):
 try:assess(prior,dict(later,**mod),state)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('revision escape')
reject({'supersedes':None},registry,'MISSING_EXPLICIT_REVISION_EDGE')
reject({'request':'other'},registry,'REVISION_SCOPE_MISMATCH')
reject({},dict(registry,live_epoch=10),'REVISION_SNAPSHOT_STALE')
reject({},dict(registry,revoked=True),'REVISION_REVOKED')
assert prior['decision']=='decline' and later['decision']=='allow'
report={'passed':True,'later_graph_order_alone':'MISSING_EXPLICIT_REVISION_EDGE','explicit_chain':'TEST_ONLY_REVISION_CHAIN_NOT_AUTHORIZED','scope_epoch_revocation':'separately checked','prior_denial_retained':True,'actual_state':'No real owner, denial, response, signed revision or authorization','scope':'Fictional event relation, not source-owner signature verification, trust root or analytic correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/revised-owner-response.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
