"""Replay actual fixed-family vault scope; do not mint a Farkas grant."""
import sys,json
from pathlib import Path
from hashlib import sha256
sys.path.insert(0,str(Path(__file__).resolve().parent))
from authority_aware_upgrade import ArchiveAuthority
v=ArchiveAuthority();event='fixed-family-retirement-e';context='fixed-two-history-context'
token=v._admit(event,context,'A') # private prototype admission, NOT public owner authentication
assert v._resolve(token,event,context)=='A'
row_digest=sha256(b'Farkas:unit-square:four-primitive-rows').hexdigest()
for e,c in ((event,row_digest),('Farkas-row-event',context)):
 try:v._resolve(token,e,c)
 except PermissionError as err:assert str(err)=='FOREIGN_RETIREMENT_ARCHIVE'
 else:raise AssertionError('foreign Farkas context authorized')
# Even a caller able to invoke the private admission with a Farkas-shaped
# string gets ONLY A/B history, not signed/authenticated primitive rows.
foreign=v._admit('Farkas-row-event',row_digest,'B')
assert v._resolve(foreign,'Farkas-row-event',row_digest)=='B'
assert v._resolve(foreign,'Farkas-row-event',row_digest)!=row_digest
v.revoke(token)
try:v._resolve(token,event,context)
except PermissionError as err:assert str(err)=='NO_ARCHIVE_AUTHORITY'
else:raise AssertionError('revoked reference accepted')
report={'passed':True,'existing_vault_binds':'process-local token to event/context and A/B original history only','foreign_event_context_refused':True,'post_revocation_use_refused':True,'farkas_row_attestation':False,'first_missing_constructor':'owner-controlled admission of independently verified primitive row statement + source identity + event, not private _admit(A/B) or caller-provided digest','scope':'Actual ArchiveAuthority replay, not an authorized Farkas grant; private _admit only exercised locally as negative scope control. Mathematical row proof remains valid after token revocation.'}
out=Path(__file__).resolve().parents[1]/'results/existing-archive-scope-for-farkas.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
