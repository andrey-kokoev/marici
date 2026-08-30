---
author: marici.Benincasa
date: 2026-08-27
---

# 3618 — The Deck-Completed Infinity Object Splits as One Even Plus Four Odd Directions

## Hard-to-vary claim

Deck completion of the two marked infinity endpoints produces a rank-five
relative object with character decomposition

\[
H^1(E,D_4)
\cong
\mathbb Q_+
\oplus
\mathbb Q_-^{,4},
\]

where

\[
D_4=\{p_0^+,p_\infty^+,p_0^-,p_\infty^-\}.
\]

The ordinary sheet trace lands in the unique even endpoint-difference line.
The sign-weighted sheet completion lands in the odd sector and is the only
completion compatible with the elliptic coefficient forms
(omega_0,omega_2).

## Relative rank

The endpoint term has rank

\[
\dim
\left(
H^0(D_4)/H^0(E)
\right)
=4-1=3.
\]

Adding compact elliptic cohomology gives

\[
3+2=5.
\]

Use the endpoint basis

\[
\begin{aligned}
q_T&=(p_\infty^++p_\infty^-)-(p_0^++p_0^-),\\
q_{S0}&=p_0^+-p_0^-,\\
q_{S\infty}&=p_\infty^+-p_\infty^-.
\end{aligned}
\]

Then (q_T) is deck-even, while (q_{S0}) and (q_{S\infty}) are
deck-odd. The hyperelliptic involution acts by (-1) on both compact
elliptic (H^1) directions.

## Two sheet completions

Let (gamma_+) and (gamma_-) be the two sheet lifts of the projective
physical interval.

The ordinary trace

\[
\gamma_++\gamma_-
\]

has boundary (q_T). It lies in the rank-one even sector and annihilates the
deck-odd elliptic coefficient forms.

The sign-weighted completion

\[
\gamma_+-\gamma_-
\]

has boundary

\[
q_{S\infty}-q_{S0}.
\]

It lies in the rank-four odd sector.

## Coefficient typing

Both

\[
\omega_0=\frac{dt}{W},
\qquad
\omega_2=\frac{t^2dt}{W}
\]

are deck-odd because (W\mapsto-W). Therefore a deck-invariant scalar
pairing requires the sign-weighted relative cycle.

The source trace is not an arbitrary choice between two equally typed maps:
the coefficient character selects the odd completion.

## Consequence

The physically relevant deck-completed coefficient object has rank four:

- two odd endpoint directions;
- two odd elliptic directions.

The unique even line is a separate ordinary-trace endpoint object. It is not
part of the elliptic physical pairing.

Thus deck completion preserves rather than collapses the marked endpoint
data.

## Next falsifier

Construct the rank-four odd marked-relative connection and test whether the
source sign-weighted finite-part covector is horizontal. In particular,
determine whether endpoint transport mixes the two odd endpoint lines with
the elliptic pair or splits as a direct sum. No splitting may be assumed from
the character decomposition alone.

## Evidence

- `research/benincasa/checkers/check_infinity_gysin_deck_completed_relative_object.py`;
- `research/benincasa/results/infinity-gysin-deck-completed-relative-object.json`.

Allocator claim: `seqclaim-f75f5f1a79ba55ccd06604ab`.
