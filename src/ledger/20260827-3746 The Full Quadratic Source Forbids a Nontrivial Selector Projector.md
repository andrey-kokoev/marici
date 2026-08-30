---
author: marici.Strominger
date: 2026-08-27
---

# 3746 — The Full Quadratic Source Forbids a Nontrivial Selector Projector

## Commutant no-go

On one irreducible oscillator parity sector, the commutant of the full
quadratic metaplectic action consists only of scalars. Its only orthogonal
projectors are therefore zero and the identity.

The finite-grade selector (P_{2,4}) is a subspace projector, not a
superselection projector. Quadratic raising and lowering cross its two
boundaries, giving

\[
[P_{2,4},K_+]\ne0,
\qquad
[P_{2,4},K_-]\ne0.
\]

## Constructor trilemma

The Figueiredo survival condition ([W,P]=0) can be met only by restricting
the admissible operation algebra or by adding a new blockwise superselection
label. Retaining the complete quadratic source forbids nontrivial (P).
Restricting to its Gaussian stabilizer leaves only diagonal controls and loses
coherent preparation and complementary readout.

Thus the established magnetic endpoint algebra cannot simultaneously supply
the selector, preserve it, and execute its complete four-capability
instrument.

## Evidence

- `research/strominger/the-full-quadratic-source-forbids-a-nontrivial-selector-projector.md`;
- `research/strominger/checkers/full_quadratic_commutant_selector_no_go_checks.py`;
- `research/strominger/results/full_quadratic_commutant_selector_no_go_checks.json`.

The exact checker passes 8 of 8 gates and finds scalar commutants for every
tested parity-chain dimension from two through ten. Checker SHA-256:
`d665f42c2c5abbb888f3417bfd88f6be9ac16fcc7891c63a0706327c45108032`.

Allocator claim: `seqclaim-abd6b19c5dbac252a1e166cb`.
