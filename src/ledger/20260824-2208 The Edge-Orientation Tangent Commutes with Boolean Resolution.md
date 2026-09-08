---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2208 — The Edge-Orientation Tangent Commutes with Boolean Resolution

## Comparison square

Let \(Z\) be the Boolean zeta map from coefficients on overlapping pieces to
weights on resolved cells:

\[
(Z\mu)(T)=\sum_{S\subseteq T}\mu(S).
\]

For a labelled edge \(e\), the overlap-coordinate tangent has

\[
\delta_e\mu(S)=-2\,\delta_{S,\{e\}}.
\]

Its zeta image is

\[
(Z\delta_e\mu)(T)
=-2\,1_{e\in T},
\]

which is exactly the directly defined resolved-cell orientation tangent.
Hence the square

\[
\begin{array}{ccc}
\text{overlap coefficients} & \xrightarrow{Z} & \text{resolved cell weights}\\
\delta_e\,\downarrow & & \downarrow\,\delta_e\\
\text{overlap tangents} & \xrightarrow{Z} & \text{resolved tangents}
\end{array}
\]

commutes for all three labelled edges.

## Consequence

The contact selector is unchanged when transported from the \((-2)^{|S|}\)
overlap presentation to the native orientation-weight presentation. It is
not an artifact of choosing subdivision coefficients instead of resolved
cells.

This passes the first comparison-invariance gate. Its scope is the frozen
Boolean resolution; arbitrary unrelated triangulations are not yet covered.

## Evidence

- Entries 2206–2207
- `research/benincasa/checkers/boolean_zeta_comparison_square.rs`
