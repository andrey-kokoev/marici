# Euler–Maclaurin tail audit for the preconditioned spline

## Question

Do the one-sided tail intervals used by `preconditioned_spline_weil.py` have the asserted orientation?

## Claim boundary

For a completely monotone function `f` on the positive half-line, the Euler–Maclaurin expansion of the tail sum, truncated after the positive B2 term, is an upper bound; including the negative B4 term is a lower bound when the successive Bernoulli terms decrease. This packet audits only the functions and cutoff used by the checker. It does not assert a general asymptotic theorem without its remainder hypotheses, RH, or a G4 comparison theorem.

For `f(x)=x^{-p}`, with `p=2,...,8`,

\[
\sum_{n=M}^{\infty}f(n+\alpha)
=\int_{M+\alpha}^{\infty}f(t)\,dt+\frac{f(M+\alpha)}2
-\frac{B_2}{2!}f'(M+\alpha)-\frac{B_4}{4!}f'''(M+\alpha)+R_6.
\]

Complete monotonicity gives alternating derivative signs. Hence the B2 contribution is positive, the B4 contribution is negative, and the B6 contribution is positive. At the checker cutoff `M=19`, exact rational assertions verify

\[
0<T_6<T_4<T_2,
\]

where

\[
T_2=\frac{p}{12}x^{-p-1},\quad
T_4=\frac{p(p+1)(p+2)}{720}x^{-p-3},\quad
T_6=\frac{p(p+1)(p+2)(p+3)(p+4)}{30240}x^{-p-5}.
\]

Thus subtracting `T4` gives the lower endpoint and omitting it gives the upper endpoint. Reversing the B4 orientation moves the proposed interval above the strict upper endpoint and is rejected.

The second function is

\[
g(t)=\frac1{t+1/4}-\frac1{t+1}=\int_{1/4}^{1}(t+s)^{-2}\,ds.
\]

This integral representation makes `g` completely monotone. Its odd derivatives used by the checker satisfy

\[
g'''(t)<0,\qquad g^{(5)}(t)<0,
\]

and exact rational assertions at `t=19` verify

\[
0<-g^{(5)}(19)/30240<-g'''(19)/720.
\]

Therefore the same B2-upper/B4-lower orientation applies to the direct `D_N` tail.

## Disposition

The one-sided orientations used in the regenerated positive Gram certificate are admitted for these functions and this cutoff. The checker now fails if B2, B4, and B6 do not alternate with decreasing magnitude. The surviving Gram claim remains the finite explicit interval reported by the checker.
