# A type-ascending comparison witness and its next coherence

## Explicit differential-graded realization

Use a differential-graded category of chain complexes, with homological grading.
Degree-zero actual/reference maps C,d are closed. A comparison witness h has

    degree(h)=1, delta(h)=C-d=rho.

Composition obeys the graded Leibniz rule. This supplies an algebraic realization
of higher witnesses, conditional on a carrier differential and admissible lifts.
It is a candidate realization, separate from the still-unspecified endpoint rule
for one-label-per-family promotion.

## Two routes and the first higher witness

For composable witnessed comparisons indexed1,2, there are two composite
homotopies:

    H_first = h2*C1 + d2*h1,
    H_second = C2*h1 + h2*d1.

Both have boundary C2*C1-d2*d1, reproducing the exact three-term residual law

    d2*rho1 + rho2*d1 + rho2*rho1.

Their discrepancy is filled by the degree-two product:

    K=h2*h1,
    delta(K)=rho2*h1-h2*rho1=H_second-H_first.

Thus the compatibility law now has a genuine degree-ascending witness. Its
record retains both homotopy endpoints, the filler, and its parent comparisons.
The mixed residual product is included in the lower boundary calculation; K
carries coherence between its two transport routes.

## The next degree ascent

For three composable witnessed comparisons, T=h3*h2*h1 has degree3. Its boundary
is the signed six-face cube:

    delta(T) = C3*h2*h1 - d3*h2*h1
               - h3*C2*h1 + h3*d2*h1
               + h3*h2*C1 - h3*h2*d1.

Positive and negative face sums have identical boundaries. A second retained
higher-comparison record takes those degree-two sums as endpoints and T as its
filler. The checker verifies its boundary and delta^2=0 exactly. These are
additive higher homotopies of chain maps; they do not identify arbitrary named
globular cells merely because their scalar responses agree.

The same general rule continues: an ordered product of n degree-one witnesses
has degree n, and its boundary is the alternating sum replacing one witness by
its actual-minus-reference boundary. This is cubical coherence, with input
arity tracked separately from the existing proposal of independent product
class doubling.

## What is chosen in the finite model

The test complex has Q^2 in degrees0,1,2,3, differential identity from1 to0 and
from3 to2, and zero elsewhere. It is contractible. Ordinary2x2 matrices embed as
identical diagonal blocks in all four degrees. A canonical degree-one lift
places the residual in blocks0->1 and2->3.

Those canonical lifts realize every embedded residual, but their pairwise
products are zero. Adding a closed degree-one history block1->2 to the middle
witness leaves C,d,rho unchanged and produces nonzero K and T. Both versions
satisfy the same boundary laws. Therefore raw residual data alone do not choose
the higher history.

This auxiliary contractible complex is a test construction, not a derivation
of the carrier's differential or topology. In an ordinary matrix space
concentrated in degree zero with zero differential, a nonzero residual has no
such homotopy filler. The proposed carrier realization must establish the
appropriate image condition rather than importing contractibility.

## Synthesis result and remaining interface

We now have an executable response-compatible higher witness, its next cube
coherence, typed endpoints and retained parent records. The identities follow
from the graded Leibniz rule and use no fitted constants.

Instantiating this construction on the original assembly still requires:

- a composable network or explicit endpoint transports;
- a carrier differential and response embedding;
- admissible lifts and a rule retaining/selecting closed witness history;
- a metric and physical readout compatible with those choices.

These requirements localize the next synthesis task: realize this graded
composition structure on the actual retained path data. The construction by
itself supplies neither a gauge identification nor a numerical constant.

## Verification

    python research/nima/checkers/check_graded_comparison_coherence.py

Exact rational block matrices check both homotopy routes, their degree-two
filler, the degree-three six-face cube, typed endpoint rejection, Leibniz signs,
boundary-of-boundary zero, retained higher-record parents, and two different
higher histories with identical lower actual/reference maps.
