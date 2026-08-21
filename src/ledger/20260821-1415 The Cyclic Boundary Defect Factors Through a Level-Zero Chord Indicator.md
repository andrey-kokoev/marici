# 1415 — The Cyclic Boundary Defect Factors Through a Level-Zero Chord Indicator

## Status

Replicated two-prime modular factorization. The scalar functional is not yet reconstructed in characteristic zero.

> **CORRECTION (Entry 1423).** The chord indicator is the support indicator of the growth-four grade. Its zero on orbits (5,11) means those orbits have no boundary rows, not that their rows vanish.

## Setup

Use the cyclic augmentation base of corrected Entry 1413 at primitive degree one. The affine system has a unique solution.

For each boundary row, evaluate the residual of that unique affine primitive.

## Exact orbit partition

The six nontrivial (C_5)-sheet orbits have representatives

\[
1,3,5,7,11,15.
\]

The compatible set is

\[
\mathcal O_{\rm diag}=\{5,11\},
\]

the diagonal-pair orbit and its complement. The obstructed set is

\[
\mathcal O_{\rm obs}=\{1,3,7,15\}.
\]

## Residual factorization

For each of twelve independently sampled boundary directions (d), there is a scalar

\[
\rho_d\in\mathbf F_p
\]

such that every sheet (S) obeys

\[
\boxed{
\operatorname{res}_d(S)
=
\rho_d\,\chi_{\rm obs}(S),
}
\]

where

\[
\chi_{\rm obs}(S)=
\begin{cases}
0,&\operatorname{orb}(S)\in\{5,11\},\\
1,&\operatorname{orb}(S)\in\{1,3,7,15\}.
\end{cases}
\]

Within each obstructed orbit, all five cyclic sheets have the same residual. Across all four obstructed orbit types, the residual is again the same.

Every nonzero row occurs at radial level zero. Each obstructed orbit contributes exactly

\[
12\times5=60
\]

nonzero rows.

The factorization is reproduced over

\[
\mathbf F_{1019}
\qquad\text{and}\qquad
\mathbf F_{1009}.
\]

## Narrow interpretation

The finite obstruction is not six unrelated failures and is not controlled by Hamming weight. It has rank-one dependence in the kinematic direction and a discrete chord-type selector on the occurrence carrier.

This is the first evidence on the cyclic base for a separation

\[
\boxed{
\text{scalar boundary functional}
\otimes
\text{Carrier chord indicator}.
}
\]

The indicator is native to the labelled five-cycle: it distinguishes diagonals from edges while respecting (C_5).

## Prohibited inference

Do not yet identify this indicator with a physical string primitive, cluster adjacency rule, or associahedral incidence class. The calculation uses a declared radial grading and modular samples.

## Next finite falsifier

Reconstruct the scalar functional (ho) from the source denominator data and determine whether the orbit indicator equals an existing graph-theoretic incidence valuation. Reject the factorization if either part depends on the sampling convention.

Artifacts:

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_kummer_ibp_pilot.rs`
- `research/benincasa/results/five-site-cyclic-level-zero-obstruction.json`

Allocator claim: `seqclaim-3346d38e5309aaee2b155241`.
