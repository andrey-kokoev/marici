# No Finite Odd-Moment Port Recovers Krein Orientation

## Question

The primitive reciprocal-tail packet retains (P-Q), while scalar completion erases it. The source tangent and Clark sheet supply an odd port. Can finitely many derivatives or moments of that port recover the orientation of every oscillatory readout?

No.

## Exact hostile for every finite depth

Fix any nonnegative integer (N) and put (m=N+1). On the separation support

\[
D_j=j,
\qquad
0\le j\le m,
\]

use the signed finite-difference vector

\[
c_j=(-1)^j\binom{m}{j}.
\]

It annihilates every polynomial of degree at most (N):

\[
\sum_{j=0}^{m}c_jD_j^k=0,
\qquad
0\le k\le N.
\]

Choose a strictly positive baseline (L_j) whose cosine readout at frequency (\pi) vanishes and whose entries dominate (|c_j|). Then define two positive measures

\[
\mu_+=\sum_j(L_j+c_j)\delta_{D_j},
\qquad
\mu_-=\sum_j(L_j-c_j)\delta_{D_j}.
\]

They have identical moments through degree (N), but

\[
\int\cos(\pi D)\,d\mu_+(D)
=2^m,
\qquad
\int\cos(\pi D)\,d\mu_-(D)
=-2^m.
\]

The first unmatched moment occurs at degree (N+1), as required by the finite-difference construction.

## Consequence

No finite jet or moment truncation of the reciprocal-odd port determines Krein orientation. This remains true even within strictly positive finite separation measures: identical finite port data can produce opposite physical signs.

Thus the additional comparison channel cannot be one more scalar, nor any fixed finite tower of tangent scalars. A faithful repair must retain one of:

1. the primitive tail pair (P,Q) before totalization;
2. the complete function-valued odd channel;
3. an infinite moment tower with a proved representation theorem;
4. a source-derived dynamical law that determines the whole odd channel from admissible boundary data.

This clarifies the four-rung versus fifth-wall issue. The extra rung is not another finite coordinate. It is closure under the entire comparison transport that scalar completion discarded.

## Scope

The hostile measures are abstract positive separation packets, not theta-source packets. The theorem proves finite observation unfaithfulness. A theta-specific finite closure could still exist if an independently derived recurrence forces every higher moment from finitely many lower ones. No such recurrence is currently known, and it must be tested rather than assumed.

## Verification

The exact symbolic checker `research/grothendieck/checkers/finite_odd_moment_ports_are_unfaithful.py` verifies the construction for depths zero through twelve, including a deliberate failure at the first omitted moment. It writes `research/grothendieck/results/finite_odd_moment_ports_are_unfaithful.json`.
