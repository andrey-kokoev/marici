"""Archive availability affects fresh replay, not an already recorded verdict."""
from hashlib import sha256
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
wrong=(((-1,0),0),((1,0),2),((0,-1),0),((0,1),1))
encode=lambda r:json.dumps(r,separators=(',',':')).encode()
digest=lambda r:sha256(encode(r)).hexdigest()
ref=digest(rows);P=(1,2,0,0);Q=(0,1,1,1)
def image(p,r):return tuple(sum(r[i][0][j]*p[i] for i in range(4)) for j in (0,1)),sum(r[i][1]*p[i] for i in range(4))
def fresh(store):
 if ref not in store:return 'ARCHIVE_UNAVAILABLE'
 r=store[ref]
 if digest(r)!=ref:return 'ARCHIVE_INTEGRITY_FAILURE'
 k=tuple(Q[i]-P[i] for i in range(4))
 if image(P,r)!=((1,0),2) or image(Q,r)!=((1,0),2) or image(k,r)!=((0,0),0):return 'MATH_INVALID'
 return 'FRESH_MATH_VERIFIED'
store={ref:rows};first=fresh(store);assert first=='FRESH_MATH_VERIFIED'
receipt={'first_verdict':first,'source_digest':ref,'verifier':'local-exact-farkas-replay','execution_authority':False}
del store[ref]
assert fresh(store)=='ARCHIVE_UNAVAILABLE'
assert receipt['first_verdict']=='FRESH_MATH_VERIFIED' # historical assertion retained
store[ref]=wrong;assert fresh(store)=='ARCHIVE_INTEGRITY_FAILURE'
store[ref]=rows;assert fresh(store)=='FRESH_MATH_VERIFIED'
report={'passed':True,'first_replay':first,'after_removal':'ARCHIVE_UNAVAILABLE','retained_receipt':'historical local mathematical verdict only','substituted_rows':'ARCHIVE_INTEGRITY_FAILURE','restored_matching_rows':'FRESH_MATH_VERIFIED','scope':'Process-local simulated availability, not independently authenticated receipt, remote archival durability, owner authorization or measured memory.'}
out=Path(__file__).resolve().parents[1]/'results/archive-loss-after-replay.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
