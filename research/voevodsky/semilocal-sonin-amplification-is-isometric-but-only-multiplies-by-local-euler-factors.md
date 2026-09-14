# Semilocal Sonin amplification is isometric but only multiplies by local Euler factors

## Primary-text computation

In arXiv:2310.18423, Connes--Consani--Moscovici define, for a finite set of places `S` containing infinity, a semilocal map

\[
\Sigma_S:L^2(\mathbb R)_{ev}\longrightarrow L^2(X_S)^{K_S}.
\]

For one finite prime `p`, the local seed is

\[
\sigma_p=\mathbf1_{\mathbb Z_p}-p^{-1}\mathbf1_{p^{-1}\mathbb Z_p},
\]

which is Fourier invariant and generates the one-dimensional invariant local Sonin space. Tensoring these local seeds with the archimedean vector defines the semilocal amplification.

## Euler-factor action

Proposition 4.6(ii) computes its Mellin/Fourier effect exactly:

\[
\mathcal F_\mu w_S(\Sigma_Sf)(s)
=
\mathcal F_\mu w(f)(s)
\prod_{p\in S\setminus\{\infty\}}
(1-p^{-1/2-is}).
\]

Equivalently, the multiplier is the inverse product of local Euler factors

\[
\prod_{p\in S\setminus\{\infty\}}
L_p(1/2+is)^{-1}.
\]

Thus finite places enter the common spectral carrier coherently through one product multiplier, not as orthogonal prime-labelled scalar summands.

## Isometric stability

Although the raw map `Sigma_S` is not unitary in the first presentation, Proposition 4.7 constructs the weighted Hardy--Titchmarsh realization in which

\[
\langle\Sigma_Sf,\Sigma_Sg\rangle
=
\langle f,g\rangle.
\]

Theorem 4.6 then proves

\[
\boxed{
\Sigma_S:\mathcal S(\mathbb R,e^\lambda)
\overset{\sim}{\longrightarrow}
\mathcal S(X_S,\lambda)
}
\]

as a Hilbertian isomorphism. This is compatible with Fourier transform and remains stable as finite places are added.

This satisfies an important requirement from the prime-shift audit: all active primes are inserted into a single Hilbert carrier through a multiplicative Euler product.

## What it does not yet do

Multiplication by

\[
1-p^{-1/2-is}
\]

is not itself the prime part of the Weil quadratic form. Squaring its modulus gives

\[
|1-p^{-1/2-is}|^2
=
1+p^{-1}-2p^{-1/2}\cos(s\log p),
\]

which contains one prime-frequency cosine with a favorable Gram origin. But the logarithmic derivative in the explicit formula requires the full prime-power tower

\[
\sum_{k\ge1}
\frac{\log p}{p^{k/2}}
\cos(ks\log p)

=
-\operatorname{Re}
\frac{d}{ds}\log L_p(1/2+is)
\]

up to the derivative convention.

A single modulus square of the inverse Euler factor does not reproduce these logarithmic prime-power weights. Differentiating the multiplier introduces them, but differentiation is an unbounded generator and destroys the immediate isometric norm-square interpretation.

## Exact missing operation

Let

\[
M_S(s)=
\prod_{p\in S\setminus\{\infty\}}
L_p(1/2+is)^{-1}.
\]

The semilocal isometry controls multiplication by `M_S`. The finite-place Weil distribution is controlled by the logarithmic derivative

\[
-i\,\partial_s\log M_S(s).
\]

Therefore the missing bridge is a differentiated trace/commutator identity converting

\[
M_S^*M_S
\]

into the logarithmic derivative contribution while retaining positivity after compression to the Sonin space.

This is exactly where the infinite-rank truncated translations enter: in physical log coordinates, differentiating the Euler multiplier produces the weighted shift tower at `k log p`.

## Why the isometry alone cannot imply positivity

Two finite-place sets have Hilbert-isomorphic Sonin spaces after the weighted transform. If that isometry by itself implied finite-place Weil positivity, positivity would be independent of the logarithmic derivative weights and would follow before the trace comparison that the authors explicitly leave as a strategy.

The source identity needed is not merely

\[
\|\Sigma_Sf\|=\|f\|,
\]

but a Green/commutator formula schematically of the form

\[
W_S(f)
=
\operatorname{Tr}(\vartheta_S(f)P_{Sonin,S})
-
E_S(f),
\]

with `E_S` controlled uniformly under enlargement of `S`.

## Cross-prime polarization

The product `M_S` does preserve coherent cross-prime multiplication before taking norms. However,

\[
|M_S|^2
=
\prod_{p\in S}|L_p^{-1}|^2
\]

contains multiplicative cross terms different from the additive logarithmic derivative

\[
\partial_s\log M_S
=
\sum_{p\in S}\partial_s\log L_p^{-1}.
\]

Passing from product geometry to additive Weil geometry requires a logarithm or infinitesimal trace. This operation is the exact polarization bottleneck; ordinary Hilbert norm squaring does not perform it.

## Disposition

The semilocal Sonin construction clears one major structural gate:

\[
\boxed{
\text{all finite primes enter one Fourier-compatible Hilbert carrier through }M_S.
}
\]

But it stops one derivative short of the Weil functional. The unresolved theorem is a positive compressed-trace identity for the logarithmic derivative of the Euler multiplier, including a uniformly controlled remainder. This is more precise than saying only that a semilocal `L2` transfer is missing.
