# Joint prime incidence has a harmonic common-mode obstruction

## Large-prime incidence columns

Embed every moving seam into the common boundary-history space. For a source
\(\phi\), the first seam at prime \(p\) is

\[
R_p\phi=\phi|_{[0,\log p]}.
\]

As \(p\to\infty\),

\[
R_p\phi\longrightarrow\phi
\]

in the source norm. After the prime half-density, the joint incidence column
has the form

\[
b_p=p^{-1/2}R_p\phi
=p^{-1/2}\phi+r_p,
\]

where

\[
r_p=-p^{-1/2}\phi|_{(log p,\infty)}.
\]

Thus all large-prime columns share one asymptotically aligned source mode.

## Harmonic obstruction

At cutoff \(X\), let

\[
w_X=(p^{-1/2})_{p\leq X}.
\]

The common-mode part of the synthesis is the rank-one map

\[
x\longmapsto
\phi\langle w_X,x\rangle.
\]

Its squared operator norm is

\[
\lVert\phi\rVert^2
\sum_{p\leq X}\frac1p.
\]

Euler's prime harmonic series diverges. Therefore the joint incidence cannot
be uniformly bounded on an unweighted \(\ell^2\) prime register if the
common source mode is retained.

For a compactly supported nonzero source, the obstruction is exact: once
\(\log p\) exceeds the support, \(r_p=0\).

For a rapidly decaying source, the residual columns may define a bounded or
compact synthesis when

\[
\sum_p\lVert r_p\rVert^2<\infty.
\]

That does not remove the common rank-one divergence.

## Meaning of the primitive boundary current

The primitive divergence is now visible before taking a determinant. It is
the non-square-summable coefficient of one common boundary direction.

The primitive boundary port must therefore retain the functional

\[
x\longmapsto\sum_p p^{-1/2}x_p
\]

in a rigged or distributional coefficient space. It cannot be represented as
an ordinary bounded row on the unweighted prime Hilbert space.

Subtracting it numerically without retaining its boundary type would make the
residual synthesis bounded at the cost of erasing the exact common mode that
reciprocal completion must orient.

## Consequence for the joint Schur block

The finite Schur matrix remains exact. Its infinite completion cannot begin
with bounded operators

\[
B:\ell^2(\mathbb P)\to\mathcal H_{\rm seam}
\]

on the naive coefficient space. The construction order must be:

1. isolate the primitive common-mode distribution;
2. place the residual incidence in its bounded completion;
3. retain the square return grade as relative Hilbert data;
4. form the third-regularized joint determinant of the remaining block;
5. glue the primitive pair reciprocally.

This is the block-operator origin of the earlier three-grade filtration.

## DPC verdict

Resolved:

- the source-derived common mode of the joint prime incidence;
- its exact prime-harmonic norm divergence;
- the necessity of a distributional primitive boundary port;
- bounded residual incidence under an explicit tail-summability condition.

Withheld:

- the precise rigged prime coefficient space;
- reciprocal pairing of the common-mode functional;
- square-grade return completion;
- the final joint Schur determinant and zero-state bridge.

The finite falsifier for naive bounded incidence is the normalized cutoff
vector proportional to \(w_X\): its input norm is one while its common-mode
output grows like the square root of the prime harmonic sum.

## Verification

The checker `check_joint_prime_common_mode.py` computes the exact finite
prime-harmonic norm growth and contrasts it with a summable residual-tail
budget.
