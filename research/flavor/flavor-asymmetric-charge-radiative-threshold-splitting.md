# Asymmetric Charge Allows Radiative Splitting of the Equal Threshold

## Question

Does WP836's equal-singular spectral minimum protect the primitive three-state
packet from the partial threshold deletion that obstructs WP841?

## Tree-level degeneracy

On the WP837 current-aligned ray,

\[
D=mH_q,
\qquad D^TD=m^2I.
\]

All three singular thresholds are equal at tree level. If this equality were
protected, the three charged states would decouple together and the
intermediate active packet ({2,3}) used in WP841--WP843 would not occur.

## Covariant radiative hostile

The asymmetric source also contains

\[
Q=\operatorname{diag}(1,2,3).
\]

The self-adjoint correction

\[
\Pi=\epsilon Q^2,
\qquad \epsilon>0,
\]

is weak-basis covariant: under (Q\mapsto UQU^\dagger), it transforms by the
same conjugation. The corrected squared thresholds are

\[
m^2+\epsilon,qquad m^2+4\epsilon,qquad m^2+9\epsilon.
\]

They are distinct for every nonzero (epsilon). This is an allowed covariant
hostile, not a claim that every admitted microscopic action produces precisely
this self-energy. Its existence proves that equal singular values are not
protected by covariance or by the primitive charge data alone.

The shift-insensitive hostile

\[
\epsilon(Q-2I)^2=\epsilon\operatorname{diag}(1,0,1)
\]

also splits the middle state from the endpoints.

## Symmetry obstruction

Because (Q) has simple spectrum, every operator commuting with it is
diagonal. No commuting symmetry mixes the three charge eigenspaces
transitively to enforce equal self-energies. More strongly, the common
commutant of (Q) and the current reflection (H_q) is scalar.

For a quadratic covariant correction

\[
aI+bQ+cQ^2,
\]

equality on all three eigenvalues forces (b=c=0). Therefore the asymmetric
charge operator permits no nonconstant quadratic correction that preserves
the degeneracy.

## Required cancellation

The traceless splitting is

\[
\Pi_{\rm tl}
=\epsilon\left(Q^2-\frac{14}{3}I\right),
\qquad
\operatorname{Tr}\Pi_{\rm tl}^2
=\frac{98}{3}\epsilon^2>0.
\]

Exact common-threshold protection requires another source contribution to
cancel this entire traceless operator, not merely its trace. Choosing that
counterterm after requiring degeneracy is tuning unless a Ward identity,
supersymmetry, or other admitted nonrenormalization theorem derives it.

## Consequence

WP836 supplies tree-level equal singular shape, not threshold survival. The
same asymmetry that fixes the portal orientation generically opens a
radiative splitting channel. The source principle must reconcile these two
requirements by deriving both:

1. the asymmetric charge operator and diameter-normalized portal flow;
2. a symmetry or dynamical identity canceling every charge-dependent
   traceless threshold self-energy while retaining the labelled contrast.

No current flavor packet supplies such an identity. Without it, sequential
decoupling reopens WP843's noncontractive matching gate.

## Disposition

Exact negative protection result. Equal singular thresholds are a tree-level
rigidification, not a radiatively stable selector, under the currently
authorized source data. The smallest falsifier is any (epsilon Q^2) with
(epsilon>0).

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp844_asymmetric_charge_radiative_threshold_splitting.py
```
