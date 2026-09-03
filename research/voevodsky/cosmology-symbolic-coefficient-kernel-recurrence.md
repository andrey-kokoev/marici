# Symbolic coefficient-kernel recurrence

## Conjecture

For the four grade-eight targets on the pure `x²` orbit, the normalized three-dimensional coefficient-relation kernel is unchanged at every even ambient index from A14 onward.

## Construction

Let `V` be the fixed four-dimensional coefficient space and let

\[
f_A:V\longrightarrow Q_A
\]

send coefficients to the corresponding four target classes in the grade-eight quotient at ambient index `A`. Squared-axis transport gives a commutative square

\[
V \xrightarrow{f_A} Q_A,
\qquad
V \xrightarrow{f_{A+2}} Q_{A+2},
\]

where the left map is the identity on target labels and the right map multiplies representatives by `x²`. The source relation packets are closed under the same monomial shift, and the filtration grade does not depend on the exponent pair. Therefore

\[
\ker(f_A)\subseteq\ker(f_{A+2}).
\]

At A14 the kernel has dimension three. Hence every later kernel has dimension at least three. Since `V` has dimension four, only two cases remain:

1. at least one transported target is nonzero, so `rank(f_A)=1` and the kernel is exactly the original three-dimensional kernel;
2. all four targets vanish, so `rank(f_A)=0` and the kernel jumps to dimension four.

A changed three-dimensional coefficient kernel is excluded by the transport inclusion. The finite A16, A18, and A20 computations realize the first case.

## DPC disposition

The original all-even recurrence conjecture is narrowed to an exact dichotomy. Kernel-shape recurrence is proved conditional on nonvanishing of one transported target. Unconditional all-even persistence is not established because no all-even nonvanishing probe has been constructed.

The explicit falsifier is now total extinction at a later even ambient index, not a different three-dimensional kernel. Surviving alternatives are all-even rank-one persistence or a first rank-one-to-zero jump.

## Next discriminating test

Construct a compatible scalar probe that is nonzero on one representative for every even ambient index, or identify the first ambient index where that probe vanishes.

## Evidence boundary

This is an algebraic pole-filtered quotient statement. It supplies no DNC, geometric specialization, or physical interpretation.
