---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2226 — All-Arity Weighted-Correlator Coefficients Are Boolean Möbius Orientation Pullbacks

## Theorem

Let \(G\) have edge set \(E\), with no restriction on \(|E|\). On the Boolean
overlap cover, define

\[
\mu(S)=(-2)^{|S|},
\qquad S\subseteq E.
\]

For every resolved cell \(T\subseteq E\),

\[
\sum_{S\subseteq T}\mu(S)
=\sum_{r=0}^{|T|}\binom{|T|}{r}(-2)^r
=(-1)^{|T|}.
\]

Since the Boolean zeta matrix is unitriangular,

\[
\boxed{
\mu=\zeta_{B_E}^{-1}\chi_{\rm orient}
}
\]

is the unique integral overlap coefficient system inducing orientation parity
\(\chi_{\rm orient}(T)=(-1)^{|T|}\).

## Consequence

The triangle result was not accidental. For every graph, the powers of two
come from incidence inversion between overlapping deletion pieces and
resolved orientation cells. They are not cosmology-specific couplings or
branch probabilities.

This theorem concerns the weighted-geometry coefficient architecture. It
does not assert that every graph has a nonzero hidden contact kernel like the
triangle.

## Evidence

- Benincasa–Dian, equation (4.69) and its binomial proof
- Entries 2205–2210
- `research/benincasa/checkers/all_arity_boolean_orientation.rs`
