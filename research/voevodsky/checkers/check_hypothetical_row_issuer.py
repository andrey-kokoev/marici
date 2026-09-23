"""Conditional trusted-process row issuer model; NOT an actual authority service."""
from hashlib import sha256
from threading import RLock
from uuid import uuid4
from pathlib import Path
import json
ROWS=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def row_digest(rows):return sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
TRUSTED=row_digest(ROWS)
class HypotheticalOwner:
 def __init__(self):self.lock=RLock();self.generation=1;self.live={}
 def admit(self,source,event,rows,owner_verified):
  with self.lock:
   if not owner_verified:raise PermissionError('OWNER_REVIEW_REQUIRED')
   if source!='fixed-unit-square' or row_digest(rows)!=TRUSTED:raise ValueError('SOURCE_ROW_MISMATCH')
   token=uuid4().hex;self.live[token]=(source,event,self.generation,TRUSTED);return token
 def resolve(self,token,source,event,rows):
  with self.lock:
   if token not in self.live:raise PermissionError('NO_LIVE_CAPABILITY')
   s,e,g,h=self.live[token]
   if (s,e)!=(source,event):raise PermissionError('FOREIGN_SOURCE_EVENT')
   if g!=self.generation:raise PermissionError('STALE_GENERATION')
   if row_digest(rows)!=h:raise ValueError('SOURCE_ROW_MISMATCH')
   return h
 def revoke(self,token):
  with self.lock:self.live.pop(token,None)
owner=HypotheticalOwner();event='declared-local-event';token=owner.admit('fixed-unit-square',event,ROWS,True)
assert owner.resolve(token,'fixed-unit-square',event,ROWS)==TRUSTED
for s,e in (('other-source',event),('fixed-unit-square','other-event')):
 try:owner.resolve(token,s,e,ROWS)
 except PermissionError as ex:assert str(ex)=='FOREIGN_SOURCE_EVENT'
 else:raise AssertionError('foreign context admitted')
forged=list(ROWS);forged[1]=((1,0),2)
try:owner.resolve(token,'fixed-unit-square',event,forged)
except ValueError as ex:assert str(ex)=='SOURCE_ROW_MISMATCH'
else:raise AssertionError('mutated row admitted')
owner.generation+=1
try:owner.resolve(token,'fixed-unit-square',event,ROWS)
except PermissionError as ex:assert str(ex)=='STALE_GENERATION'
else:raise AssertionError('stale capability admitted')
fresh=owner.admit('fixed-unit-square',event,ROWS,True);owner.revoke(fresh)
try:owner.resolve(fresh,'fixed-unit-square',event,ROWS)
except PermissionError as ex:assert str(ex)=='NO_LIVE_CAPABILITY'
else:raise AssertionError('revoked capability admitted')
try:owner.admit('fixed-unit-square',event,ROWS,False)
except PermissionError:pass
else:raise AssertionError('self assertion admitted')
# The fixed row arithmetic is unchanged by capability revocation.
assert row_digest(ROWS)==TRUSTED
report={'passed':True,'conditional_model':'hypothetical in-process owner with trusted rows and explicit owner_verified gate','foreign_source_event_refused':True,'changed_row_refused':True,'stale_generation_refused':True,'revocation_refused':True,'self_asserted_owner_refused':True,'mathematical_anchor_survives_revocation':True,'noncertification':'owner_verified is a trusted input, not an externally authenticated review; no real source owner designated and no live grant minted.'}
out=Path(__file__).resolve().parents[1]/'results/hypothetical-row-issuer.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
