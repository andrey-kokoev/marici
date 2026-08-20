---
title: "Endpoint Discriminant Normalization Produces a Canonical Odd Line"
date: 2026-08-20
entry: 1210
status: active-supported-algebraic
sector: cosmology
---

# 1210 — Endpoint Discriminant Normalization Produces a Canonical Odd Line

Sequence claim: `seqclaim-5d798378ca4aee9857d2edb9`.

## Resolved endpoint cover

Entry 1209 gives the doubled collision section \(K_2^2=0\) on either
radial endpoint. Retain the discriminant square root \(\delta\) before
forgetting its deck sheet. The endpoint cover is

\[
R
=
\mathbb Q[K_2,\delta]/(\delta^2-K_2^2).
\]

Its normalization is

\[
N=\mathbb Q[K_2]\oplus\mathbb Q[K_2],
\]

with

\[
f(K_2,\delta)
\longmapsto
\bigl(f(K_2,K_2),f(K_2,-K_2)\bigr).
\]

The two summands are the two labelled discriminant sheets; deck exchange
swaps them.

## Canonical normalization cokernel

The conductor is \(K_2N\). The normalization sequence has cokernel

\[
\boxed{
N/R\simeq\mathbb Q_{K_2=0}.
}
\]

It is generated projectively by the difference of the two sheet values. Deck
exchange acts as

\[
\boxed{\tau=-1}.
\]

Thus the endpoint coefficient cell is canonical without choosing either
lift \(\delta=+K_2\) or \(\delta=-K_2\). Choosing one branch would be
noncanonical; retaining their anti-diagonal difference is intrinsic.

Finite cutoff calculations through degree 32 give normalization/image ranks

\[
(6,5),\ (10,9),\ (18,17),\ (34,33),\ (66,65),
\]

so the cokernel remains rank one.

## Finite/infinity covariance

The finite and infinity endpoint equations are exchanged by

\[
K_0\leftrightarrow K_4,
\qquad
z\leftrightarrow w.
\]

Both therefore carry the same canonical odd normalization cokernel. An
ordered residue orientation is still required to determine the sign of a
Čech differential between the two endpoint occurrences, but not to define
either local coefficient line.

## Classification

\[
\boxed{
\text{existing endpoint support}
+
\text{canonical rank-one odd coefficient costalk}.
}
\]

No new carrier datum appears. This is a normalization/conductor object of the
sector-specific discriminant cover.

## Remaining physical gate

This calculation does not produce a physical relative-chain map. The next
test must derive the ordered endpoint residue/Gysin maps from the source
measure and compare their images in the two odd normalization costalks. A
zero or nonzero physical pairing may be stated only after that map exists.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_endpoint_discriminant_normalization.rs`
- `research/benincasa/results/five-site-endpoint-discriminant-normalization.json`
