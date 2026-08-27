# Scalar Tate cumulants cannot yet balance quadratic Ward curvature

## Prime-two typing audit

At the prime-two cutoff, the input tower supplies the exclusion projection

\[
P_{2\nmid n}.
\]

Its Ward observable on a labelled state (c) is

\[
W_2(c)=\lVert P_{2\nmid n}c\rVert^2.
\]

This is a quadratic, state-dependent quantity on the integer-label module.

The independently derived local Tate boundary determinant has

\[
q=2^{-s}
\]

and logarithmic cumulants

\[
2q,
\qquad
q^2,
\qquad
\sum_{k\ge3}\frac{2}{k}q^k.
\]

These are scalar, state-independent coordinates on the determinant line.
Their source provenance is sound, but they are not yet boundary quadratic
forms on the labelled state.

## Exact degree obstruction

Suppose a fixed scalar boundary current (b_2(s)) balanced the Ward port for
every admissible amplitude:

\[
W_2(c)=b_2(s).
\]

Under (c\mapsto\lambda c),

\[
W_2(\lambda c)=|\lambda|^2W_2(c),
\]

while (b_2(s)) is unchanged. Therefore the proposed equality cannot be a
homogeneous state-space identity unless (W_2(c)=0), which the canonical
vacuum forbids.

Normalizing (c) does not repair the typing. It merely restricts the domain
and still leaves the determinant cumulant without a source-defined action on
the labelled directions.

## Required lift

The boundary tower must supply an operator-valued or sesquilinear lift

\[
K_{2,s}:C_X\longrightarrow C_X
\]

whose quadratic readout is

\[
B_{2,s}(c)=\langle c,K_{2,s}c\rangle.
\]

Only then can the typed defect residual be formed:

\[
R_{2,s}(c)
=
\langle c,(P_{2\nmid n}-K_{2,s})c\rangle.
\]

For all primes and cutoff (X), the required object is a compatible family

\[
K_{p,s,X}
\]

acting on the same labelled module as the exclusion projections.

The scalar cumulants (2q), (q^2), and the connected tail should be
recovered as traces, determinant-line characters, or boundary matrix
coefficients of this lift. They cannot themselves be substituted for it.

## Categorical interpretation

The shared defect codomain is not the scalar determinant line. It is a
category of quadratic forms or endomorphisms on the labelled state. The
determinant line and the scalar Ward energy are two later decategorifications.

Thus the horizontal comparison channel needs one more relational rung:

\[
\text{boundary cumulant}
\longleftarrow
\text{operator-valued boundary lift}
\longrightarrow
\text{labelled Ward form}.
\]

This is not an extra physical sector. It is the missing common refinement
from which the two currently incomparable readouts descend.

## Source-authority gates

A valid (K_{p,s,X}) must:

1. be derived from valuation shift, augmentation boundary, reciprocal sewing,
   and the retained seam state;
2. exist before a zero or Ward balance is imposed;
3. reproduce primitive, square, and connected cumulants under the declared
   determinant readout;
4. act on the integer-label module without erasing the vacuum;
5. be compatible with cutoff restriction and Fourier--Tate transport;
6. yield the Green boundary term without being defined from
   (P_{p\nmid n}).

## Smallest falsifier

At (p=2), derive the proposed (K_{2,s}) and compare its action on
(e_1,e_2,e_3). The route fails if:

- the lift is only a scalar multiple of the identity with no valuation
  incidence;
- it cannot distinguish odd from even labels where the boundary law requires
  that distinction;
- its determinant cumulants disagree with (2q,q^2,ldots);
- it is obtained by setting (K_{2,s}=P_{2\nmid n}) without a source
  derivation;
- the residual vanishes only after tracing or scalar summation.

