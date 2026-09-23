"""Negative scope checks on an expressly UNVERIFIED authority-token fixture."""
from hashlib import sha256
from pathlib import Path
import json
H=lambda x:sha256(repr(x).encode()).hexdigest()
old=H(('rows',1));new=H(('rows',2))
claim={'issuer':'fictional-issuer','token':'UNVERIFIED-FIXTURE','manifest':old,'generation':1,'action':'validate-local-math'}
def scope(c,manifest,generation,action):
 if c['manifest']!=manifest or c['generation']!=generation:return 'ASSERTION_SOURCE_SCOPE_MISMATCH'
 if c['action']!=action:return 'ASSERTION_ACTION_SCOPE_MISMATCH'
 return 'SCOPE_MATCH_ONLY_NOT_AUTHENTICATED'
assert scope(claim,old,1,'validate-local-math')=='SCOPE_MATCH_ONLY_NOT_AUTHENTICATED'
assert scope(claim,new,2,'validate-local-math')=='ASSERTION_SOURCE_SCOPE_MISMATCH'
assert scope(claim,old,1,'publish-source')=='ASSERTION_ACTION_SCOPE_MISMATCH'
assert scope(claim,old,2,'validate-local-math')=='ASSERTION_SOURCE_SCOPE_MISMATCH'
report={'passed':True,'fixture_token':'explicitly unverified, never grants authority','old_source_and_action':'SCOPE_MATCH_ONLY_NOT_AUTHENTICATED','new_source_or_generation':'ASSERTION_SOURCE_SCOPE_MISMATCH','publish_action':'ASSERTION_ACTION_SCOPE_MISMATCH','scope':'Negative checks only; no owner recipient, signatures, observed issuer event or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/unverified-authority-scope-replay.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
