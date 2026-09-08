"""Exact face versus coordinate-face support certificates."""
import json
from pathlib import Path
from itertools import combinations

def closure(A,S):
    U={j for i in S for j,v in enumerate(A[i]) if v}
    return [i for i,a in enumerate(A) if all(not v or j in U for j,v in enumerate(a))]
A=[(1,0),(1,1)];ell=(1,-1)
values=[sum(x*y for x,y in zip(a,ell)) for a in A]
assert values==[1,0] # exposes the second ray as a cone face
assert closure(A,[1])==[0,1] # not a coordinate-induced face
p=json.loads(Path('research/nima/results/seven_point_fibers.json').read_text())
g=json.loads(Path('research/nima/results/seven_groebner.json').read_text())
assert p['status']=='passed' and g['status']=='complete'
T=[set(tuple(e) for e in t) for t in p['triangulations']]
Q=list(combinations(range(7),3));bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
B=[[int(all(e in t|bd for e in combinations(q,2))) for q in Q] for t in T]
records=[]
for j,q in enumerate(Q):
    S=[i for i,b in enumerate(B) if not b[j]]
    assert closure(B,S)==S
    w=[int(i in S) for i in range(42)]
    for a,b in g['basis']:
        assert all(w[i] for i,e in enumerate(a) if e)==all(w[i] for i,e in enumerate(b) if e)
    records.append({'zero_triangle':q,'support_size':len(S)})
result={'status':'passed','separating_control':{'map':'(x,y) -> (x,xy)','cone_face_support':[1],'forced_support':[0,1],'exposing_covector':[1,-1],'unliftable_point':[0,1]},'seven_point_coordinate_faces':records,'scope':'35 single-coordinate faces tested; not an exhaustive cone-face census. Support lift is distinct from coefficient lift.'}
Path('research/nima/results/face_lifting.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','unliftable_control':[0,1],'seven_point_faces_checked':len(records)}))
