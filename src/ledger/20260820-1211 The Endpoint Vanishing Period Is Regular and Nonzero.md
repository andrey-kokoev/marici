---
title: "The Endpoint Vanishing Period Is Regular and Nonzero"
date: 2026-08-20
entry: 1211
status: active-supported-local
sector: cosmology
---

# 1211 — The Endpoint Vanishing Period Is Regular and Nonzero

Sequence claim: `seqclaim-feca19cfc02c89451fe48ce9`.

## Finite endpoint

On \(K_0=0\), the transverse double-cover equation is

\[
y^2=z(K_4z+K_2).
\]

Use the source-derived root coordinate

\[
z=-\frac{K_2}{K_4}t.
\]

Then

\[
y^2=-\frac{K_2^2}{K_4}t(1-t),
\]

and the local residue form becomes

\[
\frac{dz}{y}
=
-\frac{dt}{\sqrt{K_4}\sqrt{-t(1-t)}}.
\]

The closed vanishing-cycle period is therefore, up to its ordered
orientation,

\[
\boxed{
\oint_{\gamma_0}\frac{dz}{y}
=
\frac{2\pi i}{\sqrt{K_4}}.
}
\]

## Infinity endpoint

On \(K_4=0\), use \(\xi=w/z\). The exchanged equation is

\[
y^2=\xi(K_0\xi+K_2).
\]

With \(\xi=-K_2t/K_0\),

\[
\boxed{
\oint_{\gamma_\infty}\frac{d\xi}{y}
=
\frac{2\pi i}{\sqrt{K_0}}
}
\]

again up to ordered orientation.

## Consequence

In both charts the factors of \(K_2\) cancel exactly. Hence

\[
\boxed{
\nu_{K_2}(\text{vanishing period})=0.
}
\]

The local Gysin/vanishing-cycle map into Entry 1210's odd normalization
costalk has rank one: the costalk is not killed by endpoint specialization.
Its coefficient is the expected rank-one Kummer factor
\(K_4^{-1/2}\), respectively \(K_0^{-1/2}\).

## Epistemic boundary

This is a transverse local period calculation. It does not prove that the
global Bunch--Davies relative chain contains either vanishing cycle. The
physical activation question remains separate and must retain source contour,
orientation, and occurrence data.

## Classification

\[
\boxed{
\text{existing endpoint carrier}
+
\text{nonzero rank-one Kummer specialization}
+
\text{no new carrier datum}.
}
\]

## Next falsifier

Transport the ordered finite and infinity local cycles through the common
projective radial overlap. Determine their Čech sign and whether the two
rank-one costalk maps cancel, reinforce, or form a nontrivial extension before
any physical-chain pairing is asserted.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_endpoint_vanishing_period.rs`
- `research/benincasa/results/five-site-endpoint-vanishing-period.json`
