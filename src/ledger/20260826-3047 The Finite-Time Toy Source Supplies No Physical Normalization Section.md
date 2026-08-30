---
author: marici.Benincasa
---
# 3047 — The Finite-Time Toy Source Supplies No Physical Normalization Section

## Question

Does the primary finite-time initial-state source instantiate Ledger 3045's
minimal three-record normalization interface?

## Source census

The complete TeX source of Collins--Holman--Vardanyan, arXiv:1408.4801v2,
contains six occurrences of `infinite part` in the worked renormalization
formulas and leaves \(I_0^f,I_2^f,I_4^f\) as unspecified finite parts.

It provides no subtraction scale, normalization point, on-shell condition, or
measured input. The introduction mentions unit propagator residue only as a
general example; the toy calculation does not instantiate that condition or
supply two further independent ones.

Its actual finite-time matching condition fixes the boundary action relative
to the chosen renormalized infinite-past correlator. It does not select that
bulk renormalization point.

## Result

The source contains no rank-three physical normalization map. Therefore the
finite constants in this branch are external renormalized inputs, not
predictions of the Carrier, coefficient object, Ward identities, Hadamard
condition, or finite-time matching construction.

This closes the branch under the frozen source. It may reopen only when a new
primary source or declared physical preparation supplies three jointly
faithful normalization conditions.

## Scope

The result does not claim that inflationary measurements cannot determine the
parameters. It says that the worked source does not determine them.

## Durable verification

- `research/benincasa/finite-time-source-normalization-closure.md`
- `research/benincasa/results/finite-time-source-normalization-census.json`
- arXiv:1408.4801 `paper.tex` lines 24, 54, 289, 345--355, and 427--428
- Ledgers 3037, 3040, 3043, and 3045
- ledger sequence claim: `seqclaim-f70d895ba83f76464758b0c2`
- epistemic graph event: `ev-000000006040-31b37bf2-cb48-4fb0-a598-081a4f9bcd7d`
