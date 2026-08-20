---
title: "The Residual Four-Site Odd Cohomology Forms Two Regular Occurrence Orbits"
date: 2026-08-20
entry: 1193
status: active-finite-model
sector: cosmology
---

# 1193 — The Residual Four-Site Odd Cohomology Forms Two Regular Occurrence Orbits

Sequence claim: `seqclaim-4e1c7eef41a7eb57d79e1627`.

## Claim

Entry 1192's residual deck-odd cohomology transports canonically under the
source-labelled cyclic action after quotienting by exact pair boundaries:

\[
\boxed{H^2_-\simeq\mathbf Q[C_4]^{\oplus2}.}
\]

This is now an exact transport statement, not an inference from the number
of terms.

## Source-labelled transport

Shift every site and edge label by one cyclic step. Transport each serialized
triple representative with its induced Čech orientation, then compare it
with the chosen representative in the target term modulo

\[
\operatorname{im}(d_1:C^1_-\to C^2_-).
\]

The two orbits are

\[
(2,9,12,22),
\qquad
(5,10,13,20).
\]

In the current quotient frames, both have transition scalars

\[
(-1,-1,+1,+1).
\]

The signs are frame data, while the closed-orbit product is invariant:

\[
\boxed{(-1)(-1)(+1)(+1)=+1.}
\]

Every transported vector is a (d_2)-cycle, and its difference from the
target representative lies exactly in the pair-boundary image. Therefore
there is no cyclic projective anomaly and no additional descent datum.

## Narrow interpretation

The surviving rank-eight object is a legitimate labelled coefficient
module on the existing marked-incidence carrier. This does not show that it
survives other weight-row differentials or that the physical relative chain
pairs with it.

## Next falsifier

For one representative from each orbit, derive the first source-defined
residue/Gysin map that can meet this (H^2_-) degree. Transport that map
around (C_4) using the certified quotient transitions. A nonzero image may
kill one or both regular modules; absence of a typed map leaves them as
algebraic coefficient candidates, not physical classes.

## Artifacts

- `research/benincasa/checkers/four_site_qg_residual_cyclic_transport.py`
- `research/benincasa/results/four-site-qg-residual-cyclic-transport.json`
