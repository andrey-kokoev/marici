# The half-offset is a weighted residual spectral-gap gate

Author: `marici.Nima`

## Correction to literal almost periodicity

The fully completed resolution signal is not expected to be purely almost
periodic before RH is considered. Endpoint cancellation and archimedean
completion already supply authorized decaying modes. The relevant distinction
is their decay threshold.

In the centered strip, the nearest declared endpoint singularities are at
horizontal distance \(1/2\). Gamma poles lie no closer. Their Fourier-dual
residual modes therefore begin at rate \(1/2\).

An off-seam zero at centered displacement \(a\), with \(0<a<1/2\), contributes

\[
 e^{-a|x|}e^{-ibx},
\]

which decays strictly more slowly.

## Correct completion class

Write a resolution signal as

\[
 f=g+r,
\]

where \(g\) is Bohr almost periodic and \(r\) is the preregistered residual.
For every \(\alpha<1/2\), define

\[
 \|r\|_{\alpha,\infty}
 =\sup_x e^{\alpha|x|}|r(x)|.
\]

The legal residual class is

\[
 \mathcal R_{1/2}
 =\bigcap_{0<\alpha<1/2}
 \{r:\|r\|_{\alpha,\infty}<\infty\}.
\]

The endpoint mode \(e^{-|x|/2}\) belongs to this class. A mode
\(e^{-a|x|}e^{-ibx}\) with \(a<1/2\) does not: choose
\(a<\alpha<1/2\), and its weighted norm diverges.

Thus the half-offset becomes a source-declared spectral gap in the residual
decay spectrum.

## Algebraic stability

The threshold is stable under the elementary completed operations when their
weighted norms are controlled:

- sums preserve the threshold;
- multiplication by an almost-periodic bounded factor preserves it;
- products of residuals add decay rates;
- convolution of exponentially decaying residual kernels preserves the
  minimum input rate, with polynomial factors at equal rates still controlled
  for every strict \(\alpha<1/2\);
- reciprocal conjugation preserves the rate.

This gives a plausible source category

\[
 AP\ltimes\mathcal R_{1/2},
\]

provided the decomposition and every constructor are continuous in the
declared family of weighted norms.

## Completion hazard

Finite legal modes do not suffice. The bonding maps must have
cutoff-independent bounds in every norm with \(\alpha<1/2\). Pointwise, local,
distributional, or unweighted sup convergence can lose the spectral gap by
allowing recurrence peaks or residual mass to escape to infinity.

The exact source theorem is therefore:

> After coupling endpoint, gamma, prime, seam, and projective-infinity
> channels, the regularized resolution cutoffs form a Cauchy family in every
> weighted residual norm below the half-offset, with a continuous projection
> onto the almost-periodic component.

If proved, the limit cannot contain an off-seam Poisson mode.

## What remains unproved

No current packet supplies these uniform weighted bounds for the actual
Euler-to-seam bonding maps. The pro-Gram topology, fixed-window graph norms,
and trace-class Schur completion control different quantities. None embeds
automatically into the residual decay topology.

Consequently the half-offset law is a genuine new candidate, not a consequence
of the six completion laws already falsified by the rank-one defect.

## Finite falsifier

For a proposed bound at some \(\alpha<1/2\), test the hostile

\[
 r_a(x)=e^{-a|x|}e^{-ibx},
 \qquad 0<a<\alpha.
\]

At \(x=N\),

\[
 e^{\alpha N}|r_a(N)|=e^{(\alpha-a)N}.
\]

Any claimed cutoff-independent constant is violated at a finite sufficiently
large \(N\). The phase \(b\) is irrelevant to the norm and remains correctly
typed as the zero ordinate.

## Verdict

The first noncircular orientation candidate after the combined no-go is not
positivity or pure almost periodicity. It is preservation of a source-fixed
half-offset gap in the residual decay spectrum. The decisive calculation is
now the weighted sup-norm continuity of the actual completed source
constructors.

