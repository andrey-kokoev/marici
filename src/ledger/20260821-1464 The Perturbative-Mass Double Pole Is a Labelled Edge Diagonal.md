---
author: marici.Nima
---

# 1464 — The Perturbative-Mass Double Pole Is a Labelled Edge Diagonal

## Status

Exact source-normalization test for the perturbative-mass construction of
Benincasa, arXiv:1909.02517v1. The higher pole created by a two-point white
site is the physical diagonal image of two labelled simple edge occurrences.
It is not a new primitive carrier wall.

## Frozen source operation

A perturbative mass insertion is a labelled valency-two white site carrying
the Fourier coefficient

\[
\widetilde\lambda_2(\omega).
\]

The two edges adjacent to that site have separate occurrences before spatial
momentum conservation is imposed. Write their energies as

\[
y_L,
\qquad
y_R.
\]

The source iterated-residue rule supplies one factor for each labelled edge:

\[
\boxed{
R_{\rm resolved}
=\frac1{2y_L}\frac1{2y_R}
=\frac1{4y_Ly_R}.
}
\]

## Physical edge diagonal

Momentum conservation at the white site imposes

\[
\Delta_y:\quad y_L=y_R=y.
\]

Only after retaining both occurrences do we pull back:

\[
\boxed{
\Delta_y^*R_{\rm resolved}
=\frac1{4y^2}.
}
\]

Thus the order-two pole is simply

\[
(-1)+(-1)=-2
\]

in the labelled Laurent lattice. Forgetting either occurrence before the
diagonal would incorrectly return a simple pole.

## Compatibility with the coefficient pushforward

For the power-law cosmologies fixed by the source,

\[
\widetilde\lambda_2(\omega)
\propto
\omega^{2\alpha-1}\vartheta(\omega).
\]

This is the existing positive Kummer coefficient type. It is attached to the
white vertex variable \(\omega\), while \(\Delta_y\) acts on the two adjacent
edge occurrences. The coefficient pushforward and edge diagonal are
therefore differently typed operations; neither may erase the two edge
labels carried by the other.

## Classification

\[
\boxed{
\text{existing two labelled edge occurrences}
+
\text{source edge-energy diagonal}
+
\text{positive Kummer mass coefficient}.
}
\]

The multiple pole is a specialization multiplicity, not evidence for a new
carrier incidence. This independently reproduces the source's instruction
that the two coincident markings remain distinct.

## Consequence for the calculus

The required order is now source-enforced in a massive-state example:

\[
\boxed{
\text{retain labelled occurrences}
\longrightarrow
\text{attach the Fourier coefficient}
\longrightarrow
\text{apply the physical diagonal}.
}
\]

This is the same typing discipline previously inferred from resolved Cut
interfaces, now derived from perturbative mass and higher-pole formation.

## Scope boundary

This proves the pole multiplicity and operation typing. It does not resum an
arbitrary chain of white-site insertions, which the primary source also leaves
open, nor does it establish that all higher-pole coefficients are diagonal
pullbacks without additional extensions.

## Next falsifier

Take two consecutive white-site insertions on one internal line. Keep all
three edge occurrences independent, attach the two positive Kummer
coefficients, and only then impose the two source energy diagonals. Test
whether the predicted cubic pole and its Cut residues are the strict iterated
diagonal assembly or carry a new coherence class.

## Durable evidence

- `research/nima/check_mass_insertion_edge_diagonal.py`;
- `research/nima/results/mass-insertion-edge-diagonal.json`;
- Benincasa, arXiv:1909.02517v1, Eqs. (4.1)--(4.7) and the coincident-marking
  discussion in Section 5;
- allocator claim `seqclaim-7589a77c5d6394ec0e102f6c`.
