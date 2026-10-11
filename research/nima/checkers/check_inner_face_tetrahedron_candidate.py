"""First geometric test of an inner-face electron candidate.
Uses the existing 12-triangle source; coning and subdivision are explicit trials.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import POINTS,mean,det,sub,compose,LABELS
ROOT=Path(__file__).resolve().parents[1]

def faces(cells):return Counter(frozenset(f) for c in cells for f in combinations(c,3))
def vol(c,points):
    a,b,c,d=[points[k] for k in sorted(c)]
    return abs(det((sub(b,a),sub(c,a),sub(d,a))))/6

def main():
    source=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())
    points=dict(POINTS);points['O']=(F(0),)*3
    for f in combinations(LABELS,3):points['F_'+''.join(f)]=mean([POINTS[k] for k in f])
    cells=tuple(frozenset(('O',*r['triangle'])) for r in source['triangles_and_transports'])
    assert len(cells)==len(set(cells))==12
    assert {vol(c,points) for c in cells}=={F(2,9)}
    fc=faces(cells);inner={f for f,n in fc.items() if n==2};outer={f for f,n in fc.items() if n==1}
    assert len(inner)==18 and len(outer)==12 and set(fc.values())=={1,2}
    assert all('O' in f for f in inner)
    # Source proper tetrahedral group. No viewing-axis choice.
    group={(0,1,2,3)};front=list(group)
    while front:
        p=front.pop()
        for g in ((1,2,0,3),(3,0,2,1)):
            q=compose(g,p)
            if q not in group:group.add(q);front.append(q)
    def move_vertex(v,p):
        if v=='O':return v
        if v in LABELS:return LABELS[p[LABELS.index(v)]]
        return 'F_'+''.join(sorted(LABELS[p[LABELS.index(k)]] for k in v[2:]))
    def orbit(f):return {frozenset(move_vertex(v,p) for v in f) for p in group}
    unseen=set(inner);orbits=[]
    while unseen:
        o=orbit(next(iter(unseen)));assert o<=inner;orbits.append(len(o));unseen-=o
    assert sorted(orbits)==[6,12]
    assert all(orbit(c)==set(cells) for c in cells)
    # Trial: attach a fresh tetrahedron to an occupied internal face.
    chosen=frozenset(('O','A','B'))
    attached=cells+(chosen|{'NEW'},)
    assert faces(attached)[chosen]==3
    # Manifold-preserving alternative: stellar subdivide this shared face.
    points['N']=mean([points[k] for k in chosen])
    touching=[c for c in cells if chosen<=c]
    assert len(touching)==2
    children=tuple((c-{v})|{'N'} for c in touching for v in chosen)
    refined=tuple(c for c in cells if c not in touching)+children
    rf=faces(refined)
    assert len(refined)==16 and {vol(c,points) for c in children}=={F(2,27)}
    assert sum(vol(c,points) for c in refined)==F(8,3)
    assert {f for f,n in rf.items() if n==1}==outer
    assert set(rf.values())=={1,2}
    # Further volume division is possible: interior stellar subdivision.
    c=children[0];points['M']=mean([points[k] for k in c])
    grandchildren=tuple((c-{v})|{'M'} for v in c)
    assert {vol(t,points) for t in grandchildren}=={F(1,54)}
    result=dict(schema='marici.nima.inner-face-tetrahedron-candidate.v1',status='pass',
        interpretation='Explicit geometric trial on the existing proton-like surface; not a source-selected particle creation operation.',
        cone_cells=12,cell_volume='2/9',total_volume='8/3',internal_faces=18,
        internal_face_symmetry_orbits=sorted(orbits),tetrahedron_orbit_size=12,
        inner_face_attachment={'cofaces_after_attachment':3,'manifold_ball_extension':False},
        stellar_alternative={'total_cells':16,'new_cells':6,'new_cell_volume':'2/27','same_outer_boundary':True,'same_total_volume':True},
        further_subdivision_cell_volume='1/54',
        conclusion='No unmarked unique bottom cell or inner face. Adding a third tetrahedron at a filled internal face branches the complex; stellar refinement preserves the body but supplies neither a new particle nor a minimum size.',
        open_gate='A native birth/attachment rule, a source-selected marked face or symmetric superposition, and a persistent independent excitation observable are needed before electron identification.')
    (ROOT/'results/inner-face-tetrahedron-candidate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
