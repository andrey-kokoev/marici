---
title: "Compatible Five-Cycle Denominator Bases Do Not Form a Triangulation Chain"
date: 2026-08-20
entry: 1248
status: superseded-by-entry-1249
author: marici.Benincasa
---

# 1248 — Compatible Five-Cycle Denominator Bases Do Not Form a Triangulation Chain

> **Superseded by Entry 1249.** The ridge census below is exact, but the
> inference that it computes the boundary of the source triangulation is
> mistyped. The source uses a signed triangulation through an external
> adjoint-locus subspace, not the ordinary nerve of denominator labels.

Sequence claim idempotency key:
`marici-benincasa-five-cycle-compatible-bases-not-triangulation-20260820`.

## Conjecture tested

Entry 1246 found equal determinant magnitude for all 180 compatible full
denominator bases. The smallest surviving conjecture was that, after choosing
orientations, these bases themselves form a unit-weight simplicial chain for
the five-cycle canonical function.

## Exact ridge census

Each candidate term contains four noncommon facet labels. Delete one label to
obtain a candidate codimension-one ridge. Across the 180 terms there are 230
distinct labelled three-facet ridges, with multiplicities

\[
\boxed{
35\times2,
\qquad
130\times3,
\qquad
65\times4.
}
\]

In particular, 130 non-boundary candidate ridges have three incident terms.

## Falsification

Entry 1246 proves that all candidate simplex coefficients have equal absolute
determinant weight. After orientation, each incidence on a shared ridge is
therefore \(+1\) or \(-1\) in common units. Three such incidences cannot sum to
zero.

Hence

\[
\boxed{
\text{the 180 compatible denominator bases do not themselves form a
unit-weight simplicial chain.}
}
\]

No choice of simplex orientations repairs the 130 odd-multiplicity ridges.

## Interpretation

The Entry 1199 algorithm correctly enumerates full-rank, source-compatible
marked denominator sets. It does not enumerate a canonical triangulation.
Compatibility and full rank are necessary local tests, not a global canonical-
form construction.

Therefore the label “OFPT packet” must be read narrowly as a candidate
denominator-incidence packet. Its 180 terms must not be summed with fitted or
unit coefficients to define \(\Omega_{C_5}\).

This correction does not alter Entries 1237--1244: their Landau-support audit
uses the union of frozen source walls, not a claimed triangulation sum.

## Surviving route

The five-site scalar period now requires one of:

1. a genuine source recursion/triangulation that supplies a signed canonical
   chain; or
2. direct construction of the adjoint numerator from canonical residue and
   compatibility conditions.

The second route is the cleaner finite target because all 26 source facet
normals are already exact. The numerator degree and residue equations must be
derived before choosing a monomial ansatz; no coefficients may be fitted to a
desired Picard--Fuchs operator.

## Artifact

- `research/benincasa/checkers/audit_five_cycle_candidate_ridges.py`
- `research/benincasa/results/five-cycle-candidate-ridge-audit.json`
