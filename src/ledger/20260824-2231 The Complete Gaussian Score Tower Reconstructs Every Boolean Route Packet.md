---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2231 — The Complete Gaussian Score Tower Reconstructs Every Boolean Route Packet

## Mixed-response moments

Let \(v_S\) be the preaggregation contribution of deletion route
\(S\subseteq E\), and introduce independent covariance multipliers \(g_e\):

\[
F(g)=\sum_{S\subseteq E}v_S\prod_{e\in S}g_e.
\]

For every labelled subset \(T\), the mixed logarithmic response at \(g=1\)
is

\[
M_T
=\left.\prod_{e\in T}g_e\partial_{g_e}F\right|_{g=1}
=\sum_{S\supseteq T}v_S.
\]

This is the upper Boolean zeta transform. Möbius inversion reconstructs

\[
\boxed{
v_S
=\sum_{T\supseteq S}(-1)^{|T|-|S|}M_T.
}

Hence all mixed Gaussian responses through order \(|E|\), including the
zeroth scalar value, reconstruct the entire Boolean route packet exactly.

## Meaning

No information is destroyed by scalar aggregation if the complete labelled
response tower is retained. Information merely moves to a finite hierarchy
of mixed ports. The first order suffices for the triangle contact kernel;
other graphs may require higher orders.

This is a coefficient/readout tomography theorem. Physical momentum
identifications may collapse labelled directions, and operational access to
high-order score insertions remains sector-dependent.

## Evidence

- Entries 2227–2230
- `research/benincasa/checkers/boolean_score_tomography.rs`

