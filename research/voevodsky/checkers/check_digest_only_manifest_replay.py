"""Content-addressed old-row reference needs available, verified bytes."""
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
alternative=(((-1,0),-2),((1,0),2),((0,-1),-1),((0,1),1))
encode=lambda rows:json.dumps(rows,separators=(',',':')).encode()
hash_rows=lambda rows:sha256(encode(rows)).hexdigest()
old_ref=hash_rows(old);alt_ref=hash_rows(alternative);assert old_ref!=alt_ref
P=(1,2,0,0);Q=(0,1,1,1)
def image(m,rows):return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))
def replay(ref,store):
 if ref not in store:return 'UNAVAILABLE_OLD_MANIFEST'
 rows=store[ref]
 if hash_rows(rows)!=ref:return 'REFERENCE_DIGEST_MISMATCH'
 k=tuple(Q[i]-P[i] for i in range(4))
 if image(P,rows)!=((1,0),2) or image(Q,rows)!=((1,0),2) or image(k,rows)!=((0,0),0):return 'INVALID_ARCHIVED_PATH'
 return 'INDEPENDENT_MATH_REPLAY'
assert replay(old_ref,{old_ref:old})=='INDEPENDENT_MATH_REPLAY'
assert replay(old_ref,{})=='UNAVAILABLE_OLD_MANIFEST'
assert replay(old_ref,{old_ref:alternative})=='REFERENCE_DIGEST_MISMATCH'
assert replay(alt_ref,{alt_ref:alternative})=='INDEPENDENT_MATH_REPLAY'
# Two distinct row manifests have exactly the same selected P/Q math, so
# these proof vectors cannot recover a lost old source manifest.
assert all(image(v,old)==image(v,alternative) for v in (P,Q))
report={'passed':True,'digest_only_offline_replay':'UNAVAILABLE_OLD_MANIFEST','available_matching_content_replays':True,'substituted_content_refused':True,'distinct_manifests_same_selected_proof_images':True,'retention_law':'keep row bytes or a verified AVAILABLE content-addressed source; digest alone does not reproduce old source','scope':'Finite mathematical replay only. Availability/digest do not authenticate owner or yield live grant, and no universal minimum byte cost inferred.'}
out=Path(__file__).resolve().parents[1]/'results/digest-only-manifest-replay.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
