"""Same path equations can survive a changed source without authority transport."""
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
# Coupled bound shift retains both endpoint/intermediate bound equations:
# new source is singleton (x,y)=(2,1), not the old unit square.
new=(((-1,0),-2),((1,0),2),((0,-1),-1),((0,1),1))
p=(1,2,0,0);q=(0,1,1,1);k=tuple(q[i]-p[i] for i in range(4))
def digest(rows):return sha256(repr(rows).encode()).hexdigest()
def image(v,rows):return tuple(sum(rows[i][0][j]*v[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*v[i] for i in range(4))
assert digest(old)!=digest(new)
for rows in (old,new):
 assert image(p,rows)==image(q,rows)==((1,0),2)
 assert image(k,rows)==((0,0),0)
assert old[0][1]!=new[0][1] and old[1][1]!=new[1][1]
old_root=digest(old);new_root=digest(new)
def use(record_root,current_root,mathematically_reverified,owner_admitted):
 if record_root!=current_root:return 'REQUIRES_EXPLICIT_SOURCE_REBIND'
 if not mathematically_reverified:return 'REQUIRES_MATHEMATICAL_RECHECK'
 if not owner_admitted:return 'NO_LIVE_SOURCE_AUTHORITY'
 return 'CONDITIONALLY_AUTHORIZED'
assert use(old_root,new_root,True,False)=='REQUIRES_EXPLICIT_SOURCE_REBIND'
assert use(new_root,new_root,True,False)=='NO_LIVE_SOURCE_AUTHORITY'
report={'passed':True,'source_digest_changed':True,'old_and_new_path_packet_equations_valid':True,'old_and_new_syzygy_equations_valid':True,'source_sets_differ':'old [0,1]^2; new singleton {(2,1)}','old_root_new_source_refused':'REQUIRES_EXPLICIT_SOURCE_REBIND','rebound_math_without_owner_refused':'NO_LIVE_SOURCE_AUTHORITY','scope':'Hypothetical coupled primitive-bound edit. Mathematical revalidation is not semantic equality of source sets or owner-authorized migration.'}
out=Path(__file__).resolve().parents[1]/'results/path-valid-across-source-identity-change.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
