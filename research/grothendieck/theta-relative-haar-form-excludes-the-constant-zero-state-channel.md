# Theta relative Haar form excludes the constant zero-state channel

## Bounded question

Does the exact relative-Haar energy with critical cocycle apply to the
source-derived rank-two tail state whose endpoint determinant is the theta
Mellin readout?

## Two distinct Haar maps

Let

\[
\mathcal H_a=L^2(\mathbb R_{>0},dx),
\qquad
\mathcal H_m=L^2(\mathbb R_{>0},dx/x).
\]

Two maps must not be conflated.

The half-density normalization

\[
Wf=x^{1/2}f
\]

is unitary from \(\mathcal H_a\) to \(\mathcal H_m\). The identity inclusion

\[
If=f
\]

is instead a closed unbounded operator on

\[
\operatorname{Dom}I
=\mathcal H_a\cap\mathcal H_m.
\]

Its positive relative modular operator is

\[
\Delta=I^*I=M_{1/x}.
\]

For additive unitary dilation \(U_a(p)f=p^{1/2}f(px)\),

\[
U_a(p)^*\Delta U_a(p)=p\Delta.
\]

After Mellin multiplication by \(p^{-s}\), the relative energy therefore has
the exact factor \(p^{1-2\Re s}\).

## Source-derived zero-state channel

The tail equation

\[
(\partial_q+s)G+cf=0
\]

becomes homogeneous only after adjoining the constant degree of freedom (c).
For a nontrivial spectral state, (c\ne0). The zero condition is an endpoint
condition on (G), not removal of this constant channel.

If the constant is represented in the multiplicative carrier, its relative
Haar energy is

\[
\int_0^\infty|c|^2\frac{dx}{x}=\infty.
\]

Thus the canonical rank-two zero-state does not lie in the componentwise
domain of the relative-Haar form.

## No positive restriction-monotone extension

This divergence cannot be repaired by declaring a finite positive norm for the
constant while retaining the original form locally. Let

\[
c_R(x)=c\,\mathbf 1_{[R^{-1},R]}(x).
\]

Then

\[
\|c_R\|_{\mathcal H_m}^2=2|c|^2\log R\longrightarrow\infty.
\]

Suppose an enlarged positive form agrees with the relative-Haar form on compact
supports and does not increase energy when a state is restricted to a compact
interval. Its putative constant energy must dominate every displayed cutoff
energy and is therefore infinite. Thus no positive restriction-monotone local
extension can contain the constant. Subtracting the logarithmic divergence
would instead define a relative or indefinite boundary functional, not such an
extension of \(\Delta\).

## Typed consequence

The exact critical cocycle and the exact zero-to-endpoint state currently live
on different domains:

- \(\Delta\) supplies the oriented positive energy on the relative-Haar tail;
- the affine constant supplies the source-derived Evans endpoint determinant;
- the constant is excluded from \(\operatorname{Dom}\Delta^{1/2}\).

Their direct sum does not solve the problem because packet 227 requires the
determinant channel to be coupled to the oriented energy before scalar
compression.

## Required boundary extension

The surviving architecture must keep the constant as an independent boundary
coordinate and derive a block quadratic form

\[
\mathfrak q_s(G,c)
=\langle G,\Delta G\rangle
+2\Re\langle B_sG,c\rangle
+\beta_s|c|^2.
\]

The operators (B_s) and \(\beta_s\) must come from endpoint, primitive,
prime-square, seam, and archimedean currents. They cannot be chosen to cancel
the divergence after the fact.

The finite falsifier is immediate: if the declared source currents leave
(B_s=0) or leave an uncancelled logarithmic coefficient in \(\beta_s\), the
relative-Haar Evans bridge fails.

## Scope

This packet proves that the unbounded relative-Haar form has the exact critical
energy cocycle but excludes the constant channel of the canonical affine tail
zero-state. It proves that no positive restriction-monotone local extension can
include that constant while agreeing with the Haar form. It does not rule out
a typed relative boundary form, construct its source currents, or prove RH.
