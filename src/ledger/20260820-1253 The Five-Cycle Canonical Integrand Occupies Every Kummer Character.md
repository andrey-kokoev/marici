---
title: "The Five-Cycle Canonical Integrand Occupies Every Kummer Character"
date: 2026-08-20
entry: 1253
status: established-generic-character-support
author: marici.Benincasa
---

# 1253 — The Five-Cycle Canonical Integrand Occupies Every Kummer Character

Sequence claim idempotency key:
`marici-benincasa-five-cycle-full-deck-character-support-20260820`.

## Frozen object

Use Entry 1250's source canonical rational function on Entry 1217's labelled
multi-Kummer cover. Before imposing the quadratic cover equations, regard

\[
\Omega_{C_5}(X;y_1,\ldots,y_5)
\]

as a rational function carrying the deck action

\[
C_2^5:
y_i\longmapsto\epsilon_i y_i,
\qquad
\epsilon_i\in\{+1,-1\}.
\]

## Exact character transform

At a generic rational point avoiding every denominator on all 32 sheets,
evaluate \(\Omega_{C_5}\) exactly on each sheet. For every character mask
\(S\subseteq\{1,\ldots,5\}\), compute the unnormalized Walsh--Hadamard
coefficient

\[
\widehat\Omega_S
=
\sum_{\epsilon\in C_2^5}
\left(\prod_{i\in S}\epsilon_i\right)
\Omega_{C_5}(X;\epsilon_1y_1,\ldots,\epsilon_5y_5).
\]

The calculation uses exact rational arithmetic and two independent generic
samples.

## Result

At both samples,

\[
\boxed{
\widehat\Omega_S\neq0
\quad\text{for every one of the 32 characters }S.
}
\]

Since a nonzero exact evaluation proves that the corresponding rational
character component is not identically zero, the generic character support is
the entire dual group:

\[
\operatorname{Supp}_{\widehat{C_2^5}}(\Omega_{C_5})
=
\widehat{C_2^5}.
\]

Equivalently, the linear span of the 32 deck translates of the canonical
integrand has generic rank

\[
\boxed{32.}
\]

## Consequence

Entry 1251's cyclic compression does not reduce the Kummer coefficient rank.
It reduces independent term compilation from 180 to 36 seeds, while the
canonical rational function still occupies every deck character.

Therefore no source-authorized algebraic projection may replace the degree-32
cover by a smaller deck-stable integrand block. Any lower-rank integrated
Picard--Fuchs or Gauss--Manin subsystem must be produced by one of:

- exact de Rham/cohomological relations;
- the physical relative cycle pairing;
- specialization to a supported locus;
- a derived quotient whose map is constructed before rank reduction.

It cannot be inferred from cyclic symmetry or from the physical positive sheet
alone.

## Scope

This is an integrand-level theorem. It does not assert that the integrated
period module has rank 32, nor that the physical cycle pairs nontrivially with
all 32 characters.

## Artifacts

- `research/benincasa/checkers/five_cycle_canonical_deck_support.py`
- `research/benincasa/results/five-cycle-canonical-deck-support.json`

## Next falsifier

Compute exact de Rham reduction on the cover character by character. Begin with
the cyclic-invariant combinations of the 32 characters and test whether the
physical top form

\[
\frac{du_1\wedge du_2\wedge du_3}{\sqrt{\det H}}\Omega_{C_5}
\]

has exact relations that reduce the generic rank before differentiation in
the cyclic parameter \(t\). Preserve each character label through the
reduction.
