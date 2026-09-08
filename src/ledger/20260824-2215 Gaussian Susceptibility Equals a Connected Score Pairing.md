---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2215 — Gaussian Susceptibility Equals a Connected Score Pairing

## Normalized-response identity

For any boundary observable \(O\), differentiation of the normalized measure
gives

\[
\boxed{
\frac{\partial}{\partial\log K}\langle O\rangle
=\langle O\,S_K\rangle_c.
}
\]

The connected subscript is precisely the normalization subtraction. For the
hostile quadratic test,

\[
\langle x^4\rangle=3K^2
\]

implies

\[
\operatorname{Cov}(x^2,S_K)
=a\langle x^4\rangle-\frac12\langle x^2\rangle
=K,
\]

matching \(\partial_{\log K}\langle x^2\rangle=K\).

In Wick expansions the same identity marks each propagator carrying \(K\).
Therefore the edge-counting rule of Entry 2211 survives normalization exactly;
vacuum terms cancel through connected pairing.

## Contact application

For each triangle edge,

\[
\langle O_{\rm ct}S_{K_e}\rangle_c=-8C_e.
\]

The geometric conormal class is thus paired by a source-normalized quadratic
boundary insertion.

## Evidence

- Entries 2211–2214
- `research/benincasa/checkers/gaussian_score_response_identity.rs`
