---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Independent Scaling Fiber Replicates the Canonical Marked Wall Data

## Question

Entry 375 tested the generic four-stratum reduction engine only at
\((x,y)=(1,3)\). Freeze the harder claim

\[
\boxed{\text{the canonical seven-coordinate projection fails at the
independent nonsymmetric scaling fiber }(x,y)=(2,5).}
\]

The expected values are taken without modification from the source-derived
one-wall and two-wall certificates, both of which predate the generic engine.

## Frozen path and calculation

Use

\[
u=E,\qquad v=2(x+y)-E=14-E,
\qquad \frac d{dE}=\partial_u-\partial_v.
\]

The marked walls are retained in their source form

\[
\ell_1=b+x-E,\qquad \ell_2=a+y-E.
\]

At 80 exact points over the prime
\(2305843009213693951\), reduce the three marked masters against the same
four exact-denominator strata and project to

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_6,e_7,e_8,e_9).
\]

Bounded rational reconstruction uses all samples. The largest selected
numerator and denominator degrees remain 14 and 16. One global sign is fixed
only by the predeclared source normalization
\([E^{-2}e_6]\nabla\Omega_{111}=1/8\).

## Exact replication

For the first wall, the source-normal algebraic tail is

\[
[e_7,e_8,e_9]
=\left[\frac3{40},-\frac1{140},\frac1{140}\right],
\]

and the exchanged wall gives

\[
[e_7,e_8,e_9]
=\left[-\frac3{40},\frac1{140},-\frac1{140}\right].
\]

Both marked quotient residues vanish. For the two-wall master,

\[
[E^{-2}e_6]\nabla\Omega_{111}=\frac18,
\]

while the source-normal first grade is

\[
[\Omega_{111},\Omega_{101},\Omega_{110}]
=\left[1,-\frac1{10},-\frac14\right],
\]

\[
[e_7,e_8,e_9]
=\left[-\frac9{800},\frac3{2800},-\frac3{2800}\right].
\]

Every value agrees with the frozen certificates.

## Verdict

The tested claim is falsified:

\[
\boxed{\text{the canonical marked projection survives the independent
nonsymmetric scaling fiber without a new denominator stratum.}}
\]

Together with Entry 375, this removes the simplest one-fiber interpolation
failure. It is evidence for a common marked relative coefficient geometry,
not a universal identity in \((x,y)\).

## Classification and boundary

| Datum | Classification |
|---|---|
| two marked-wall divisors | existing Cut/energy carrier |
| seven fixed coordinates | relative coefficient data |
| five unfixed coordinates | exact-lift gauge |
| residual denominator | none |
| new carrier datum | none found |

The next falsifier is the radial pullback of this seven-coordinate projection.
It must include the already frozen rank-nine Rees weights and the
\(e_6/(8E)\) marked shear. A pole away from the strict transforms of the
energy, soft, conductor, or Cut divisors would be new support; it must not be
removed by fitting a new frame.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_wall_second_fiber.rs`;
- `research/benincasa/marked-wall-second-fiber-certificate.json`;
- `research/benincasa/one-wall-total-energy-extension.json`;
- `research/benincasa/two-wall-second-rees-extension.json`;
- Entries 374 and 375.
