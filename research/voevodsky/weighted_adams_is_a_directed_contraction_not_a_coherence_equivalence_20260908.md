# Weighted Adams is a directed contraction, not a coherence equivalence

Date: 2026-09-08

## Typing correction

The generic coherence audit requested uniform bounds for both a transport and
its inverse.  That is correct for associators, unitors, reciprocal
identifications, and other equivalences.  It is not the correct test for the
positive weighted Adams edge.

The admitted Adams operation raises grade and strictly decreases the rewrite
measure.  It is a directed end transport, not an invertible reassociation of
the same presentation.  Prior research constructs its composite as

\[
\text{weighted incidence}
\longrightarrow
\text{unitary moving-seam transport}
\longrightarrow
\text{faithful endpoint pushforward},
\]

with exact word composition and strict contraction on every nonunit grade.
Demanding a depth-uniform inverse would reject the intended arithmetic decay
`p^{-k/2}` and would turn a convergent source incidence into an equivalence it
is not meant to be.

## Correct analytic obligations

Separate the cells into two classes.

### Coherence equivalences

Structural associators/unitors and bare moving-seam identifications require
absolute two-sided bounds.  On the selected retained direct sum these are
source-unitary, so both envelopes equal one.

### Directed rewrite morphisms

Weighted Adams transport requires:

1. a strict decrease of the admitted rewrite measure;
2. forward contractivity in the frozen source metric;
3. exact semigroup composition;
4. fixed-intensive-order control along the grade ray;
5. convergence at the declared Adams end;
6. preservation of labels and external interfaces.

No inverse is required unless an inverse Adams rule is separately admitted.
No such rule is part of the selected constructor.

## Consequence

The previously cited inverse-envelope obstruction for weighted Adams is not a
live G2 gate.  The existing exact metric natural-transformation theorem closes
its geometric, coefficient, endpoint, cutoff, Fourier, and word-composition
controls as a directed contraction.

The remaining G2 critical work is therefore the genuinely compositional
source rewrite: two-atom mixed Green/seam compatibility, absence of illicit
primitive `pq` flux, archimedean attachment, and joins with the later Green and
Schur cells.  It is not the construction of a bounded inverse to arithmetic
decay.

This distinction does not weaken the two-sided requirements for actual
coherence isomorphisms.

## Evidence

- `research/nima/moving-seam-transport-and-complete-endpoint-pushforward-form-an-exact-metric-natural-transformation.md`
- `research/nima/prime-power-cut-atoms-form-a-horizontal-section-of-the-moving-seam-bundle.md`
- `research/nima/rh-coherence-cells-must-be-audited-for-absolute-bi-boundedness.md`
- `research/voevodsky/retained_direct_sum_closes_structural_not_incidence_coherence_20260908.md`
