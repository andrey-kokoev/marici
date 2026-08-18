---
authors:
  - marici.Nima
date: 2026-08-18
---
# 669 — No Minimal Source Syzygy Is Uniformly Improved at All Five K–Wall Corners

## Hard-to-vary claim

None of the three minimal degree-seven source-logarithmic vector fields has
an extra Cayley--Menger normal factor at all five codimension-two strata

\[
K_E=q_i=0.
\]

Thus Entry 668's generic smooth-boundary vanishing does not extend by a
single uniformly improved minimal primitive across the complete marked
divisor.

## Corner condition

Write a complete logarithmic syzygy as

\[
V(K_E)=n_0K_E,
\qquad
V(q_i)=\lambda_iq_i.
\]

On the \(K_E\)-face, the primitive flux retains a marked factor

\[
K_E^{\epsilon+1/2}\frac{n_0}{q_i}.
\]

A source-derived sufficient condition for removing this corner pole is

\[
n_0|_{K_E=0}\in(q_i),
\]

or equivalently

\[
n_0\in(K_E,q_i).
\]

The checker imposes this ideal-membership condition coefficientwise.  It
does not replace it by the stronger global divisibility condition
\(q_i\mid n_0\), although both ranks are retained as a cross-check.

## Exact finite-field result

Within the stable three-dimensional degree-seven syzygy space, the
dimensions satisfying the individual corner conditions are

\[
\boxed{(1,1,2,2,2)}
\]

for

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}},q_{g_{31}}).
\]

The same dimensions arise from global wall divisibility, but that equality
is observed rather than assumed.

Imposing all five ideal-membership conditions simultaneously gives

\[
\boxed{
\dim\{V:n_0\in\bigcap_i(K_E,q_i)\}=0.
}
\]

Both statements reproduce at the generic fibers

\[
(x,y,z)=(2,3,4),\qquad(3,5,7)
\]

over \(\mathbb F_{2305843009213693951}\).

## Consequence

The codimension-two audit does not break the three-dimensional ambiguity by
selecting a distinguished minimal primitive.  Instead, the strongest
uniform corner-regularity condition excludes all three directions.

This does not prove the physical IBP identities invalid.  Corner residues
may cancel between boundary faces, be integrable without pointwise
vanishing, or require a relative-chain/Stokes prescription.  It does prove
that generic \(K_E\)-face vanishing cannot be promoted to complete-divisor
vanishing merely by choosing one of the existing degree-seven syzygies.

At the meta level, regulator geometry has changed roles: it is not a
normalization that selects one primitive.  It is an obstruction showing
that the primitive must be interpreted in a combined corner complex.

## Updated frontier

Construct the oriented two-face corner functional for each
\(K_E=q_i=0\), adding the \(K_E\)-face and \(q_i\)-face contributions before
taking \(\epsilon\to0\).  Test whether their polar terms cancel for the
source-prescribed combination.  Only this summed Stokes calculation can
distinguish a genuine corner anomaly from failure of pointwise uniform
vanishing.

## Evidence

- `research/benincasa/check_shared_wall_log_syzygy.rs`, schema v4;
- Entries 651--652 and 668.

## Outcome contract

~~~json
{
  "claim": "A nonzero minimal degree-seven source syzygy has improved K-normal order at every marked K_E=q_i corner.",
  "status": "falsified",
  "minimal_syzygy_dimension": 3,
  "individual_corner_subspace_dimensions": [1, 1, 2, 2, 2],
  "all_corner_intersection_dimension": 0,
  "generic_fibers": [[2, 3, 4], [3, 5, 7]],
  "pointwise_corner_vanishing_required_for_physical_IBP": "not established",
  "next_experiment": "Compute the summed oriented two-face Stokes functional at every K_E=q_i corner."
}
~~~
