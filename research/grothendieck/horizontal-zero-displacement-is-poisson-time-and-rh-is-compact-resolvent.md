# Horizontal zero displacement is Poisson time and RH is compact resolvent

## Fourier--resolution transform

Use the Fourier convention

\[
\widehat\mu(x)=\int_{\mathbb R}e^{-ixt}\,d\mu(t).
\]

For the normalized Poisson kernel

\[
P_a(t-b)=\frac1\pi\frac{a}{a^2+(t-b)^2},
\]

one has

\[
\widehat{P_a(\,\cdot-b)}(x)
=
e^{-a|x|}e^{-ibx}.
\]

Therefore the two kinds of divisor supply transform as follows:

\[
\delta_b
\longmapsto
e^{-ibx},
\]

while a right-sector zero at horizontal distance `a` gives

\[
2P_a(t-b)\,dt
\longmapsto
2e^{-a|x|}e^{-ibx}.
\]

The vertical ordinate `b` is frequency. The horizontal displacement `a` is
exactly exponential decay rate in the Fourier-resolution coordinate.

## Poisson-semigroup interpretation

Let `|D|` be the positive Fourier multiplier with symbol `|x|`. Then

\[
P_a(\,\cdot-b)
=
e^{-a|D|}\delta_b.
\]

An off-seam zero is therefore a boundary atom evolved for positive Poisson
time. A seam zero is the unevolved state at time zero.

This gives geometric meaning to the critical line: it is the zero-dissipation
face of divisor transport. Moving away from it does not destroy the divisor;
it turns its atomic boundary incidence into a diffuse harmonic state.

## Canonical self-adjoint supply operator

Because `mu_supply` is a positive locally finite measure, it canonically
defines the spectral Hilbert space

\[
\mathcal H_{\mathrm{supply}}
=
\int_{\mathbb R}^{\oplus}\mathbb C^{m(t)}\,d\mu_{\mathrm{supply}}(t),
\]

where the atomic fiber dimension records zero multiplicity and the diffuse
fiber is one-dimensional. Define

\[
(M\psi)(t)=t\psi(t)
\]

on its maximal multiplication domain. The operator `M` is self-adjoint
without assuming RH.

If RH holds, the supply measure is purely atomic at the discrete ordinates
`gamma`, with finite multiplicities and no finite accumulation. Then

\[
(M-i)^{-1}
\]

is compact and the spectrum is exactly the Riemann-zero ordinate multiset.

If RH fails, one right-sector zero makes the diffuse density strictly positive
on all of `R`. The multiplication operator then has nontrivial absolutely
continuous spectrum with essential support `R`, and its resolvent is not
compact.

Consequently, RH holds if and only if `M` has compact resolvent.

Equivalently, RH says the canonical supply representation has pure-point
spectral type.

## Hilbert--Polya correction

Self-adjointness is no longer the missing property: the positive supply
measure gives it automatically. The RH-bearing theorem is source compactness,
or exclusion of a dissipative/continuous spectral component.

This operator is not yet a Hilbert--Polya proof because it is constructed
from the boundary supply measure, whose diffuse component already encodes the
possible open-sector divisor. The noncircular target is to derive the same
operator from labelled theta--Poisson constructors and prove compactness
before canonical factorization reveals its spectral type.

## Sharp hostile test

Insert one reciprocal off-seam zero pair. Its supply contribution becomes a
Poisson-semigroup orbit with decay `e^(-a|x|)`, and the multiplication
operator immediately acquires continuous spectrum. A source-derived compact
model must reject that modification before its zeros are inspected.

## Scope

This packet proves the Poisson-time identity and the compact-resolvent
equivalence for the canonical supply representation. It does not construct
that representation independently from labelled theta dynamics, prove its
source compactness, or prove RH.
