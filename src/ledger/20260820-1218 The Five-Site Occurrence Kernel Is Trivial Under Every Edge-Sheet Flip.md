---
title: "The Five-Site Occurrence Kernel Is Trivial Under Every Edge-Sheet Flip"
date: 2026-08-20
entry: 1218
status: active-supported-equivariant
sector: cosmology
---

# 1218 — The Five-Site Occurrence Kernel Is Trivial Under Every Edge-Sheet Flip

Sequence claim: `seqclaim-37b8775b72ce796bbdde5ee8`.

## Frozen occurrence kernel

Entry 1203 gives 240 complementary-occurrence generators, assembled as

\[
K_{\rm occ}\simeq\mathbb Q[C_5]^{48}.
\]

They split into

\[
200\ \text{generators of type }(1|4),
\qquad
40\ \text{of type }(2|3).
\]

## Edge-sheet action

For every connected subset \(A\) of the five-cycle,

\[
\partial A=\partial A^c
\]

as a labelled edge-occurrence vector. Consequently

\[
q_A
=
\sum_{i\in A}X_i+\sum_{e\in\partial A}y_e
\]

and \(q_{A^c}\) contain exactly the same labelled \(y_e\) terms.

Each deck generator of Entry 1217's \(C_2^5\) cover changes the sign of one
\(y_e\). It therefore acts identically on both members of every complementary
pair. The exact audit of all 240 generators gives

\[
\boxed{
K_{\rm occ}
\simeq
\mathbf1_{C_2^5}\otimes\mathbb Q[C_5]^{48}.
}
\]

No nontrivial edge-sheet Kummer character occurs in the occurrence kernel.

## Higher-normal compatibility

Entry 1204's first-Rees symbols are

\[
\widehat q_A-\widehat q_{A^c}=2\rho X_A
\qquad(E_T=0).
\]

They contain no edge-sheet variable. Hence the first-Rees attachment and the
soft Koszul/conormal complexes of Entries 1205--1206 are \(C_2^5\)-equivariant
with trivial action on their occurrence factors.

The physical coefficient object is therefore

\[
\boxed{
\mathcal K_{\det(H)^{-1/2}}
\otimes
\mathbf1_{C_2^5}
\otimes
\mathbb Q[C_5]^{48},
}
\]

before inserting the remaining marked-relative cohomology.

## Meaning

The multi-Kummer cover is necessary to make all marked denominators linear,
but its edge-sheet deck characters do not decorate the complementary
occurrence kernel. Occurrence multiplicity and coefficient-sheet multiplicity
are independent typed structures.

No new carrier datum or residual edge Kummer character is found.

## Next falsifier

Compute the marked-relative cohomology over this cover rather than only its
occurrence kernel. Determine which of the 32 edge-sheet characters actually
occur in the cohomology of the 26-section arrangement and whether the
Euclidean positive sheet selects a canonical invariant/trace object. This is
a coefficient question; only new support would challenge the carrier.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_occurrence_kummer_characters.rs`
- `research/benincasa/results/five-site-occurrence-kummer-characters.json`
