# Gauge quotient as a genuine over-extension sector

## Question

Does Marici contain a sourced projection-and-kernel sequence that realizes the over-attachment variance missing from the enlarged Green construction?

## Claim boundary

This packet classifies the completed gauge target sequence. It does not identify it with a Green-form extension, and it does not promote noncanonical linear splittings to gauge-covariant structure.

## Sourced sequence

Strominger declares the exact-shift subspace

\[
\mathcal G=d\mathcal D'(S^2)
\]

and the exact sequence

\[
0\longrightarrow\mathcal G
\longrightarrow\mathcal A_P
\overset{q}{\longrightarrow}\mathcal A_P/\mathcal G
\longrightarrow0.
\]

The source states that the kernel of the quotient is exactly the exact subspace. Its existing checker reproduces this as `GAUGE.exact`: the target quotient kills exactly the declared gauge line.

## Variance classification

This is a genuine over-category object over

\[
X=\mathcal A_P/\mathcal G:
\qquad q:\mathcal A_P\twoheadrightarrow X.
\]

Its kernel is typed independently as gauge redundancy. Pullback along a map \(Y\to X\) is the ordinary fiber product

\[
Y\times_X\mathcal A_P\longrightarrow Y,
\]

whose kernel remains \(\mathcal G\) in the ambient linear category. Thus contravariant reindexing is defined here, unlike unrestricted covariant pushout transport for Green isometries.

## Splitness and extension strength

As a sequence of plain real vector spaces, it admits noncanonical linear sections, so its ordinary vector-space extension class is trivial. The source does not supply a canonical gauge-covariant section. Therefore the live structured content is the quotient presentation and identified gauge kernel, not a nonzero ordinary Ext class.

A chosen gauge fixing would be extra section data. Treating existence of a linear complement as a canonical physical representative would violate presentation-versus-physics descent.

## Displayed-univalence gate

Objects over \(X\) are quotient presentations \(q:E\to X\) with identified gauge kernel. An isomorphism over \(X\) need not be literal equality of presentations. Displayed univalence therefore requires an explicit universe or path principle identifying structured isomorphisms over \(X\) with equalities of presentations. The exact sequence and checker do not provide that principle.

The first executable test is instead invariance: verify that observable maps out of \(E\) descend precisely when they annihilate \(\ker q\). This quotient universal property is the correct precursor to any univalence claim.

## Disposition

Marici has a sourced over-extension sector: the completed gauge quotient. It is pullback-oriented and kernel-typed, but ordinarily split noncanonically. It supplies the missing variance example while leaving displayed univalence unverified.

## Verification

- `research/strominger/completed-gauge-conservation-antipodal-quotient.md`, lines 8, 14–19, 110, 118–120
- `research/strominger/checkers/completed_gauge_conservation_antipodal_quotient_checks.py`
- `research/strominger/results/completed_gauge_conservation_antipodal_quotient.json`
- reproduced command: `uv run --with sympy python research/strominger/checkers/completed_gauge_conservation_antipodal_quotient_checks.py`
- reproduced outcome: `SUMMARY 6/6`
