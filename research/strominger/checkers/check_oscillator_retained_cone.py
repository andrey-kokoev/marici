"""Finite/symbolic specialization of ThreeWitnessRetainedCone.Focus/Cone.
Exact presentation maps and retained payload recovery; no new Agda compilation.
"""
from dataclasses import dataclass, replace
from itertools import combinations
from pathlib import Path
import copy
import hashlib
import json
import sympy as s
from check_oscillator_family_promotion import promotion_api
from check_oscillator_fibration_cut import transfer

ROOT=Path(__file__).resolve().parents[3]
API=promotion_api()
Row=API['Row']


@dataclass(frozen=True)
class Focus:
    packet: tuple
    selector: str
    selected: object


def select(packet,selector):
    if selector=='raw':
        return packet
    return API['indexed'](packet,selector)


def decorate(packet,selector):
    return Focus(packet,selector,select(packet,selector))


def recover(view):
    if not isinstance(view,Focus) or view.selector not in ('raw','source','target'):
        raise ValueError('Wrong focus type')
    if view.selected != select(view.packet,view.selector):
        raise ValueError('Focus certificate fails')
    return view.packet


def read(packet):
    rows=tuple((r.value,r.source[0],r.target[0]) for r in API['leaves'](packet))
    return transfer(rows,0,3),transfer(rows,1,3)


SELECTORS={1:'raw',2:'source',3:'target'}


def edge(i,j,value):
    packet=value if i==0 else recover(value)
    if i!=0 and value.selector!=SELECTORS[i]:
        raise ValueError('Wrong source vertex')
    return packet if j==0 else decorate(packet,SELECTORS[j])


def build(packet):
    return (packet,)+(tuple(decorate(packet,SELECTORS[i]) for i in (1,2,3)))


def triangle_decode(face):
    if len(face)!=3:
        raise ValueError('Need three focused vertices')
    for v,i in zip(face,(1,2,3)):
        if v.selector!=SELECTORS[i]:
            raise ValueError('Wrong extracted face')
    p=recover(face[0])
    if any(recover(v)!=p for v in face[1:]):
        raise ValueError('Faces disagree on retained packet')
    return p


def main():
    g,h=s.symbols('g h',positive=True,real=True)
    d=s.symbols('delta',real=True)
    chi=1/((g*g+h*h)/2-s.I*d)
    initial=tuple(Row(('leaf',i),(a,),(b,),v) for i,(v,a,b) in enumerate(((g*chi,0,2),(h*chi,1,2),(-g,2,3),(s.Integer(1),0,3))))
    fixture={g:1,h:2,d:0}
    reports={}
    for policy in ('inherited','common'):
        middle=API['incoming_promotion'](initial,1,policy)
        packet=API['incoming_promotion'](middle,2,policy)
        vertices=build(packet)
        # Six typed comparisons, and their actual inverses.
        for i,j in combinations(range(4),2):
            assert edge(i,j,vertices[i])==vertices[j]
            assert edge(j,i,edge(i,j,vertices[i]))==vertices[i]
        # Four face witnesses: independently computed direct/composite maps.
        for i,j,k in combinations(range(4),3):
            assert edge(j,k,edge(i,j,vertices[i]))==edge(i,k,vertices[i])
        # Two whiskered face-composition routes have the same endpoint map.
        route_a=edge(2,3,edge(1,2,edge(0,1,vertices[0])))
        route_b=edge(1,3,edge(0,1,vertices[0]))
        route_c=edge(2,3,edge(0,2,vertices[0]))
        direct=edge(0,3,vertices[0])
        assert route_a==route_b==route_c==direct
        # Standalone extracted face: an independent object graph, with no apex
        # argument or external copy of the primitive input in its decoder.
        face=copy.deepcopy(vertices[1:])
        decoded=triangle_decode(face)
        assert decoded==packet and decoded is not packet
        assert API['leaves'](decoded)==initial
        assert tuple(child for r in decoded for child in r.members)==middle
        rr,qq=read(decoded)
        assert s.simplify(rr-(1-g*g*chi))==0
        assert s.simplify(qq+g*h*chi)==0
        assert s.simplify(rr*s.conjugate(rr)+qq*s.conjugate(qq)-1)==0
        # Corruption of a displayed view must fail its own equality certificate.
        broken=replace(face[1],selected={})
        try:
            triangle_decode((face[0],broken,face[2]))
        except ValueError:
            pass
        else:
            raise AssertionError('Stale focus accepted')
        # A consistent new packet with a zero bath remains representable, but
        # must change the readout: the cone cannot hide the physical defect.
        def poison(r):
            return replace(r,members=tuple(poison(c) for c in r.members)) if r.members else replace(r,value=s.Integer(0) if r.label==('leaf',1) else r.value)
        bad_packet=tuple(poison(r) for r in packet)
        bad_face=copy.deepcopy(build(bad_packet)[1:])
        br,bq=read(triangle_decode(bad_face))
        assert bq==0
        assert s.simplify((br*s.conjugate(br)+bq*s.conjugate(bq)).subs(fixture))==s.Rational(9,25)
        try:
            triangle_decode((bad_face[0],face[1],face[2]))
        except ValueError:
            pass
        else:
            raise AssertionError('Mixed packet face accepted')
        reports[policy]={'vertices':4,'edge_comparisons':6,'face_equations':4,
                         'tetrahedral_route_compatibility':True,
                         'standalone_triangle_recovers_final_and_intermediate_packets':True,
                         'resonant_r':str(rr.subs(fixture)),'resonant_q':str(qq.subs(fixture)),
                         'commutator_weight':'1','nested_bath_erasure_weight':'9/25',
                         'rejects':['stale focus certificate','mixed retained packets']}
    sources=['research/nima/agda/ThreeWitnessRetainedCone.agda','research/nima/agda/RetainedTetrahedralPackage.agda','research/nima/checkers/check_rung_transport_diagram.py','research/strominger/checkers/check_oscillator_family_promotion.py','research/strominger/checkers/check_oscillator_fibration_cut.py',str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','policies':reports,
            'binding':'Cone P P FromView ToView identity source-index target-index; P is the actual twice-promoted packet.',
            'proof_boundary':'Exact finite/symbolic specialization checks maps and commuting routes. Generic Cubical path horn/filler is reused from the inspected constructor, not freshly compiled or numerically proved here.',
            'geometry_boundary':'Typed retained tetrahedron, not Euclidean tetrahedral metric or FCC lattice.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}}
    out=ROOT/'research/strominger/results/oscillator-retained-cone/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
