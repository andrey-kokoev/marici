---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2227 — Gaussian Scores Realize Every Labelled Deletion Tangent

## All-edge identity

For an arbitrary erased subset \(S\subseteq E(G)\), the probability-
distribution expansion contains

\[
K_S=\prod_{e\in S}K(y_e),
\qquad
K(y)=\bigl(2\operatorname{Re}\psi_2(y)\bigr)^{-1}.
\]

For every labelled edge,

\[
\boxed{
\partial_{\log K_e}\log K_S=1_{e\in S}.
}

Thus the direct sum of normalized quadratic scores realizes the full labelled
deletion tangent space before the physical momentum-function pullback:

\[
\bigoplus_{e\in E(G)}\mathbb Q\,S_{K_e}
\longrightarrow
T_w\mathcal W_{\rm orient}.
\]

Each independent Gaussian mode contributes Fisher norm \(1/2\). The map is
strictly occurrence-labelled and equivariant under graph automorphisms.

## Scope

This is an all-graph readout theorem for deletion tangents. Whether a
particular tangent pairs nontrivially with a correlator kernel remains a
graph- and coefficient-specific calculation.

## Evidence

- Entries 2211–2216 and 2226
- `research/benincasa/checkers/all_edge_gaussian_scores.rs`

