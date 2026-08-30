# Coupled Gain Reachability Can Certify When Boxes Cannot

## Question

Does retaining cross-setting calibration covariance merely tighten a robust
determinant bound, or can it change whether the instrument certifies at all?

## Shared-mode model

Let one latent detector mode \(\theta\) determine all four imbalance products:

\[
(k_{XX},k_{YY},k_{XY},k_{YX})
=
(\theta,-\theta,\theta,-\theta).
\]

Suppose calibration leaves exactly two reachable gain states,

\[
\theta\in\{-3/100,3/100\}.
\]

This is a coupled reachable set with two trajectories. Its coordinate-wise
projection is the box in which each setting may independently take either
sign. That box contains sixteen combinations, fourteen of which violate the
shared-mode dynamics.

## Exact separating fixture

Take true coherence coordinates

\[
\operatorname{Re}z=1/50,
\qquad
\operatorname{Im}z=3/100,
\]

so

\[
|z|^2=13/10000.
\]

Let the population product be

\[
bc=1/1000.
\]

The true NPT margin is \(3/10000\).

Generate the observed four-setting packet with the positive shared gain mode.
Correcting it over both reachable coupled modes gives a minimum coherence norm
of \(13/10000\); the other reachable reconstruction has a larger norm. The
coupled worst-case margin therefore remains \(3/10000\) and certifies NPT.

Now forget the shared-mode relation but retain the same marginal gain values at
each setting. Enumerating the sixteen Cartesian combinations produces a
strictly smaller coherence norm below \(1/1000\). The box margin is negative
and cannot certify.

No new measurement uncertainty was introduced. The loss comes entirely from
admitting gain trajectories that the Carrier dynamics forbids.

## Control interpretation

A robust certificate must propagate the reachable nuisance set, not the
product of its coordinate projections. Marginal intervals forget dynamic and
cross-channel constraints. That forgetful map can cross a nonlinear decision
boundary even when the original reachable set does not.

The relevant Marici object therefore includes the relation among calibration
coordinates. Four scalar gain intervals are projections of the sensor-state
Carrier; they are not necessarily a complete sensor state.

This is the same structural lesson as the capability correspondence:
compatible tuples form a locus inside a Cartesian product. Robust optimization
over the full product can be safe but needlessly inconclusive. Robust
optimization over the source-derived compatibility locus is both safe and more
informative.

## Acquisition consequences

Cross-setting covariance may come from:

- one monitored common gain mode with known analyzer response signs;
- shared detector electronics;
- a low-dimensional drift model fitted to interleaved anchors;
- simultaneous calibration records linked to several settings;
- or a state estimator retaining the joint posterior/support set.

The relation must be source-derived and verified. Fitting covariance solely to
recover a desired determinant sign would replace conservative uncertainty with
an unjustified restriction.

## Verification boundary

The dependency-free exact checker enumerates both coupled gain trajectories and
all sixteen Cartesian combinations. It verifies that the coupled worst-case
margin is positive while the box worst-case margin is negative, with identical
per-setting marginal gain sets.

This finite two-mode result does not derive the shared detector model for a
particular apparatus. Aspect's instrument must establish that model through
calibration and hardware provenance before using the tighter certificate.
