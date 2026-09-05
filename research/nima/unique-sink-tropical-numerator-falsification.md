# Unique-sink tropical-numerator conjecture: falsification

## Problem

Test whether the quartic tropical numerator of Arkani-Hamed and Figueiredo, arXiv:2402.06719, canonically assembles precisely on quadrangulations with a unique sink, with sink slots giving its complete contact sector.

## Bold conjecture tested

For every even multiplicity, the published quartic tropical numerator admits canonical quadrangulation assembly exactly on unique-sink quadrangulations, and its polynomial contacts are the two sink-slot terms of each such quadrangulation.

## Named rivals

1. The published numerator multiplies contributions from all quadrilaterals visible in a triangulation cone, including mutually overlapping ones, and therefore defines a different non-polynomial theory.
2. Unique-sink assembly applies only to the repository's separately defined QTDS quadrangulation product, not to the numerator of arXiv:2402.06719.

## Strongest falsification test

The rendered full text of arXiv:2402.06719 was inspected around its definition and contact-term derivation. It states that, in a cone, the nontrivial quartic factors come from quadrilaterals made from triangulation chords; many overlap. Their product “does not know how to paste together subsets of non-overlapping quadrilaterals into quadrangulations.” The paper then derives the theory actually produced by the numerator.

For constant quartic input `g`, every triangulation cone contributes to the contact term, and the published `m`-point contact coefficient is

\[
C_{m-2}g^{m-3}.
\]

The resulting interaction is the paper's Catalan Lagrangian, with interactions at both even and odd multiplicity. For general quartic input, equation (30) sums products over all triangulations of the `m`-gon, not over unique-sink quadrangulations.

## Exact residual

The index sets and coefficients disagree before any subtle sign or normalization issue:

- published numerator: all triangulation cones, including overlapping quadrilateral factors;
- conjectured numerator: nonoverlapping quadrangulations satisfying a unique-sink condition;
- published contacts: Catalan coefficients at every multiplicity;
- conjectured contacts: two scalar slot terms per unique-sink quadrangulation at even multiplicity.

No map equating these objects is present, and their support rules are incompatible. The phrase in the paper about failure to assemble quadrangulations describes a feature of its numerator, not an open problem that the unique-sink restriction can solve without changing the theory.

## Disposition

The bold conjecture is falsified. Rival 1 survives: arXiv:2402.06719 constructs a Catalan non-polynomial theory rather than the repository's QTDS quadrangulation product. The marked unique-sink theorem may remain a standalone combinatorial result or apply to QTDS after QTDS is independently defined, but it cannot be advertised as a classification of the published quartic tropical numerator's contact sector.

A distinct comparison could ask whether a projection, deformation, or coefficient extraction from the published Catalan numerator yields QTDS. That requires an explicit source-derived map and cannot be inferred from matching Catalan language.
