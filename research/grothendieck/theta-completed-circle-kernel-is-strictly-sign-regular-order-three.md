# The completed circle kernel is strictly sign-regular of order three

## Bounded question

Does the coherent order-two orientation of packet 108 survive the first
genuinely coupled, three-mode test?

## Closed derivative tower

Positive row and column factors do not affect oriented minors, so write

\[
 f_\lambda(t)=(2\lambda t-3)e^{-\lambda t},
 \qquad \lambda=\pi x.
\]

For every `k>=0`, direct differentiation gives

\[
 \boxed{
 f_\lambda^{(k)}(t)
 =(-\lambda)^k
 \bigl(2\lambda t-(2k+3)\bigr)e^{-\lambda t}.}
\]

For three ordered spectral parameters, the Wronskian factors exactly as

\[
 W_3
 =e^{-t(\lambda_1+\lambda_2+\lambda_3)}
 (\lambda_1-\lambda_2)(\lambda_1-\lambda_3)
 (\lambda_2-\lambda_3)P,
\]

where, after setting `y_j=lambda_j t`,

\[
 P(y_1,y_2,y_3)
 =8y_1y_2y_3
 -12(y_1y_2+y_1y_3+y_2y_3)
 +30(y_1+y_2+y_3)-105.
\]

## Exact positivity of the residual polynomial

On the physical domain,

\[
 y_j=\pi tx_j\ge\pi>3.
\]

For example,

\[
 \partial_{y_1}P
 =8y_2y_3-12(y_2+y_3)+30.
\]

On `y_2,y_3>=3`, this derivative is increasing in each variable and its
minimum is

\[
 8\cdot3\cdot3-12(3+3)+30=30>0.
\]

The same holds cyclically.  Therefore `P` is coordinatewise increasing on the
larger box `[3,infinity)^3`, and

\[
 P(y_1,y_2,y_3)
 >P(3,3,3)=57>0.
\]

Thus `W_3` never vanishes.  For
`lambda_1<lambda_2<lambda_3`, its Vandermonde factor in the displayed ordering
is negative, so `W_3<0` everywhere on `t>=1`.

Together with positivity of `f_lambda` and the nonvanishing order-two
Wronskian from packet 108, the three-function family is an extended complete
Chebyshev system.  Hence all ordered three-by-three evaluation determinants
have one coherent nonzero orientation.  Restoring the positive prefactors in
`b(t,x)` preserves the conclusion:

\[
 \boxed{
 b(t,x)\text{ is strictly sign-regular through order three on }
 t,x\ge1.}
\]

## Meaning of the constants

The number `3` in the completion polynomial is the only possible source of a
fold.  The arithmetic lower bound `lambda t>=pi` places the physical chart
beyond it.  The apparently accidental numerical fact `pi>3` is more than
enough: the residual third-order obstruction is already positive at the
rational comparison point `(3,3,3)` with reserve `57`.

So the first three coherent orientations arise from one explanation:

\[
 \text{completion polynomial}
 +\text{integral spectral gap}
 +\text{outer modular chart}
 \Longrightarrow
 \text{Chebyshev rigidity through order three}.
\]

## Scope and next gate

This is an exact finite-order variation-diminishing theorem, not an all-orders
total-positivity theorem and not RH.  The next symbolic gate is the general
Wronskian

\[
 W_r(t;\lambda_1,\ldots,\lambda_r).
\]

Its entries already have the closed affine form above.  The best conjecture is
that, after Vandermonde division, the residual polynomial is positive whenever
all `lambda_j t>=pi`.  The smallest falsifier is the first order `r>=4` and
positive ordered tuple for which that residual changes sign.

Verification used exact symbolic factorization of the displayed determinant;
the sign proof itself is the rational lower-bound argument above, not a
floating-point census.
