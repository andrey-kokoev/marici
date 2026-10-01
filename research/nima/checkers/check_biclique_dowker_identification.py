"""Compare local biclique chains with ordinary Dowker simplicial chains over Q."""
from itertools import combinations, product
from collections import defaultdict
from biclique_complex import analyze, biclique, dowker, fixture


def normalized(homology): return {d:n for d,n in homology.items() if n}


def compare(name,edges):
    dims,diffs,_,_=biclique(edges)
    ranks,homology=analyze(dims,diffs)
    ddims,ddiffs=dowker(edges)
    _,dhomology=analyze(ddims,ddiffs)
    assert normalized(homology)==normalized(dhomology)
    print(f'{name}: biclique dimensions={dims}; ranks={ranks}',flush=True)
    print(f'  rational Betti numbers={normalized(homology)}; Dowker match passed (simplex counts {ddims}).',flush=True)
    return normalized(homology)


simple=[('complete-2x3',[(('s',i),('t',j)) for i,j in product(range(2),range(3))],{0:1}),
        ('six-cycle',[(('s',i),('t',j)) for i,j in product(range(3),repeat=2) if i!=j],{0:1,1:1}),
        ('cube-incidence',[(('s',i),('t',j)) for i,j in product(range(4),repeat=2) if i!=j],{0:1,2:1})]
for name,edges,expected in simple: assert compare(name,edges)==expected
assert compare('137-slot missing-arrow fixture',fixture())=={0:17}
restored=compare('160-slot restored-arrow fixture',fixture(restore=True))
assert restored=={0:17,2:2,4:1}
print(f'Restored-arrow result: {restored}',flush=True)

# Rectangular completion identifies the square relation's face-poset retract
# with the product of primitive Dowker face posets.
def faces(relation):
    neighbors=defaultdict(set)
    for u,v in relation: neighbors[v].add(u)
    result=set()
    for members in neighbors.values():
        ordered=sorted(members)
        for n in range(1,len(ordered)+1):
            result.update(frozenset(c) for c in combinations(ordered,n))
    return result

for restore in (False,True):
    primitive=[(a,b) for a,b in product(range(4),repeat=2)
               if a!=b and (restore or (a,b)!=(0,1))]
    primitive_faces=faces(primitive)
    square=[((a,c),(b,d)) for a,b in primitive for c,d in primitive]
    square_faces=faces(square)
    closed=set()
    for face in square_faces:
        left=frozenset(a for a,b in face); right=frozenset(b for a,b in face)
        assert left in primitive_faces and right in primitive_faces
        rectangle=frozenset(product(left,right))
        assert face<=rectangle and rectangle in square_faces
        closed.add(rectangle)
    expected={frozenset(product(a,b)) for a,b in product(primitive_faces,repeat=2)}
    assert closed==expected and len(closed)==len(primitive_faces)**2
    assert len(primitive_faces)==(14 if restore else 13)
    print(f'Primitive restore={restore}: {len(primitive_faces)} nonempty Dowker faces; square closure has {len(closed)} product faces.',flush=True)
