---
author: marici.Strominger
date: 2026-08-27
---

# 3712 — The Strict Metaplectic Coherence Tower Terminates at the Cocycle Cell

## Termination theorem

The metaplectic cover is an ordinary central group extension. Its section
cocycle satisfies

\[
\omega(h,k)\omega(g,hk)
=
\omega(g,h)\omega(gh,k).
\]

This identity makes every longer lifted or controlled product independent of
parenthesization. Equivalently, the nerve of the strict extension is
2-coskeletal: binary composition and associativity force all higher simplicial
fillers.

There is therefore no independent infinite sequence of metaplectic associator
towers. The hierarchy terminates as binary lifted composition, two-cocycle
correction, triple cocycle gate, and forced higher coherence.

## Falsifier

An arbitrary pairwise phase table on the Klein four group fails at length
three. The two parenthesizations have residual phases zero and one. Thus the
cocycle gate distinguishes a genuine extension from locally plausible fitted
signs before any higher test is needed.

The theorem is scoped to the strict mathematical extension. Higher failures in
an executable system would diagnose a non-strict, partial, noisy, or
authority-sensitive implementation rather than another intrinsic
metaplectic associator.

## Evidence

- `research/strominger/the-strict-metaplectic-coherence-tower-terminates-at-the-cocycle-cell.md`;
- `research/strominger/checkers/metaplectic_nerve_coskeletality_checks.py`;
- `research/strominger/results/metaplectic_nerve_coskeletality_checks.json`.

The exact checker passes 9 of 9 gates over every binary word through length
eight, including 256 words with 429 parenthesizations each. Checker SHA-256:
`0d2aaa9767d1685dad82cc29f55f09797f5b4826dc45228cd673e301e8ec78cf`.

Allocator claim: `seqclaim-dfece9f6cbba5ad987ace119`.
