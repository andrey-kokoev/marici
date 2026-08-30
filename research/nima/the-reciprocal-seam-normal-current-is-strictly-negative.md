# The reciprocal seam normal current is strictly negative

## Result

The seam normal current constructed previously is nonzero and has the exact sign

\[
\Phi''(0)<0.
\]

The proof is an elementary dominant-label estimate. The \(n=1\) theta label is strictly negative and dominates the positive tail \(n\ge2\).

Thus the jet-valued seam port is faithful on its source one-dimensional normal line.

## Label formula

Write

\[
H(u)
=
e^{u/2}
\left(
1+2\sum_{n\ge1}e^{-\lambda_n e^{2u}}
\right),
\qquad
\lambda_n=\pi n^2,
\]

and

\[
\Phi(u)
=
\left(\partial_u^2-\frac14\right)H(u).
\]

The wall term \(e^{u/2}\) is killed by the completion operator. For one exponential label,

\[
h_\lambda(u)=e^{u/2}e^{-\lambda e^{2u}},
\]

direct differentiation gives

\[
\left(\partial_u^2-\frac14\right)h_\lambda(u)
=
2\lambda
\left(
2\lambda e^{2u}-3
\right)
e^{5u/2-\lambda e^{2u}}.
\]

Differentiating twice more and evaluating at \(u=0\) gives

\[
\left.
\partial_u^2
\left(\partial_u^2-\frac14\right)
h_\lambda(u)
\right|_{u=0}
=
\frac{\lambda}{2}
P(\lambda)e^{-\lambda},
\]

where

\[
P(x)=32x^3-224x^2+330x-75.
\]

The pair of labels \(n\) and \(-n\) contributes twice this amount. Hence

\[
\Phi''(0)
=
\sum_{n\ge1}
\lambda_nP(\lambda_n)e^{-\lambda_n}.
\]

This series is absolutely convergent.

## Sign of the first label

Using the elementary enclosure

\[
3.14159<\pi<3.14160,
\]

direct interval evaluation gives

\[
P(\pi)<-256.
\]

Also

\[
\pi[-P(\pi)]>803
\]

and

\[
e^{-\pi}>e^{-3.142}>0.043.
\]

Therefore the magnitude of the negative first contribution satisfies

\[
-\pi P(\pi)e^{-\pi}>34.
\]

## Positive tail bound

For \(x\ge4\pi\),

\[
P(x)
<
32x^3+330x
<
59x^3.
\]

Thus, regardless of the exact sign of each tail term,

\[
\sum_{n\ge2}
\lambda_nP(\lambda_n)e^{-\lambda_n}
<
59\pi^4
\sum_{n\ge2}n^8e^{-\pi n^2}.
\]

Let

\[
b_n=n^8e^{-\pi n^2}.
\]

For \(n\ge2\),

\[
\frac{b_{n+1}}{b_n}
=
\left(1+\frac1n\right)^8e^{-\pi(2n+1)}
<
5\cdot10^{-6}.
\]

Consequently,

\[
\sum_{n\ge2}b_n
<
\frac{2^8e^{-4\pi}}{1-5\cdot10^{-6}}.
\]

Using the same elementary enclosures for \(\pi\) and the exponential gives

\[
59\pi^4
\sum_{n\ge2}n^8e^{-\pi n^2}
<
6.
\]

Combining the estimates,

\[
\Phi''(0)<-34+6<0.
\]

In particular,

\[
\Phi''(0)\ne0.
\]

The deliberately coarse gap is sufficient; no floating-point sign decision is used.

## Seam observer consequence

The first seam jet is

\[
j_0^1(\Phi')
=
\left(0,\Phi''(0)\right)
\]

with a strictly negative normal component in the frozen \(u\)-orientation.

Therefore the source normal line is observed faithfully. If its source metric is normalized by the exact theta-history Gram, the local seam frame constant is

\[
m_{\mathrm{seam}}
=
\frac{|\Phi''(0)|}
{\|J_{\mathrm{normal}}(0)\|_{\mathrm{source}}}
>0.
\]

This is a single fixed local number, not yet a global prime/cutoff margin.

Reversing the normal coordinate changes the oriented component's sign. The numerical second derivative remains the same only if one forgets the normal-line orientation, which the typed seam port must retain.

## Compatibility with the eighth-order formula

The label-series expression agrees with the previously derived Jacobi formula

\[
\Phi''(0)
=
\frac{\Theta_8(0,1)}{16\pi^4}
+
\frac{7\Theta_6(0,1)}{4\pi^3}
+
\frac{165\Theta_4(0,1)}{16\pi^2}
+
\frac{75\Theta_2(0,1)}{8\pi}.
\]

The first form proves the sign through arithmetic label dominance. The second identifies the same current as a derivative-comb contraction with the seventh-order odd front jet. Their equality is the desired additive-to-ordered cross-check at the local seam.

## Remaining comparison

The seam normal port is now constructed, bounded on the positive heat range, and nonzero. The next gate is normalization compatibility:

> Compare the fixed negative normal current \(\Phi''(0)\) with the Wronskian wall current and the reciprocal Euler odd port through source-derived linking maps.

Only after that comparison can the three odd ports be treated as calibrated realizations of one seam orientation coordinate.
