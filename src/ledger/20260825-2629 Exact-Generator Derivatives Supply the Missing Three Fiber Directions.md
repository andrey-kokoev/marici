# 2629 — Exact-Generator Derivatives Supply the Missing Three Fiber Directions

## Problem

The physical first-normal packet plus the cyclic quadratic class has fiber
rank four, while the complete localized Cayley--Menger quotient has rank
seven. Entry 2625 retained the primitive provenance of the four source exact
generators. The finite question was whether derivatives of those generators
account for the missing directions.

## Frozen test

Start from the four labelled associated-grade classes

\[
(\nu_1,\nu_2,\nu_3,c_{\rm cyc})
\]

and append, in source order, the twelve base derivatives of

\[
(5K_a,5K_b,5K_c,zK-1).
\]

The order is fixed before reduction. Incremental ranks were computed at A, B,
and HOMA, with a second-prime replication at A.

## Result

All four runs give the same sequence:

\[
4,5,6,7,7,7,7,7,7,7,7,7,7.
\]

The first labelled gradient-derivative triple contributes exactly the three
missing directions. All later exact-generator derivatives are fiberwise
dependent. Therefore the associated-grade rank four together with the
source-exact coherence directions spans the complete rank-seven fiber.

## Narrow conclusion

The former rank discrepancy has a source-derived explanation: three
directions live in the motion of the exact ideal rather than in the visible
first-normal classes. No new carrier cell or fitted coefficient class is
needed at this fiberwise gate.

This does not establish a flat rank-seven connection. The next gate is to use
Entry 2625's primitive coefficients and these generator derivatives to form
common lifted base derivatives, then test mixed flatness exactly.

## Artifacts

- `research/benincasa/cm-exact-generator-derivative-span.md`
- `research/benincasa/checkers/check_cm_exact_generator_derivative_span.py`
- `research/benincasa/results/cm-exact-generator-derivative-span.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

Ledger sequence claim: `seqclaim-a5404aad4881a5e5c2b2b31d`.

Epistemic event: `ev-000000003930-a5e93982-25b8-4d19-a2d7-7f996bcdb06c`.
