# Central rank-six pivot coordinate-monotonicity target

## Objective

For the certified central source coefficients `F_n`, let

\[
 H_r^{(i)}(x)=h_r(x_1,\ldots,x_{i+1})
\]

be the complete homogeneous polynomial in the first `i+1` ordered chord
coordinates, and define the symmetric rank-six Loewner matrix

\[
 A_{ij}(x)=\sum_{n\ge1}F_n
 \sum_{k=i}^{n-1-j}H_{k-i}^{(i)}(x)H_{n-1-k-j}^{(j)}(x),
 \qquad 0\le i,j<6.
\]

Write `d_1,...,d_6` for the diagonal pivots in the directed Newton--`LDL*`
factorization of `A`. The target is

\[
 d_6(x)>0,
 \qquad 0\le x_1\le\cdots\le x_6\le .01,
\]

preferably through the stronger coordinate theorem

\[
 \partial_{x_j}d_6(x)<0\quad(j=1,\ldots,6).
\]

One rigorously localized negative pivot, nonnegative derivative, failed
denominator, or excessive continuum remainder is the accepted falsifier.

## Initial directed audit

The source polynomial is retained through degree 39. Coefficients of degrees
39 and higher are bounded using `|F_n|<=6.038308` through degree 200 and a
geometric tail with ratio `.011`; no zeta-zero locations enter.

At the zero-confluent, upper-confluent, and mixed anchor
`(0,0,.002,.004,.007,.01)`, all six pivots are strictly positive. The sixth
pivot ranges from approximately `1.65125406e-32` at zero to
`1.65077876e-32` at the upper endpoint. Its directed interval width is about
`2e-46`, so the analytic source-tail uncertainty is fourteen orders below the
positivity margin.

Differentiating the full Newton--`LDL*` recursion analytically, including the
source tail, proves all eighteen probed coordinate derivatives negative. The
closest observed upper endpoint to zero is approximately `-2.85909709e-35`
at the upper-confluent anchor. The sixth-coordinate derivatives are near
`-3.32e-34`.

The prefix-cached grid audit is now complete. All `C(16,6)=8008`
nondecreasing anchors have six strictly positive directed pivots, and every
pivot minimum occurs at `(0.01,...,0.01)`. The weakest sixth-pivot interval is

`[1.6507787637605424e-32, 1.6507787637605621e-32]`.

Shared algebra reduces the audit to 12,376 prefix tables and 68,068 matrix
entries. The first-five continuum denominator gate also closes by prefix
inheritance: the first four determinant/Hadamard floors remain valid, while
the rank-five monotonicity theorem supplies `d_5>6.665113678415503e-26`.
The full 48,048-derivative cached audit is the next active gate.

RH is not proved.
