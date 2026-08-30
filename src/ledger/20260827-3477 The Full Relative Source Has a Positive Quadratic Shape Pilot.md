---
author: marici.Benincasa
date: 2026-08-27
status: numerical discovery evidence
---

# 3477 — The Full Relative Source Has a Positive Quadratic Shape Pilot

## Question

Does the quadratic shape response detected by the absolute elliptic
coefficient block survive in the complete source-defined relative period, or
is it cancelled by the remaining coefficient and boundary terms?

## Fixed-cycle representation

Use the source momentum representation to replace the moving
Cayley--Menger cycle by \(\ell\in\mathbb R^3\). Along

\[
X_1=1+t,\qquad X_2=1-t,\qquad X_3=1,
\]

choose exact planar momenta with lengths \(X_i\) and zero sum. The three loop
edge lengths are

\[
y_{12}=|\ell|,\qquad
y_{23}=|\ell+p_1|,\qquad
y_{31}=|\ell+p_1+p_2|.
\]

Substitute these into the literal six-simplex source of equation (51),
retaining all three site poles, all three deleted-edge poles, and all three
two-site poles. This computes the complete scalar integrand rather than an
absolute elliptic projection.

## Deterministic QMC pilot

A Halton integration on \(\mathbb R^3\), using
\(r=u/(1-u)\) and the exact spherical Jacobian, gives the correlated symmetric
finite difference

\[
\frac{I(h)-2I(0)+I(-h)}{h^2}.
\]

At four million samples and \(h=0.02\), three disjoint Halton windows give

\[
4.5445\times10^{-4},\qquad
4.6066\times10^{-4},\qquad
4.7264\times10^{-4}.
\]

At the first window, the step scan \(h=0.04,0.02,0.01\) gives

\[
4.6344\times10^{-4},\qquad
4.5445\times10^{-4},\qquad
4.6409\times10^{-4}.
\]

The corresponding first differences remain near zero, as required by the
site-exchange symmetry.

## Narrow interpretation

The complete relative source displays a stable positive quadratic shape
response in this numerical representation. Thus cancellation of the
elliptic response by the rest of the physical source is not observed.

This is discovery evidence, not a theorem. The computation still requires:

1. an exact check of the normalization in the momentum-space pushforward;
2. a certified integration and tail error bound, or an exact relative IBP
   reduction;
3. replication in an independently parameterized fixed-cycle chart.

No new carrier support or localization splitting was used.

## Next falsifier

Differentiate the fixed-cycle source integrand analytically at \(t=0\).
Determine whether its angular average or a source-derived divergence identity
has a fixed sign. If not, reduce the exact second-shape insertion in the
relative marked-wall complex and pair it with the physical cycle.

## Evidence

- `research/benincasa/marici-gm/src/bin/physical_relative_shape_qmc.rs`;
- `research/benincasa/results/physical-relative-shape-qmc-pilot.json`;
- primary source equation (51) and momentum representation (54).

Allocator claim: `seqclaim-77f08f906031f0f937766633`.

