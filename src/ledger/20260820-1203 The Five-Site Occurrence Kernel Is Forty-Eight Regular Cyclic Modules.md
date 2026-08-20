---
title: "The Five-Site Occurrence Kernel Is Forty-Eight Regular Cyclic Modules"
date: 2026-08-20
entry: 1203
status: active-occurrence-descent
sector: cosmology
---

# 1203 — The Five-Site Occurrence Kernel Is Forty-Eight Regular Cyclic Modules

Sequence claim: `seqclaim-476788d941c21f006f4737cc`.

## Canonical occurrence map

For a term with (m) geometric marks, map its nine labelled occurrences to
the geometric degree-one logarithmic generators:

\[
0\longrightarrow K_{\rm occ}
\longrightarrow\mathbf Q^9
\longrightarrow\mathbf Q^m
\longrightarrow0.
\]

Because Entry 1200's multiplicities are at most two, (K_{\rm occ}) is
generated canonically by differences

\[
[g_A]-[g_{A^c}]
\]

whenever complementary source labels define the same infinity hyperplane.

The termwise kernel ranks are

\[
2,quad1,quad0
\]

for the seven-, eight-, and nine-geometric-mark profiles respectively.

## Global cyclic transport

Across all 180 terms,

\[
\dim K_{\rm occ}^{\rm labelled}
=70\cdot2+100\cdot1=240.
\]

Transport every ordered difference under the labelled five-cycle action.
When the canonical lexical order reverses, retain the induced sign. Exact
transport gives 48 free five-element orbits, and every closed-orbit sign is

\[
+1.
\]

Therefore

\[
\boxed{
K_{\rm occ}^{\rm global}
\simeq
\mathbf Q[C_5]^{\oplus48}.}
\]

## Meaning

Occurrence multiplicity is neither disposable metadata nor additional
geometric complement cohomology. It is a regular labelled presentation
module over Entry 1202's seven geometric OS carrier types.

This realizes the shared-carrier architecture in a concrete exact sequence:

\[
\text{labelled occurrence presentation}
\twoheadrightarrow
\text{geometric carrier},
\]

with a source-derived cyclic kernel and no descent anomaly.

## Next falsifier

Attach the five-site infinity double-cover coefficient system to the seven
geometric OS types, then pull it back through the occurrence presentation.
Test whether the (K_{\rm occ}) directions act trivially on coefficients or
carry nontrivial Kummer characters. A nontrivial action must be derived from
the branch equation; it may not be inferred from label multiplicity alone.

## Artifacts

- `research/benincasa/checkers/five_site_qg_occurrence_kernel.py`
- `research/benincasa/results/five-site-qg-occurrence-kernel.json`
