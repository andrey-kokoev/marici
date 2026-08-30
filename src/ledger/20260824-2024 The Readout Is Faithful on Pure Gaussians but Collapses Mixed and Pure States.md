---
author: marici.Benincasa
---

# 2024 — The Readout Is Faithful on Pure Gaussians but Collapses Mixed and Pure States

## Question

Entry 2023 showed that complete thermal states map to the ray \((P,S)=(0,n)\). Does the intrinsic late-time quotient faithfully retain the two parameters of a complete pure squeezed state?

## Frozen covariance geometry

Write the phase-rotated anomalous covariance in two real quadratures \((P,Y)\), with readout

\[
S=\nu+Y.
\]

Gaussian positivity is

\[
P^2+Y^2\le\nu(\nu+1),
\]

and a pure Gaussian saturates it. Substituting \(Y=S-\nu\) into the pure equation gives

\[
P^2+(S-\nu)^2=\nu(\nu+1),
\]

hence

\[
\boxed{P^2+S^2=(2S+1)\nu}.
\]

## Exact inverse

For every point in the physical half-plane \(S>-1/2\), the unique pure covariance above it is

\[
\boxed{
\nu=\frac{P^2+S^2}{2S+1},
\qquad
Y=S-\frac{P^2+S^2}{2S+1}.
}
\]

These expressions satisfy \(P^2+Y^2=\nu(\nu+1)\) identically and \(\nu\ge0\). Thus, after identifying the undefined squeezing phase at the vacuum, the pure Gaussian state space maps bijectively onto the entire readout half-plane.

## Mixed-state collapse

The full positive Gaussian space is three-dimensional \((\nu,P,Y)\), while the readout is two-dimensional \((P,S)\). Interior mixed states therefore share readouts with pure states.

The thermal point

\[
(P,S)=(0,n),\qquad n>0,
\]

has thermal covariance \((\nu,\kappa)=(n,0)\), but its unique pure preimage is

\[
\nu_{\rm pure}=\frac{n^2}{2n+1},
\qquad
Y_{\rm pure}=\frac{n(n+1)}{2n+1}.
\]

These are distinct physical covariance states with the same late-time readout.

## Narrow result

\[
\boxed{
\text{the quotient is faithful on pure Gaussian states, but not on all Gaussian states.}
}
\]

In particular, a thermal mixed state and an appropriately phased pure squeezed state cannot be distinguished by \((P,S)\) alone.

This is the cosmological form of the programme's projection rule:

\[
\boxed{
\text{compatibility in a reduced observable does not imply state reconstruction.}
}
\]

## Consequence

The half-plane \(S>-1/2\) has a dual interpretation:

1. it is the image of all positive Gaussian states;
2. it is already parametrized exactly once by pure Gaussian states.

Accordingly, positivity does not reveal whether the underlying source is pure or mixed. Recovering that distinction requires one additional faithful observable, naturally an unequal-time or momentum-momentum covariance.

## Verification

The dependency-free exact checker verifies the inverse and thermal/pure collision on 238 rational half-plane samples and 16 positive thermal samples:

`research/benincasa/checkers/pure_squeezed_readout_injectivity.py`

`research/benincasa/checkers/results/pure-squeezed-readout-injectivity.json`

## Next falsifier

Adjoin the smallest source-normalized covariance observable that can recover \(\nu\) independently. Test whether

\[
(P,S,\nu)
\]

is a faithful coordinate on the complete one-mode Gaussian quotient and whether that observable is invariant under the allowed future-boundary counterterm shifts.

## Provenance

- Entries 2013, 2018, and 2023;
- allocator claim `seqclaim-a7dd9d1e73c093d6b189af13`.

Epistemic graph event: `ev-000000002757-c5086a03-6f7d-49cc-9001-181ed94a8bca`.
