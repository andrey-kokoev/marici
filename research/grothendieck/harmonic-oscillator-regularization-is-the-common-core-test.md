# Harmonic-oscillator regularization is the common-core test

## Question

How can one approximate simultaneously in a spectral logarithmic norm and a Fourier-side exponential norm when the two weights live in conjugate coordinates?

## Coordinate obstruction

An inequality comparing `log(2+|x|)` with `exp(beta|x|)` collapses the intersection only when both sector weights act in the same coordinate. In the explicit formula, the gamma multiplier acts in the spectral variable while endpoint evaluation imposes exponential control in its Fourier-dual variable. No pointwise domination crosses the Fourier transform.

Thus the common domain is genuinely phase-space typed:

\[
H_W
=
\{f:
(1+\log(2+|u|))f(u)\in L^2,
\quad
e^{\beta|x|/2}\widehat f(x)\in L^2
\},
\]

with the fixed-width prime row appended.

## Harmonic regularizer

Let

\[
H_{\rm osc}=-\partial_u^2+u^2
\]

and use the Mehler semigroup

\[
S_\epsilon=e^{-\epsilon H_{\rm osc}}.
\]

It regularizes both conjugate coordinates symmetrically, preserves Gaussian phase-space decay, and has Hermite eigenvectors. This makes it a candidate simultaneous approximation operator, unlike a cutoff in only `u` or only `x`.

## Sufficient core theorem

The Gaussian translate span is a core for `H_W` if the following are proved:

1. `S_epsilon` is bounded on `H_W` for `0<epsilon<=1`;
2. `S_epsilon f -> f` in the full `H_W` norm as `epsilon->0`;
3. Hermite spectral truncations of `S_epsilon f` converge in `H_W`;
4. each Hermite function is an `H_W`-limit of finite differences of real Gaussian translates;
5. the labelled prime row is bounded or relatively form-bounded uniformly along these approximations.

Then every `f in H_W` is approximated first by a Mehler-regularized vector, then by a finite Hermite sum, then by finite Gaussian-translate combinations.

## Why one-sided cutoffs fail

A compact cutoff in the spectral variable generally produces only polynomial Fourier tails and may leave the endpoint exponential domain. A Fourier cutoff analogously disrupts control of the gamma multiplier. The harmonic semigroup avoids this asymmetric loss.

## Relation to the dual-injectivity route

Strong continuity of `S_epsilon` on the intersection gives a constructive core proof. Gaussian-convolution injectivity on the form dual gives a uniqueness proof. Either suffices; they have different failure modes. The Mehler route localizes failure to a boundedness or convergence estimate rather than to an abstract generalized-function class.

## Disposition

Use harmonic-oscillator regularization as the primary acceptance test for simultaneous endpoint--gamma core density. Do not collapse the two norms by a pointwise weight inequality until a source-derived map places them in the same coordinate.