# Completed theta already supplies the Fisher metric on the wrong axis

## 1. Completed positive family

Let the fixed completed theta source be

\[
  X(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,
  \qquad \Phi(u)\ge0,
\]

with the standard super-exponential tails. On the nonoscillatory axis put

\[
  Z(y)=X(-iy)=\int_{\mathbb R}\Phi(u)e^{yu}\,du.
\]

This is finite and strictly positive for every real \(y\). Normalize the
tilted source:

\[
  d\mathbb P_y(u)
  =
  \frac{e^{yu}\Phi(u)\,du}{Z(y)}.
\]

Then direct differentiation gives

\[
  \partial_y\log Z(y)=\mathbb E_yU,
\]

and

\[
  \boxed{
  \partial_y^2\log Z(y)
  =
  \operatorname{Var}_y(U)\ge0.}
\]

Thus the completed source already selects a canonical global Fisher metric
without a prime cutoff.

## 2. Euler compatibility

Where the Euler product converges, the same scalar has the completed
factorization

\[
  \xi(s)
  =
  \tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Consequently its logarithmic curvature decomposes exactly as

\[
  \partial_s^2\log\xi(s)
  =
  -\frac1{s^2}
  -\frac1{(s-1)^2}
  +\frac14\psi_1(s/2)
  +\partial_s^2\log\zeta(s).
\]

The final term is the sum of positive prime Fisher informations. The first
three terms are the inseparable endpoint--gamma completion. Their combined
sum equals the theta variance after the variables are matched.

This proves scalar normalization uniqueness: the completed theta source fixes
the counterterm because it fixes the entire partition function.

## 3. Why this does not reopen the prime lane

The equality occurs after all labels have been compressed to the scalar
partition function. It does not construct a positive place-indexed form whose
Schur descent yields the scalar variance. Therefore it does not solve the
precompression gate \(C_Y\ge0\).

More decisively, the variance identity lives on the Laplace axis. On the
oscillatory axis,

\[
  X(x)=\int\Phi(u)e^{ixu}\,du,
\]

the normalized weight is complex and logarithmic curvature is no longer a
variance in a positive probability state.

\[
\boxed{
\text{completed Fisher positivity on the Laplace axis}
\not\Longrightarrow
\text{critical-line orientation}.}
\]

This is the all-place version of the earlier positive-separation-measure
obstruction.

## 4. Exact disposition

The renormalized *scalar* Fisher metric exists and is canonical:

\[
  I_{\mathrm{comp}}(y)
  =
  \operatorname{Var}_y(U).
\]

Hence constructing this quantity is no longer a live RH objective. The
remaining target must retain place or label directions before scalar
aggregation and must control their oscillatory compression.

The correct question is:

> Does the completed theta source carry a positive operator-valued covariance
> whose vacuum compression is the scalar curvature and whose modular
> transport remains positive for oscillatory characters?

A scalar covariance identity cannot answer this because it holds for every
positive source with sufficient tails, including hostile sources.

## 5. New falsifier

Take a hostile positive Fourier-stable source whose Mellin transform has
off-critical zeros. It still produces:

1. an entire positive Laplace partition function;
2. a positive Fisher variance for every real tilt; and
3. a positive-definite difference kernel from its characteristic function.

Therefore any proposed theorem using only these three properties is
falsified as an RH mechanism. The discriminator must be a labelled
operator-valued modular correspondence absent from the hostile source.

## 6. Scope

The completed variance identity and its Euler-chamber factor decomposition
are exact. They settle scalar metric selection but only after aggregation and
on the nonoscillatory axis. No positive place-indexed completion, oscillatory
operator inequality, determinant incidence theorem, or RH result follows.
