"""Targeted Smith controls for the general face-lattice proof."""
import json
from pathlib import Path
from itertools import combinations
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
p=json.loads(Path('research/nima/results/seven_point_fibers.json').read_text());assert p['status']=='passed'
Q=list(combinations(range(7),3));bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
T=[set(tuple(e) for e in t) for t in p['triangulations']]
B=Matrix([[int(all(e in t|bd for e in combinations(q,2))) for q in Q] for t in T])
def factors(M):
    d=smith_normal_form(M,domain=ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]
records=[]
for j in range(35):
    ids=[i for i in range(42) if B[i,j]==0]
    U=[q for q in range(35) if any(B[i,q] for i in ids)]
    M=B.extract(ids,U);f=factors(M)
    assert all(v==1 for v in f)
    records.append({'zero_triangle_index':j,'support_size':len(ids),'rank':len(f),'smith_factors':f})
assert factors(Matrix([[2]]))==[2]
# In F_3, the character 2 -> 2 on 2Z cannot extend to Z:
assert all(pow(x,2,3)!=2 for x in (1,2))
r={'status':'passed','faces_checked':records,'nonsaturated_F3_control_rejected':True,'scope':'35 boundary Smith checks and an exact nonextension control; all-face theorem comes from integral interval decomposition and character extension, not this sample.'}
Path('research/nima/results/boundary_integral_lifting.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','faces_checked':len(records),'nonsaturated_control_rejected':True}))
