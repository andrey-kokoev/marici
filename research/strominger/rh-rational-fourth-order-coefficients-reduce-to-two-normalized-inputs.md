# Rational fourth-order coefficients reduce to two normalized inputs

## Question

What minimal Jacobi asymptotic data imply

\[
r_3=-\frac{163}{8},
\qquad
e_4=\frac{103}{8}?
\]

Write the off-diagonal coefficient as

\[
a_n=A n^4\left(1+\frac{\alpha_2}{n^2}+O(n^{-3})\right).
\]

Direct division gives

\[
\frac{a_n}{a_{n+1}}
=1-rac4n+rac{10}{n^2}
+rac{-20+2\alpha_2}{n^3}+O(n^{-4}).
\]

Hence \(r_3=-163/8\) is equivalent to

\[
\alpha_2=-\frac3{16}.
\]

Next normalize the parabolic defect numerator by

\[
a_n+a_{n+1}-b_n
=A n^2\left(2+rac2n+rac{d_2}{n^2}+O(n^{-3})\right).
\]

Dividing by \(a_{n+1}\) yields

\[
\varepsilon_n
=rac2{n^2}-rac6{n^3}
+rac{d_2+12-2\alpha_2}{n^4}+O(n^{-5}).
\]

Therefore \(\alpha_2=-3/16\) and \(d_2=1/2\) imply \(e_4=103/8\).

## Disposition

Reduce the rational-coefficient conjecture to two normalized theorem inputs. The next leaves are `weibull-offdiagonal-alpha2` for \(\alpha_2=-3/16\) and `weibull-defect-numerator-d2` for \(d_2=1/2\). Neither follows from the leading equilibrium calculation.

## Claim boundary

This algebra proves equivalence, not either asymptotic input. Regression remains the only present evidence for their values.
