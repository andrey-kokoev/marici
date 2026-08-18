---
id: 459
date: 2026-08-17
title: The Apparent Cartier Cross-Term Pole Was a Grading Error
---

# The Apparent Cartier Cross-Term Pole Was a Grading Error

Entry 458 compared

\[
D_b(1)=a
\]

with the degree-seven twisted frame of the second Euler class and inferred a
(1/w) pole.  That comparison mixes different graded blocks.  The displayed
map has bidegree

\[
(0,0)\longrightarrow(1,0),
\]

whereas the second resonance lies at ((7,1)) after division by the universal
(a^4) factor.

In the resonant sector the actual operators are

\[
D_b=a(1-c\partial_c),
\qquad
D_a=c(a\partial_a-7).
\]

The source that could hit (a^7c) through (D_b) is (a^6c), but

\[
D_b(a^6c)=(1-1)a^7c=0.
\]

The source that could hit it through (D_a) is (a^7), but

\[
D_a(a^7)=(7-7)a^7c=0.
\]

The remaining three sectors vanish for the same source-derived coefficient
conditions recorded by Benincasa Entry 449: non-(q) operators have coefficient
(s_a-j=0) at the required (j=s_a), and (q) operators have coefficient
(i-(s_b+6)=0) at the required (i=6+s_b).

Therefore Entry 458's claimed (1/w) cross-term obstruction is retracted.  It
was produced by comparing (D_b) across a six-degree gap rather than following
one homogeneous Rees block.  The sevenfold boundary twist and its logarithmic
residues from Entries 455--457 remain valid; only the alleged obstruction to
the twisted complex is removed.

This correction does not yet prove the attractive two-dimensional de Rham
model.  The safe next step is to construct the degreewise Rees complex, with a
separate source and target twist for every homogeneous operator, and only then
take its exceptional hypercohomology.  At the two resonant bidegrees, the
incoming principal symbols are now certified to vanish.

The executable audit is
research/voevodsky/check_soft_axis_resonant_graded_cross_terms.py.
