# The theta Ubersector should live in a nuclear rigged exact category

## Bounded attack

The puncture DPC now asks why restricted-product completion cannot lose a
contracting partner inside either open half-plane.  Instead of proving this in
an arbitrary Hilbert completion, test whether the completed theta/Tate source
canonically lives in a category where the relevant completion functor
preserves strict split exactness.

## Candidate carrier category

The source already suggests a rigging of the form

\[
 \mathcal S(\mathbb A)
 \subset L^2(\mathbb A)
 \subset \mathcal S'(\mathbb A),
\]

with local Schwartz--Bruhat factors and restricted tensor products relative
to their canonical vacua.  The test-space level is nuclear; its strong dual
retains distributional boundary currents that are absent from the bare
Hilbert tensor product.

This matches the three Tate strata:

\[
 \begin{array}{c|c}
 k=1 & \text{dual/distributional boundary object}\\
 k=2 & \text{Hilbert boundary object}\\
 k\ge3 & \text{nuclear/trace-class interior readout}.
 \end{array}
\]

The proposed Ubersector is therefore a diagram across the rigging, not one
complex in one normed space.

## Exactness strategy

Construct finite labelled complexes `C_(s,X)` as strictly split complexes of
nuclear test spaces.  Require their contractions to be compatible with the
restricted-product embeddings and equicontinuous for `s` in every compact
subset of either open half-plane.

The hoped-for structural implication is

\[
 \boxed{
 \text{equicontinuously split source complex}
 \Longrightarrow
 \text{strictly exact completed restricted product}.}
\]

Nuclear completed tensor products preserve appropriate strict exact
sequences under hypotheses that arbitrary Banach/Hilbert completions do not.
If the source complex satisfies those hypotheses, completion-stable pairing
could follow from the carrier category rather than from an order-by-order
scalar inequality.

This is not yet an application of a named exactness theorem. One must specify:

1. the precise locally convex or bornological category;
2. whether the restricted product is an inductive limit, projective limit,
   completed tensor product, or a composite of these;
3. the strict morphisms and closed-image condition;
4. continuity and equicontinuity of the source contractions;
5. how the strong dual boundary currents enter without reversing exactness.

## Why the epsilon falsifier is rejected

For

\[
 \mathbb C\xrightarrow{\varepsilon_X}\mathbb C,
 \qquad \varepsilon_X\to0,
\]

the contractions have size `|epsilon_X|^(-1)`. They are not equicontinuous.
Thus this family does not define a strictly split compatible object in the
proposed completed category. The rejection occurs before taking the limiting
cohomology.

This is the exact behavior wanted from a source-authorized type system: the
hostile limit is ill-typed as a completion-stable contraction rather than
being discovered only after it creates a zero.

## Geometric-algebra form

Let `d_s` and `h_s` act as odd operators on the completed exterior/Clifford
module of the labelled source. The identity

\[
 d_sh_s+h_sd_s=1
\]

must hold as a continuous identity in the test-space rigging and extend by
duality to its authorized boundary currents. Nuclear exactness then protects
the pairing under formation of the global restricted product.

An off-seam puncture would require one of three source-visible failures:

\[
 \text{loss of strictness},\qquad
 \text{loss of equicontinuity},\qquad
 \text{unauthorized deletion of a dual boundary state}.
\]

## Hard falsifier

The programme fails if the actual theta/Tate comparison complex cannot be
made strictly split in any source-canonical nuclear rigging, or if its
contractions cease to be equicontinuous on a compact subset strictly inside a
half-plane.  It also fails if a hostile divisor multiplier admits the same
labelled nuclear complex and contractions.

## Present boundary

Nuclearity alone does not imply RH, does not construct the comparison complex,
and does not make every completion exact. The next construction must begin
with local Tate source maps and derive a finite two-term complex whose
contracting homotopy is continuous without using `Xi` or its zeros.

