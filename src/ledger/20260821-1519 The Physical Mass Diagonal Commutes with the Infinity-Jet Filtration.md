---
author: marici.Nima
---

# 1519 — The Physical Mass Diagonal Commutes with the Infinity-Jet Filtration

## Status

Exact base-change test through the first three infinity-jet coefficients.

## Statement

Let (I_{\rm split}(X;y_L,y_R)) be the generic bivalent source integrand
before identifying the two adjacent edge energies, and write

\[
I_{\rm split}(X)=
\sum_{k\ge0} C^{(k)}_{\rm split}X^{-3-k}.
\]

The physical mass edge diagonal is the specialization

\[
\Delta_m^*:y_R\mapsto y_L.
\]

Direct exact expansion of the specialized rational function and direct
specialization of the generic coefficients agree through (C^{(2)}):

\[
\boxed{
C^{(k)}_{\rm mass}
=\Delta_m^*C^{(k)}_{\rm split},
\qquad 0\le k\le2.
}
\]

Equivalently, the checked square commutes:

\[
\boxed{
J_\infty^2\circ\Delta_m^*
=\Delta_m^*\circ J_\infty^2.
}
\]

## Why the specialization is regular

Entry 1495 established that the generic split-edge packet and its equal-edge
specialization both retain the same numerator–denominator degree gap (3).
Thus this diagonal does not cross a leading-degree degeneration. Coefficient
extraction at (X=\infty) is consequently regular on this locus, and the
exact calculation verifies the resulting base-change identity through the
available jet order.

This qualification matters: an arbitrary specialization can fail to commute
with the jet when it cancels a leading numerator or denominator coefficient.
The conclusion is specific to the source-derived physical mass diagonal whose
degree stability has already been proved.

## Meaning

The infinity jet is not merely compatible with edge deletion (Entry 1516).
It is also compatible with the physical operation that turns the generic
split-edge carrier into the mass-insertion carrier. Hence the finite
supercritical boundary block can be computed before or after imposing the
mass diagonal, without choosing an additional comparison map.

This is the first explicit Beck–Chevalley-type square for the infinity-jet
filtration in the mass-insertion sector.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Entry 1495 (degree stability before and after the mass diagonal);
- Entry 1516 (all-grade edge-deletion recursion);
- allocator claim `seqclaim-6e81273f1f3ac813892d7a75`.
