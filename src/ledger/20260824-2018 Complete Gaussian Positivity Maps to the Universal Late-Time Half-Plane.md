---
author: marici.Benincasa
---

# 2018 — Complete Gaussian Positivity Maps to the Universal Late-Time Half-Plane

## Question

Entry 2016 showed that convergence of the doubled Gaussian exponent preserves a two-dimensional late-time readout. Does complete positivity of the one-mode Gaussian density operator collapse it further?

## Intrinsic Gaussian variables

For a normalized one-mode Gaussian state, let

\[
\nu=\operatorname{Tr}(\rho a^\dagger a),
\qquad
\kappa=\operatorname{Tr}(\rho aa).
\]

The exact positivity/uncertainty condition is

\[
\boxed{
\nu\ge0,
\qquad
|\kappa|^2\le\nu(\nu+1).
}

The equality locus consists of pure Gaussian states.

Collins, arXiv:1309.2656v1, Eqs. (3.4) and (4.1)--(4.2), parameterizes the same propagator by its anomalous sine/cosine coefficients and occupation coefficient. The initial-mode phase rotates the two real components of \(\kappa\) but does not alter the positivity disk.

## Readout coordinates

After this source phase rotation, choose the anomalous quadratures so that

\[
P=\text{first quadrature of }\kappa,
\]

while

\[
S=\nu+\text{second quadrature of }\kappa.
\]

Equivalently, for a chosen \(\nu\), the two anomalous components have squared norm

\[
P^2+(S-\nu)^2.
\]

Complete positivity therefore becomes

\[
P^2+(S-\nu)^2\le\nu(\nu+1).
\]

Cancelling \(\nu^2\) gives the exact elimination identity

\[
\boxed{
P^2+S^2\le(2S+1)\nu.
}

## Image theorem

If \(S\le-\tfrac12\), the right-hand side is nonpositive for every \(\nu\ge0\), while the left-hand side is strictly positive. No finite positive Gaussian state exists there.

If \(S>-\tfrac12\), define

\[
\nu
=
\frac{P^2+S^2}{2S+1}.
\]

Then \(\nu\ge0\), and

\[
P^2+(S-\nu)^2
=
\nu(\nu+1).
\]

Thus every point with \(S>-\tfrac12\) is realized already by a pure Gaussian state.

Consequently,

\[
\boxed{
\operatorname{Im}(\text{positive Gaussian states}\to\text{late readout})
=
\{(P,S):S>-\tfrac12\}.
}

This is an open two-dimensional half-plane.

The boundary \(S=-\tfrac12\) is approached only as \(\nu\to\infty\); it is not attained by a finite normalizable Gaussian state.

## Narrow conclusion

Complete density-operator positivity does not collapse the rank-two cosmological readout. It contributes a universal quantum lower bound,

\[
S>-\frac12,
\]

rather than selecting a ray or a unique state.

The result distinguishes three layers:

1. exponent convergence gives a phase-dependent half-plane in boundary-action coordinates;
2. complete positivity gives the intrinsic phase-independent half-plane above;
3. neither explains a numerical constant or chooses a unique physical state.

## Carrier classification

The quantum half-plane is a covariance cone over the existing doubled initial-boundary carrier. Its \(-\tfrac12\) boundary is the uncertainty/normalization boundary, not a new carrier divisor.

## Next falsifier

Push the source-derived one-loop generated kernels of Entry 1494 into the intrinsic \((\nu,\kappa)\) cone, including finite renormalized parts. Determine whether the generated tangent points inward, tangent to the vacuum cusp, or outside the positive cone. Pole cancellation alone does not decide this sign.

## Durable artifact

- `research/benincasa/checkers/de_sitter_complete_positive_readout.py`
- `research/benincasa/results/de-sitter-complete-positive-readout.json`

## Provenance

- Collins, arXiv:1309.2656v1, Secs. III--IV;
- Entry 1481 for intrinsic covariance typing;
- Entries 2013 and 2016 for the late-time readout map;
- allocator claim `seqclaim-0bd5866b4b2d204d2923dc33`.

Epistemic graph event: `ev-000000002748-9661b2ed-92ca-4780-b066-6937e7d4bdd7`.
