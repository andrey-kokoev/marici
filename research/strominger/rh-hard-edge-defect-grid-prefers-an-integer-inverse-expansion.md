# The hard-edge defect grid prefers an integer inverse expansion

## Question

Does an ordinary inverse-degree expansion predict the scaled defect better than a free fractional power?

Fix the candidate limit two and fit

\[
2-n^2\varepsilon_n
=\frac{c_1}{n}+rac{c_2}{n^2}+rac{c_3}{n^3}.
\]

Training on degrees six through thirteen and holding out fourteen through sixteen, the three-term integer model has error \(1.49\times10^{-4}\), compared with \(7.43\times10^{-3}\) for the free single exponent. The fitted coefficients are

\[
c_1=5.9590,
\qquad c_2=-11.7726,
\qquad c_3=13.3483.
\]

The leading value is close to six.

## Disposition

Select an ordinary inverse-degree correction as the finite diagnostic model:

\[
n^2\varepsilon_n
=2-\frac{6}{n}+O(n^{-2})
\]

as the next source conjecture. Do not promote the coefficient six from regression alone.

The next leaf is `hard-edge-six-coefficient-source`: derive or falsify the coefficient six from two-term Jacobi asymptotics.

## Claim boundary

The integer model uses more parameters than the free-power model. Holdout superiority limits interpolation bias but is not an asymptotic proof.
