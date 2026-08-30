# The two-spectral Maass–Selberg kernel is a scalar scattering Bezoutian

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact relative-automorphic no-go

## Two cusp solutions

Write the constant term of the modular Eisenstein state as

\[
f_s(y)=y^s+\varphi(s)y^{1-s}.
\]

It satisfies the radial eigen-equation

\[
-y^2f_s''=s(1-s)f_s.
\]

For two spectral parameters (s,w), Green’s identity gives

\[
\bigl(s(1-s)-w(1-w)\bigr)
\int f_s(y)f_w(y)\,\frac{dy}{y^2}
=\left[f_sf_w'-f_s'f_w\right]_{\partial}.
\]

## Exact boundary concomitant

Put (a=\varphi(s)) and (b=\varphi(w)). Direct expansion gives

\[
\begin{aligned}
f_sf_w'-f_s'f_w
={}&(w-s)y^{s+w-1}\\
&+b(1-w-s)y^{s-w}\\
&+a(w-1+s)y^{w-s}\\
&+ab(s-w)y^{1-s-w}.
\end{aligned}
\]

Every term is determined by the two scalar scattering coefficients and the
spectral parameters. No nonconstant Fourier-mode coordinate survives in the
boundary form.

This is the structural content of the two-parameter Maass–Selberg relation:
the automorphic bulk pairing descends to a Bezoutian-like expression built
from (arphi(s)) and (arphi(w)).

## Degenerate diagonal limit

When the two parameters approach the unitary conjugate pair, the vanishing
spectral denominator produces the familiar logarithmic and derivative terms.
In particular, the diagonal norm contains

\[
-\frac{\varphi'}{\varphi}.
\]

This limiting derivative is not additional source data. It is forced by the
same scalar two-point boundary formula.

## Consequence

The first relative automorphic candidate also closes without new RH force.
Although it begins with two full Eisenstein states and integrates their bulk
interaction, Green reduction leaves only the scalar one-cusp scattering
function.

Therefore none of the following is independently constraining:

- the constant term;
- the vector of linear Fourier modes;
- the one-parameter Maass–Selberg norm;
- the two-parameter Maass–Selberg pairing.

They are four presentations of the same scalar scattering divisor.

## Boundary of the automorphic-energy lane

A larger Rankin–Selberg formula is useful only if it couples the Riemann
Eisenstein state to an independently sourced representation whose spectral
data are not algebraically determined by (arphi). Self-pairing the same
one-cusp family cannot qualify.

The smallest legitimate candidate is a twisted comparison against a
nontrivial norm-one idele character. But ledger 3074 shows that this changes
the source sector from the untwisted Riemann vacuum to a Dirichlet or Hecke
sector. Any transfer back to RH would require an independently proved
descent theorem across those sectors.

Thus the untwisted automorphic-energy lane has reached an honest structural
boundary.

## Scope

This no-go concerns linear and bilinear pairings within the standard one-cusp
Eisenstein family. It does not rule out independently sourced twisted
families or nonlinear arithmetic correspondences.

## Verification

The checker expands the boundary concomitant and verifies the exact Green
derivative identity symbolically.
