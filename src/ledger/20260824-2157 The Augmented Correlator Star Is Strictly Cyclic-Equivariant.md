---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2157 — The Augmented Correlator Star Is Strictly Cyclic-Equivariant

## Labelled action

Let the cyclic generator act by

\[
12\mapsto23\mapsto31\mapsto12,
\qquad
1\mapsto2\mapsto3\mapsto1.
\]

It permutes the eight deletion subsets while preserving deletion grade.
Consequently it preserves the source weight

\[
w_S=(-2)^{|S|}.
\]

Endpoint translation is covariant under the same relabelling, so the ports
satisfy

\[
\sigma_{mathcal R}T_S
=T_{sigma S}\sigma_S.
\]

Therefore the weighted augmentation of Entry 2156 is strictly equivariant:

\[
\boxed{
\sigma_{mathcal R}\epsilon
=
\epsilon\left(\bigoplus_S\sigma_S\right).
}
\]

## Orbit census

The empty and fully deleted sectors are fixed. The three grade-one sectors
form one free orbit and the three grade-two sectors form another. The
permutation character is

\[
\chi=(8,2,2).
\]

Over (mathbb Q), the indexing representation is

\[
4\,mathbb Q_{m triv}
\oplus
2\,mathbb Q(\zeta_3).
\]

This decomposition concerns the labelled sector index. It does not identify
the sector-specific coefficient modules or assert a rank for
(operatorname{Fib}(\epsilon)).

## Consequence

Cyclic coherence does not require inter-grade cube arrows. It is already a
strict naturality property of the source-defined star. Any future fiber or
cofiber of (epsilon) inherits the cyclic action functorially, provided it is
formed in a category containing the actual coefficient modules.

No new Carrier cell, fitted transition, or post-hoc symmetry projector is
required.

## Evidence

- `research/benincasa/checkers/three_site_weighted_correlator_adapter.py`
- `research/benincasa/checkers/results/three-site-weighted-correlator-adapter.json`
- allocator claim `seqclaim-7a80a5a23ee623e7159525e0`
