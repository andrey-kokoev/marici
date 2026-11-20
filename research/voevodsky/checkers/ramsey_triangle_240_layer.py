"""Compare the G-sets, including stabilizer class rather than just orbit size. G actions ordered as in the DFA symmetry audit."""
from itertools import permutations,product
from collections import Counter
import ramsey_triangle_memory_symmetry as m
import json
A=list(product(range(3),range(8)));P={(a,b) for a in A for b in A if a[0]==b[0] or a[1]==b[1]};gs=[]
for p in permutations(range(3)):
 for c in (0,7):gs.append({(j,v):(p[j],c^sum(1<<p[k] for k in range(3) if v>>k&1)) for j,v in A})
def fingerprint(S,act):
 left=set(S);cnt=Counter()
 while left:
    z=next(iter(left));o={act(i,z) for i in range(12)};left-=o;stab=min(tuple(i for i in range(12) if act(i,v)==v) for v in o);cnt[str(stab)]+=1
 return dict(sorted(cnt.items()))
H={v for v,d in m.dist.items() if d==3};h=fingerprint(H,lambda i,v:m.G[i][v]);p=fingerprint(P,lambda i,v:tuple(gs[i][z] for z in v));out=dict(depth_three=h,shared_coordinate_pairs=p,equivariant_bijection_exists=h==p);print(out);(m.D/'ramsey_triangle_240_layer.json').write_text(json.dumps(out,indent=2)+'\n')
