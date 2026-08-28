# The divisor supply has a positive atomic--diffuse Lebesgue decomposition

## Canonical factorization formula

Let `E_+` be the endpoint-reduced bounded-type Euler section in
`Re(s)>1/2`. Write each right-sector zero as

\[
\rho=\frac12+a_\rho+i\gamma_\rho,
\qquad a_\rho>0,
\]

with multiplicity `m_rho`. The Blaschke condition supplied by bounded type
ensures that the associated Poisson-kernel sum converges as a locally finite
boundary measure.

The supply measure constructed from the archimedean phase and the outer
boundary magnitude has the exact decomposition

\[
d\mu_{\mathrm{supply}}(t)
=
d\nu_{\mathrm{seam}}(t)
+
\sum_{\Re\rho>1/2}
m_\rho
\frac{2a_\rho}{\pi\bigl(a_\rho^2+(t-\gamma_\rho)^2\bigr)}\,dt.
\]

The first term counts seam zeros with multiplicity. The second is the
right-sector Blaschke current with its sign converted to positive harmonic
measure.

## Universal positivity

Both summands are positive measures. Therefore

\[
\mu_{\mathrm{supply}}\ge0
\]

without assuming RH.

This is the first universal positivity statement in the phase lane. It does
not locate the zeros by a sign inequality; it states that every divisor unit
has a positive boundary realization.

The decomposition is the Lebesgue decomposition of the measure:

\[
\mu_{\mathrm{supply}}
=
\mu_{\mathrm{atomic}}+\mu_{\mathrm{diffuse}},
\]

where

\[
\mu_{\mathrm{atomic}}=\nu_{\mathrm{seam}}
\]

and the displayed Poisson sum is absolutely continuous with respect to
Lebesgue measure.

## Strict global visibility of one off-seam zero

Every individual Poisson kernel is strictly positive for every real `t`.
Consequently, if even one right-sector zero exists, then

\[
\frac{d\mu_{\mathrm{diffuse}}}{dt}(t)>0
\]

for every real `t` at which the locally finite density is evaluated.

An off-seam zero is therefore not visible only near its projected ordinate.
It produces a weak but nonzero harmonic signal on every seam interval. As its
horizontal displacement tends to zero, the profile narrows and converges to
an atom; every fixed finite-resolution probe may remain positive throughout
that approach.

This gives a precise version of the operator's earlier intuition about
nonzero finite-resolution probabilities persisting arbitrarily close to the
critical line.

## RH as vanishing of one canonical component

By uniqueness of Lebesgue decomposition,

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
\mu_{\mathrm{diffuse}}=0
\quad\Longleftrightarrow\quad
\mu_{\mathrm{supply}}=\nu_{\mathrm{seam}}.
\]

This formulation separates a theorem already proved from the remaining
conjecture:

- positivity of the full supply measure is unconditional;
- absence of its diffuse component is RH-equivalent.

No cancellation among right-sector zeros can hide the diffuse part, because
all Poisson densities enter with the same positive sign.

## Smallest falsifier

A single hostile reciprocal zero pair creates a strictly positive diffuse
density of total mass two in the global budget while leaving the atomic seam
measure unchanged. Detecting any nonzero absolutely continuous component
falsifies atomic saturation immediately.

## Scope

This packet proves positivity and the unique atomic--diffuse decomposition
from canonical factorization. It does not prove that the diffuse component
vanishes for zeta and does not prove RH.
