"""Explicit retained-face/flag growth policy, not uniquely selected WG dynamics.
Each new vertex retains an old nonempty simplex; each new cell is a flag.
"""
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import POINTS,mean,LABELS,det,sub
ROOT=Path(__file__).resolve().parents[1]

def closure(tops):
    return {frozenset(s) for t in tops for k in range(1,len(t)+1) for s in combinations(sorted(t),k)}
def vector(complex):return [sum(len(s)==k for s in complex) for k in range(1,5)]
def volume(cell,points):
    a,b,c,d=[points[i] for i in sorted(cell)]
    return abs(det((sub(b,a),sub(c,a),sub(d,a))))/6

def grow(tops,points):
    old=closure(tops);records=tuple(sorted(old,key=lambda s:(len(s),tuple(sorted(s)))))
    index={s:i for i,s in enumerate(records)}
    newpoints={i:mean([points[v] for v in s]) for i,s in enumerate(records)}
    children=set();parents={}
    for t in tops:
        for order in permutations(sorted(t)):
            chain=tuple(frozenset(order[:k]) for k in range(1,len(t)+1))
            assert all(a<b for a,b in zip(chain,chain[1:]))
            child=frozenset(index[s] for s in chain)
            assert child not in children
            children.add(child);parents[child]=t
            assert records[max(child,key=lambda i:len(records[i]))]==t
            assert volume(child,newpoints)==volume(t,points)/24
    assert set(records)==old
    assert set(parents.values())==set(tops)
    assert sum(volume(t,points) for t in tops)==sum(volume(t,newpoints) for t in children)
    new=closure(children);fv=vector(new)
    assert fv[0]-fv[1]+fv[2]-fv[3]==1
    # Every actual old face persists as a labelled record, and its singleton
    # descendants recover original vertices without any averaging inversion.
    assert all(records[index[frozenset((v,))]]==frozenset((v,)) for v in points)
    return children,newpoints,records

def main():
    tops={frozenset(range(4))};points={i:POINTS[k] for i,k in enumerate(LABELS)}
    progression=[dict(level=0,f_vector=vector(closure(tops)),cell_volume=str(volume(next(iter(tops)),points)))]
    initial_flags={tuple(frozenset(p[:k]) for k in range(1,5)) for p in permutations(range(4))}
    for p in permutations(range(4)):
        image={tuple(frozenset(p[v] for v in face) for face in flag) for flag in initial_flags}
        assert image==initial_flags
    for level in (1,2):
        tops,points,records=grow(tops,points)
        progression.append(dict(level=level,f_vector=vector(closure(tops)),cell_volume=str(volume(next(iter(tops)),points))))
    assert [p['f_vector'] for p in progression]==[[4,6,4,1],[15,50,60,24],[149,796,1224,576]]
    src=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())
    named=dict(POINTS);named['O']=(F(0),)*3
    for row in src['triangles_and_transports']:
        f=row['triangle'][0];named[f]=mean([POINTS[k] for k in f[2:]])
    ids={v:i for i,v in enumerate(sorted(named))};cp={ids[v]:p for v,p in named.items()}
    ct={frozenset(ids[v] for v in ('O',*r['triangle'])) for r in src['triangles_and_transports']}
    before=vector(closure(ct));nt,np,records=grow(ct,cp);after=vector(closure(nt))
    assert before==[9,26,30,12] and after==[77,400,612,288]
    result=dict(schema='marici.nima.retained-flag-shape-growth.v1',status='pass',
        policy='Promote each old nonempty simplex to a vertex retaining that simplex; connect strict inclusion flags.',
        tetrahedron_progression=progression,
        existing_cone_body={'before':before,'after':after,'volume':'8/3'},
        relabelling_checks=24,
        retention='All old faces recovered from vertex records; every new maximal flag has its exact old parent.',
        geometry='Same underlying filled body and volume; each old tetrahedron partitions into 24 equal-volume tetrahedra.',
        selection_boundary='Canonical given this subdivision policy, not forced by native WG completion. Numeric barycenters require the existing affine realization; the face-poset construction does not.',
        physics_boundary='No new independent particle, exterior volume, energy law or 137-state stopping bound is generated.')
    (ROOT/'results/retained-flag-shape-growth.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
