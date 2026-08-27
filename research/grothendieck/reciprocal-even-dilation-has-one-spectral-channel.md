# Reciprocal-even dilation has one spectral channel

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact spectral-typing theorem

## Logarithmic realization

Let (H_{\mathrm{even}}\subset L^2(\mathbb R,dx)) be the even subspace. Define

\[
(Uf)(q)=\sqrt2\,e^{q/2}f(e^q),
\qquad q\in\mathbb R.
\]

Then

\[
\|Uf\|_{L^2(dq)}^2
=2\int_{\mathbb R}e^q|f(e^q)|^2\,dq
=2\int_0^\infty|f(x)|^2\,dx
=\|f\|_{L^2(dx)}^2.
\]

Thus (U) is unitary from the even carrier to one copy of
(L^2(\mathbb R,dq)).

For unitary dilation

\[
(R_uf)(x)=e^{u/2}f(e^ux),
\]

one has

\[
U(R_uf)(q)=(Uf)(q+u).
\]

Therefore the self-adjoint dilation observable is unitarily equivalent to
(-i\partial_q), whose Fourier representation is multiplication by one real
spectral coordinate with multiplicity one.

## Consequence for the two-sector picture

Before reciprocal projection, positive and negative (x)-rays provide two
copies of the logarithmic coordinate. Evenness identifies them. The surviving
unitary seam is not a two-channel interference space; it is a single scalar
spectral fiber at each real frequency.

For two admissible even vectors (v,w), their cross-spectral density factors
fiberwise as

\[
\overline{\widehat{Uv}(t)}\,\widehat{Uw}(t).
\]

There is no sum over an internal multiplicity index. A zero on the unitary
seam therefore means that at least one scalar fiber amplitude vanishes, not
destructive cancellation between two hidden spectral planes.

## Where the two sectors went

The reciprocal grades of ledger 3057 remain real before projection: Fourier
reflection exchanges dilation orientation. But the physical even source and
even arithmetic boundary select the multiplicity-one quotient on the unitary
seam. The two half-planes arise when the real Mellin character is continued to
nonunitary weights on either side of that seam.

Hence an off-seam zero is not automatically a spectral event of the
self-adjoint dilation generator. It is a zero of the nonunitary analytic
continuation of a generalized matrix coefficient.

## Remaining RH bridge

This cleanly states the missing Hilbert–Pólya step. One must prove that every
nontrivial zero of the analytically continued arithmetic matrix coefficient
is realized on the unitary dilation spectrum. Self-adjointness of the carrier
generator alone cannot do this, because analytic continuation lives outside
its unitary spectral parameter.

The arithmetic comb is distributional rather than an (L^2) vector. A valid
proof must therefore construct a rigged spectral pairing whose continued
divisor is supported by the unitary fibers. Assuming that support statement
would assume RH in operator language.

## Scope

The unitary logarithmic model, multiplicity-one spectrum, and fiberwise
factorization are exact. Extension of the distributional comb pairing and
support of its analytic divisor on the unitary spectrum remain unproved. RH is
not proved.

