# Helium candidate: four-cell ring and role-selection test

## Fresh result

The small octahedron can be subdivided along its selected entry–exit diagonal
into **four equal-volume tetrahedral wedges**. They share that diagonal and
form a ring, with four internal triangular faces and eight exterior triangular
faces. This is the abstract incidence pattern described in the prior
[retained helium-4 core probe](../strominger/helium4-core-probe-v1.md).

The comparison is incidence-level only. No metric, marked-window, reader,
electron-port or coefficient adapter to that prior carrier was constructed.

## Role assignments

There are six ways to label two of the four wedges P and the other two N.
Adding the rule that every neighbouring pair has opposite roles leaves two:

    P N P N
    N P N P.

Thus an alternating rule yields 2P+2N, but that rule is an additional hypothesis.
A quarter turn fixes both ordered poles and cyclically permutes the four
wedges. Neither assignment is invariant under it. The only subsets invariant
under that quarter turn are the empty set and the entire ring.

Consequently the directed entry–exit pair alone does not canonically select
which wedges are protons. It permits the unlabelled opposite-pair partition;
labelled species selection needs an additional mark, witness or operation.
The same symmetry argument holds for the four equatorial vertices, separately
from their use in defining the wedges.

## Metric and cell boundary

These wedges are a **subdivision of one octahedral cell**, not the original
regular tetrahedral cells of the honeycomb. Each wedge has five squared edge
lengths 2 and one squared length 4 in the integer FCC chart. The long edge is
the inserted polar diagonal, which is not an elementary nearest-neighbour edge.

Each wedge has volume 1/3 and their total volume is 4/3, the whole octahedron.
The square equator divides into four sectors meeting the polar diagonal;
these cones have disjoint interiors. This provides the geometric partition,
not just a volume coincidence.

No ordinary electron exit or full coherence closure is derived here. In
particular, the prior helium probe explicitly retains reader and electron-exit
questions; matching its six-vertex outer shape does not solve them.

## Verification

`python research/realization-tower/check_helium_roles.py` freshly passed.
It enumerates all six 2+2 assignments, tests pole-preserving rotation, checks
four equal volumes, edge lengths and internal/external face multiplicities.

[Receipt](results/helium-role-test-v1.json).

Survivor: the shared-edge four-wedge ring and the conditional alternating 2+2
pattern. Not established: species selection from the endpoints alone, or
identification of the wedges with four primitive equal-edge lattice cells.
