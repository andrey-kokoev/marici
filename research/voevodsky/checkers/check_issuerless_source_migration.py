"""Digest-correct migration is mathematically scoped, not owner-issued."""
from hashlib import sha256
from pathlib import Path
import json
rows1=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
rows2=rows1[:3]+(((0,1),2),)
def H(x):return sha256(repr(x).encode()).hexdigest()
proposal={'old_digest':H(rows1),'new_digest':H(rows2),'old_generation':1,'new_generation':2,'change':'y-upper 1 -> 2','issuer':None,'issuer_grant':None}
def assess(p,old,new):
 if p['old_digest']!=H(old) or p['new_digest']!=H(new) or p['new_generation']!=p['old_generation']+1:return 'STRUCTURAL_MISMATCH'
 if not p['issuer'] or not p['issuer_grant']:return 'LOCAL_DIGEST_SCOPE_ONLY_NO_ISSUER'
 return 'UNVERIFIED_GRANT_NEEDS_OWNER_CONTRACT'
assert assess(proposal,rows1,rows2)=='LOCAL_DIGEST_SCOPE_ONLY_NO_ISSUER'
assert assess(dict(proposal,new_digest=H(rows1)),rows1,rows2)=='STRUCTURAL_MISMATCH'
assert assess(dict(proposal,issuer='unverified-name',issuer_grant='unverified-token'),rows1,rows2)=='UNVERIFIED_GRANT_NEEDS_OWNER_CONTRACT'
report={'passed':True,'digest_correct_issuerless':'LOCAL_DIGEST_SCOPE_ONLY_NO_ISSUER','bad_digest':'STRUCTURAL_MISMATCH','arbitrary_claimed_issuer':'UNVERIFIED_GRANT_NEEDS_OWNER_CONTRACT','scope':'No real source was edited; no verified issuer, authorization or analytic correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/issuerless-source-migration.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
