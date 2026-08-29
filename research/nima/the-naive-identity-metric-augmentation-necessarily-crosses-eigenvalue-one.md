# The naive identity-metric augmentation necessarily crosses eigenvalue one

## Rank-one eigenvalue

Take the label-diagonal Green metric to be the identity in the unweighted label frame. For the off-seam augmentation row

\[
a_{\sigma,p,k}
=
\frac1k p^{-k(1/2+\sigma)},
\]

the normalized rank-one loading has sole nonzero eigenvalue

\[
\lambda(\sigma)
=
\|a_\sigma\|^2
=
\sum_p\sum_{k\ge1}
\frac1{k^2}p^{-k(1+2\sigma)}.
\]

Equivalently,

\[
\lambda(\sigma)
=
\sum_p
\operatorname{Li}_2
\bigl(
p^{-(1+2\sigma)}
\bigr).
\]

## Forced crossing

For \(\sigma>0\), the series converges and depends continuously and strictly decreasingly on \(\sigma\).

As

\[
\sigma\downarrow0,
\]

the \(k=1\) terms give the divergent prime harmonic series, so

\[
\lambda(\sigma)\to\infty.
\]

As

\[
\sigma\to\infty,
\]

every term vanishes and dominated convergence gives

\[
\lambda(\sigma)\to0.
\]

Therefore there exists a unique

\[
\sigma_*>0
\]

such that

\[
\lambda(\sigma_*)=1.
\]

At that displacement,

\[
I-U_{\sigma_*}^{*}U_{\sigma_*}
\]

has a nontrivial kernel.

## Consequence

The naive identity-metric rank-one loading cannot be the RH defect operator. It manufactures an unavoidable eigenvalue-one collision at a positive off-seam location determined only by the normalization of the prime augmentation row.

This collision is not a zeta zero and therefore falsifies any spectral-identification theorem using this unnormalized pair.

The strict contraction claim

\[
U_\sigma^{*}U_\sigma<I
\]

can hold only sufficiently far into the convergence half-plane. It cannot hold throughout the open sector.

## Required repair

The diagonal Green metric must be source-derived and carry the correct relative energy scale:

\[
\lambda_G(\sigma)
=
\left\|
U_\sigma G_{\mathrm{diag}}(\sigma)^{-1/2}
\right\|^2.
\]

A valid theorem must prove either:

- \(\lambda_G(\sigma)<1\) throughout the claimed region;
- or, more minimally, \(\lambda_G(\sigma)\ne1\) with the collision set identified exactly with the intended spectral zeros.

Rescaling \(G_{\mathrm{diag}}\) merely to push the crossing away is unauthorized. Its normalization must come from the complete Green boundary energy.

## Weighted-domain warning

If the source norm absorbs the same Euler coefficient into each label basis vector, then the normalized augmentation coefficients can become order one. The common summation row is then not bounded on an infinite \(\ell^2\) label sum.

Thus two statements must remain separate:

- Euler weighting makes local incidence upper-bounded;
- common scalar augmentation is continuous on the completed source domain.

The second requires additional Green energy or a rigged dual topology.

## Finite-cutoff hostile

For every finite cutoff \(X\),

\[
\lambda_X(\sigma)
=
\sum_{\substack{p^k\le X}}
\frac1{k^2}p^{-k(1+2\sigma)}
\]

is finite. As \(X\) increases, its eigenvalue-one crossing moves. Any proof based only on fixed-cutoff contraction can therefore conceal the false completed collision.

## Frontier

The next calculation must extract the actual diagonal Green weights

\[
g_{p,k}(\sigma)
\]

and evaluate

\[
\lambda_G(\sigma)
=
\sum_{p,k}
\frac{|a_{\sigma,p,k}|^2}
{g_{p,k}(\sigma)}
\]

on reduced support.

Until those weights are source-fixed, the rank-one loading inequality is not merely unproved; the simplest normalization is decisively false.
