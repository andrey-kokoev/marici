# A two-chart transition does not fix the common divisor

## Setup

Let \(\Delta_+\) and \(\Delta_-\) be nonzero analytic chart sections on the
upper and lower spectral half-planes.  Suppose their seam transition is

\[
g=\frac{\Delta_+}{\Delta_-}.
\]

The transition records relative sewing.  It does not determine the common
normalization of the two chart sections.

## Common-factor ambiguity

For any entire function \(h\), define

\[
\widetilde\Delta_+=h\Delta_+,
\qquad
\widetilde\Delta_-=h\Delta_-.
\]

Where the ratio is defined,

\[
\frac{\widetilde\Delta_+}{\widetilde\Delta_-}
=
g.
\]

Thus the transition, its reciprocal law, its boundary modulus, and its cocycle
all survive common multiplication.  The divisor does not.

Choose

\[
h(\lambda)=(\lambda-a)^2+b^2,
\qquad
a\in\mathbf R,
\qquad
b>0.
\]

This factor is positive on the real seam and has conjugate zeros
\(a\pm ib\).  It leaves every seam ratio unchanged while inserting one zero
in each open half-plane.

Therefore a source-derived transition alone cannot prove zero confinement.

## What self-adjointness adds

If \(\Delta_\pm\) are actual perturbation determinants of one fixed
self-adjoint operator, resolvent invertibility can make them nonzero in their
respective open half-planes.  The hostile common factor then ceases to be
operator-derived.

But this helps only after the chart sections themselves, not merely their
ratio, have been derived from the source.  The bridge to framed \(\Xi\) must
show that its chart representatives equal the operator determinants up to a
common factor that is both source-fixed and nowhere zero.

## Four pieces of two-chart authority

A completed determinant-line claim needs all four:

1. source-derived upper and lower chart sections;
2. nonvanishing of each chart section off the spectral seam;
3. a source-derived transition and closed cocycle;
4. a source normalization or growth law excluding divisor-changing common
   factors.

The fourth item is independent of transition coherence.

## Categorical reading

The transition defines a line bundle or descent datum.  A divisor belongs to a
section of that line bundle.  Knowing the bundle does not determine the
section.  Common multiplication changes the section while preserving the
descent object.

Thus coherencer authority and section authority are different constructor
types.

## Finite falsifier

Take constant chart sections

\[
\Delta_+=\Delta_-=1,
\qquad
g=1.
\]

Multiply both by \(h(\lambda)=\lambda^2+1\).  The transition remains \(1\),
including unitary seam modulus and zero winding, while the new section has
zeros at \(\lambda=\pm i\).

Any theorem deriving zero-freeness solely from the transition is disproved by
this example.

## Revised frontier

The theta/Tate task is not only to derive the reciprocal scattering or
determinant transition.  It must derive normalized chart determinants from the
fixed self-adjoint source extension and prove that the framed theta section is
their unique admissible glued section under an independently sourced
normalization, asymptotic, or outer-factor law.

