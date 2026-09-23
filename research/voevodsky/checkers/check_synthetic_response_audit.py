"""Hash-linked hypothetical response log detects edits only with pinned head."""
from hashlib import sha256
from pathlib import Path
import json
p=json.loads((Path(__file__).resolve().parents[1]/'results/unsent-owner-handoff-payload.json').read_text())
def H(obj):return sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
events=[{'id':'fictional-prepare','kind':'prepared','request':p['request_sha256'],'parent':None},{'id':'fictional-receipt','kind':'receipt','request':p['request_sha256'],'parent':'fictional-prepare'},{'id':'fictional-deny','kind':'deny-proof-use','request':p['request_sha256'],'parent':'fictional-receipt'},{'id':'fictional-revision','kind':'revision-allow','request':p['request_sha256'],'parent':'fictional-deny'}]
def chain(entries):
 previous='GENESIS';prior_id=None
 for e in entries:
  if e['parent']!=prior_id:raise ValueError('AUDIT_PARENT_MISMATCH')
  previous=H({'previous':previous,'entry':e});prior_id=e['id']
 return previous
pinned=chain(events)
assert chain(events)==pinned
def validate(entries):
 if chain(entries)!=pinned:raise ValueError('AUDIT_PINNED_HEAD_MISMATCH')
 return 'TEST_ONLY_LOCAL_CHAIN_INTACT_NOT_AUTHENTICATED'
assert validate(events)=='TEST_ONLY_LOCAL_CHAIN_INTACT_NOT_AUTHENTICATED'
tampered=[dict(e) for e in events];tampered[2]['kind']='allow-proof-use'
try:validate(tampered)
except ValueError as err:assert str(err)=='AUDIT_PINNED_HEAD_MISMATCH'
else:raise AssertionError('denial overwrite unnoticed')
try:validate(events[:2]+events[3:])
except ValueError as err:assert str(err)=='AUDIT_PARENT_MISMATCH'
else:raise AssertionError('denial removal accepted')
assert chain(tampered)!=pinned # adversary able to rewrite both chain and local pin could conceal edit
report={'passed':True,'pinned_head':pinned,'denial_overwrite':'AUDIT_PINNED_HEAD_MISMATCH','denial_removal':'AUDIT_PARENT_MISMATCH','full_rewrite_plus_pin':'not detectable without independent external anchor','real_events':'NONE; no actual handoff/receipt/issuer response','scope':'Synthetic local log only, not a Narada ledger, trusted timestamp, signature or owner authority.'}
out=Path(__file__).resolve().parents[1]/'results/synthetic-response-audit.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'overwrite_refused':True,'removal_refused':True,'external_anchor_required':True}))
