---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2229 — Gaussian Scores Define an Observability Filtration on Correlator Kernels

## First observability map

Let

\[
\epsilon:V\to R
\]

be a source-defined correlator augmentation and let \(N_e\) count deletion of
edge \(e\). On the hidden scalar kernel \(K=\ker\epsilon\), define

\[
\mathcal O_1:K\longrightarrow R^{E},
\qquad
k\longmapsto(\epsilon N_e k)_{e\in E}.
\]

Entry 2227 identifies each component with a normalized Gaussian score
response. The first-score blind subspace is

\[
K^{(1)}=K\cap\bigcap_e\ker(\epsilon N_e).
\]

Thus

\[
\boxed{
K/K^{(1)}
=\text{the part of the scalar-hidden kernel visible at first Gaussian order}.
}
\]

## Architectural status

This construction uses only the existing augmentation, labelled deletion
operators, and Gaussian coefficient lens. It adds no Carrier cells. It types
the phrase “hidden information” as a finite observability problem rather
than a metaphor.

## Evidence

- Entries 2199 and 2227–2228
- `research/benincasa/checkers/deletion_score_observability.rs`
