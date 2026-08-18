---
id: 544
date: 2026-08-18
title: The Global Log Realization Is an Artin-Cone Kernel Not a Raw Span
---

# The Global Log Realization Is an Artin-Cone Kernel Not a Raw Span

Entry 543 rules out an ordinary raw-DNC equivalence preserving the physical
connector.  The correct logarithmic algebraic realization can nevertheless be
assembled canonically from the fs monoidal data of Entries 426--429.

For each of the 215 loaded PC cells, let (P_{S,H}) be its fine saturated
characteristic monoid and form the Artin cone

\[
\mathcal A_{P_{S,H}}
=
[\operatorname{Spec}\mathbb Z[P_{S,H}]/
  \operatorname{Spec}\mathbb Z[P_{S,H}^{\mathrm{gp}}]].
\]

The 522 cellular incidences are strict face localizations.  All 840 composable
two-step routes induce the same target groupification, so the atlas cocycles
commute strictly.  The Artin cones therefore glue to a global logarithmic
Artin-cone stack \(\mathcal A_{\mathrm{PC}}\).

The full constructible category of \(\mathcal A_{\mathrm{PC}}\) is larger than the
finite PC category because it includes nontrivial chart-torus inertia
characters.  The finite category is precisely the Kato-pulled sector with
trivial inertia.  Entry 428 proves that every operation used by the connector
preserves this sector:

\[
j^*, j_!, i^!, i_*, L\pi_!, R\pi_*,
\otimes, \underline{\operatorname{Hom}}, \mathbb D.
\]

## Correct type of the bridge

The normalization--conductor geometry has opposite geometric and coefficient
variance, as Entry 432 proves.  Consequently its global bridge is not a
morphism of Artin stacks.  It is the constructible bimodule kernel of Entries
433--435, hence an integral transform between the corresponding Kato sectors.
Applying it to the distinguished sheet object gives the unique framed
connector.

Thus the algebraic realization is

\[
\boxed{
\text{fs Artin-cone stacks}
\quad+\quad
\text{a mixed-variance constructible kernel},
}
\]

not a raw scheme span.  External products and strict Cut face maps preserve
trivial inertia, so Entry 542 propagates this realization to every even arity.

The raw DNC comparison remains the generic localization (X^{-1}).  It is
nonconservative and supplies the mandatory forgetting functor; it is not the
physical realization.

Therefore

\[
\boxed{\text{the global logarithmic Artin mixed-variance realization is
complete in the Kato sector}.}
\]

What remains outside this theorem is the larger nontrivial-inertia Artin
category, any raw-scheme enhancement that does not preserve the supported
class, and comparison with numerical amplitude or worldsheet formulas.

The executable audit is
`research/voevodsky/check_global_log_artin_mixed_variance_realization.py`.
