# The relative hard-edge remainder resolves to minus alpha squared

## Question

After removing the relative \((\alpha/\beta)n\log n\) free-energy term, is the centered determinant remainder compatible with \(O(n^{-2})\)?

Exact determinant ratios through degree twenty-two give

\[
R_n^{(\alpha)}=
\log\frac{(a_n^{(\alpha)})^2}{(a_n^{(0)})^2}
-\frac{\alpha}{\beta}\Delta^2(n\log n).
\]

For \(n=18,\ldots,22\), the scaled values \(n^2R_n^{(\alpha)}\) stabilize as follows:

- \(\alpha=1/4\): from \(-0.06552\) to \(-0.06496\), near \(-\alpha^2=-0.0625\);
- \(\alpha=1/2\): from \(-0.25481\) to \(-0.25389\), near \(-\alpha^2=-0.25\);
- \(\alpha=1\): from \(-0.99926\) to \(-0.99922\), near \(-\alpha^2=-1\).

Thus the finite data support the sharpened relative expansion

\[
R_n^{(\alpha)}=-\frac{\alpha^2}{n^2}+o(n^{-2}).
\]

## Disposition

Complete the finite centered-remainder diagnostic. It supports the relative first-shift law with a resolved candidate second correction.

The next leaf is `alpha-squared-relative-remainder`: derive the coefficient \(-\alpha^2\) from the relative Mellin-Hankel free energy. The independent \(\alpha=0\) baseline remains open.

## Claim boundary

Bounded degree-twenty-two scaled remainders are not uniform asymptotics. Their apparent limits do not prove either the \(O(n^{-2})\) bound or the coefficient.
