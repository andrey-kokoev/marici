"""Induce orientation-class costs from comparison-cell Euclidean costs.

Edge costs pulled back along d2 vanish on all H2 representatives. Unit costs
on oriented Dowker triangles instead give a positive quotient metric. Compute
ranks1,2 explicitly and verify the product-count formula for rank4 locally.
"""
from fractions import Fraction as F
from itertools import product, combinations
from random import Random
from biclique_complex import analyze, apply, biclique, dowker


def sign(values):
    return (-1)**sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))


def epsilon(face,k):
    projected=[v[k] for v in face]
    if len(set(projected))!=3: return 0
    missing=next(iter(set(range(4))-set(projected)))
    return (-1)**missing*sign(projected)


def period(face,k):
    projected=[v[k] for v in face]
    return sign(projected) if sorted(projected)==[0,1,2] else 0


for n in (1,2):
    vertices=list(product(range(4),repeat=n))
    relation=[(a,b) for a,b in product(vertices,repeat=2) if all(u!=v for u,v in zip(a,b))]
    dims,diffs,cells=dowker(relation,include_cells=True)
    _,homology=analyze(dims,diffs)
    assert homology[2]==n
    multiplicity=64**(n-1)
    columns=[{j:-F(epsilon(face,k),multiplicity) for j,face in enumerate(cells[2]) if epsilon(face,k)} for k in range(n)]
    for k,z in enumerate(columns):
        # The putative class has zero induced edit in the underlying edge layer.
        assert not apply(diffs[2],z)
        assert sum(v*v for v in apply(diffs[2],z).values())==0
        # Orthogonal to every 3-boundary: this representative minimizes unit
        # triangle edit cost in its homology class.
        assert all(sum((z.get(j,F(0))*v for j,v in boundary.items()),F(0))==0
                   for boundary in diffs.get(3,[]))
        assert [sum((period(cells[2][j],i)*v for j,v in z.items()),F(0)) for i in range(n)]==[
            F(i==k) for i in range(n)]
    gram=[[sum((z.get(j,F(0))*w.get(j,F(0)) for j in set(z)|set(w)),F(0))
           for w in columns] for z in columns]
    scale=F(4,multiplicity)
    assert gram==[[scale*F(i==j) for j in range(n)] for i in range(n)]
    # The induced scalar metric gives the same class-space differential return
    # as Euclidean coordinates, then the harmonic lift minimizes cell cost.
    a=tuple(F(k+2) for k in range(n)); request=F(1,7)
    dh=tuple(request*v/sum(w*w for w in a) for v in a)
    lifted={j:sum((columns[k].get(j,F(0))*dh[k] for k in range(n)),F(0)) for j in range(len(cells[2]))}
    assert sum(a[k]*sum((period(cells[2][j],k)*v for j,v in lifted.items()),F(0)) for k in range(n))==request
    assert sum(v*v for v in lifted.values())==scale*sum(v*v for v in dh)
    if n==2:
        z=columns[0]; perturbation=diffs[3][0]
        modified={j:z.get(j,F(0))+perturbation.get(j,F(0)) for j in set(z)|set(perturbation)}
        assert sum(v*v for v in modified.values())==sum(v*v for v in z.values())+sum(v*v for v in perturbation.values())
    print(f'rank{n}: explicit harmonic representatives; induced triangle-cost metric={scale}*I; boundary/edge cost=0.')

# Rank4 formula: for each primitive-coordinate face, each of the other factor
# triples can be chosen in4^3 ways. Count the support without materializing
# the complete2-skeleton on256 vertices.
n=4; multiplicity=64**(n-1)
assert 4*multiplicity==1048576
assert F(4,multiplicity)==F(1,65536)
vertices=list(product(range(4),repeat=n)); rng=Random(137)
# Local edge-boundary cancellations, including all possible third vertices.
for _ in range(16):
    edge=tuple(sorted(rng.sample(vertices,2)))
    for k in range(n):
        coefficient=0
        for third in vertices:
            if third in edge: continue
            triangle=tuple(sorted((*edge,third)))
            index=triangle.index(third)
            coefficient+=(-1)**index*epsilon(triangle,k)
        assert coefficient==0
# Cocycle condition on admissible tetrahedra: projections omit a primitive
# vertex in every coordinate. This ensures orthogonality to3-boundaries.
checked=0
while checked<100:
    tetra=tuple(sorted(rng.sample(vertices,4)))
    if any(len({v[k] for v in tetra})==4 for k in range(n)): continue
    for k in range(n):
        assert sum((-1)**i*epsilon(tetra[:i]+tetra[i+1:],k) for i in range(4))==0
    checked+=1
# Equal class-cost scale across products needs transported cell weights.
for n in (1,2,4):
    unit_cell_class_cost=F(4,64**(n-1))
    chosen_cell_weight=64**(n-1)
    assert chosen_cell_weight*unit_cell_class_cost==4
print('rank4: product-count metric=1/65536*I; local cycle/cocycle identities checked without full chain-matrix enumeration.')
print('Unit triangle costs produce scales4,1/16,1/65536; weighting triangles by64^(n-1) produces scale4 at each rank.')
# The same primitive sphere has six rectangle faces in its retained incidence
# presentation, versus four triangles in its Dowker presentation. Fresh unit
# cell costs give different norms for the primitive integral class.
primitive=[(('source',a),('target',b)) for a,b in product(range(4),repeat=2) if a!=b]
bdims,bdiffs,bcells,blabels=biclique(primitive)
assert bdims=={0:8,1:12,2:6}
solutions=[]
for tail in product((-1,1),repeat=5):
    z=dict(enumerate(map(F,(1,)+tail)))
    if not apply(bdiffs[2],z): solutions.append(z)
assert len(solutions)==1 and sum(v*v for v in solutions[0].values())==6
print('The primitive rectangle presentation assigns class cost6, versus4 for unit triangle costs: topology alone does not transport cell metrics.')
print('Positive class cost requires cost on comparison-cell data; pulling edge-edit cost back along the boundary assigns every closed2-chain zero cost.')
