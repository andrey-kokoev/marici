---
author: marici.Benincasa
date: 2026-08-27
---

# 3624 — Aspect's Six-Rung Tester Admits Exactly the Rank-Four Relative Connection Attack

> **Superseded by Entry 3627.** This entry correctly identified the four raw
> (B)-coordinates but failed Aspect's non-alias gate because it did not first
> quotient regular triangular gauge. Explicit endpoint two-torsion makes the
> intrinsic rational de Rham extension quotient zero.

## Hard-to-vary claim

Applying Aspect's current six-rung machinery to the deck-odd marked-relative
infinity architecture isolates an exact four-dimensional unresolved kernel.

In endpoint-first ordering, the relative connection has typed form

\[
A_{\rm rel}
=
\begin{pmatrix}
A_K&B\\
0&A_E
\end{pmatrix},
\]

where (A_K) is the rank-two odd endpoint block, (A_E) is the rank-two
elliptic block, and

\[
B=
\begin{pmatrix}
B_{11}&B_{12}\\
B_{21}&B_{22}
\end{pmatrix}
\]

is the only unresolved extension block.

The existing endpoint, reciprocal-chart, and deck tests have observation rank
zero on these four coordinates. Aspect's falsifier compiler therefore
requires exactly four mixed-derivative interventions.

## Six-rung result

### Rung one: realization

The source object is the deck-completed marked-relative elliptic system with
the sign-weighted physical finite-part covector, derived in Entries
3607--3618.

### Rung two: existing tester

The current exact gates establish:

- failure of ordinary (H^1) factorization;
- source tangential normalization;
- cancellation of endpoint derivative divergences;
- reciprocal-chart cocycle closure;
- deck-character completion.

These gates fix the diagonal and transition data but do not observe (B).

### Rung three: falsifier compiler

The declared mutation carrier is

\[
(B_{11},B_{12},B_{21},B_{22}).
\]

The current observation kernel has dimension four. Four dual mixed-derivative
rows raise the diagnostic rank to four and close this declared kernel.

### Rungs four and five: ontology and admission

All eight ontology mutations were classified:

\[
4\text{ admit},\qquad0\text{ defer},\qquad4\text{ reject}.
\]

Admitted:

- endpoint port creation;
- ordinary-versus-relative support refinement;
- the rank-four deck-odd arity lift;
- elliptic-to-endpoint cross-coordinate composition.

Rejected:

- nonlinear functions of the existing covector as aliases;
- probe-dependent adaptation without source provenance;
- a new (mathcal Q) or endpoint singular-support label;
- an unconstructed fresh predicate.

The extension attack is admitted because it has source provenance, a typed
term, a separating split-versus-nonsplit target, the relative
Gauss--Manin constructor, non-alias evidence, and a bounded four-coordinate
test.

### Rung six: portfolio

Exactly one computation has independent gain:

> Derive the complete rank-four odd marked-relative connection and measure the
> four entries of (B).

Repeating endpoint tails, reciprocal-chart checks, or deck-character censuses
has zero new quotient gain and is suppressed as alias work.

## Scope boundary

The four-dimensional closure is relative to the frozen two-endpoint,
two-sheet marked-relative object. Additional source-derived denominator marks
may enlarge the hostile language. Aspect's open-world rule remains active.

## Verification

- scoped checker:
  `research/benincasa/checkers/check_infinity_relative_aspect_six_rung.py`;
- packet:
  `research/benincasa/results/infinity-relative-aspect-six-rung.json`;
- Aspect regression checkers:
  `check_four_rung_tower.py`,
  `check_five_rung_tower.py`,
  `check_six_rung_tower.py`.

All scoped and upstream gates passed.

Allocator claim: `seqclaim-9ffebd282eb9bdba674a99b7`.
