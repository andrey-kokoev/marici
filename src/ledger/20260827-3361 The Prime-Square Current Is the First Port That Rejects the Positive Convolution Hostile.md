# The Prime-Square Current Is the First Port That Rejects the Positive Convolution Hostile

Normalize the positive convolution hostile in the right sector with
`u=exp(-z)`:

\[
1+\frac45\cosh z
=\frac25e^z(1+2u)(1+\tfrac12u).
\]

Its connected logarithmic coefficients are

\[
a_k=\frac{(-1)^{k+1}}{k}(2^k+2^{-k}).
\]

The primitive coefficient passes the positive-sign test:

\[
a_1=\frac52>0.
\]

The prime-square coefficient is the first failure:

\[
a_2=-\frac{17}{8}<0.
\]

Thus the separately retained `k=2` boundary current is the first exact port
that rejects this divisor-bearing positive convolution before its zeros are
examined. Discarding it in determinant regularization erases the earliest
source-provenance discriminator.

This is a discrimination theorem, not zero confinement: finite-place Fock
grammar still does not control independently modified archimedean carriers.

Research packet:
`research/grothendieck/the-prime-square-current-is-the-first-port-that-rejects-the-positive-convolution-hostile.md`

Exact checker:
`research/grothendieck/checkers/check_prime_square_rejects_convolution_hostile.py`

The checker passes 6/6 gates.
