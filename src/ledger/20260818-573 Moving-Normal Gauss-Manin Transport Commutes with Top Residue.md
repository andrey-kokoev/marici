---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# Moving-Normal Gauss--Manin Transport Commutes with Top Residue

## Question

Entry 571 proved the Cousin identity for literal logarithmic
representatives.  This entry tests whether their residue maps are natural
under kinematic transport.  Since the source denominator hyperplanes move
with the energies, differentiating at fixed loop variables is not the typed
comparison.  The correct derivative holds their normal coordinates fixed.

## Horizontal lifts

Write

\[
(c,a,b)=(y_{12},y_{23},y_{31})
\]

and retain

\[
q_1=X_1+c+b,
\qquad
q_2=X_2+c+a,
\qquad
q_3=E+c.
\]

Solving (D_iq_j=0) for all (j) gives the unique moving-normal lifts

\[
\boxed{
D_{X_1}=\partial_{X_1}-\partial_c+\partial_a,
}
\]

\[
\boxed{
D_{X_2}=\partial_{X_2}-\partial_c+\partial_b,
}
\]

and

\[
\boxed{
D_{X_3}=\partial_{X_3}-\partial_c+\partial_a+\partial_b.
}
\]

The exact checker verifies all nine identities

\[
D_{X_i}q_j=0.
\]

Hence every (d\log q_j) normal factor is horizontal.

## Twist comparison

On the clean triple section,

\[
K_\Sigma
=
E^2\ell_-^2\ell_+^2,
\]

where

\[
\ell_-=X_2+X_3-X_1,
\qquad
\ell_+=X_1+X_3-X_2.
\]

Exact symbolic differentiation in all three kinematic directions verifies

\[
\boxed{
(D_{X_i}K)|_\Sigma
=
\partial_{X_i}(K|_\Sigma).
}
\]

Thus the Kummer connection induced on the iterated residue line is

\[
\nabla_\Sigma
=
d+\gamma\,d\log K_\Sigma
=
d+2\gamma
\left(
d\log E+d\log\ell_-+d\log\ell_+
\right).
\]

Its support consists only of three existing energy letters.

## Naturality result

For the top logarithmic representative and both mixed-face residues,

\[
\boxed{
\nabla\operatorname{Res}_{q_j}
=
\operatorname{Res}_{q_j}\nabla
}
\]

on the clean support subquotient.  The same identity holds after the second
residue to the (q_{\mathcal G_{12}})-closed target.  Consequently the
anticommuting square of Entry 571 is a square of local systems, not only a
fiberwise exterior-algebra identity.

## Classification and scope

- moving normal coordinates: source denominator geometry;
- residue maps: shared Cartier/Gysin calculus;
- induced connection: sector-specific Kummer coefficient object;
- singular support: existing total and signed-energy letters;
- new carrier datum: none.

This verifies Gauss--Manin naturality on the canonical rank-one clean
support subquotient.  It does not yet construct full (21\times21),
(18\times18), and (16\times16) connection matrices or prove that the
support filtration splits globally.

## Next falsifier

Transport the clean rank-one top line around each of

\[
E=0,
\qquad
\ell_-=0,
\qquad
\ell_+=0
\]

and compare its Kummer characters with the corresponding mixed-face and
\(q\)-only nearby cycles.  The first possible obstruction is no longer
failure of residue naturality; it is a nontrivial extension of this line by
the remaining rank-20 top module at the energy boundaries.

## Evidence

- `research/benincasa/marici-gm/src/bin/top_sector_residue_boundary.rs`;
- `research/benincasa/top-sector-residue-boundary.json`;
- Entries 340, 568, and 571.

## Outcome contract

~~~json
{
  "claim": "Moving-normal Gauss-Manin transport fails to commute with the source top residues.",
  "status": "falsified_on_the_clean_rank_one_support_subquotient",
  "horizontal_lifts": [[-1, 1, 0], [-1, 0, 1], [-1, 1, 1]],
  "all_q_horizontal": true,
  "twist_derivatives_commute": true,
  "connection_support": ["E", "X2+X3-X1", "X1+X3-X2"],
  "new_carrier_datum": false,
  "next_experiment": "Compute nearby-cycle compatibility and extension data at the three energy boundaries."
}
~~~
