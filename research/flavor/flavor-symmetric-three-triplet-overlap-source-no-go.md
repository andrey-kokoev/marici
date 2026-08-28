# The minimal symmetric three-triplet source selects only CP-blind endpoints: WP960

## Question

Does the most economical readout-independent action on three normalized
complex family triplets derive a CP-bearing ordered projective triple?

## Frozen source grammar

Let `P`, `Q`, and `R` be the normalized rank-one projectors supplied by the
canonical WP959 triplet interface.  The lowest-degree permutation-symmetric
relational scalar is

\[
S(P,Q,R)=\operatorname{Tr}(PQ)+\operatorname{Tr}(QR)+\operatorname{Tr}(RP).
\]

Each summand is the squared magnitude of a normalized inner product and lies
between zero and one.  Add ordinary positive radial squares to fix the three
nonzero norms; on that radial locus the relational action is

\[
V_{\rm rel}=\kappa S.
\]

This grammar is independent of flavor readout, invariant under simultaneous
weak-basis conjugation, invariant under independent triplet rescaling, and
symmetric under permutation of the three source ports.

## Exact global classification

The sharp bounds are

\[
0\leq S\leq3.
\]

The lower bound is attained exactly when the three rays are pairwise
orthogonal.  The upper bound is attained exactly when all three projectors
coincide.  Consequently:

- for positive `kappa`, every global minimum is an orthonormal projective
  frame modulo common `U(3)` and port permutation;
- for negative `kappa`, every global minimum is a collinear triple;
- for zero `kappa`, the projective relations are flat.

At the repulsive endpoint the Bargmann invariant is zero.  At the attractive
endpoint it is one.  Both have zero imaginary part.  The collinear endpoint
also fails to span the family carrier.

## Disposition

The canonical three-triplet interface does not by itself create a selector.
The unique symmetric pair-overlap action selects only CP-blind boundary
orbits.  A CP-capable source requires a genuinely cyclic three-body invariant,
frustrated additional structure, or an equivalent irreducible complex tensor.

This result does not authorize inserting a coefficient chosen to reproduce
the WP959 witness.  A CP-even cyclic source may at most select a conjugate
pair; selecting one orientation requires either spontaneous CP breaking with
both conjugate minima retained or an independently admitted CP-odd source
term.  Completion and calibrated instrument transport remain open.  No
composition is assigned physical time or causality.

## Smallest exact falsifier

The two endpoint triples are sufficient: an orthonormal frame has `S=0` and
zero Bargmann invariant, while three coincident rays have `S=3` and Bargmann
invariant one.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp960_symmetric_three_triplet_overlap_source_no_go.py

Generated result:
`research/flavor/results/wp960_symmetric_three_triplet_overlap_source_no_go.json`.
