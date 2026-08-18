---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 731 — The Rational Weighted Crossing Has No Exceptional Extension Resonance

## Frozen crossing

At the rational intersection (D_2\cap D_3), put

\[
y=(u+v)/2-1,
\qquad D_2=(y-u^2),
\qquad D_3=(y+u^2).
\]

Entry 726 found unequal raw pole orders ((-3,-2)).  The Newton equality

\[
\operatorname{wt}(y)=2\operatorname{wt}(u)
\]

therefore forces the weighted blowup with weights ((1,2)).

## Charts

The two charts are

\[
U_u:\quad u=e,\quad y=e^2t,
\]

and the stack chart

\[
U_y:\quad u=es,\quad y=e^2,
\]

with its intrinsic (mu_2)-action.  On their overlap (t=s^{-2}).

## Forced exceptional transform

Pullback of the complete adapted rank-four connection, including its
algebraic--elliptic extension block, gives the exceptional valuation matrix

\[
\begin{pmatrix}
-1&\infty&\infty&\infty\\
3&-1&\infty&\infty\\
-1&-5&-1&-2\\
1&-3&2&-1
\end{pmatrix}.
\]

The unique minimum-sum normalized nonnegative integral shear making every
entry logarithmic is

\[
\boxed{(0,0,4,2).}
\]

The frame transition on the overlap is consequently

\[
\boxed{\operatorname{diag}(1,1,s^{-4},s^{-2}).}
\]

Its even exponents prove (mu_2)-descent; no square-root trivialization was
chosen.

## Exceptional residue

Both charts give

\[
\operatorname{rank}R_{23}=4,
\qquad
\ker R_{23}=\operatorname{coker}R_{23}=0.
\]

For the algebraic--elliptic extension indicial operators,

\[
\boxed{\ker L_m(R_{23})=0\quad(1\le m\le10).}
\]

Meanwhile the strict transforms (t=1) and (t=-1) remain logarithmic and
retain two-dimensional first indicial kernels.  Thus the loss of resonance is
specific to the new rational exceptional component.

## Relation to Entry 728

The constant resolved dual graph has the invariant cycle

\[
\gamma_0=(e_{12}^++e_{12}^-)-(e_{13}^++e_{13}^-)+2e_{23}.
\]

The rational edge (e_{23}) does not acquire an exceptional
algebraic--elliptic extension resonance from the weighted crossing.  This is a
local coefficient statement, not yet a proof that the global invariant cycle
is exact: that requires the actual restriction maps from vertex and edge
coefficient objects.

## Narrow conclusion

\[
\boxed{
D_2\cap D_3\text{ contributes no local exceptional extension-resonance
class after the Newton-forced transform.}
}
\]

No new carrier component and no pairwise physical obstruction are inferred.

## Evidence

- `research/benincasa/gysin_weighted_crossing_blowup.py`;
- `research/benincasa/marici-gm/gysin-weighted-crossing-conventions.md`;
- `research/benincasa/marici-gm/src/bin/gysin_weighted_crossing_certificate.rs`;
- allocator claim `seqclaim-7d16f08f97e1c708a87cfa61`.
- epistemic event
  `ev-000000000344-f9226ca3-5c10-4dee-ac04-142d898cfa51`.

## Next falsifier

Construct the coefficient Čech differential on the resolved five-edge graph
using the chart transition matrices from Entries 729 and 731.  Project it to

\[
\mathbf1\oplus\chi_{-3}\oplus\chi_5.
\]

Only a nonzero cofiber in the invariant block can support a rational
pairwise obstruction.
