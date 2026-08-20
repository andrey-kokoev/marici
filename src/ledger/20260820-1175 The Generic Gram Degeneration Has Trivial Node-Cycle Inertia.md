---
title: "The Generic Gram Degeneration Has Trivial Node-Cycle Inertia"
date: 2026-08-20
entry: 1175
status: active
sector: cosmology
---

# 1175 — The Generic Gram Degeneration Has Trivial Node-Cycle Inertia

Sequence claim: `seqclaim-5d328540d2df9ad9844f37eb`.

## Transverse normal form

At a generic rank-two point of \(\det G=0\), choose étale coordinates and a
transverse parameter \(s\) so that

\[
G(s)=\operatorname{diag}(1,1,s),
\qquad
\operatorname{adj}(G(s))=\operatorname{diag}(s,s,1).
\]

At any of the eight persistent node sections, the double-solid equation has
quadratic normal form

\[
\boxed{
W^2-x_3^2-s(x_1^2+x_2^2)=0.
}
\]

The Hessian discriminant vanishes to order two in \(s\). At \(s=0\),

\[
(W-x_3)(W+x_3)=0,
\]

so the special fiber is a pair of components meeting along the
\((x_1,x_2)\)-plane.

## Nearby character

Over the quadratic Kummer cover \(s=\tau^2\), the generic quadratic form is
trivialized by

\[
(x_1,x_2)\longmapsto(\tau x_1,\tau x_2).
\]

The deck involution \(\tau\mapsto-\tau\) flips two transverse coordinates:

\[
(W,x_3,x_1,x_2)longmapsto(W,x_3,-x_1,-x_2).
\]

Its determinant on the vanishing three-sphere is \(+1\). Therefore the
rank-one node cycle has

\[
\boxed{T_{\det G}=+1.}
\]

The Kummer square root is present in the normalization, but its two sign
flips cancel on the vanishing-cycle orientation. There is no new generic
inertia character.

## Consequence

The generic Gram specialization is accounted for by:

\[
\boxed{
\text{existing Gram divisor}
+
\text{existing quadratic Kummer normalization}
+
\text{trivial node-cycle inertia}.
}
\]

This closes the generic codimension-one transport test. It does not compute
the full supported costalk where the Gram rank drops further or where Gram
support meets soft/signed-energy strata.

## Next falsifier

Move to the first deeper Gram stratum, \(\operatorname{rank}G\le1\). Compute
the labelled iterated nearby-cycle/Koszul complex and compare it with the
existing Gram-minor incidence cube. A residual cofiber there would be new
coefficient complexity; only an undeclared support divisor would threaten
the carrier hypothesis.

## Evidence

- `research/benincasa/checkers/four_site_qg_gram_nearby_cycle.py`
- `research/benincasa/results/four-site-qg-gram-nearby-cycle.json`
- Entries 1165 and 1174.
