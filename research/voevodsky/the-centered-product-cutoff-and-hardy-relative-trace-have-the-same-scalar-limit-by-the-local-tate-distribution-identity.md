# Conditional comparison: centered product cutoff and uncompressed Hardy relative trace have the same sourced scalar limit, but placement remains

## Two centered scalar regulators

Let

\[
h=g*g^*.
\]

Define Connes's centered product-cutoff scalar

\[
\boxed{
C_{\Lambda,S}(h)
=
\operatorname{Tr}
\left(
P_\Lambda Q_\Lambda U_S(h)
\right)
-
2\log\Lambdah(1).
}
\]

For `L=log Lambda`, define the angularly assembled centered Hardy relative trace

\[
\boxed{
H_{L,S}(g)
=
\sum_\chi
\operatorname{Tr}_{rel}
\left(
M_{|m_{g,\chi}|^2}
(\Pi_{e^{2iLs}\gamma_\chi}-
\Pi)
\right)
-
2Lh(1).
}
\]

Endpoint/winding terms are included in `Tr_rel` with the same local additive-character normalization used to define the Tate gamma factors.

## Connes limit

The semilocal cutoff theorem gives

\[
\boxed{
C_{\Lambda,S}(h)
\longrightarrow
W_S(h).
}
\]

Here

\[
W_S(h)
=
\sum_{v\in S}
\int_{k_v^*}^{\prime}
\frac{h(u^{-1})}{|1-u|_v}d^*u

\]

with each principal value normalized by the chosen basic additive character.

## Hardy trace after centering

The relative projection-pair formula and Mellin Plancherel give

\[
\boxed{
H_{L,S}(g)
=
\sum_\chi
\left[
\frac1{2\pi i}
\int_\mathbb R
|m_{g,\chi}(s)|^2
\partial_s
\log\gamma_\chi(s)ds
+
e_{end,\chi}(g)
\right].
}
\]

The right side is independent of `L`.

Denote it by

\[
W_S^{Tate}(h).
\]

## Local Tate distribution identity

For each place `v`, the local functional equation identifies the Fourier transform of the normalized principal-value distribution

\[
u
\longmapsto
\frac1{|1-u|_v}
\]

with the logarithmic derivative of the local Tate gamma factor on the unitary axis.

In the present normalization this is precisely

\[
\boxed{
W_v(h)
=
\sum_{\chi_v}
\left[
\frac1{2\pi i}
\int
|m_{g,\chi_v}(s)|^2
\partial_s
\log\gamma_{v,\chi_v}(s)ds
+
e_{end,v,\chi_v}(g)
\right].
}
\]

The prime on the physical-space integral and the endpoint/winding term on the spectral side encode the same normalization datum. They must not be added independently a second time.

Summing the finitely many places in `S` and assembling product angular characters gives

\[
\boxed{
W_S^{Tate}(h)
=W_S(h).
}
\]

## Centered scalar regulator convergence

Combining the two identities yields

\[
\begin{aligned}
C_{\Lambda,S}(h)
-
H_{\log\Lambda,S}(g)
&=
C_{\Lambda,S}(h)
-
W_S(h)\\
&\longrightarrow0.
\end{aligned}
\]

Therefore

\[
\boxed{
\operatorname{Tr}
(P_\Lambda Q_\Lambda U_S(h))
-
\sum_\chi
\operatorname{Tr}_{rel}
\left(
M_{|m_{g,\chi}|^2}
(\Pi_{e^{2iL s}\gamma_\chi}-
\Pi)
\right)
\longrightarrow0
}
\]

with `L=log Lambda`, provided both expressions use the matching orientation.

The common linear terms cancel before the limit.

## Polarization

For two observers `g,k`, use

\[
h_{g,k}
=g*k^*.
\]

The diagonal identity extends by complex polarization:

\[
\boxed{
C_{\Lambda,S}(g,k)
-
H_{\log\Lambda,S}(g,k)
\longrightarrow0.
}
\]

Hence the centered cutoff and Hardy constructions define the same limiting sesquilinear form on every finite observer packet.

## What this proves for `C_34`

At the scalar/form level, the boundary sewing is complete:

\[
\boxed{
\text{centered Connes cutoff form}
\longrightarrow
W_S
=
\text{centered Tate--Hardy relative form}.
}
\]

This proves equality of matrix coefficients, not convergence of individual Hilbert--Schmidt legs.

## Why trace-norm regulator comparison is stronger

From

\[
\operatorname{Tr}(A_\Lambda)
-
\operatorname{Tr}_{rel}(B_\Lambda)
\to0
\]

one cannot conclude

\[
\|A_\Lambda-B_\Lambda\|_1
\to0
\]

or convergence of chosen square-root features.

Large positive and negative singular-value contributions may cancel in the scalar trace. Therefore the source theorem closes only the signed/form-valued `C_34` face.

## Positive boundary remains open

To construct the positive filler, one still needs an orthogonal bulk-removal map and residual features

\[
\widetilde\Phi_\Lambda(g)
\]

such that

\[
\boxed{
\langle
\widetilde\Phi_\Lambda(g),
\widetilde\Phi_\Lambda(k)
\rangle
\longrightarrow
W_S(g*k^*)
}
\]

or to a completed positive enlargement containing the signed Weil form as a readout.

The scalar equality does not imply such a positive Gram realization, because `W_S` is precisely the form whose positivity is the arithmetic target.

## Endpoint bookkeeping

There are two conventions:

1. normalized principal values on the physical side;
2. a branch of `log gamma` plus endpoint index on the spectral side.

The local Tate identity equates them. A regulator comparison that includes both the normalized principal value and an additional independent copy of the endpoint term double-counts the boundary.

Thus the endpoint must be transported, not duplicated.

## Angular summability

For smooth compact observers, angular Mellin coefficients decay rapidly, while local logarithmic gamma derivatives grow at most logarithmically/polynomially. Hence

\[
\sum_\chi
\int
|m_{g,\chi}(s)|^2
|\partial_s\log\gamma_\chi(s)|ds
<\infty.
\]

This justifies angular assembly of the scalar Tate form without invoking a bare semilocal transition trace.

## Exact logical dependencies

The scalar comparison uses:

1. Connes's semilocal product-cutoff asymptotic;
2. the localized Hardy projection-pair formula;
3. Mellin Plancherel normalization;
4. the local Tate distribution identity;
5. angular dominated convergence.

It does not use:

- Hilbert--Schmidt finiteness of a bare Hardy transition;
- an `o(log Lambda)` estimate for uncentered sewing;
- trace-norm convergence between regulators;
- positivity of the Weil form.

## Subsequent placement correction

The standard projection-pair formula evaluates the uncompressed difference `Q_T-Q_0`, whereas exact transport of Connes's ordered product retains a left Hardy projection `Pi(Q_T-Q_0)`. Their traces differ by a Hardy-reflection placement term. See `correction-the-relative-projection-trace-formula-does-not-directly-evaluate-the-left-hardy-compressed-product.md`. Thus the limit comparison below is conditional on computing that term or producing an exact cyclic reformulation.

## Disposition

Conditionally, the centered signed regulator comparison is:

\[
\boxed{
C_{\Lambda,S}
-
H_{\log\Lambda,S}
\longrightarrow0.
}
\]

The remaining `C_34` task is specifically positive-feature convergence after orthogonal bulk removal. It must not be described as an unresolved scalar normalization or finite-part identity.
