"""Two successive independent comparisons of promoted incoming families.

Promotion retains incoming members. Comparison chooses both family operands
independently and retains their Cartesian member pairs. Verify the fibre law
against direct relation squaring at each stage. Topology is checked by explicit
coordinate sphere cycles; product Betti predictions use the proved Dowker law.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


@dataclass(frozen=True)
class Record:
    source: tuple
    target: tuple
    parents: tuple = ()


def promote(records, level):
    groups=defaultdict(dict)
    for rid,row in records.items(): groups[row.target][rid]=row
    # Explicit family namespace; targets also identify the grouping fibres.
    return {(level,target):members for target,members in groups.items()}


def compare_families(records, level):
    families=promote(records,level)
    next_records={}; comparison_families={}; provenance={}
    for left_id,right_id in product(families,repeat=2):
        target=left_id[1]+right_id[1]
        family_id=(level+1,target)
        members={}
        for left,right in product(families[left_id],families[right_id]):
            # Ordered primitive-origin tuple is the comparison record identity.
            rid=left+right
            row=Record(records[left].source+records[right].source,target,(left,right))
            assert rid not in next_records
            members[rid]=row; next_records[rid]=row
        comparison_families[family_id]=members
        provenance[family_id]=(left_id,right_id)
    # The same result from squaring first and grouping second.
    direct={left+right:Record(a.source+b.source,a.target+b.target,(left,right))
            for (left,a),(right,b) in product(records.items(),repeat=2)}
    assert next_records==direct
    assert comparison_families==promote(direct,level+1)
    assert len(provenance)==len(families)**2
    for family_id,(left_id,right_id) in provenance.items():
        assert len(comparison_families[family_id])==len(families[left_id])*len(families[right_id])
    return next_records,provenance


def primitive_faces(primitive):
    faces=set()
    for target in range(4):
        members=[a for a,b in primitive if b==target]
        for size in range(1,len(members)+1):
            faces.update(frozenset(c) for c in combinations(members,size))
    return faces


def is_face(vertices,faces):
    # Product relation: each coordinate projection must have a common neighbor.
    return all(frozenset(v[k] for v in vertices) in faces for k in range(len(vertices[0])))


def coordinate_sphere(arity, coordinate):
    # Boundary of an oriented tetrahedron in one factor; other vertices fixed0.
    result={}
    for omitted in range(4):
        triangle=[]
        for vertex in range(4):
            if vertex!=omitted:
                point=[0]*arity; point[coordinate]=vertex; triangle.append(tuple(point))
        result[tuple(triangle)]=F((-1)**omitted)
    return result


def boundary(cycle):
    result=defaultdict(F)
    for face,value in cycle.items():
        for i in range(len(face)): result[face[:i]+face[i+1:]]+=value*((-1)**i)
    return {face:value for face,value in result.items() if value}


def evaluate(cycle,coordinate):
    total=F(0)
    for face,value in cycle.items():
        projected=[v[coordinate] for v in face]
        if sorted(projected)==[0,1,2]:
            inversions=sum(projected[i]>projected[j] for i in range(3) for j in range(i+1,3))
            total+=value*((-1)**inversions)
    return total


for restored in (True,False):
    primitive=[(a,b) for a,b in product(range(4),repeat=2)
               if a!=b and (restored or (a,b)!=(0,1))]
    faces=primitive_faces(primitive)
    records={(i,):Record((a,),(b,)) for i,(a,b) in enumerate(primitive)}
    record_counts=[]; family_counts=[]
    for level in range(3):
        arity=2**level
        assert len(records)==len(primitive)**arity
        assert all(len(row.source)==len(row.target)==arity for row in records.values())
        record_counts.append(len(records)); family_counts.append(len(promote(records,level)))
        assert family_counts[-1]==4**arity
        # Each role is independently selectable; the domain is a full tuple set.
        assert set(records)==set(product(range(len(primitive)),repeat=arity))
        for coordinate in range(arity):
            sphere=coordinate_sphere(arity,coordinate)
            assert not boundary(sphere)
            if restored:
                assert all(is_face(face,faces) for face in sphere)
                assert [evaluate(sphere,k) for k in range(arity)]==[
                    F(-1) if k==coordinate else F(0) for k in range(arity)]
            else:
                assert any(not is_face(face,faces) for face in sphere)
        if level<2: records,provenance=compare_families(records,level)
    expected=[12,144,20736] if restored else [11,121,14641]
    assert record_counts==expected and family_counts==[4,16,256]
    print(f'Restored={restored}: comparison arities [1,2,4]; arrow records {record_counts}; incoming families {family_counts}.')
    if restored:
        print('  Independent coordinate sphere witnesses passed at all three stages.')
        print('  Product-theorem Betti predictions:',[
            {2*j:comb(n,j) for j in range(n+1)} for n in (1,2,4)])
    else:
        print('  Independent operand choices survive; the primitive missing facet blocks every coordinate sphere.')
print('Both promotion/comparison squares commute exactly, with ordered parent provenance and complete member coverage.')
print('This checker covers the arrow relation; auxiliary state-pair slots are not added to higher comparisons.')
