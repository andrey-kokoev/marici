# D convolution ratio structure

## Question

Do the coefficient sequences entering the diagonal dominance inequality satisfy a standard convolution order strong enough to support an all-order proof?

## Claim boundary

For every tested `2<=n<=8`, `0<=s<=2`, both coefficient sequences `HD_n` and `R` are log-concave, and the ratios `R_i/(HD_n)_i` are nondecreasing on their common positive support. This is an exact bounded TP2/monotone-likelihood-ratio pattern. It does not yet prove the signed autocorrelation inequality for imaginary-axis coefficients. The governing DPC case remains `rh-quarter-D-imaginary-axis-dominance.md`.

## Disposition

The log-concavity rival survives all 21 cases with one orientation and no exceptions. The next leaf is a generic algebraic lemma: determine whether log-concavity plus monotone likelihood-ratio order implies

\[
[\omega^{2k}]|HD_n(i\omega)|^2
+ [\omega^{2k}]2\operatorname{Re}(HD_n(i\omega)\overline{R(i\omega)})\geq0.
\]

A counterexample to that implication would reject this proof route without changing the observed D-family dominance.
