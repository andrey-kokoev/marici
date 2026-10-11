"""Exact source-support comparison and open-fan extension control.
No new electron/proton phase assignment is assumed.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from collections import defaultdict
from fractions import Fraction as F
import json
from check_spinor_matter_link_adapter import decode
from check_electron_tetrahedral_spinor import D, gmm, trace, ma, sm, ident

BASE=Path(__file__).resolve().parents[1]


def oriented(vertices):
    sign=(-1)**sum(vertices[i]>vertices[j] for i in range(len(vertices)) for j in range(i+1,len(vertices)))
    return tuple(sorted(vertices)),sign


def chain(terms):
    out=defaultdict(int)
    for verts,coeff in terms:
        key,sign=oriented(verts);out[key]+=coeff*sign
    return {key:value for key,value in out.items() if value}


def boundary(c):
    return chain([(v[:i]+v[i+1:],coeff*(-1)**i) for v,coeff in c.items() for i in range(len(v))])


def add(a,b):return chain(list(a.items())+list(b.items()))


def subtract(a,b):return add(a,{v:-x for v,x in b.items()})


def main():
    paths={name:BASE/'results'/file for name,file in [('electron','electron_tetrahedral_spinor_store.json'),('proton','proton_merkle_store.json')]}
    raw={name:p.read_bytes() for name,p in paths.items()}
    electron=json.loads(raw['electron']);proton=json.loads(raw['proton'])
    objects=proton['objects'];geo=objects[objects[proton['root']]['geometry']]['payload']
    triangles=geo['triangles_and_transports']
    assert len(triangles)==12
    tetra=chain([(('A','B','C','D'),1)])
    faces=boundary(tetra)
    assert boundary(faces)=={}
    # The geometrical source orientation in this coordinate realization is
    # opposite the lexical tetrahedron boundary orientation; compare intact.
    actual=chain([(tuple(row['triangle']),1) for row in triangles])
    assert boundary(actual)=={}
    subdivided={}
    for face,sign in faces.items():
        a,b,c=face;center='F_'+''.join(face)
        split=chain([((center,a,b),sign),((center,b,c),sign),((center,c,a),sign)])
        assert boundary(split)==boundary({face:sign})
        subdivided=add(subdivided,split)
    assert actual=={v:-x for v,x in subdivided.items()}
    assert {''.join(sorted(row['triangle'][0][2:])) for row in triangles}=={''.join(f) for f in faces}
    # Recover the electron's normal-to-face correspondence from exact source
    # coordinates; n points away from the missing vertex.
    vertices={'A':(1,1,1),'B':(1,-1,-1),'C':(-1,1,-1),'D':(-1,-1,1)}
    matched=[]
    for normal in electron['normals']:
        n=tuple(D(F(a),F(b)) for a,b in normal)
        missing=[label for label,v in vertices.items() if n==tuple(D(0,F(-x,3)) for x in v)]
        assert len(missing)==1
        matched.append(tuple(sorted(set(vertices)-set(missing))))
    assert set(matched)==set(faces)
    # Open fan is a proper source restriction, not the stored whole electron.
    fan={f:x for f,x in faces.items() if 'A' in f}
    cap={f:x for f,x in faces.items() if 'A' not in f}
    assert len(fan)==3 and len(cap)==1 and len(boundary(fan))==3
    assert boundary(fan)=={v:-x for v,x in boundary(cap).items()}
    assert add(fan,cap)==faces
    # Coefficient checks: tetrahedral local effects cannot all be the same
    # scalar view and therefore subdivision alone is not an encoder map.
    ps=[tuple(tuple(decode(z) for z in row) for row in p) for p in electron['face_projectors']]
    assert len(ps)==4
    for p in ps:assert gmm(p,p)==p and trace(p)==(D(1),D(0))
    for i,j in combinations(range(4),2):assert trace(gmm(ps[i],ps[j]))==(D(F(1,3)),D(0))
    total=ma(ma(ps[0],ps[1]),ma(ps[2],ps[3]))
    assert total==sm(2,ident(2))
    # With the original encoder normalization, removing one face leaves
    # Gram I-P_cap/2, eigenvalues 1 and 1/2: open does not mean rank one.
    cap_index=matched.index(next(iter(cap)))
    fan_gram=ma(ident(2),sm(F(-1,2),ps[cap_index]))
    assert trace(fan_gram)==(D(F(3,2)),D(0))
    assert ma(gmm(fan_gram,fan_gram),ma(sm(F(-3,2),fan_gram),sm(F(1,2),ident(2))))==sm(0,ident(2))
    assert geo['assembled_identity']['rank']==1
    report={'verification_passed':True,'source_sha256':{n:sha256(r).hexdigest() for n,r in raw.items()},
        'stored_electron_support':'All four faces of tetrahedral ABCD, not the three-face open fan; this is the spinor source, not the later pentachoron display.',
        'stored_proton_support':'All four faces, each refined into three centroid-edge triangles.',
        'source_face_counts':{'electron':4,'proton':12},
        'boundary_chains':{'electron':0,'proton':0},
        'geometric_relation':'Facewise subdivision with boundary preserved; globally equal support up to orientation convention, not open-to-closed attachment.',
        'open_fan_control':{'faces':3,'boundary_edges':3,'cap_faces':1,'volume_filler':'A separate 3-simplex; closure of the 2-chain alone is not a volume constructor.'},
        'local_coefficient_overlap':'Tr(P_i P_j)=1/3 for every i!=j',
        'restricted_open_fan_encoder_gram_eigenvalues':['1','1/2'],
        'open_fan_coefficient_rank':2,
        'coherent_ranks':{'electron':2,'proton':1},
        'phase_assignment':'Neither electron=1+2/proton=3+4 nor electron=1+2/proton=1..4 is derived by the stored supports.',
        'missing_map':'A source-derived coefficient/transport adapter respecting the refinement and accounting for the rank change.',
        'next_test':'Build a separately labelled rooted open-fan prototype with retained attachments; do not relabel the complete stored electron as that prototype.'}
    (BASE/'results/electron_proton_assembly_relation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
