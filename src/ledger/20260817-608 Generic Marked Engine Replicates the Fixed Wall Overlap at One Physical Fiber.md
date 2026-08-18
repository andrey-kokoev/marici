---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Generic Marked Engine Replicates the Fixed Wall Overlap at One Physical Fiber

## Question

Entry 374 constructed the generic four-stratum reduction engine. Its first
source-replication claim is

\[
\boxed{\text{the canonical seven-coordinate projection fails to reproduce
the fixed one- and two-wall Laurent data.}}
\]

## Physical wall path

Freeze

\[
x=1,\qquad y=3,
\]

and vary total energy with

\[
u=E,\qquad v=2(x+y)-E=8-E.
\]

Thus the physical normal derivative at fixed \((x,y)\) is

\[
\frac d{dE}=\partial_u-\partial_v.
\]

The engine is evaluated at 80 exact finite-field points on this path. For
each invariant coordinate, bounded rational reconstruction is performed on
\(E A_E\) for the one-wall classes and \(E^2A_E\) for the two-wall top class.
The largest selected numerator and denominator degrees are 14 and 16.

One global connection sign is calibrated by the frozen source datum

\[
[E^{-2}e_6]\nabla\Omega_{111}=\frac18.
\]

No coordinate-dependent sign or normalization is fitted.

## One-wall replication

For \(\Omega_{101}\), the reconstructed source-normal residues in the
canonical overlap are

\[
[e_7,e_8,e_9]
=
\left[\frac16,-\frac1{24},\frac1{24}\right].
\]

For \(\Omega_{110}\), they are

\[
[e_7,e_8,e_9]
=
\left[-\frac16,\frac1{24},-\frac1{24}\right].
\]

The marked quotient residues vanish. These are exactly the specialization of
the frozen one-wall formulas and their exchanged companion at \((x,y)=(1,3)\).

## Two-wall replication

The second ordinary grade is

\[
\boxed{[E^{-2}e_6]\nabla\Omega_{111}=\frac18.}
\]

The fixed first-grade coordinates are

\[
[\Omega_{111},\Omega_{101},\Omega_{110}]
=
\left[1,-\frac16,-\frac12\right],
\]

\[
[e_7,e_8,e_9]
=
\left[-\frac1{18},\frac1{72},-\frac1{72}\right].
\]

These agree with the universal patterns inferred from the independent source
fibers in the earlier two-wall certificate.

## Verdict

The tested claim is falsified:

\[
\boxed{\text{the generic engine reproduces every fixed wall coordinate at
the tested physical fiber.}}
\]

No new denominator stratum is required. The result validates the engine on
the intrinsic seven-coordinate overlap; it does not select values for the
five exact-lift-gauge coordinates.

## Epistemic scope and next falsifier

This is one physical wall fiber over one large prime. Rational fits use all
80 exact samples and bounded degree search, but no universal cleared identity
in \((x,y)\) is claimed.

The next test is replication at a nonsymmetric second fiber, followed by the
radial pullback of the invariant seven-coordinate projection. Failure at the
second fiber falsifies universality of the present reconstruction. If it
passes, any radial pole outside the frozen energy/soft/conductor divisors is
the remaining rank-twelve support falsifier.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_wall_replication.rs`;
- `research/benincasa/marked-wall-replication-certificate.json`;
- `research/benincasa/one-wall-total-energy-extension.json`;
- `research/benincasa/two-wall-second-rees-extension.json`;
- Entry 374.
