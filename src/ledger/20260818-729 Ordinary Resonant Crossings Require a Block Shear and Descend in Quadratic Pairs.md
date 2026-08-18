---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 729 — Ordinary Resonant Crossings Require a Block Shear and Descend in Quadratic Pairs

## Frozen question

Resolve the four simple crossings \(D_1\cap D_2\) and \(D_1\cap D_3\), pull
back the full adapted rank-four Gysin connection, and determine its exceptional
local type without treating conjugate geometric points as rationally
independent.

Here

\[
D_1=(v-u),\qquad D_2=(y-u^2),\qquad D_3=(y+u^2),
\quad y=(u+v)/2-1.
\]

## Ordinary charts and forced frame

At a crossing \((u_0,u_0)\), use

\[
U_u:\ u=u_0+e,\ v=u_0+et,
\qquad
U_v:\ u=u_0+es,\ v=u_0+e.
\]

In the unmodified adapted frame the quotient-to-kernel block has exceptional
order \(-2\).  Hence it is not logarithmic.  The existing Gysin block
filtration forces the elementary transform

\[
(e_6,v_{\rm alg};\omega_0,\omega_2)
\longmapsto
\operatorname{diag}(1,1,e,e)
(e_6,v_{\rm alg};\omega_0,\omega_2).
\]

No fitted exceptional factor is used.  After this transform every coefficient
has at most a logarithmic exceptional pole.  On the overlap

\[
e_v=e_ut,\qquad s=t^{-1},
\]

the transformed frames differ by

\[
\boxed{\operatorname{diag}(1,1,t,t)}.
\]

## Exact local census

The exact modular function-field calculation gives the same local dimensions
at all four geometric crossings and in both charts:

\[
\operatorname{rank}R_E=3,
\qquad
\dim\ker R_E=\dim\operatorname{coker}R_E=1,
\]

and the first indicial operator has

\[
\boxed{\dim\ker L_1(R_E)=\dim\operatorname{coker}L_1(R_E)=2.}
\]

Both strict transforms remain logarithmic at their points on \(E\), and each
has a two-dimensional first resonant kernel.  These dimensions are invariant
under exchange of the two ordinary charts.

## Arithmetic descent

The crossings are not four rational coefficient objects.  They form the two
closed points

\[
u_0^2-u_0+1=0,
\qquad
u_0^2+u_0-1=0,
\]

with involutions

\[
u_0\mapsto1-u_0,
\qquad
u_0\mapsto-1-u_0.
\]

The chart construction, block shear, transition exponents, and rank packet are
equivariant under these involutions.  Thus the two pairs descend as Weil
restrictions over \(\mathbb Q(\sqrt{-3})\) and \(\mathbb Q(\sqrt5)\), in accord
with Entries 727–728.

## Narrow result

\[
\boxed{
\text{Each simple pairwise crossing carries a logarithmic rank-three
exceptional residue after the source-derived }(0,0,1,1)\text{ shear.}
}
\]

This does **not** yet produce a pairwise obstruction class.  Kernel dimensions
alone do not define the resolved Čech differential.  In particular, the two
quadratic-character cycles of Entry 728 cannot be promoted to rational
physical classes.

## Evidence and reproducibility

- exact derivation harness:
  `research/benincasa/gysin_ordinary_crossing_blowup.py`;
- generated convention packet:
  `research/benincasa/marici-gm/gysin-ordinary-crossing-blowup.json`;
- durable convention packet:
  `research/benincasa/marici-gm/gysin-ordinary-crossing-conventions.md`;
- durable Rust certificate:
  `research/benincasa/marici-gm/src/bin/gysin_ordinary_crossing_certificate.rs`;
- allocator claim `seqclaim-05a4a756273b413389cab0c5`.
- epistemic event
  `ev-000000000342-5011b534-32c7-4de6-af84-91c9326f25b9`.

## Next falsifier

Resolve the rational non-simple crossing (D_2\cap D_3=(0,2)).  Derive the
weighted Newton charts from the unequal pole orders \((-3,-2)\), then compare
its exceptional coefficient object with the invariant incidence cycle

\[
\gamma_0=(e_{12}^++e_{12}^-)-(e_{13}^++e_{13}^-)+2e_{23}.
\]

Only the resulting coefficient Čech differential can decide whether a
nonzero rational pairwise obstruction survives.
