# Entry 1616 — The Source Cubic Production Amplitude Has the Correct Labelled Cut Norm

## Claim

The frozen finite-time source fixes a normalized first-order cubic production
amplitude whose Cut square has the corrected labelled endpoint multiplicities.

## Source derivation

Equation (17) expands the ket evolution as

\[
\exp(-iH+iS),
\]

so the first-order production amplitude is

\[
A_{\rm prod}=-iH+iS=-i(H-S).
\]

Equation (18) gives the same object after introducing the integrated boundary
Hamiltonian

\[
H_0=-S.
\]

The exact second-order coefficients in both forms are

\[
-\frac12H^2+HS-\frac12S^2
=-\frac12(H-S)^2.
\]

Sewing the ket amplitude to its Hermitian bra gives

\[
\boxed{
A_{\rm prod}\overline{A_{\rm prod}}
=|H-S|^2\ge0.
}
\]

Before identifying mixed occurrences, this is precisely the four-term Cut
complex of Entry 1615 and pushes forward to location multiplicities
\((1,2,1)\).

## Result

The source-normalization and labelled-location gates for the Gaussian
second-Rees Cut conjecture both pass.  The printed Eq. (19) normalization
defect is excluded from this conclusion.

## Remaining finite falsifier

Derive the second phase-space jet of the statistical Dyson correction in the
same normalization and test

\[
n_{2,p}^{\rm Dyson}
\stackrel?=
\int d\Pi_{qk}\,|A_{\rm prod}(p;q,k)|^2.
\]

The comparison must retain the two internal occurrence labels until the
physical Cut trace is applied.

## Evidence

- `research/benincasa/checkers/eq17_eq18_endpoint_expansion.rs`
- `research/benincasa/results/eq17-eq18-endpoint-expansion.json`
- `research/benincasa/results/source-cubic-production-amplitude.json`

Allocator claim: `seqclaim-be8136c5a8c3e3417e083f18`.
