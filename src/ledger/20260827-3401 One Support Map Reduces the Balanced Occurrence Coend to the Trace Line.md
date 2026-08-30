---
author: marici.Benincasa
date: 2026-08-27
---

# 3401 — One Support Map Reduces the Balanced Occurrence Coend to the Trace Line

## Question

Entry 3398 identifies instrument evaluation as a mate pairing. Does that
balance law still permit several unrelated scalar readouts, or do the admitted
occurrence maps select a universal quotient?

## Balanced quotient

Write an instrument–state pair as the rank-one matrix

\[
X=b\otimes d.
\]

For every admitted occurrence map (f), the mate identity imposes

\[
(df)(b)=d(fb).
\]

On (X), this is the balance relation

\[
Xf\sim fX.
\]

The finite coend is therefore the nine-dimensional matrix space modulo the
span of the commutators

\[
Xf-fX.
\]

## Exact census

The checker computes the relation rank and quotient dimension for five frozen
map families.

| Admitted maps | Relation rank | Coend dimension | Generated algebra rank |
|---|---:|---:|---:|
| cyclic transport (P) | 6 | 3 | 3 |
| (P) and incidence (F) | 6 | 3 | 3 |
| support projector (S) | 4 | 5 | 2 |
| (P) and (S) | 8 | 1 | 9 |
| (P,S,F) | 8 | 1 | 9 |

The incidence operator adds no algebra beyond cyclic transport in this
representation. Cyclic transport alone therefore leaves three balanced
readout channels.

One independently declared support map changes the result completely. The
pair (P,S) generates the full (3\times3) matrix algebra, and its commutators
span the eight-dimensional traceless subspace. The coend is one-dimensional.

## Universal scalar

The trace annihilates every balance relation:

\[
\operatorname{tr}(Xf-fX)=0.
\]

Since the quotient has dimension one, trace spans its dual and is the unique
balanced scalar up to normalization.

For the matched source pair

\[
b=d=(0,-1,1),
\]

the universal scalar is

\[
\operatorname{tr}(b\otimes d)=d(b)=2.
\]

## Result

Static cyclic symmetry does not select a unique scalar readout. Cyclic
transport plus one source-declared support operation does.

This supplies a precise role for support in the (3+2+1) architecture:
support may create a mixed comparison defect, as in Entry 3385, while
simultaneously making the balanced instrument quotient faithful and
one-dimensional.

The two effects are compatible because Beck–Chevalley comparison and coend
balance are different constructions.

## Falsifier

The trace-line conclusion fails if the physical occurrence category does not
admit the support map (S), or if its source-derived representation differs
from the labelled route projector used here. Physical uniqueness therefore
cannot be inferred from the algebraic quotient until that support operation is
typed in the cosmological source.

## Scope

This is a finite occurrence theorem. It does not prove that the physical
Bunch–Davies instrument factors through this coend, and it does not authorize
adding a support map solely to force scalar uniqueness.

## Verification

Checker: `research/benincasa/checkers/audit_occurrence_coend_readout.py`.

Packet: `research/benincasa/results/occurrence_coend_readout.json`.

Allocator claim: `seqclaim-8c8a636d61f1e9bfc3a0c6f9`.

Epistemic graph event:
`ev-000000007291-ce49a808-bd2a-4a87-adc7-7a913a7eb14b`.
