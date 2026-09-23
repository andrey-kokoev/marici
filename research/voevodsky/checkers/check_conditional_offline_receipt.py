"""Conditional offline audit receipt; trusted verifier key is an assumption."""
import hashlib,hmac,json
from pathlib import Path
KEY=b'hypothetical-owner-secret-not-an-actual-source-grant'
canonical=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
row_digest=hashlib.sha256(b'fixed-four-primitive-rows').hexdigest()
body={'source':'fixed-unit-square','event':'event-A','issuer':'hypothetical-owner-A','row_digest':row_digest,'epoch':1,'sequence':7,'kind':'audit-committed'}
mac=lambda b:hmac.new(KEY,canonical(b),hashlib.sha256).hexdigest()
receipt={'body':body,'mac':mac(body),'log_inclusion':{'sequence':7,'event':'event-A','committed':True}}
def verify(r,expected_event,trust_key=None):
 b=r.get('body',{})
 if not all(k in b for k in ('source','event','issuer','row_digest','epoch','sequence','kind')):return 'INCOMPLETE_TYPED_RECEIPT'
 if b['event']!=expected_event:return 'FOREIGN_EVENT'
 if trust_key is None:return 'NO_INDEPENDENT_ISSUER_TRUST_ANCHOR'
 claimed=r.get('mac')
 if not isinstance(claimed,str) or not hmac.compare_digest(claimed,hmac.new(trust_key,canonical(b),hashlib.sha256).hexdigest()):return 'INVALID_ISSUER_AUTHENTICATOR'
 log=r.get('log_inclusion',{})
 if (log.get('sequence'),log.get('event'),log.get('committed'))!=(b['sequence'],b['event'],True):return 'MISSING_COMMIT_EVIDENCE'
 return 'CONDITIONALLY_VERIFIED_PAST_AUDIT'
assert verify(receipt,'event-A')=='NO_INDEPENDENT_ISSUER_TRUST_ANCHOR'
assert verify(receipt,'event-A',KEY)=='CONDITIONALLY_VERIFIED_PAST_AUDIT'
assert verify({'body':body,'mac':hashlib.sha256(canonical(body)).hexdigest(),'log_inclusion':receipt['log_inclusion']},'event-A',KEY)=='INVALID_ISSUER_AUTHENTICATOR'
assert verify({**receipt,'body':{**body,'issuer':'self-asserted'}},'event-A',KEY)=='INVALID_ISSUER_AUTHENTICATOR'
assert verify(receipt,'event-B',KEY)=='FOREIGN_EVENT'
assert verify({**receipt,'log_inclusion':{}},'event-A',KEY)=='MISSING_COMMIT_EVIDENCE'
# Past audit remains a past statement after a prospective revocation; it
# never becomes current capability. KEY is local/trusted for this toy only.
report={'passed':True,'required_fields':list(body),'untrusted_hash_only_refused':True,'self_asserted_issuer_refused':True,'foreign_event_refused':True,'missing_commit_refused':True,'conditional_trusted_key_result':'CONDITIONALLY_VERIFIED_PAST_AUDIT','noncertification':'HMAC secret is embedded toy trust assumption, not public-key independent authentication, real owner issuance, append-only log verification or live execution grant.'}
out=Path(__file__).resolve().parents[1]/'results/conditional-offline-receipt.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
