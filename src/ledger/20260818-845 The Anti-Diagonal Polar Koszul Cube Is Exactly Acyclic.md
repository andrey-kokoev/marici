---
authors:
  - marici.Nima
date: 2026-08-18
---
# 845 — The Anti-Diagonal Polar Koszul Cube Is Exactly Acyclic

## Source of the cube

The anti-diagonal part of the labelled polar pair is

\[
M=2EP_3ab.
\]

Because this monomial is multilinear in the four normal coordinates, all
iterated normal maps are forced mixed derivatives. Their orientations are
the standard Koszul signs:

\[
(-1)^{\#\{\text{earlier indices already present}\}}.
\]

Mixed partials commute, while the incidence signs anticommute. Hence every
square face satisfies \(d^2=0\) without an additional fitted homotopy.

## Exact total complex

After removing the nonzero generic monomial units on each stratum, the
anti-diagonal incidence complex has dimensions

\[
1\longrightarrow4\longrightarrow6\longrightarrow4\longrightarrow1.
\]

The four differential ranks are

\[
\boxed{1,\ 3,\ 3,\ 1.}
\]

Therefore its homology dimensions are

\[
\boxed{0,\ 0,\ 0,\ 0,\ 0.}
\]

The checker constructs every signed incidence matrix, verifies all three
matrix products \(d_{k+1}d_k=0\), and computes the ranks over
\(\mathbb Q\).

## Consequence

The anti-diagonal labelled direction has no cubical coherence obstruction:

\[
\boxed{
H^\bullet\operatorname{Tot}_{E,P_3,a,b}(M)=0.
}
\]

Thus Entry 844's remaining uncertainty lies entirely in the filtered
diagonal column

\[
C=E^2(a^2-b^2)-P_1^2a^2+P_2^2b^2,
\]

where second-order \(a,b\) jets must be combined with order-zero
restrictions. Exactness of the anti-diagonal cube does not by itself close
that column.

## Verification

- checker: research/nima/audit_polar_antidiagonal_koszul_cube.py;
- packet: research/nima/polar-antidiagonal-koszul-cube.json;
- allocator claim: seqclaim-3b9652f16d80d8ea7a1a8e0c.
