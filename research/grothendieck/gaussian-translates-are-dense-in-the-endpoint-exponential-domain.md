# Gaussian translates are dense in the endpoint exponential domain

## Question

Does the two-sided exponential topology required by endpoint evaluation exclude the fixed-width Gaussian translate observer family from being a core?

## Endpoint Hilbert space

Fix `beta>1`, with the threshold adjusted to the explicit-formula convention, and define

\[
H_\beta
=
L^2(\mathbb R,e^{\beta|x|}dx)
\]

in the Fourier variable `x`. Cauchy--Schwarz then bounds the endpoint functionals involving `e^(plus-or-minus x/2)`.

The Fourier transforms of real translates of a fixed Gaussian have the form

\[
\widehat{\tau_ag_\sigma}(x)
=
e^{-iax}e^{-d_\sigma x^2}
\]

up to a nonzero normalization.

## Density theorem

Suppose `F in H_beta` is orthogonal in `H_beta` to every Gaussian translate. Then for every real `a`,

\[
0
=
\int F(x)e^{-d_\sigma x^2}e^{iax}
 e^{\beta|x|}\,dx.
\]

The function

\[
H(x)=F(x)e^{-d_\sigma x^2}e^{\beta|x|}
\]

belongs to `L^1`. Indeed,

\[
\|H\|_1
\le
\|F e^{\beta|x|/2}\|_2
\|e^{-d_\sigma x^2}e^{\beta|x|/2}\|_2,
\]

and the second factor is finite by Gaussian decay.

The displayed orthogonality says that the Fourier transform of `H` vanishes at every real frequency. Fourier uniqueness on `L^1` gives `H=0`, hence `F=0`. Therefore

\[
\overline{\operatorname{span}\{\widehat{\tau_ag_\sigma}:a\in\mathbb R\}}^{H_\beta}
=H_\beta.
\]

So fixed-width Gaussian translates are dense in the endpoint exponential domain.

## What remains

This proves endpoint-sector density, while the earlier finite-difference argument proves gamma-sector graph-core density. Neither separate result proves density in the intersection topology

\[
\|f\|^2+
\|f\|_{\rm endpoint}^2+
\|f\|_{\Gamma}^2+
\|f\|_{\mathbb P}^2.
\]

Dense in each of two spaces separately does not imply dense in their graph intersection. A simultaneous approximation operator preserving both endpoint exponential control and gamma logarithmic control is still required.

## Disposition

Discharge the endpoint-sector density blocker: the exponential weight is compatible with fixed-width Gaussian translate completeness. Retain the common-core blocker only at simultaneous endpoint--gamma approximation, with the prime row bounded at fixed width.
