"""Exact simplicial-chain fillability with fixed barycentric geometry.

The tests vary admitted top-dimensional cells, retaining the entire lower
skeleton. This is additive chain fillability, not arbitrary native WG filling.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import POINTS, mean, sub, dot

ROOT = Path(__file__).resolve().parents[1]


def canonical(simplex):
    inversions = sum(a > b for i,a in enumerate(simplex) for b in simplex[i+1:])
    return tuple(sorted(simplex)), (-1)**inversions


def boundary(chain):
    result = {}
    for simplex, coefficient in chain.items():
        for i in range(len(simplex)):
            face, sign = canonical(simplex[:i]+simplex[i+1:])
            result[face] = result.get(face, F(0)) + coefficient*(-1)**i*sign
    return {s:c for s,c in result.items() if c}


def add(chains):
    out = {}
    for chain in chains:
        for s,c in chain.items(): out[s] = out.get(s,F(0))+c
    return {s:c for s,c in out.items() if c}


def main():
    examples=[]
    for labels in ('ABC','ABCD'):
        n=len(labels)-1
        vertices={i:POINTS[v] for i,v in enumerate(labels)}
        center=mean(list(vertices.values()))
        m=len(labels)
        vertices[m]=center
        residual=tuple(len(labels)*center[j]-sum(POINTS[v][j] for v in labels) for j in range(3))
        assert residual == (F(0),)*3
        outer=tuple(range(len(labels)))
        z=boundary({outer:F(1)})
        assert boundary(z)=={}
        # Cone each oriented outer face to the retained center. All proper
        # faces of these cells are admitted in every tested presentation.
        cones=[]
        for face,coefficient in z.items():
            cell,sign=canonical((m,)+face)
            cones.append((cell,coefficient*sign))
        full_filler=dict(cones)
        assert boundary(full_filler)==z
        cases=[]
        for bits in product((0,1),repeat=len(cones)):
            admitted={cell:c for bit,(cell,c) in zip(bits,cones) if bit}
            if all(bits):
                assert boundary(admitted)==z
                cases.append(dict(mask=''.join(map(str,bits)),fillable=True,
                                  filler=[dict(cell=cell,coefficient=str(c)) for cell,c in admitted.items()]))
            else:
                # Choose the unique exterior face of a missing cone. Its
                # coefficient functional annihilates every admitted boundary
                # but evaluates to +/-1 on z: an exact no-filler certificate
                # over Z, Q or R, not a failure of one guessed filling.
                missing=next(cell for bit,(cell,c) in zip(bits,cones) if not bit)
                face=tuple(v for v in missing if v!=m)
                assert z[face] != 0
                assert all(boundary({cell:F(1)}).get(face,0)==0 for cell in admitted)
                cases.append(dict(mask=''.join(map(str,bits)),fillable=False,
                                  obstruction_face=face,obstruction_value=str(z[face])))
        assert sum(c['fillable'] for c in cases)==1
        # Wrong boundary fails the prior cycle gate, despite identical center.
        bad=dict(z)
        face=next(iter(z));bad[face]+=1
        assert boundary(bad)!={}
        # Equal-weight midpoint equations hold for every retained edge,
        # independent of which top cells are admitted.
        for i,j in combinations(vertices,2):
            mid=mean([vertices[i],vertices[j]])
            assert tuple(2*mid[k]-vertices[i][k]-vertices[j][k] for k in range(3))==(F(0),)*3
        examples.append(dict(source=labels,dimension=n,center=list(map(str,center)),
                             barycenter_residual=list(map(str,residual)),
                             fixed_data='same embedded vertices and complete cone lower skeleton in every mask',
                             tested_presentations=len(cases),fillable_presentations=1,
                             cases=cases,noncycle_control='rejected by nonzero boundary of proposed boundary'))
    result=dict(schema='marici.nima.barycentric-fillability.v1',status='pass',
                obligation='forward additive realization and readout descent from full oriented incidence to center geometry',
                examples=examples,
                claim='Barycenter and lower-skeleton geometry do not determine chain fillability. Admitted cone cells construct a filler; a missing exterior-face functional certifies nonfillability.',
                scope='all 8 triangle-cone and 16 tetrahedron-cone top-cell subsets with fixed lower skeleton; exact integral certificates',
                residual='No claim that native WG admissibility is determined by this chain model, or that an embedded geometric hole alone derives the admissibility rule.')
    (ROOT/'results/barycentric-fillability.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='examples'},indent=2))
    for e in examples:
        print(e['source'],e['tested_presentations'],'presentations;',e['fillable_presentations'],'fillable')


if __name__=='__main__':main()
