# Main-space channel counts from tetrahedral boundary geometry

## Question, boundary and frozen experiment

Operator asks whether a main space, codimension-one tetrahedra and unique-channel
exhaustion can produce electronic shell capacities. Construct candidate operators
from geometry BEFORE comparing with 2n^2; do not insert n incoming times n
outgoing states as an assumption.

Test two DIFFERENT kinds of source arena:

1. Existing reciprocal P/N network, on periodic quotients of sizes2,3,4. Its
   periodic topology is not asserted to be S3.
2. All regular convex4-polytopes with tetrahedral boundary facets:5-cell,
   16-cell and600-cell. Their4D interiors are main spaces; tetrahedra are3D
   codimension-one boundary cells, with boundary topology S3. They are separate
   candidate channel arenas, not assumed realizations of the prior P/N duality.

Scalar channels use the unit-weight graph Laplacian H=dI-A on boundary vertices.
Spin is an independent two-state factor. No covariant spin connection or physical
Hamiltonian is smuggled in. No field weights, boundary cutoff, band grouping or
particle-dependent projection is fitted. Atomic neutral populations are supplied
reference observations, not outputs used to construct the adjacency.

## Independent source construction

Use exact coordinates (a+b sqrt5)/4. For the600-cell generate8 signed coordinate
axes,16 signed half-coordinate vertices, and96 even permutations of
(0, +/-1/2, +/-phi/2, +/-1/(2phi)), with phi=(1+sqrt5)/2. Every vertex has unit
norm. Nearest-neighbor inner products determine edges exactly. Enumerate4-cliques
as candidate tetrahedra; verify supporting hyperplanes, nondegeneracy, triangular
face pairing, and Euler characteristic. No spectrum or shell target enters this.

The5-cell uses five regular-simplex points on S3; the16-cell uses the eight signed
coordinate axes. These are the complete regular convex4D tetrahedral-facet family,
not a post-test search over arbitrary graphs.

## Exact spectrum without projecting away channels

Build a rooted equitable partition using only adjacency counts. Calculate the
integer characteristic polynomial of its small quotient. Its square-free part
is ONLY a candidate annihilator: explicitly verify p(A)=0 on the FULL original
adjacency matrix. A quotient spectrum alone is insufficient.

Derive the multiplicity of every simple root r by the exact projector trace

    multiplicity(r) = tr[(p(A)/(A-rI))] / p'(r).

The numerator here means evaluating the polynomial p(t)/(t-r), not inverting
A-rI. Count closed walks directly on the original graph to obtain its trace
moments. Require positive integral ranks summing to the original vertex count.
Symmetry of A gives a complete real orthogonal spectral decomposition. All
original vertices, edges, facet data and projector polynomials remain retained.
No physical channel is discarded merely because it is invisible in a quotient.

The independent spin factor doubles the ranks. The fermionic exterior-algebra
occupancy rule then gives at most one occupant per spin-resolved mode. Neither
spin multiplicity nor fermionic statistics is derived from the geometry here.
Geometric link degree is not an electron capacity: modes can multiplex a link.

## Risky comparisons

Define candidate shell n as the n-th DISTINCT Laplacian band in ascending order.
Compare the resulting ranks with2n^2 for n1..6. Record finite termination and all
later bands as well; a matching prefix is not an infinite shell theorem.

A strong prospective expectation is that the600-cell has a six-band match while
the smaller tetrahedral S3 meshes and the existing dual lattice do not supply
that entire ladder. This is a risky mathematical prediction, not input to the
operator. The topology S3 alone therefore cannot constitute an explanation.

Then test the stronger claim using the SAME unchanged operator: fill lower bands
first up to electron number Z, and compare with C,Ca,Fe,Pb populations in the
fixture. Do not call capacity agreement an atomic explanation if filling fails.
Changing to a Coulomb, covariant-spin, interaction or sub-shell operator would
be a new hypothesis, not a repair declared to have passed this test.

## Issue-boundary DPC and disposition criterion

1. Problem: raw path/face counts did not establish independent channel ranks or
   the observed occupations. The4D/codimension-one proposal supplies a new arena.
2. Bold candidate: canonical adjacency on a tetrahedral4D boundary can generate
   the shell-capacity ranks; the stronger candidate also claims its lowest-band
   filling explains the supplied neutral populations.
3. Rivals: matching only the first few ranks; selecting geometry or band groupings
   after the fact; quotient loss; topology mistaken for operator data; geometry
   mistaken for Pauli exclusion; capacities mistaken for actual atomic filling.
4. Risk: exact full-graph spectral certificates, a predeclared complete regular
   family and old-lattice controls, full band census and unchanged filling tests.
5. Strongest falsifier: independently compare the first six band ranks AND the
   neutral filling predictions, retaining nonzero occupation residuals rather
   than inventing splitting or thresholds after seeing them.
6. Disposition: mathematical execution success and physical candidate survival
   are separate fields. The receipt records successes and failures per candidate;
   a mixed result must not be promoted to a native P/N/E or atomic explanation.

## Reproduce and stopping boundary

    uv run --with sympy python research/strominger/checkers/check_tetrahedral_channel_capacity.py

The SCC adapter uses the same ephemeral dependency invocation. Sympy is required;
a standalone uv-managed Python without that environment is not sufficient.

Receipts: `results/tetrahedral-channel-capacity/verification.json` and
`disposition.md`. No other owner's outputs or existing lattice source are changed.

The4D arenas do not automatically admit the earlier two reciprocal tetrahedral
lattices: native attachment/occupation maps remain missing. In particular600-cell
cell duality is with the120-cell, whose cells are dodecahedral, not tetrahedral.
A capacity result must retain that limitation. No waiting-only successor or
new physical selection rule is invented at this boundary.
