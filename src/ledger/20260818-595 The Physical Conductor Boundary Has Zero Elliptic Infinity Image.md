---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Physical Conductor Boundary Has Zero Elliptic Infinity Image

## Supported class from Entry 594

The obstruction to q-only descent is represented by simple residues at the
conductor roots

\[
R_i(t)=0
\]

on the three normalized shared walls.  This is finite supported data, so its
possible elliptic image is governed by the support-base-change test of Entry
236.

## Projective support test

All three square roots (R_i(t)) are quadratic in their affine wall
parameter.  Their leading coefficients are

\[
\operatorname{lc}(R_1)=-x,
\qquad
\operatorname{lc}(R_2)=y,
\qquad
\operatorname{lc}(R_3)=z.
\]

After projective homogenization, evaluation at the wall point at infinity is
therefore respectively

\[
-x,qquad y,qquad z.
\]

On the generic nonsoft open (xyz\ne0), none vanishes.  Hence every
conductor root is in the finite affine chart and

\[
\boxed{
\operatorname{Supp}(\partial_W\omega_{\rm phys})
\cap D_\infty=\varnothing.
}
\]

## Infinity-Gysin consequence

Let (i_C) denote the inclusion of the finite conductor support and
(j_\infty) the infinity boundary.  The Cartesian pullback is empty, so
proper/support base change gives

\[
j_\infty^*i_{C!}=0.
\]

Since the elliptic infinity-Gysin projection factors through this boundary
restriction,

\[
\boxed{
R_\infty(i_{C!}\partial_W\omega_{\rm phys})=0.
}
\]

Thus the physical conductor obstruction cannot generate the rank-two
Legendre quotient.  Whenever a source-defined supported pushforward into the
nine-master sequence is constructed, its image is forced into

\[
\ker R_\infty=\mathcal T_7,
\]

the rank-seven algebraic/Tate kernel.

This does not construct coordinates in (mathcal T_7), nor does it turn the
relative physical class into an absolute q-only class.  It constructs the
support-level zero elliptic component of the required localization-triangle
morphism.

## Evidence

- `research/benincasa/physical_g12_conductor_infinity_support.py`;
- Entry 236 and `research/benincasa/finite-wall-infinity-gysin.json`;
- Entries 592--594.

## Outcome contract

~~~json
{
  "claim": "The nonzero conductor boundary of the physical q_G12 residue may map directly to the elliptic infinity quotient.",
  "status": "falsified",
  "wall_root_degrees": [2, 2, 2],
  "projective_infinity_values": ["-x", "y", "z"],
  "generic_open": "x*y*z != 0",
  "conductor_support_meets_infinity": false,
  "elliptic_gysin_image_rank": 0,
  "conditional_supported_placement": "rank-seven algebraic/Tate kernel T7",
  "next_experiment": "Construct the source-defined supported pushforward and determine its coordinates and flat saturation inside T7."
}
~~~
