"""Faithful decorated FCC-cell chart of the existing oscillator retained cone.
Geometry is a representation convention, not derived physical space.
"""
from pathlib import Path
from itertools import permutations, combinations
import copy
import hashlib
import json
import sympy as s
from check_oscillator_retained_cone import API, Row, build, edge, triangle_decode, read

ROOT=Path(__file__).resolve().parents[3]
COORDS=((0,0,0),(1,1,0),(1,0,1),(0,1,1))


def encode(vertices,chart):
    # Preserve typed roles, not just spatial positions or counts.
    return {'vertices':tuple((COORDS[chart[i]],i,vertices[i]) for i in range(4)),
            'edges':tuple((COORDS[chart[i]],COORDS[chart[j]],i,j) for i,j in combinations(range(4),2)),
            'faces':tuple(tuple(COORDS[chart[i]] for i in face) for face in combinations(range(4),3))}


def decode(encoded):
    records=encoded['vertices']
    if len(records)!=4 or {r[0] for r in records}!=set(COORDS) or {r[1] for r in records}!=set(range(4)):
        raise ValueError('Invalid chart vertices')
    by_role={r[1]:r for r in records}
    vertices=tuple(by_role[i][2] for i in range(4))
    chart=tuple(COORDS.index(by_role[i][0]) for i in range(4))
    if encode(vertices,chart)!=encoded:
        raise ValueError('Incidence/role mismatch')
    for i,j in combinations(range(4),2):
        if edge(i,j,vertices[i])!=vertices[j]:
            raise ValueError('Decoration comparison mismatch')
    return vertices


def main():
    assert all(sum(v)%2==0 for v in COORDS)
    assert all(sum((a-b)**2 for a,b in zip(u,v))==2 for u,v in combinations(COORDS,2))
    determinant=s.Matrix.hstack(*(s.Matrix(COORDS[i])-s.Matrix(COORDS[0]) for i in (1,2,3))).det()
    assert abs(determinant)==2
    def source(bath_coefficient=-s.Rational(4,5)):
        # Canonical resonant equations: chi=2/5, g=1, h=2.
        # h*chi=4/5; final bath transfer is its negative.
        return tuple(Row(('leaf',i),(a,),(b,),v) for i,(v,a,b) in enumerate(((s.Rational(2,5),0,2),(-bath_coefficient,1,2),(-s.Integer(1),2,3),(s.Integer(1),0,3))))
    counts={}
    for policy in ('inherited','common'):
        packet=API['incoming_promotion'](API['incoming_promotion'](source(),1,policy),2,policy)
        vertices=build(packet)
        for chart in permutations(range(4)):
            encoded=copy.deepcopy(encode(vertices,chart))
            recovered=decode(encoded)
            assert recovered==vertices
            # Extract the opposite-apex face by retained role, not by a fixed
            # coordinate choice; no apex or external source is passed to decoder.
            face=tuple(next(value for _,role,value in encoded['vertices'] if role==i) for i in (1,2,3))
            assert triangle_decode(face)==packet
            assert read(triangle_decode(face))==(s.Rational(3,5),-s.Rational(4,5))
        # Deliberately retain geometry while changing the nested physical data.
        altered=API['incoming_promotion'](API['incoming_promotion'](source(s.Integer(0)),1,policy),2,policy)
        original_chart=encode(vertices,(0,1,2,3))
        changed_chart=encode(build(altered),(0,1,2,3))
        assert original_chart['edges']==changed_chart['edges'] and original_chart['faces']==changed_chart['faces']
        assert tuple((c,r) for c,r,_ in original_chart['vertices'])==tuple((c,r) for c,r,_ in changed_chart['vertices'])
        assert read(triangle_decode(decode(changed_chart)[1:]))==(s.Rational(3,5),s.Integer(0))
        assert original_chart!=changed_chart
        corrupt=copy.deepcopy(original_chart)
        corrupt['edges']=corrupt['edges'][:-1]
        try:
            decode(corrupt)
        except ValueError:
            pass
        else:
            raise AssertionError('Missing incidence admitted')
        counts[policy]=24
    sources=['research/chatgpt/20261019/fcc_gaussian_boundary_recursion.md',
             'research/strominger/checkers/check_oscillator_retained_cone.py',
             'research/strominger/checkers/check_oscillator_family_promotion.py',
             str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','representation':'decorated canonical FCC tetrahedral cell T_1',
            'coordinates':COORDS,'squared_edge_length':2,'volume':'1/3',
            'charts_verified':counts,'triangle_readout':['3/5','-4/5'],
            'geometry_only_is_not_faithful':True,'missing_incidence_rejected':True,
            'claim_boundary':'Exact finite decorated representation; no physical metric, lattice dynamics, infinite FCC tiling or unique representation derived.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}}
    out=ROOT/'research/strominger/results/oscillator-fcc-representation/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
