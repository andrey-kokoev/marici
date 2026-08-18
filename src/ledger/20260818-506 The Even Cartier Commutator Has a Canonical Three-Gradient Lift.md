---
id: 506
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Even Cartier Commutator Has a Canonical Three-Gradient Lift

Entry 505 identifies the unique principal homotopy coefficient

\[
h=2am,qquad m=fL_1^{e_a}L_2^{e_b},
\]

for the commutator

\[
[q,a^2](f)=hK.
\]

The lifting equation into the retained three-gradient complex is solved
canonically by the Euler bridge of Entry 493:

\[
K=\frac a4K_a+\frac u2K_u.
\]

Multiplication by (h) gives

\[
\boxed{
hK=
\frac{a^2m}{2}K_a
+uamK_u.
}
\]

Thus the required gradient vector is

\[
\boxed{
H_{a^2}(f)=
\left(\frac{a^2m}{2},,0,,uam\right).
}
\]

It is polynomial, sector-uniform, and uses no fitted splitting.  Under
(ho(a)=-a), the Euler vector is equivariant because (a e_a) and
(u e_u) are invariant.  Hence the lift respects the mechanical deck
action.

At (u=0), it specializes to

\[
H_{a^2}(f)|_{u=0}
=
\left(\frac{a^2m}{2},0,0\right).
\]

## Consequence

Entry 504's rank-one multiplication commutator is nullhomotopic in the
source-defined principal-to-three-gradient comparison.  Therefore a
corrected derived (a^2)-operation exists without adding a carrier cell.

This does not yet prove that its induced action on the stable plus defect is
zero.  The homotopy component contributes to the mapping-cone action and
must be retained in that calculation; applying naive multiplication to
cokernel representatives remains invalid.

## Next falsifier

Build the corrected mapping-cone action

\[
M_{a^2}^{\mathrm{corr}}=(a^2,H_{a^2})
\]

on the cutoff complexes and compute its induced map on the stable
(u)-homology across (D\to D+2).  Entry 503's incidence hypothesis
predicts zero on the one-dimensional plus defect.  A nonzero induced map
falsifies the reduced incidence quotient.

## Evidence

- `research/benincasa/marici-gm/src/bin/soft_axis_a2_euler_homotopy.rs`;
- Entries 493, 504, and 505.
