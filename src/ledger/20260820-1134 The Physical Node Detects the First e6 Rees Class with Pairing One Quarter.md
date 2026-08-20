---
title: "The Physical Node Detects the First e6 Rees Class with Pairing One Quarter"
date: 2026-08-20
entry: 1134
status: established-supported-rational
sector: cosmology
---

# 1134 — The Physical Node Detects the First \(e_6\) Rees Class with Pairing One Quarter

Sequence claim: `seqclaim-0ab79a55824704561b4fe4d7`.

## Supported pairing

Entry 1133 gives the ordered-sheet covector

\[
\operatorname{Sp}^{(1)}(e_6)
=\left(-\frac18,+\frac18\right).
\]

Entry 1131 gives the physical normalization boundary

\[
\partial\gamma_{CM}=e_- - e_+
=(-1,+1).
\]

Their source-oriented pairing is therefore

\[
\boxed{
\left\langle\operatorname{Sp}^{(1)}(e_6),
\partial\gamma_{CM}\right\rangle
=\frac14.
}
\]

This is nonzero. The physical soft node detects \(e_6\), but only at first
higher-Rees order; the leading ordinary grade remains exact.

## Conductor-face coherence

The smoothing parameter is

\[
t=p\,s\,(B-1).
\]

In face order \((p,s,B-1)\), each labelled face maps to the same universal
anti-invariant Tate class with coefficient \(-1/8\). Thus the three edge
differences are

\[
(-1/8)-(-1/8)=0.
\]

The first-Rees covector is therefore compatible with the existing oriented
node simplex at both deeper faces \(s=0\) and \(B-1=0\); no fitted overlap
cell is required. The physical fixed-base soft slice has \(s=1\) and lies on
the generic conductor locus \(B-1\ne0\), selecting the \(p\)-face.

## Scope

The number \(1/4\) is canonical in the frozen source de Rham, sheet, and
relative-chain conventions. It is not yet an integral index because the
saturated Betti lattice of the target \(e_6\) line remains unconstructed.

This result is coefficient/relative-period data on the existing soft,
marked-wall, and normalization carrier. It adds no cosmology-specific
carrier incidence.

## Evidence and next falsifier

- `research/benincasa/checkers/rank12_u2v0_e6_supported_pairing.py`;
- `research/benincasa/results/rank12-u2v0-e6-supported-pairing.json`;
- Entries 1103--1104 and 1131--1133.

Next transport this supported first-Rees pairing through all three cyclic
site-soft occurrences. Unlike the retracted Entry 1128, the object being
transported is now typed: a higher-Rees coefficient covector paired with a
physical relative boundary.

