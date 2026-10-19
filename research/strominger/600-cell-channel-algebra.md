# Are the square capacities genuine input/output spaces?

## Question and boundary

The preregistered geometry/operator calculation completed with a six-band match
on the600-cell, but not a successful atomic filling rule. This independent
mechanism check asks whether the scalar square ranks come from a two-sided
channel structure, rather than counting entries of one arbitrary matrix.

Do not change the prior operator, geometry, band ordering, source code, receipt
or failed occupation predictions. Input is that pinned full calculation.

## Declared mathematical test

Treat each original600-cell unit vertex as a quaternion. Test all14400 products
for closure on the SAME120 vertices, identity, inverse, all1728000 associativity
triples, and left/right permutation actions. Reconstruct adjacency from the
neighbor set of the identity, not from any expected representation dimension.

Compute every conjugacy class and verify the twelve nearest neighbors form an
entire conjugacy class. Verify both left and right translations preserve every
original edge. Thus the exact graph operator is a central convolution on C[G].

Finite-group representation theory then gives

    C[G] = direct sum_rho V_rho tensor V_rho*,

with one simple two-sided block per conjugacy class. A central operator is scalar
on each block. If the independently computed number of distinct bands equals
the independently counted conjugacy classes, there is exactly one block per
band. Its full scalar rank must be dim(V_rho)^2. This is a statement about
independent matrix-COEFFICIENT FUNCTIONS on the group, not counting entries of a
single fixed transport matrix as electron states.

Expected result: nine classes/bands with input/output dimensions1,2,3,4,5,6,3,4,2
in the already fixed Laplacian ordering. Verify against the prior rank certificate,
not by constructing states with those dimensions. The first six give n^2; later
bands depart from that ladder. No irrep basis, spin multiplicity or Pauli law is
claimed to follow from a numerical square-root observation alone.

## DPC and disposition

Problem: raw path products could be dependent and false square coincidences.
Candidate: the unchanged source graph realizes independent left/right channel
indices by a central finite-group operator. Rivals: missing closure, noncentral
nearest-neighbor selection, several irreducibles merged in a band, matrix entries
mistaken for functions, or a capacity match mistaken for an atomic theory.
Risky consequence: all group/commutation cells, class/band count and full ranks
must agree without modifying the failed filling test. Execution receipt governs
this finite mechanism result. It cannot repair that failed physical candidate.

    python research/aspect/scc/scc.py check 600-cell-channel-algebra-v1 --verbose

Standard library only. Complete multiplication table, conjugacy classes,
left/right dimensions and source hashes are retained in
`results/600-cell-channel-algebra/verification.json`.

Scope: separate candidate channel arena. Linking these factors to the reciprocal
P/N fitting lattice requires a source map not constructed here. No full SO4
symmetry, continuum limit, physical charge, statistics or electron filling law
is derived; no waiting-only task is created from those missing objects.
