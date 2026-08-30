# Off-seam divisor charge is the diffuse part of the seam phase measure

## Completed and Euler-normalized boundary phases

Write

\[
\xi(s)=A_\infty(s)E_+(s),
\qquad
A_\infty(s)=\frac12s^2\pi^{-s/2}\Gamma(s/2),
\]

where

\[
E_+(s)=\frac{s-1}{s}\zeta(s).
\]

On the critical seam the completed function is real. Choose the lifted phase
obtained by upward traversal with right-sector semicircular indentations at
seam zeros. If `nu_seam` is the multiplicity measure of those zeros, then the
phase identity holds distributionally:

\[
d\arg E_+
+d\arg A_\infty
=
\pi\,d\nu_{\mathrm{seam}}.
\]

Every boundary zero contributes its sector half-index `m pi` to this lifted
phase.

## Hardy decomposition

For the endpoint-reduced bounded-type carrier, write the boundary phase as

\[
d\arg E_+
=
\mathcal H\bigl(d\log|E_+|\bigr)+\kappa_+.
\]

There is no separate singular-inner measure for this normalization. The
remaining inner current is the Blaschke current of open-sector zeros.
Combining the two identities gives

\[
\pi\,d\nu_{\mathrm{seam}}
=
d\arg A_\infty
+\mathcal H\bigl(d\log|E_+|\bigr)
+\kappa_+.
\]

Equivalently, define the source-visible supply measure

\[
d\mu_{\mathrm{supply}}
=
\frac1\pi
\left(
d\arg A_\infty
+\mathcal H(d\log|E_+|)
\right).
\]

Then

\[
d\mu_{\mathrm{supply}}
=
d\nu_{\mathrm{seam}}-\frac1\pi\kappa_+.
\]

## Atomic versus diffuse realization

A right-sector zero `w=a+ib` contributes

\[
-\frac1\pi\kappa_{+,w}(t)\,dt
=
\frac1\pi
\frac{2a}{a^2+(t-b)^2}\,dt.
\]

This is a positive Poisson density of total mass `2` under the present
one-sector phase convention. As `a` tends to zero from the right, the density
converges distributionally to twice a point mass at `b`; after sector
half-index normalization, one copy becomes the seam fold atom.

Thus the same divisor supply has two geometrically distinct realizations:

- a seam zero is an atomic boundary fold;
- an off-seam zero is diffuse harmonic measure on the seam.

Reciprocal doubling supplies the matching left-sector profile and restores
integral global multiplicity.

## RH as atomicity

The saturation defect is precisely the diffuse part of the source-visible
phase measure. RH is equivalent to the assertion that

\[
d\mu_{\mathrm{supply}}=d\nu_{\mathrm{seam}},
\]

so every unit of divisor supply is realized atomically on the fixed seam and
no Poisson component remains suspended in either open sector.

This is not merely a count. It is a measure-level statement and therefore
retains height localization. A hostile off-seam quartet inserts a positive
pair of Poisson profiles while preserving reciprocal total charge.

## Deutsch--Popperian target

The new hard-to-vary conjecture is:

> Labelled theta--Poisson sewing produces a purely atomic supply measure, and
> its atoms are exactly the transverse seam folds of the completed section.

The sharp falsifier is any nonzero absolutely continuous Poisson component in
`mu_supply` after all authorized archimedean and anomaly-frame terms are
removed. Since such a component is positive, it cannot be hidden by
cancellation with another off-seam zero in the same sector.

## Scope

This packet derives the distributional decomposition and identifies RH with
atomic saturation. It does not prove that the theta supply measure is purely
atomic and does not prove RH.
