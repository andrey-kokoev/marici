# Two complex horizontal lines continuously recover the codiagonalized projective source

## Question

Which displacement-sensitive observer is strong enough to recover the projective coefficients after common-history codiagonalization?

## Claim boundary

For the deconvolved exponential sum, uniform observation on the two horizontal lines at imaginary heights \(\pm R\) continuously controls every source seminorm \(q_\delta\) once

\[
R>\delta+\frac32.
\]

The extra margin beyond the Euler half-density loss pays for summation over all prime powers. This is a genuine post-codiagonal recovery estimate. It is conditional on access to the entire deconvolved function on those lines; the earlier low-frequency theta division does not itself supply that global continuation continuously.

## Entire exponential sum

Write

\[
F_c(z)=
\sum_{p,k}d_{p,k}^+e^{izL_{p,k}}
+d_{p,k}^-e^{-izL_{p,k}},
\]

where

\[
L_{p,k}=k\log p,
\qquad
d_{p,k}^{\pm}
=\frac1k e^{-L_{p,k}/2}c_{p,k}^{\pm}.
\]

Projective exponential summability makes this series uniformly convergent on every horizontal line and every closed strip.

Define

\[
S_R(F)
=
\max\left\{
\sup_{x\in\mathbb R}|F(x+iR)|,
\sup_{x\in\mathbb R}|F(x-iR)|
\right\}.
\]

## Bohr extraction on the amplified line

On \(z=x-iR\), the positive-orientation coefficient is amplified by \(e^{RL_{p,k}}\). Its Bohr coefficient is

\[
d_{p,k}^+e^{RL_{p,k}}
=
\lim_{T\to\infty}
\frac1{2T}
\int_{-T}^{T}F_c(x-iR)e^{-ixL_{p,k}}\,dx.
\]

Distinct signed prime-power displacements ensure that all other frequencies average to zero. Therefore

\[
|d_{p,k}^+|e^{RL_{p,k}}
\le S_R(F_c).
\]

The line \(z=x+iR\) gives similarly

\[
|d_{p,k}^-|e^{RL_{p,k}}
\le S_R(F_c).
\]

## Projective recovery bound

Since

\[
|c_{p,k}^{\pm}|
=k e^{L_{p,k}/2}|d_{p,k}^{\pm}|,
\]

we obtain

\[
q_\delta(c)
\le
2S_R(F_c)
\sum_{p\ {m prime}}\sum_{k\ge1}
k e^{-(R-\delta-1/2)k\log p}.
\]

Put

\[
\varepsilon=R-\delta-\frac12.
\]

The numerical majorant is

\[
K_\varepsilon
=
2\sum_p\sum_{k\ge1}k p^{-k\varepsilon}
=
2\sum_p\frac{p^{-\varepsilon}}
{(1-p^{-\varepsilon})^2}.
\]

It is finite for every \(\varepsilon>1\). Hence, whenever

\[
R>\delta+\frac32,
\]

one has the explicit continuous inverse estimate

\[
q_\delta(c)
\le K_{R-\delta-1/2}S_R(F_c).
\]

This estimate does not require uniform separation of the logarithmic frequencies, a Sidon inequality, or a Hilbert frame bound.

## Forward continuity

Conversely,

\[
S_R(F_c)
\le
\sum_{p,k}\frac1k
 e^{(R-1/2)L_{p,k}}
\left(|c_{p,k}^+|+|c_{p,k}^-|\right),
\]

so every \(S_R\) is controlled by a sufficiently strong source seminorm. The projective source topology and the family of two-line observer seminorms therefore induce equivalent topologies on the deconvolved synthesis range, with finite shifts of exponential order.

## Authority and remaining gate

The observer is not yet a theorem about the raw common history. The raw Fourier transform satisfies

\[
\widehat h_c(z)=\widehat\Phi(z)F_c(z).
\]

To derive \(S_R(F_c)\) from raw-history seminorms, one needs global control of division by \(\widehat\Phi\) on both entire horizontal lines, or a source-authorized parametrix producing the same Bohr coefficients. The source-fixed interval near zero cannot provide this continuously because compact-window continuation was disproved.

Thus the topology problem has split cleanly:

1. deconvolved two-line observation gives continuous projective recovery;
2. transporting that observer through the completed-theta factor remains open;
3. retaining labels bypasses step 2 through the existing fibrewise recovery port.

## Direction rescore

- All-strip deconvolved recovery: completed, with two lines per seminorm sufficient.
- Required height: any \(R>\delta+3/2\).
- Compact real-window recovery: disproved.
- Raw-history to two-line deconvolution: 8/10; requires global theta divisor/growth control.
- Label-retaining G4 recovery: completed on the source range, interface-blocked for G4.

## Disposition

Codiagonalization admits a continuous projective inverse once the observer retains complex horizontal growth of the deconvolved response. The remaining depth-first question is whether the completed-theta transform permits this two-line observer to descend continuously from the raw common history without inserting zero-dependent data. No RH or Hilbert closed-range conclusion is authorized.
