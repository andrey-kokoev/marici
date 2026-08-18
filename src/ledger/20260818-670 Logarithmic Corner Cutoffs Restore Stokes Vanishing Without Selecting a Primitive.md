---
authors:
  - marici.Nima
date: 2026-08-18
---
# 670 — Logarithmic Corner Cutoffs Restore Stokes Vanishing Without Selecting a Primitive

## Hard-to-vary claim

At a generic transverse corner \(K_E=q_i=0\), every complete
source-logarithmic primitive has vanishing corner contribution at the
physical value \(\epsilon=0\) under the monomial cutoffs intrinsic to the
real-oriented/logarithmic blowup.  The extra pointwise divisibility condition
tested in Entry 669 is sufficient but not necessary.

## Local SNC model

Use local normal-crossing coordinates

\[
r=K_E,
\qquad
s=q_i.
\]

At the physical source weight, suppressing bounded unit factors, the bulk
two-form has order

\[
\Omega\sim r^{\epsilon-1/2}s^{-1}\,dr\wedge ds.
\]

For a vector field logarithmic along both faces,

\[
V=rA\partial_r+sB\partial_s,
\]

the primitive is

\[
\iota_V\Omega
=
r^{\epsilon+1/2}s^{-1}A\,ds
-
r^{\epsilon-1/2}B\,dr.
\]

## Oriented two-face asymptotics

On the \(r=\delta\) face, use a monomial corner cutoff

\[
s_{\min}=\delta^p,
\qquad p>0.
\]

The corner part has order

\[
\delta^{\epsilon+1/2}
\int_{\delta^p}\frac{ds}{s}
=
O\!\left(\delta^{\epsilon+1/2}\log\delta\right).
\]

On the \(s=\delta^p\) face, the corner part has order

\[
\int_0^\delta r^{\epsilon-1/2}\,dr
=
O\!\left(
\frac{\delta^{\epsilon+1/2}}{\epsilon+1/2}
\right).
\]

Both vanish in the common chamber

\[
\operatorname{Re}\epsilon>-\frac12,
\]

including \(\epsilon=0\).  No cancellation between the two faces is needed.

## Consequence for Entry 669

Entry 669 correctly proves that no minimal degree-seven syzygy removes every
pointwise \(s^{-1}\) coefficient on the \(K_E\)-face.  The logarithmic
corner integral shows why that does not obstruct Stokes: the gained
\(r^{1/2}\) order beats the logarithmic \(s\)-divergence for every monomial
approach to the corner.

Therefore all three minimal primitives remain admissible at generic
transverse corners.  Corner regularity again fails to choose a distinguished
direction:

\[
\boxed{
\text{generic smooth faces and generic SNC corners preserve the full
three-dimensional primitive ambiguity.}
}
\]

This shifts the frontier away from generic regulator asymptotics.  Any
selection or anomaly must occur at a nontransverse/singular corner, depend
on non-logarithmic cutoff data, or arise from a physical-chain/Gysin
normalization.

## Scope

The result uses bounded logarithmic coefficients \(A,B\), transverse local
coordinates, and monomial/log-blowup cutoffs.  It does not establish
independence under arbitrary non-monomial approaches such as exponentially
coupled cutoffs, nor does it cover singular points of \(K_E=0\).

## Updated frontier

Audit the five restricted polynomials \(K_E|_{q_i=0}\) for multiple roots.
Simple roots are covered by this entry.  Only multiple roots or collisions
with other marked walls require a new local model and can still generate a
regulator-sensitive primitive selection.

## Evidence

- `research/benincasa/physical_log_corner_stokes.py`;
- Entries 651--652 and 668--669.

## Outcome contract

~~~json
{
  "claim": "Failure of pointwise wall divisibility forces a nonzero Stokes corner anomaly for every minimal source syzygy.",
  "status": "falsified",
  "local_model": "transverse SNC K_E=q_i=0",
  "K_face_integral_order": "delta^(epsilon+1/2)*log(delta)",
  "q_face_integral_order": "delta^(epsilon+1/2)/(epsilon+1/2)",
  "physical_epsilon_zero_vanishes": true,
  "primitive_dimension_remaining": 3,
  "singular_corners_tested": false,
  "next_experiment": "Detect multiple roots of K_E restricted to every marked wall and their marked-wall collisions."
}
~~~
