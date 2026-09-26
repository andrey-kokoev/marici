"""Transport Farkas weights with an explicit row permutation, not old slot identities."""
from hashlib import sha256
from pathlib import Path
import json
rows=(((-1,0),0,'left'),((1,0),1,'right'),((0,-1),0,'bottom'),((0,1),1,'top'))
weights=(0,1,0,0);perm=(2,0,3,1)
new_rows=tuple(rows[i] for i in perm);new_weights=tuple(weights[i] for i in perm)
def implied(rs,ms):return tuple(sum(rs[i][0][j]*ms[i] for i in range(4)) for j in (0,1)),sum(rs[i][1]*ms[i] for i in range(4))
def H(x):return sha256(repr(x).encode()).hexdigest()
assert implied(rows,weights)==implied(new_rows,new_weights)==((1,0),1)
assert H(rows)!=H(new_rows) and H((rows,weights))!=H((new_rows,new_weights))
assert implied(new_rows,weights)!=implied(rows,weights)
witness={'old_rows_digest':H(rows),'new_rows_digest':H(new_rows),'permutation':perm,'old_weights':weights,'new_weights':new_weights,'authority':'NONE'}
assert all(new_rows[j]==rows[i] and new_weights[j]==weights[i] for j,i in enumerate(perm))
report={'passed':True,'transported_math':'x<=1 preserved','naive_untransported_weights':'different implied normal/bound','ordered_source_and_packet_digests':'different','witness':'explicit permutation of old slot indices; no source authority','scope':'Synthetic reorder only, no owner publication or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/row-permutation-transport.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
