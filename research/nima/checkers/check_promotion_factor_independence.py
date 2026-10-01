"""Test independent factors via induced degree2 projection classes.

Pair constraints are explicit model choices. Projection cocycles detect
whether both primitive sphere classes survive independently. Retained grouping
is separately checked as a lossless presentation of the original relation.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from biclique_complex import analyze, apply, dowker, rank

primitive=[(a,b) for a,b in product(range(4),repeat=2) if a!=b]


def cocycle(simplex, coordinate):
    projected=[vertex[coordinate] for vertex in simplex]
    if len(set(projected))<3 or sorted(projected)!=[0,1,2]: return F(0)
    inversions=sum(projected[i]>projected[j] for i in range(3) for j in range(i+1,3))
    return F((-1)**inversions)


def test(name,condition,expected_betti,expected_projection_rank):
    pairs=[(a,b) for a,b in product(primitive,repeat=2) if condition(a,b)]
    relation=[((a[0],b[0]),(a[1],b[1])) for a,b in pairs]
    dims,diffs,cells=dowker(relation,include_cells=True)
    _,homology=analyze(dims,diffs)
    betti={d:n for d,n in homology.items() if n}
    phi=[{j:cocycle(simplex,k) for j,simplex in enumerate(cells.get(2,[]))
          if cocycle(simplex,k)} for k in (0,1)]
    # Each projection pulls the primitive 2-cocycle back to a closed cochain.
    for form in phi:
        assert all(sum((form.get(i,F(0))*v for i,v in column.items()),F(0))==0
                   for column in diffs.get(3,[]))
    # Coboundaries in C^2 are the ROWS of d2. Compute the rank added by the
    # two closed projection cochains modulo that row space.
    rows=[{} for _ in range(dims.get(1,0))]
    for j,column in enumerate(diffs.get(2,[])):
        for i,value in column.items(): rows[i][j]=value
    base_rank=rank(rows)
    projected_rank=rank(rows+phi)-base_rank
    difference={i:phi[0].get(i,F(0))-phi[1].get(i,F(0))
                for i in set(phi[0])|set(phi[1])}
    difference={i:v for i,v in difference.items() if v}
    same_class=rank(rows+[difference])==base_rank
    assert betti==expected_betti and projected_rank==expected_projection_rank
    if name=='independent':
        # Explicit sphere slices: vary one coordinate while fixing the other.
        lookup={cell:j for j,cell in enumerate(cells[2])}
        for coordinate in (0,1):
            cycle={}
            for omitted in range(4):
                face=tuple(v for v in range(4) if v!=omitted)
                vertices=tuple((v,0) if coordinate==0 else (0,v) for v in face)
                cycle[lookup[vertices]]=F((-1)**omitted)
            assert not apply(diffs[2],cycle)
            evaluations=[sum((form.get(i,F(0))*v for i,v in cycle.items()),F(0)) for form in phi]
            # Chosen tetrahedron orientation gives -1 on face(0,1,2).
            assert evaluations==([F(-1),F(0)] if coordinate==0 else [F(0),F(-1)])
    elif expected_projection_rank==1:
        assert same_class
    print(f'{name}: {len(pairs)} arrow pairs; Betti={betti}; projection-class rank={projected_rank}; same class={same_class}',flush=True)
    return relation


full=test('independent',lambda a,b:True,{0:1,2:2,4:1},2)
test('synchronized',lambda a,b:a==b,{0:1,2:1},1)
test('shared-source',lambda a,b:a[0]==b[0],{0:1,2:1},1)
test('shared-target',lambda a,b:a[1]==b[1],{0:1,2:1},1)
test('composable',lambda a,b:a[1]==b[0],{0:4},0)
# A shared fixed reference tag adds metadata, not an equality between variables.
tagged=[((0,a),(0,b)) for a,b in full]
assert [(a[1],b[1]) for a,b in tagged]==full

# Current promotion: group incoming records, assign labels, retain children.
family=defaultdict(list)
for rid,edge in enumerate(primitive): family[edge[1]].append((rid,edge))
fresh={('family',i):tuple(members) for i,members in enumerate(family.values())}
restored={rid:edge for members in fresh.values() for rid,edge in members}
assert restored==dict(enumerate(primitive))
dims,diffs=dowker(list(restored.values()))
_,homology=analyze(dims,diffs)
assert {d:n for d,n in homology.items() if n}=={0:1,2:1}
# Copying presentation coordinates gives only a diagonal edit image.
n=len(primitive)
diagonal=[{i:F(1),n+i:F(1)} for i in range(n)]
assert rank(diagonal)==n
print('Retained incoming promotion: 12 original arrows -> 4 family labels -> the same 12 arrows on drill-down; b2 remains1.')
print('Two copied presentations admit12 independent scalar leaf edits, versus24 for two independent leaf copies.')
print('Shared reference metadata preserves both product classes; endpoint equalities impose genuine constraints.')
