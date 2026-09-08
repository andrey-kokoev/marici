---
author: marici.Benincasa
date: 2026-08-27
---

# 3406 — The Denominator Deletion Cube Does Not Authorize the Occurrence Support Projector

## Question

Entry 3401 proves that cyclic transport plus one support projector reduces the
finite occurrence coend to the trace line. Does the frozen cosmological source
already supply that projector through its Boolean denominator deletion cube?

## Two three-label systems

The denominator deletion cube of Entries 340 and 580 has axes

\[
q_{g_1},\qquad q_{g_2},\qquad q_{\mathcal G_{12}}.
\]

It has eight mask objects and twelve directed deletion arrows. Every arrow
changes the denominator mask and therefore maps between two differently
supported coefficient modules.

The occurrence coend of Entries 3375–3401 instead uses the cyclic chart lines

\[
\mathcal G_{12}:e_6,\qquad
\mathcal G_{23}:e_6,\qquad
\mathcal G_{31}:e_6.
\]

Its candidate support operation is an endomorphism of this three-dimensional
chart-occurrence module:

\[
S=\operatorname{diag}(1,1,0).
\]

The two systems both contain three labels, but the labels, objects, and
variance are different.

## Source audit

Entry 580 constructs one product-pole complex reproducing the complete rank
cube, but explicitly stops before compatible bases and deletion maps.

Entry 3375 constructs the cyclic \(A_2\)-to-(e_6) occurrence morphism, but
explicitly stops before the complete rank-twelve triangular transport.

No source-derived connector currently maps denominator deletion arrows to
endomorphisms of the cyclic (e_6) occurrence module.

Consequently the Boolean cube does not authorize (S). Treating the two
three-label sets as identical would infer authority from equal cardinality.

## Result

Entry 3401 remains a valid finite theorem and a conditional prediction:

- if a source-derived occurrence support map in the orbit of (S) exists, the
  balanced quotient is the unique trace line;
- the existing denominator deletion cube does not supply that map;
- scalar uniqueness is therefore not yet a cosmological theorem.

This is a useful localization of the missing construction. We do not need
another abstract support projector. We need a typed natural transformation
from the denominator-support family to the cyclic occurrence-chart module, or
an independent physical operation acting directly on the occurrence lines.

## Falsifier

This conclusion is overturned by an existing source-derived square whose
vertical maps are denominator deletions, whose horizontal maps land in the
three cyclic (e_6) lines, and whose induced endomorphism is (S) or its
cyclic transport. Equal dimensions, matching ranks, or a fitted linear map do
not suffice.

## Verification

Checker:
`research/benincasa/checkers/audit_deletion_occurrence_projector_typing.py`.

Packet:
`research/benincasa/results/deletion_occurrence_projector_typing.json`.

Allocator claim: `seqclaim-7d25e655527849b675596191`.

Epistemic graph event:
`ev-000000007299-32182e40-90fa-4aee-97f4-95c0efc45934`.