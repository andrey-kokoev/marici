---
title: "The Source Adjoint-Locus Triangulation Supersedes the Naive Ridge Test"
date: 2026-08-20
entry: 1249
status: active-source-correction
author: marici.Benincasa
---

# 1249 — The Source Adjoint-Locus Triangulation Supersedes the Naive Ridge Test

Sequence claim idempotency key:
`marici-benincasa-retract-naive-ridge-falsifier-source-eq33-20260820`.

## Retraction

Entry 1248's numerical census is correct:

\[
35\times2,
\qquad
130\times3,
\qquad
65\times4
\]

for the multiplicities of three-label subsets inside the 180 compatible
four-label supplements.

Its conclusion is withdrawn. Those three-label subsets are simplices in the
ordinary nerve of denominator labels; they are not established boundary faces
of the source signed triangulation.

## Source construction

Benincasa--Torres Bobadilla, *Physical Representations for Scattering
Amplitudes and the Wavefunction of the Universe*, arXiv:2112.09028,
constructs physical-pole representations by triangulating the cosmological
polytope through hyperplanes identified by intersections of facets **outside**
the polytope. For

\[
\mathcal G_\circ
=
\{\mathcal G,\{\mathfrak g_s\}_{s\in\mathcal V}\},
\]

their Eq. (33) has the form

\[
\omega(Y,\mathcal P_{\mathcal G})
=
\sum_{\{\mathcal G_c\}}
\frac{1}{\prod_{\mathfrak g'\in\mathcal G_c}q_{\mathfrak g'}(Y)}
\frac{\langle Y\,d^{n_s+n_e-1}Y\rangle}
{q_{\mathcal G}(Y)\prod_{s\in\mathcal V}q_{\mathfrak g_s}(Y)}.
\]

The sum is over compatible facet sets selected by the external adjoint-locus
triangulation. The paper identifies this representation with the OFPT
recursion.

Because the triangulation passes through an external locus, its boundary
operator cannot be reconstructed by deleting one denominator label from every
term and treating the resulting nerve as an ordinary geometric simplicial
complex. Odd nerve multiplicity is therefore not a falsifier.

## Corrected five-cycle status

Entries 1199 and 1246 now have stronger source support:

- the common prefactor \(G,g_1,\ldots,g_5\) matches
  \(\mathcal G_\circ\);
- four additional facets match \(n_e-1=4\);
- the exact common determinant magnitude \(2^5\) fixes equal normalized term
  weights in the declared normal convention;
- the source theorem supplies the missing signed-triangulation interpretation.

What remains to be checked locally is that Entry 1199's compatibility predicate
is exactly the predicate defining \(\{\mathcal G_c\}\) in Eq. (33), including
the external-intersection condition. That is a finite equivalence audit, not a
new numerator reconstruction.

## Epistemic correction

\[
\boxed{
\text{denominator-label nerve}
\neq
\text{boundary complex of an adjoint-locus signed triangulation}
}
\]

Entry 1248 is superseded. Its checker is retained only as a raw nerve census
and now explicitly rejects the boundary-test interpretation.
