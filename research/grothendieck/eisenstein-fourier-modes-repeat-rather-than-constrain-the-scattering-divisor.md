# Eisenstein Fourier modes repeat rather than constrain the scattering divisor

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact uncompressed-mode no-go

## Full Fourier expansion

For the modular Eisenstein series, the constant term is

\[
y^s+\varphi(s)y^{1-s},
\qquad
\varphi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
\]

The nonconstant part has the form

\[
\frac{2}{\Lambda(2s)}
\sum_{n\ne0}
\tau_{s-1/2}(|n|)\sqrt y\,
K_{s-1/2}(2\pi|n|y)e(nx).
\]

This standard expansion and the associated Maass–Selberg norm formula are
given in [A conjecture for the regularized fourth moment of Eisenstein
series](https://doi.org/10.1016/j.jnt.2017.06.012).

## Common-divisor theorem

Every nonconstant Fourier mode shares the same scalar denominator

\[
\Lambda(2s).
\]

The first divisor coefficient satisfies

\[
\tau_{s-1/2}(1)=1.
\]

Its Bessel profile is not identically zero as a function of (y). Therefore
the vector of nonconstant modes faithfully repeats the pole divisor coming
from (1/\Lambda(2s)). It does not replace that divisor by a new
operator-valued spectral condition.

After removing the common scalar factor, ratios between Fourier modes depend
on divisor sums and Bessel profiles but lose the Riemann pole divisor
entirely. Thus the internal mode geometry and the resonance locations
separate multiplicatively.

## Green-form audit

The truncated Eisenstein Green identity yields the Maass–Selberg term

\[
-\frac{\varphi'(s)}{\varphi(s)}.
\]

But

\[
\frac{\varphi'(s)}{\varphi(s)}
=2\frac{\Lambda'(2s-1)}{\Lambda(2s-1)}
-2\frac{\Lambda'(2s)}{\Lambda(2s)}.
\]

The positive truncated norm therefore measures the logarithmic derivative of
the same scalar scattering divisor. It supplies a spectral density and time
delay, not an independent law restricting where the resonances may occur.

## Consequence

The uncompressed Fourier expansion is richer than the constant term as a
state profile, but not as divisor provenance. All modes inherit their poles
from one scalar completed factor. Their joint Green energy repackages its
logarithmic derivative.

This closes the simplest mode-coupling route to RH. Merely retaining all
Eisenstein Fourier modes does not create the missing resonance-confinement
law.

## What remains

The first structure not exhausted by the common scalar denominator is the
nonlinear interaction among modes—products, Rankin–Selberg pairings, or a
relative comparison with a source-independent reference Eisenstein family.
Such an operation would introduce two spectral arguments or two source
states rather than one scalar factor times a fixed vector.

The acceptance gate remains Deutschian: the pairing must be derived from the
modular source before examining the Riemann divisor, and a generic one-cusp
scattering coefficient must fail it for an identifiable reason.

## Scope

The Fourier factorization and Maass–Selberg reduction are exact. The result
does not rule out every nonlinear or relative automorphic mechanism.

## Verification

The checker verifies the first divisor coefficient, common scalar factor,
divisor-free mode ratios, and scalar scattering logarithmic derivative.
