"""Row support narrows math rechecks, never preserves old source grant."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
new=old[:3]+(((0,1),2),)
packets={'P':((Q(1),Q(2),Q(0),Q(0)),Q(0)),'Q':((Q(0),Q(1),Q(1),Q(1)),Q(0)),'single':((Q(0),Q(1),Q(0),Q(0)),Q(1))}
def check(rows,packet):
 m,c=packet
 return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))+c
old_values={name:check(old,packet) for name,packet in packets.items()}
new_values={name:check(new,packet) for name,packet in packets.items()}
assert all(x==((Q(1),Q(0)),Q(2)) for x in old_values.values())
assert new_values['P']==new_values['single']==((Q(1),Q(0)),Q(2))
assert new_values['Q']==((Q(1),Q(0)),Q(3))
index={i:sorted(name for name,(m,_) in packets.items() if m[i]) for i in range(4)}
assert index[3]==['Q']
p,q=packets['P'][0],packets['Q'][0];delta=tuple(q[i]-p[i] for i in range(4))
assert check(new,(delta,Q(0)))==((Q(0),Q(0)),Q(1))
def H(rows):return sha256(repr(rows).encode()).hexdigest()
assert H(old)!=H(new)
report={'passed':True,'edited_row':'y-upper bound 1 -> 2','support_index_changed_row':['Q'],'P_and_single':'same exact x<=2 packet equations locally','Q':'now bound3; no nonnegative surplus can make its fixed multiplier prove exact bound2','old_signed_comparison':'zero normal, bound difference now 1; invalid exact comparison','full_source_manifest':'changed; every old-manifest publication claim stale even for unaffected packets','scope':'Incremental LOCAL mathematics, not publication authorization, no source issuer or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/incremental-square-bound-edit.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
