# Frozen bivariant network signature v3

## Status

Version 3 is a new frozen candidate. Version 2 remains unchanged and falsified.

The repair replaces bare labelled route spaces with labelled metric route spaces. It replaces the raw matrix associator with a metric matrix route associator. Cell creation during replay remains disabled, and maximum declared depth remains two.

## Route-space data

Every route space must carry:

- route labels;
- a nondegenerate Hermitian Gram matrix \(G\);
- its signature.

A singular Gramian is not silently inverted. It belongs to a separately declared degeneracy stratum.

For an associator

\[
F:(V_L,G_L)\longrightarrow(V_R,G_R),
\]

the dagger is

\[
F^\sharp=G_L^{-1}F^*G_R.
\]

The invariant isometry law is

\[
F^*G_RF=G_L.
\]

Positive and indefinite nondegenerate metrics are both admitted, but their signatures are typed and must match across an invertible isometry.

## General frame covariance

Under independent invertible coordinate changes \(S_L,S_R\),

\[
F'=S_R^{-1}FS_L,
\]

\[
G_L'=S_L^*G_LS_L,
\qquad
G_R'=S_R^*G_RS_R.
\]

Then

\[
F'^*G_R'F'=G_L'.
\]

This is the covariance missing from v2.

## Frozen laws

The metric associator must satisfy:

1. dimension and signature matching;
2. metric-relative dagger isometry;
3. every applicable pentagon with transported route metrics;
4. independent \(GL\) frame covariance;
5. restriction/extension naturality;
6. every applicable braided hexagon;
7. separately declared contextual exposure.

Pairings, associators, and primitive lifts remain distinct types even when represented by identical arrays. In particular, associator data cannot change Strominger's independently defined filling or homotopy quotient.

## Local gates

The v2 failure packet now passes: the nonorthonormal Ising matrix preserves its transported positive Gramian.

The first unused local packet is a rational Lorentz isometry on a signature-\((1,1)\) route space, placed in independent nonunitary domain and codomain frames. It passes the metric isometry and metric-dagger inverse laws while failing raw Euclidean unitarity, exactly as v3 predicts.

These are local schema gates only. Full v3 admission requires a complete unused metric fusion packet with every required metric pentagon and hexagon.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v3.py
```
