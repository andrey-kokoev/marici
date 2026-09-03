# No uniform Gram gap blocks a small-prime perturbation proof

## Candidate mechanism

At a favorable fixed Gaussian width, the prime part of the explicit difference kernel may be exponentially small relative to the endpoint--gamma part. This does not by itself prove all-rank PSD by perturbation.

## Confluent degeneration

Let `K0` be any smooth strictly positive-definite difference kernel. For two translates separated by `d`, its Gram determinant is

\[
K_0(0)^2-|K_0(d)|^2.
\]

As `d` tends to zero, this determinant tends to zero. If the kernel is even and twice differentiable, its leading margin is only quadratic:

\[
K_0(0)^2-K_0(d)^2
=
-K_0(0)K_0''(0)d^2+O(d^4).
\]

For larger tuples coalescing at one point, successive Gram eigenvalues vanish at increasingly high powers of the separations; their limits are governed by Hermite-jet moment matrices. Therefore there is no positive spectral gap uniform over tuple size and translate geometry.

## Consequence for sector splitting

A bound of the form

\[
\sup_d|K_{\mathbb P}(d)|<\varepsilon
\]

cannot establish

\[
K_{\rm endpoint}+K_\Gamma+K_{\mathbb P}
\]

positive definite at all ranks. Arbitrarily confluent configurations have baseline eigenvalues smaller than any fixed absolute perturbation scale.

A valid perturbative proof must instead establish relative quadratic-form domination on the entire Gaussian translate span, or derivative-sensitive bounds at every confluent order. Those conditions are already operator/complete-moment strength; they cannot be replaced by pointwise smallness of the prime kernel.

## Disposition

Reject an all-rank proof based only on exponential smallness of the prime sector at a selected width. Such estimates may prove fixed separated finite matrices, but the RH-faithful contract includes arbitrary coalescence and rank. Preserve the coupled completed kernel or prove a relative form bound with common null spaces and all jet orders.
