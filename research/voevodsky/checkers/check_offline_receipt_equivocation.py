"""Two individually authenticated toy receipts can equivocate without log consistency."""
import hashlib,hmac,json
from pathlib import Path
key=b'conditional-local-issuer-secret'
encode=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
base={'source':'unit-square','issuer':'toy-A','event':'event-A','epoch':1,'sequence':7,'operation':'audit-committed'}
def sign(row_digest):
 body={**base,'row_digest':row_digest}
 return {'body':body,'mac':hmac.new(key,encode(body),hashlib.sha256).hexdigest()}
r1=sign('digest-of-row-source-one');r2=sign('digest-of-row-source-two')
def individual(r):return hmac.compare_digest(r['mac'],hmac.new(key,encode(r['body']),hashlib.sha256).hexdigest())
assert individual(r1) and individual(r2)
def reconcile(receipts):
 slots={}
 for r in receipts:
  if not individual(r):return 'BAD_AUTHENTICATOR'
  b=r['body'];slot=(b['issuer'],b['source'],b['event'],b['epoch'],b['sequence'])
  if slot in slots and slots[slot]!=b['row_digest']:return 'EQUIVOCATION_SAME_SLOT'
  slots[slot]=b['row_digest']
 return 'LOCALLY_NONCONFLICTING_ONLY'
assert reconcile([r1])=='LOCALLY_NONCONFLICTING_ONLY'
assert reconcile([r2])=='LOCALLY_NONCONFLICTING_ONLY'
assert reconcile([r1,r2])=='EQUIVOCATION_SAME_SLOT'
# One process-local slot map prevents a conflicting second commit, but an
# offline verifier with only one receipt cannot establish global uniqueness.
class LocalLog:
 def __init__(self):self.slots={}
 def commit(self,r):
  b=r['body'];slot=(b['issuer'],b['event'],b['epoch'],b['sequence'])
  if slot in self.slots and self.slots[slot]!=b['row_digest']:raise ValueError('FORK_ATTEMPT')
  self.slots[slot]=b['row_digest']
log=LocalLog();log.commit(r1)
try:log.commit(r2)
except ValueError:pass
else:raise AssertionError('local log permitted equivocation')
report={'passed':True,'individually_toy_authenticated_receipts':2,'joint_verdict':'EQUIVOCATION_SAME_SLOT','local_single_log_fork_refused':True,'one_offline_receipt_cannot_establish_uniqueness':True,'missing_external_obligation':'independently trusted append-only log root with cross-client consistency/anti-fork evidence','scope':'Toy shared-secret issuer and local log; no real signature, globally consistent log, physical event truth or source-owner authority.'}
out=Path(__file__).resolve().parents[1]/'results/offline-receipt-equivocation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
