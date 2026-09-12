# Absolute exponential shift Hankel matrices have full rank at every finite depth

## Theorem

Let \(x_1,\ldots,x_N\) be distinct real displacements and define

\[
H_{ij}=e^{-|x_i+x_j|}.
\]

If the displacement set is closed under negation, then

\[
\operatorname{rank}H=N.
\]

Consequently, for multiplicatively independent positive labels \(p_1,\ldots,p_d\), the depth-\(k\) signed-word Hankel matrix indexed by

\[
V_{d,k}=\{\nu\in\mathbb Z^d:\|\nu\|_1\le k\}
\]

has full rank \(|V_{d,k}|\).

## Reduction to the Laplace kernel

Negation permutes the column index set. After replacing the column displacement \(x_j\) by \(-x_j\), the matrix becomes

\[
K_{ij}=e^{-|x_i-x_j|}.
\]

Thus \(H\) and \(K\) have the same rank.

## Strict positive definiteness

The translation-invariant kernel

\[
k(x-y)=e^{-|x-y|}
\]

has strictly positive Fourier density

\[
\widehat k(\xi)=\frac{2}{1+\xi^2}>0.
\]

For coefficients \(c_1,\ldots,c_N\),

\[
\sum_{i,j}\overline{c_i}c_j e^{-|x_i-x_j|}
=
\frac{1}{2\pi}
\int_{\mathbb R}
\frac{2}{1+\xi^2}
\left|\sum_jc_je^{i\xi x_j}\right|^2d\xi.
\]

If this vanishes, the exponential polynomial

\[
\sum_jc_je^{i\xi x_j}
\]

vanishes almost everywhere and hence identically. Distinct frequencies are linearly independent, so every \(c_j=0\). Therefore \(K\) is positive definite and invertible.

## Prime-labelled consequence

For

\[
x_\nu=\sum_{r=1}^d\nu_r\log p_r,
\]

unique factorization implies

\[
x_\nu=x_\mu\Longrightarrow\nu=\mu.
\]

Hence every finite signed-word context gives a distinct displacement, and the Hankel rank is exactly

\[
|V_{d,k}|
=
\sum_{j=0}^d2^j\binom dj\binom kj.
\]

For four prime directions this is

\[
1,9,41,129,321,\ldots
\]

and grows asymptotically as

\[
\frac{2^d}{d!}k^d.
\]

## Meaning

The reciprocal boundary source \(e^{-|x|}\) has no finite-dimensional linear realization under independently labelled signed shifts. This is now a theorem at every finite depth, not merely the depth-three computational observation.

The infinite realization is nevertheless canonical: \(e^{-|x-y|}\) is the Green/covariance kernel of the one-dimensional massive operator. Thus finite internal orbit dimension and infinite contextual memory coexist:

```text
one-dimensional displacement geometry
+ strictly positive boundary kernel
= one independent state direction per labelled context
```

## Scope

This theorem assumes exact distinguishability of all signed words and the complete scalar context family. Restricting contexts, identifying labels, or changing the source kernel may reduce rank. Such reductions require an explicit protocol or kernel theorem.
