# 1880 — Signed Loop Coordinates Leave One Positive-Sheet Triple Fold

## Correction tested

Entries 1877--1879 tested the Galois branch, positivity of the free squared
loop coordinates, fold nondegeneracy, and projective multiplier signs.  Those
tests do not by themselves place a solution on the positive loop-coordinate
sheet: the wall equations determine signed linear coordinates

\[
y_e=c_e t,
\]

not only their squares.

## Exact signed-sheet audit

For the surviving common-multiplier-sign root of

\[
D_3:\quad g_{123}\mid g_4\mid g_5,
\]

the fixed wall solution contains

\[
(y_3,y_4,y_5)=\left(-\frac32t,\frac12t,-\frac32t\right).
\]

Its coefficient signs are mixed.  No real choice of \(t\) makes all three
fixed loop coordinates positive.  Thus its positive critical squares do not
define a point of the literal positive loop-coordinate sheet.

For

\[
D_4:\quad g_{12}\mid g_{34}\mid g_5,
\]

the fixed solution is

\[
(y_2,y_4,y_5)=\left(-\frac32t,-\frac12t,-\frac12t\right).
\]

All signs agree.  Choosing \(t<0\) makes the fixed coordinates positive;
the two free critical squares are already exactly certified positive, and
their positive square roots complete a positive real loop point.

## Narrow result

\[
\boxed{
2\ \text{common-sign real }A_1\text{ folds}
\;\longrightarrow\;
1\ \text{positive-loop-sheet candidate}.
}
\]

The survivor is the earlier \(+\sqrt5\) root of \(D_4\), isolated by

\[
\frac{196583683}{67108864}
<z<
\frac{786334733}{268435456},
\qquad z=t^2,
\]

with projective multiplier signs \((-,-,-)\) and the required branch
\(t<0\).

This corrects any reading of Entry 1877 in which positivity of squared
coordinates was treated as positivity of the signed source loop variables.
It does not alter the algebraic existence of \(D_3\) or its rank-one local
vanishing cycle; it removes only its literal positive-loop-sheet activation.

## Remaining falsifier

There is now one local candidate.  Determine whether the source continuation
from the positive Bunch--Davies chamber to the \(t<0\) sheet gives a nonzero
oriented intersection with the \(D_4\) fold thimble.  The continuation path,
the square-root sheets of the two free coordinates, and the original
\(i\epsilon\) boundary value must be transported together.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_pilot.rs`
- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_real_roots.rs`
- `research/benincasa/results/five-site-cyclic-triple-region-census.json`
- `research/benincasa/results/five-site-cyclic-triple-region-real-roots.json`
- allocator claim: `seqclaim-66f258f69e55441887fc9e3f`
- epistemic event: `ev-000000002238-e1abcce6-2a41-41ee-b089-3362e3db49c1`
