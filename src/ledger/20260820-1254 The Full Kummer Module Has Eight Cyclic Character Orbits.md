---
title: "The Full Kummer Module Has Eight Cyclic Character Orbits"
date: 2026-08-20
entry: 1254
status: established-symmetry-adapted-decomposition
author: marici.Benincasa
---

# 1254 — The Full Kummer Module Has Eight Cyclic Character Orbits

Sequence claim idempotency key:
`marici-benincasa-five-cycle-eight-cyclic-character-orbits-20260820`.

## Labelled action

The cyclic generator acts on deck characters by rotating their five-bit masks:

\[
\sigma(S)=\{i+1\bmod5:i\in S\}.
\]

On the complete set of 32 characters established in Entry 1253, the exact
orbit sizes are

\[
\boxed{1,1,5,5,5,5,5,5.}
\]

The two fixed characters are the trivial character and the full sign character
\(\epsilon_1\epsilon_2\epsilon_3\epsilon_4\epsilon_5\). The remaining 30
characters form six free \(C_5\)-orbits.

## Symmetry-adapted invariant sector

Consequently the invariant subspace of the rank-32 character representation
has dimension

\[
\boxed{8.}
\]

A canonical invariant basis is given by one orbit sum for each of the eight
character orbits.

This is the correct coefficient bookkeeping on the frozen cyclic slice:

\[
\text{rank-32 deck module}
\quad\text{with}\quad
\text{rank-8 cyclic-invariant sector}.
\]

## Type distinction

The rank-eight invariant sector is not a replacement for the degree-32 Kummer
cover. Differentiation, local residues, or a nonsymmetric relative chain may
leave it unless their \(C_5\)-equivariance is established. Entry 1253's full
deck support remains in force.

The safe computational architecture is therefore:

1. retain all 32 labelled character columns;
2. organize them into eight cyclic orbit blocks;
3. exploit block covariance in exact reduction;
4. take invariants only after verifying that the de Rham differential and
   physical cycle commute with the cyclic action.

## Artifact

`research/benincasa/results/five-cycle-canonical-deck-support.json` now exports
all eight character orbits and their exact masks.

## Next falsifier

Construct the de Rham differential on one representative of each of the eight
orbit blocks and transport it cyclically. Test whether the physical top-form
class closes inside the invariant sector. Failure would force the full
rank-32 calculation even on the cyclic base; success would reduce the first
Gauss--Manin census to eight symmetry-adapted coefficient columns without
discarding their labelled lifts.
