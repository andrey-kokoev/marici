# 580 — The Labelled Product-Pole Complex Closes the Deletion Cube

## Hard-to-vary claim

The complete three-denominator deletion cube is realized by one generic twisted de Rham complex over the frozen Cayley--Menger cover, provided every source denominator retains its own pole axis and localization transition.

No new carrier cell, generic \(q\)-regulator, or fitted support summand is needed.

## Frozen product lattice

For a selected subset \(S\) of

\[
q_{g_1},\qquad q_{g_2},\qquad q_{\mathcal G_{12}},
\]

retain presentations

\[
\frac{P}{K^m\prod_{i\in S}q_i^{n_i}}.
\]

For a polynomial vector field \(V\), the differential is

\[
\boxed{
\frac{\operatorname{div}V}{K^m\prod_iq_i^{n_i}}
+(\gamma-m)\frac{V(K)}{K^{m+1}\prod_iq_i^{n_i}}
-\sum_{i\in S}n_i\frac{V(q_i)}{K^m q_i^{n_i+1}\prod_{j\ne i}q_j^{n_j}}.
}
\]

Each axis has its own localization relation:

\[
\frac{P}{K^m\prod_iq_i^{n_i}}
=\frac{PK}{K^{m+1}\prod_iq_i^{n_i}},
\qquad
\frac{P}{K^m\prod_iq_i^{n_i}}
=\frac{Pq_j}{K^m q_j^{n_j+1}\prod_{i\ne j}q_i^{n_i}}.
\]

Freeze

\[
\gamma=5,\qquad \mathbb F_{32003},
\]

pole depth two on \(K\) and every selected \(q_i\), and degree-at-most-five numerators in the block with one pole on each selected divisor.

## Complete census

In nonzero mask order \(001,010,011,100,101,110,111\), the ranks at \((X_1,X_2,X_3)=(2,3,4)\) are

\[
\begin{array}{c|rrrrrrr}
N&001&010&011&100&101&110&111\\
\hline
7&18&18&16&26&25&25&24\\
8&10&10&10&18&19&19&21\\
9&8&8&9&16&18&18&21\\
10&8&8&9&16&18&18&21
\end{array}
\]

The second generic point \((3,5,6)\) reproduces the complete \(N=9\) row.

Including the calibrated empty mask gives

\[
\boxed{(7,8,8,9,16,18,18,21),}
\]

exactly the independently certified deletion cube. Its Möbius inversion is

\[
\boxed{(7,1,1,0,9,1,1,1).}
\]

Thus the lower pair has zero proper support grade, while each upper pair and the triple contribute one proper class.

## What has been established

The source-labelled divisor arrangement supplies a single chain-level coefficient complex whose deletion restrictions reproduce every rank in the cube. The distinction between geometric strata and proper support grades is retained: the lower-pair stratum exists even though its Möbius grade is zero.

This closes the finite rank-calibration gate needed before constructing Gauss--Manin transport.

It does **not** yet establish a compatible basis across deletion maps, the two-parameter connection, the rank-nine/rank-five extension, specialization to \(\gamma=-\tfrac12\), or compatibility with the physical relative integration chain.

## Consequence

No cosmology-specific carrier incidence was required. All additional ranks arise from the relative/logarithmic coefficient object over the existing source divisors.

\[
\boxed{
\text{shared carrier survives}
\quad+\quad
\text{sector-specific filtered coefficient complex is explicit at rank level}.
}
\]

This strongly updates H2, not H1.

## Next falsifier

Construct compatible normal-form bases and deletion maps for all eight masks from this same product-pole complex. Then derive two independent Gauss--Manin connection matrices before specializing \(\gamma\).

The first finite obstruction is failure of the connection to preserve the deletion filtration or failure of its curvature to vanish modulo exact rows. Either failure must be recorded without adding carrier cells.

## Artifacts

- \`research/benincasa/marici-gm/src/bin/generic_q_pole_twisted_derham_rank.rs\`
- \`research/benincasa/generic-multi-q-pole-twisted-derham-rank.json\`
