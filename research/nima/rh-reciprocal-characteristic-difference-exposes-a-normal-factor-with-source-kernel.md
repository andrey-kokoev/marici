# The reciprocal characteristic difference exposes a normal factor with source kernel

Scope correction: the displayed variable \(z\) is the real normal coordinate.
For the full complex parameter, the reciprocal characteristic factor uses
\(1-\overline{s}\) and exposes \(2\operatorname{Re}(s)-1\).

## Two labelled characteristic operators

After retaining the full labelled reservoir, the direct and reciprocal sector
adjugates have characteristic factors

\[
\Delta_{+,X}(P)=(P+z)R_X(P),
\]

and

\[
\Delta_{-,X}(P)=(P+1-z)R_X(P),
\]

where

\[
R_X(P)=\prod_{j=1}^{N_X}(P+\lambda_j).
\]

The same reservoir factor occurs because reciprocal sewing changes the sector
coordinate while preserving the labelled source modes.

## Exact normal-factor identity

Subtracting the two ordered sector responses gives

\[
\Delta_{+,X}(P)-\Delta_{-,X}(P)
=2\left(z-\frac12\right)R_X(P).
\]

This is the first exact appearance of the normal displacement in the labelled
reverse-arrow calculation.  It is not yet a Cartan contraction: the normal
factor is multiplied by the common reservoir operator.

## Why the common factor cannot simply be cancelled

For every admitted source mode,

\[
R_X(P)e^{-\lambda_jq}=0.
\]

Hence \(R_X(P)\) is not invertible on the source-generated state space.  The
very vectors that repaired the commutator lie in its kernel.  Cancelling
\(R_X(P)\) would quotient away the labelled reservoir and repeat the original
type erasure.

This yields a precise three-object architecture:

1. the direct observer produces \(\Delta_{+,X}\);
2. the reciprocal observer produces \(\Delta_{-,X}\);
3. a boundary or seam coherencer must resolve the common kernel of \(R_X\).

The third object is not optional bookkeeping.  Without it, the two observers
agree identically on all source reservoir modes, independently of whether
\(z\) lies on the critical seam.

## DPC statement

The reciprocal difference factors through the normal displacement, but only
in the quotient by the common reservoir kernel.  A valid RH-bearing
coherencer must therefore provide a source-derived exact sequence or boundary
pairing that retains the kernel data while making the residual normal factor
observable.

The following shortcuts are rejected:

- algebraically divide by \(R_X(P)\);
- discard its kernel as gauge without source authority;
- infer \(z=1/2\) from vanishing of the sector difference alone;
- replace the kernel by a scalar trace that forgets its labelled multiplicity.

The smallest finite falsifier uses one source mode.  The off-seam vector
\(e^{-\lambda q}\) is killed by both characteristic operators because it lies
in the common reservoir kernel.  Thus sector-response equality alone does not
confine \(z\).

## New frontier

The required additional structure is now sharply typed.  It must be a seam
incidence on the common reservoir kernel, not another bulk adjugate.  Its task
is to distinguish genuine source modes inside \(\ker R_X\), transport that
distinction through cutoff completion, and couple it to the normal factor
without dividing by the completed scalar section.

## Verification

`check_rh_reciprocal_characteristic_factor.py` verifies the polynomial identity
for several labelled cutoffs, confirms linear growth of the common-kernel
dimension, and checks an explicit off-seam common-kernel witness.
