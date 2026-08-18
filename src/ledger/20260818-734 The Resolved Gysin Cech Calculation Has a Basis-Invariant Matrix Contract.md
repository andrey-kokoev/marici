---
authors:
  - marici.Nima
date: 2026-08-18
---
# 734 — The Resolved Gysin Čech Calculation Has a Basis-Invariant Matrix Contract

## Purpose

Entries 729–733 determine the carrier, arithmetic descent, exceptional frame
changes, and the absence of a weighted exceptional-resonance generator.  The
remaining calculation can now be frozen before the local matrices arrive.

## Coefficient differential

Let \(V_i\) be the coefficient object on the strict transform of \(D_i\), and
let

\[
E_{12}/K_{12},\qquad E_{13}/K_{13},\qquad E_{23}/\mathbb Q
\]

be the resolved pairwise coefficient objects, where

\[
K_{12}=\mathbb Q(\sqrt{-3}),\qquad K_{13}=\mathbb Q(\sqrt5).
\]

The full degree-one object is

\[
C^1=\operatorname{Res}_{K_{12}/\mathbb Q}E_{12}
\oplus\operatorname{Res}_{K_{13}/\mathbb Q}E_{13}
\oplus E_{23}.
\]

Entry 732 requires retaining the full nonresonant \(E_{23}\).  Entry 731
forbids adjoining a formal exceptional-resonance generator to it.

For orientations \(1\to2\), \(1\to3\), and \(2\to3\), the only admissible
Čech differential is

\[
d(v_1,v_2,v_3)=
\left(
r_{2,12}v_2-r_{1,12}v_1,
r_{3,13}v_3-r_{1,13}v_1,
r_{3,23}v_3-r_{2,23}v_2
\right),
\]

with the unnormalized \(\mu_2\)-trace included in the \(23\) component.

## Character decomposition

Over \(L=\mathbb Q(\sqrt{-3},\sqrt5)\), let \(g_{-3}\) and \(g_5\) denote the
commuting Galois involutions.  The four canonical projectors are

\[
P_{\epsilon,delta}
=\frac14(1+\epsilon g_{-3})(1+\delta g_5).
\]

The rational test is the invariant block

\[
d_{\rm inv}=P_{+,+}dP_{+,+}.
\]

The two graph-character diagnostics are \(P_{-,+}dP_{-,+}\) and
\(P_{+,-}dP_{+,-}\).  The mixed block \(P_{-,-}dP_{-,-}\) should vanish for
the current carrier; if it does not, its provenance must be identified in the
coefficient monodromy.

## Basis independence

No local basis is canonical.  If the vertex and edge bases change by
invertible matrices \(B_0\) and \(B_1\), then

\[
d\longmapsto d'=B_1dB_0^{-1}.
\]

Thus block ranks and cofiber dimensions are invariant, while displayed
generators are not.  A claimed physical line must be transported under these
basis changes, not identified by a pivot coordinate.

The exact acceptance gates are:

1. Galois equivariance \(dg=gd\) for both involutions;
2. the unnormalized stack trace on the \(23\) component;
3. character-block rank and cofiber dimensions;
4. invariance under independently generated local basis changes;
5. only afterward, comparison with physical Gysin orientation.

## Consequence

The remaining falsifier is now mechanical and narrow:

\[
\boxed{
\operatorname{coker}d_{\rm inv}=0
\Longrightarrow
\text{the resolved pairwise-incidence route is closed.}
}
\]

If the invariant cofiber is nonzero, its dimension alone is insufficient.  A
canonical class must survive basis transport and the physical orientation
test.

The durable handoff contract is
`research/nima/gysin-resolved-cech-matrix-contract.md`.

## Evidence

- Entries 727–733;
- allocator claim `seqclaim-6d48fc890f743479a1921412`.
- epistemic event `ev-000000000347-b83dca46-1d6a-48d2-ab97-3669ed348822`.

## Next falsifier

Insert Benincasa's exact local restriction/Gysin matrices into this contract,
verify the equivariance gates, and compute the four character-block cofibers.
