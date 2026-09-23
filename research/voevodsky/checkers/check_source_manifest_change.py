"""Upper-bound migration invalidates some leaves but not bracket syntax."""
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
new=(((-1,0),0),((1,0),2),((0,-1),0),((0,1),1))
hash_rows=lambda r:sha256(json.dumps(r,separators=(',',':')).encode()).hexdigest()
assert hash_rows(old)!=hash_rows(new)
leaves={'a':((1,2,0,0),(1,0),2),'b':((0,0,1,2),(0,1),2),
        'c':((0,1,0,0),(1,0),1),'d':((0,0,0,1),(0,1),1)}
def valid(proof,rows):
 m,target,bound=proof
 return min(m)>=0 and tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in range(2))==target and sum(rows[i][1]*m[i] for i in range(4))==bound
assert all(valid(p,old) for p in leaves.values())
retained={k:valid(p,new) for k,p in leaves.items()}
assert retained=={'a':False,'b':True,'c':False,'d':True}
assert (2,0)[0]>1 # c: x<=1 is no longer true on widened square
assert valid(((0,1,0,0),(1,0),2),new) # a can be re-proved, not replayed as old proof
old_composite=(tuple(sum(p[0][i] for p in leaves.values()) for i in range(4)),(2,2),6)
assert old_composite[0]==(1,3,1,3) and valid(old_composite,old) and not valid(old_composite,new)
assert valid(((0,2,0,2),(2,2),6),new)
# Formal bracketing rotation depends only on ordered labels, not bounds.
start=((('a','b'),'c'),'d');mid=(('a','b'),('c','d'));end=('a',('b',('c','d')))
rotate=lambda t:(t[0][0],(t[0][1],t[1]))
assert rotate(start)==mid and rotate(mid)==end
report={'passed':True,'manifest_digest_changed':True,'archived_leaf_valid_after_change':retained,'old_composite_invalid':True,'new_composite_exists_with_different_multipliers':True,'c_target_x_leq_1_false_on_new_source':True,'formal_rotation_path_remains_well_formed':True,'old_source_rooted_path_not_valid_as_new_proof':True,'scope':'Hypothetical mathematical source change [0,1]^2 -> [0,2]x[0,1]. No owner admission, live revocation or analytic role map asserted.'}
out=Path(__file__).resolve().parents[1]/'results/source-manifest-change.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
