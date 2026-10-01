"""Promote incidence cycles to explicit 2-cells, then relations to 3-cells.

Compare a forest-dependent minimal filling with all four-edge comparison cells.
Exact rational linear algebra; chain groups describe additive edit comparisons.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import runpy

base=runpy.run_path(str(Path(__file__).with_name('check_family_incidence_structure.py')))
ends=base['ends']; cycles=base['cycles']; chords=base['chords']
divergence=base['divergence']


def add_scaled(out, vector, scale):
    for key,value in vector.items():
        new=out.get(key,F(0))+scale*value
        if new: out[key]=new
        else: out.pop(key,None)


def boundary(columns, coefficients):
    out={}
    for i,value in coefficients.items(): add_scaled(out,columns[i],value)
    return out


# Minimal 2-cell boundaries are the independent fundamental cycles.
minimal=[{i:F(v) for i,v in enumerate(cycle) if v} for cycle in cycles]
assert len(minimal)==90
assert all(all(value==0 for value in divergence(cycle).values()) for cycle in cycles)
# The chord-row minor of d2 is identity, hence ker(d2)=0 and im(d2)=ker(d1).
assert all(cycle[chord]==(i==j) for i,cycle in enumerate(cycles) for j,chord in enumerate(chords))

# A relation-local alternative: all rectangles present in the bipartite graph.
lookup={pair:i for i,pair in enumerate(ends)}
assert len(lookup)==len(ends)  # fixture has no parallel edges
neighbors=defaultdict(set)
for u,v in ends: neighbors[u].add(v)
rectangles=[]
rectangle_labels={}
for u,w in combinations(sorted(neighbors,key=repr),2):
    for v,z in combinations(sorted(neighbors[u]&neighbors[w],key=repr),2):
        rectangle_labels[(u,w,v,z)]=len(rectangles)
        rectangles.append({lookup[u,v]:F(1),lookup[u,z]:F(-1),
                           lookup[w,v]:F(-1),lookup[w,z]:F(1)})
for rect in rectangles:
    assert all(v==0 for v in divergence([rect.get(i,F(0)) for i in range(len(ends))]).values())
    # Chord coordinates exactly reconstruct each full edge boundary.
    reconstructed=boundary(minimal,{k:rect[c] for k,c in enumerate(chords) if c in rect})
    assert reconstructed==rect

# Reduce d2 in the 90-dimensional cycle coordinates. Track each dependency as
# an explicit d3 column in the ORIGINAL rectangle labels.
pivots={}; relations=[]; dependent_labels=[]
for label,rect in enumerate(rectangles):
    vector={k:rect[c] for k,c in enumerate(chords) if c in rect}
    expression={label:F(1)}
    for pivot in sorted(pivots):
        if pivot in vector:
            basis,combination=pivots[pivot]; factor=vector[pivot]
            add_scaled(vector,basis,-factor); add_scaled(expression,combination,-factor)
    if vector:
        pivot=min(vector); scale=vector[pivot]
        pivots[pivot]=({k:v/scale for k,v in vector.items()},
                       {k:v/scale for k,v in expression.items()})
    else:
        assert boundary(rectangles,expression)=={}
        relations.append(expression); dependent_labels.append(label)

rank=len(pivots)
# Every d3 column has a distinct unit redundant-cell coordinate, and all other
# entries are independent-cell coordinates; this proves d3 injective.
assert all(relation.get(label,F(0))==(i==j)
           for i,relation in enumerate(relations) for j,label in enumerate(dependent_labels))
assert len(relations)==len(rectangles)-rank
assert rank==90
# Explicit nonzero 2-cycle and its 3-cell filling.
assert relations and len(relations[0])>=3
# Local 3-cells: three rectangles on a K(2,3) or K(3,2) incidence block.
# Their boundaries are c01-c02+c12. Test how much of ker(d2) these generate.
local_relations=[]
for u,w in combinations(sorted(neighbors,key=repr),2):
    for v,z,t in combinations(sorted(neighbors[u]&neighbors[w],key=repr),3):
        local_relations.append({rectangle_labels[u,w,v,z]:F(1),
                                rectangle_labels[u,w,v,t]:F(-1),
                                rectangle_labels[u,w,z,t]:F(1)})
for u,w,h in combinations(sorted(neighbors,key=repr),3):
    for v,z in combinations(sorted(neighbors[u]&neighbors[w]&neighbors[h],key=repr),2):
        local_relations.append({rectangle_labels[u,w,v,z]:F(1),
                                rectangle_labels[u,h,v,z]:F(-1),
                                rectangle_labels[w,h,v,z]:F(1)})
local_pivots={}
for relation in local_relations:
    assert boundary(rectangles,relation)=={}
    vector={i:relation[label] for i,label in enumerate(dependent_labels) if label in relation}
    for pivot in sorted(local_pivots):
        if pivot in vector: add_scaled(vector,local_pivots[pivot],-vector[pivot])
    if vector:
        pivot=min(vector); scale=vector[pivot]
        local_pivots[pivot]={i:value/scale for i,value in vector.items()}
local_rank=len(local_pivots)
assert len(rectangles)==672 and len(local_relations)==1304 and local_rank==582
# Same local biclique rule predicts dimension4 from K(2,4), K(3,3), K(4,2).
predicted_four=0
for p in (2,3,4):
    q=6-p
    for sources in combinations(sorted(neighbors,key=repr),p):
        common=set.intersection(*(neighbors[u] for u in sources))
        predicted_four+=comb(len(common),q) if len(common)>=q else 0
print(f'Next local-rule prediction: {predicted_four} dimension4 cells; their boundary rank is not yet computed.')
print(f'Local K(2,3)/K(3,2) 3-cells: count={len(local_relations)}, rank={local_rank}, remaining H2={len(relations)-local_rank}, H3 without 4-cells={len(local_relations)-local_rank}.')
print('Minimal fundamental-cycle filling: dimensions C0,C1,C2 = (64,137,90); ranks d1,d2 = (47,90).')
print('Minimal filling homology dimensions H0,H1,H2 = (17,0,0); no nonzero next kernel.')
print(f'All-rectangle filling: {len(rectangles)} 2-cells, rank d2={rank}, H1={90-rank}, H2={len(relations)}.')
print(f'Explicit independent d3 columns={len(relations)}; d2*d3=0 for every column; H2 after filling=0, H3=0.')
print(f'First relation uses {len(relations[0])} rectangle cells: {sorted(relations[0].items())}')
print('Higher comparison structure depends on the chosen filling presentation; independent-kernel filling terminates after one step.')
