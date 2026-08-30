---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2152 — The Three Final Triangle Deletions Are Typed Logarithmic Port Morphisms

> **RETRACTED by Entry 2153.** The three rational ratios and their cyclic
> formulas are exact, but calling them typed cube arrows confuses a
> presentation gauge with a source-defined coefficient morphism.

## Hard-to-vary claim

The three adjacent edges from deletion grade two to the all-deleted triangle
sector inherit Entry 2149's rational port map and Entry 2150's strict
logarithmic lift.

## Representative labelled edge

Take

\[
S=\{12,23\},
\]

so the retained edge is \(31\). The nontrivial connected component has
shifted endpoint energies

\[
A_1=X_1+y_{12},
\qquad
A_3=X_3+y_{23},
\]

and component total

\[
Q_{13}=A_1+A_3
=X_1+X_3+y_{12}+y_{23}.
\]

Deleting the last edge \(31\) replaces the connected line factor by its two
contacts and gives

\[
\boxed{
D_{31}=\frac{Q_{13}}{y_{31}}.
}
\]

The endpoint contact poles are

\[
q_1=A_1+y_{31},
\qquad
q_3=A_3+y_{31}.
\]

The isolated site-2 contact and the previously deleted-edge factors are
common spectators.

## Cyclic packet

Cyclic relabelling gives

\[
D_{12}
=
\frac{X_1+X_2+y_{31}+y_{23}}{y_{12}},
\]

\[
D_{23}
=
\frac{X_2+X_3+y_{12}+y_{31}}{y_{23}}.
\]

Each map carries the forced connection shift

\[
\boxed{
A_{E}=A_{E\setminus\{ij\}}
-d\log Q_{ij}+d\log y_{ij}.
}
\]

It is a strict coefficient morphism away from \(Q_{ij}y_{ij}=0\).

## Physical chain

On the literal positive chamber, every \(Q_{ij}>0\). Near the erased-edge
soft boundary, the same \(d=3\) radial argument as Entry 2151 leaves
\(r,dr\), so no soft Gysin current survives at generic external separation.

Therefore the three final deletion edges are both coefficient-horizontal and
physical-chain compatible on the generic physical chamber.

## Scope

This types exactly the three arrows

\[
\{12,23\},\{23,31\},\{12,31\}
\longrightarrow
\{12,23,31\}.
\]

It does not type the six grade-one-to-grade-two arrows or the three
grade-zero-to-grade-one arrows. Those involve connected path or loop
coefficients rather than a universal last-edge line deletion.

## Evidence

- Benincasa--Dian, arXiv:2401.05207, equations (2.14), (2.27)--(2.30);
- Entries 2135 and 2149--2151;
- `research/benincasa/marici-gm/src/bin/triangle_final_deletion_maps.rs`;
- allocator claim `seqclaim-581fda22c7fe35127ce32498`.

## Next falsifier

Construct one grade-one-to-grade-two deletion morphism from the actual
connected path integrand. Determine whether it is again a rational
logarithmic gauge map or whether deletion-induced graph disconnection
requires a nontrivial localization/Gysin cone.
