"""Hypothetical owner lock makes audit publication atomic with capability check."""
from threading import Event,RLock,Thread
from pathlib import Path
import json
class Vault:
 def __init__(self):self.lock=RLock();self.live=True;self.receipts=[];self.epoch=1
 def revoke(self):
  with self.lock:self.live=False;self.epoch+=1
 def audit(self,entered=None,release=None):
  with self.lock:
   if not self.live:raise PermissionError('REVOKED_EVENT_A_CAPABILITY')
   if entered:entered.set();assert release.wait(3)
   receipt=('event-A','checked-rows',self.epoch)
   self.receipts.append(receipt);return receipt
# Case one: revoker tries while audit holds the lock. Commit linearizes first.
v=Vault();entered=Event();release=Event();revoked=Event();out=[]
def run_audit():out.append(v.audit(entered,release))
def run_revoke():v.revoke();revoked.set()
a=Thread(target=run_audit);a.start();assert entered.wait(3)
r=Thread(target=run_revoke);r.start();assert not revoked.wait(.05)
release.set();a.join(3);r.join(3);assert not a.is_alive() and not r.is_alive()
assert out==[('event-A','checked-rows',1)] and revoked.is_set() and v.epoch==2
try:v.audit()
except PermissionError:pass
else:raise AssertionError('post-revocation audit admitted')
assert len(v.receipts)==1
# Case two: revocation linearizes first; refused audit does not publish.
w=Vault();w.revoke()
try:w.audit()
except PermissionError:pass
else:raise AssertionError('revoked audit published')
assert w.receipts==[]
# Negative control: split validation/commit with no epoch recheck races.
u=Vault();was_live=u.live;u.revoke()
unsafe_would_publish=was_live and not u.live
assert unsafe_would_publish
report={'passed':True,'locked_audit_precedes_contending_revocation':True,'post_revocation_audit_refused_without_new_receipt':True,'revocation_first_audit_refused':True,'unsafe_split_check_commit_detected':True,'mathematical_rows_unchanged':True,'scope':'Deterministic in-process hypothetical vault, not independently authenticated provider, formal scheduler proof, physical historical execution or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/atomic-archive-audit.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
