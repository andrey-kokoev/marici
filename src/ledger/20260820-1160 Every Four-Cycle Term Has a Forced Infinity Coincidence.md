---
title: "Every Four-Cycle Term Has a Forced Infinity Coincidence"
date: 2026-08-20
entry: 1160
status: established-incidence-census
sector: cosmology
---

# 1160 — Every Four-Cycle Term Has a Forced Infinity Coincidence

Sequence claim: `seqclaim-17d4777912b64f96e4d02493`.

## Frozen packet

Entry 1159 derives 28 four-cycle OFPT terms. Removing the total-energy
factor \(q_G\), every term contains seven labelled denominators depending
on the four loop-edge variables.

At edge-variable infinity, retain the labelled denominator but take its
degree-one edge normal. Complementary connected subgraphs have the same
normal:

\[
\operatorname{in}_\infty q_{g_S}
=
\operatorname{in}_\infty q_{g_{S^c}}.
\]

They remain distinct affine denominators; only their infinity sections
coincide.

## Termwise census

The seven labelled infinity normals in every OFPT term are non-generic.
Their multiplicity profiles are

\[
\boxed{
20\text{ terms}: (2,1,1,1,1,1),
\qquad
8\text{ terms}: (2,2,1,1,1).
}
\]

Thus every term contains at least one forced complementary pair, and eight
terms contain two.

This is occurrence data. Deduplicating equal equations would erase which
source subgraphs approach the common infinity section.

## Residue-pivot census

There are

\[
28\times7=196
\]

labelled choices of a first marked residue. The exact census gives:

- 72 pivots have a parallel labelled partner whose leading restriction
  vanishes on the entire residue plane;
- 124 pivots have no partner in their own normal class;
- after grouping retained occurrence labels by geometric line, no two
  distinct active lines coincide;
- only 8 pivots have no forced triple concurrence;
- 80 pivots have one forced concurrent triple;
- 108 pivots have two forced concurrent triples.

The full profile, including the number of active distinct lines, is exported
in the result packet.

## Geometric meaning

For the 72 parallel-partner pivots, the ordinary restriction to Entry
1154's residue plane is not a simple arrangement of six marked elliptic
curves. The partner's leading normal vanishes identically, while its affine
constant separates it at the next compactification order. This is a
source-forced filtered/nearby incidence problem.

For the other pivots, repeated labels can still define the same marked
curve, and the active distinct lines contain source-forced triple points.
These are incidence cells already compiled from the labelled source
hyperplanes. They are not generic-position accidents and do not justify a
new carrier stratum.

## Architectural update

The first explicit higher-site packet strengthens the need for

\[
\boxed{
\text{occurrence-resolved carrier}
+\text{ filtered infinity specialization}
+\text{ relative elliptic coefficients}.
}
\]

The componentwise elliptic result of Entry 1156 survives, but a naive
normal-crossing union of independent elliptic curves does not.

## Next falsifier

Choose one representative from each of Entry 1159's seven cyclic term
orbits and one representative of every pivot profile. Compactify the full
affine denominator pair, not only its leading normal, and derive the local
normal form at the common infinity section. Then compute whether the
filtered partner contributes only Tate/Kummer extension data between the
existing elliptic residues, or creates a new coefficient Hodge type.

Evidence:

- `research/benincasa/checkers/audit_four_cycle_residue_incidence.py`;
- `research/benincasa/results/four-cycle-residue-incidence.json`;
- Entry 1159's exact 28-term denominator packet.
