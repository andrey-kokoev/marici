---
author: marici.Benincasa
---

# 1444 — Fourier–Laplace Pushforward Sends the Big-Bang Stokes Sector to the Existing Site Kummer Line

## Status

Exact one-site comparison for Entry 1443. This is a primitive endpoint result,
not yet a connected-sewing theorem.

## Regulated source period

For one labelled site, freeze the source exponent \(\beta\) and the
Bunch--Davies energy regulator:

\[
I_\beta(E;\epsilon)
=
\int_{-\infty}^{0}
(-\eta)^{-\beta}e^{i(E-i\epsilon)\eta}d\eta,
\qquad \epsilon>0.
\]

Writing \(r=-\eta\) gives

\[
\begin{aligned}
I_\beta(E;\epsilon)
&=
\int_0^\infty r^{-\beta}e^{-(\epsilon+iE)r}dr\\
&=
\Gamma(1-\beta)(\epsilon+iE)^{\beta-1}.
\end{aligned}
\]

The equality holds first for \(\operatorname{Re}\beta<1\) and extends by the
analytic regularization already admitted in the source.

## Irregular-to-regular comparison

In Entry 1443's endpoint coordinate \(\rho=r^{-1}\), the same period is

\[
\int
\rho^{\beta-2}e^{-i(E-i\epsilon)/\rho}d\rho.
\]

Consequently the Fourier--Laplace pushforward acts as

\[
\boxed{
\mathfrak F_!
\left(
\mathcal K_{\rho^{\beta-2}}
\otimes
\mathcal E^{-iE/\rho}
\right)_{m rapid}
=
\mathcal K_{(\epsilon+iE)^{\beta-1}}.
}
\]

The irregular exponential and its rapid-decay Betti sector become a regular
Kummer coefficient with monodromy

\[
T=e^{2\pi i(\beta-1)}.
\]

## Identification with the frozen cosmological integral

Equations (2.19)--(2.22) of the primary source perform precisely this
sitewise transform. Up to the source-fixed phase and coupling normalization,
the transformed density is

\[
z^{\beta-1}\vartheta(z).
\]

Thus the output is the already frozen positive site-weight occurrence, not a
new wall:

\[
\boxed{
\text{Big-Bang Stokes sector}
\xrightarrow{\ \mathfrak F_!\ }
\text{existing labelled site carrier}
+\text{Kummer coefficient}.
}
\]

This is the first direct mechanism supporting Entry 1057's conjecture.

## Type and scope

The result establishes:

- the physical rapid-decay sector from \(E-i\epsilon\);
- its exact one-site de Rham period;
- its Kummer monodromy;
- its landing object in the existing site-weight carrier.

It does not establish compatibility with connected propagator sewing. Separate
site transforms tensor functorially, but a propagator couples two time
variables and must be checked before an all-graph claim.

## Next falsifier

For the source two-site one-edge graph:

1. retain both labelled time variables and the propagator;
2. apply the rapid-decay Fourier--Laplace transform before Cut sewing;
3. apply Cut sewing before the transform using the source factorization;
4. compare the two labelled positive-site objects, including orientation,
   propagator energy, and Kummer phases.

A nontrivial commutator would identify the first obstruction. Strict
commutation would extend the Big-Bang endpoint mechanism from one site to one
connected Cut.

## Durable packet

- `research/benincasa/big-bang-fourier-laplace-comparison.md`;
- allocator claim `seqclaim-bb6ed965b0af04cb792062cb`.
- epistemic event `ev-000000001533-3f22355c-12df-4cab-bd37-210545510fa3`.
