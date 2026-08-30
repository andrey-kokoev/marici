---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2214 — The Gaussian Kernel Tangent Has a Normalized Quadratic Score

## One-mode calculation

For the normalized Gaussian boundary measure

\[
P_a(x)=\sqrt{\frac a\pi}\,e^{-ax^2},
\qquad
K=\langle x^2\rangle=\frac1{2a},
\]

the score for the logarithmic covariance parameter is

\[
S_K(x)=\frac{\partial}{\partial\log K}\log P_a(x)
=ax^2-\frac12.
\]

It is centered and has positive Fisher norm:

\[
\langle S_K\rangle=0,
\qquad
\langle S_K^2\rangle=\frac12.
\]

The subtraction \(-1/2\) is forced by normalization. Thus vacuum or partition-
function variation is not an untracked correction; it is already included in
the score.

## Consequence

The tangent of Entry 2211 has an actual boundary-field representative: a
centered quadratic power insertion. It is not merely a derivative in an
abstract coefficient space.

For independent momentum modes, the corresponding scores are orthogonal.
Their Fisher metric is positive and diagonal before evaluation coincidences
are imposed.

## Evidence

- Entry 2211
- `research/benincasa/checkers/normalized_gaussian_score.rs`

