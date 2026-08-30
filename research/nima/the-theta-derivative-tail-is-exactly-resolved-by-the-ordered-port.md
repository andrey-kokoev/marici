# The theta derivative-tail is exactly resolved by the ordered port

## Operators on the rapid zero-mode-reduced core

Let

\[
D=\partial_t
\]

and let the ordered port satisfy

\[
DS_{\mathrm{ord}}
=
S_{\mathrm{ord}}D
=
-2I.
\]

For the theta tail kernel

\[
K(r)=\int_r^\infty\Phi(s)\,ds,
\]

let \(H_K\) denote the corresponding one-sided full-line convolution. The
derivative-tail part of the completed theta history is

\[
B=H_KD.
\]

All three operators are translation-invariant on the full-line rapid core.
Hence \(H_K\) commutes with \(D\), and with the convolutional ordered port
on the zero-mode-reduced domain.

## Exact resolution identity

On the right,

\[
BS_{\mathrm{ord}}
=
H_KDS_{\mathrm{ord}}
=
-2H_K.
\]

On the left,

\[
S_{\mathrm{ord}}B
=
S_{\mathrm{ord}}H_KD
=
H_KS_{\mathrm{ord}}D
=
-2H_K.
\]

Therefore

\[
BS_{\mathrm{ord}}
=
S_{\mathrm{ord}}B
=
-2H_K.
\]

The unbounded derivative-tail channel becomes the bounded tail convolution
after composition with the ordered inverse derivative.

## Reconstructed history

Since

\[
H_\Phi=M_\Phi I+B,
\]

the completed theta history has the ordered-port factorization

\[
H_\Phi
=
M_\Phi I
-
2H_KS_{\mathrm{ord}}^{-1}
\]

on the range where the inverse notation is authorized. The safer
constructor statement is the product identity

\[
(H_\Phi-M_\Phi I)S_{\mathrm{ord}}
=
-2H_K.
\]

This form avoids inventing an inverse outside the reduced derivative range.

## Curvature composition

The connection curvature satisfies

\[
S_{\mathrm{ord}}\Omega=4A.
\]

Consequently,

\[
B S_{\mathrm{ord}}\Omega
=
-2H_K\Omega,
\]

or equivalently,

\[
4BA=-2H_K\Omega.
\]

Thus the curvature-to-theta-tail comparison is governed by one explicit
commuting diagram:

\[
\begin{array}{ccc}
\text{odd curvature}
&\xrightarrow{\ S_{\mathrm{ord}}\ }&
\text{even dilation current}\\
\downarrow H_K&&\downarrow B\\
\text{bounded tail history}
&=&
\text{theta derivative-tail}.
\end{array}
\]

The exact placement of arrows depends on the declared source and target
domains, but the operator products are fixed.

## Boundedness

If \(K\in L^1(0,\infty)\), then

\[
\|H_K\|\le\|K\|_1.
\]

Therefore the ordered-port-resolved derivative tail is bounded:

\[
\|BS_{\mathrm{ord}}\|
\le
2\|K\|_1.
\]

This is stronger than treating \(B=H_KD\) only as an operator on a joint
derivative graph.

## Zero-mode qualification

The ordered port has a singular zero-frequency multiplier. The identity above
must be read after:

- retaining the constant wall separately;
- restricting the derivative channel to the zero-mode-reduced core;
- or using the relative-history quotient where the wall coordinate is
  explicit.

The wall term \(M_\Phi I\) is precisely what must not be absorbed into the
ordered inverse.

## Reflection

Reflection exchanges the causal and anticausal tail convolutions and reverses
\(S_{\mathrm{ord}}\). Hence the resolved pair has the correct
reciprocal-odd character, while \(M_\Phi I\) remains reflection-even.

## What this closes

The primitive ordered port and the completed-theta convolution are no longer
separate unexplained histories. Their non-wall parts satisfy the exact
source-native relation

\[
(H_\Phi-M_\Phi I)S_{\mathrm{ord}}
=
-2H_K.
\]

The tail propagator is determined by \(\Phi\) and is bounded by its first
moment.

## Remaining gate

The remaining window/seam comparison is concentrated entirely at:

1. the wall identification;
2. transport of the two-ray half-density domains into the common
   zero-mode-reduced convolution core;
3. quadratic Green compatibility after this transport.

The odd kernel-synthesis arrow itself is now explicit.
