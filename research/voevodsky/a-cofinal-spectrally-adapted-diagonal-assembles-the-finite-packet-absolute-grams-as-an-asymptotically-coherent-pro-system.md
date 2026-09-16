# A cofinal spectrally adapted diagonal assembles the finite-packet absolute Grams as an asymptotically coherent pro-system

## Target filtration

Let

\[
A=\mathcal A_S
\]

be the bounded self-adjoint phase-energy multiplier. Prior work supplies nested finite-rank projections

\[
E_1\le E_2\le\cdots,
\qquad
E_n\longrightarrow I
\]

strongly, with spectral mesh \(\delta_n\to0\), such that

\[
\|[A,E_n]\|
\le2\delta_n
\]

and

\[
\left\|
|E_nAE_n|-E_n|A|E_n
\right\|
\le2\delta_n.
\]

## Finite physical input

Let \(D_\lambda\) be the aligned centered physical regulator at regulator index \(\lambda\). On every fixed finite packet, centered convergence gives

\[
E_nD_\lambda E_n
\longrightarrow
E_nAE_n
\]

in matrix norm.

The finite-packet common-edge theorem then produces the canonical residual absolute Gram

\[
R_{n,\lambda}
=
|E_nD_\lambda E_n|
\]

for sufficiently large \(\lambda\) on the coercive edge quotient.

## Cofinal diagonal choice

Choose a positive sequence \(\varepsilon_n\to0\). Recursively select a cofinal regulator sequence

\[
\lambda_1\preceq\lambda_2\preceq\cdots
\]

such that

\[
\left\|
E_nD_{\lambda_n}E_n
-
E_nAE_n
\right\|
\le
\varepsilon_n.
\]

Finite-dimensional continuity of absolute value gives a modulus

\[
\omega_n(t)
\longrightarrow0
\]

with

\[
\left\|
|E_nD_{\lambda_n}E_n|
-
|E_nAE_n|
\right\|
\le
\omega_n(\varepsilon_n).
\]

Choose the diagonal so that

\[
\omega_n(\varepsilon_n)
\le
\delta_n.
\]

Then

\[
\boxed{
\left\|
R_n-E_n|A|E_n
\right\|
\le3\delta_n,
}
\]

where

\[
R_n=|E_nD_{\lambda_n}E_n|.
\]

## Asymptotic packet compatibility

For \(m\le n\), compare the larger-packet residual with the residual selected at level \(m\):

\[
E_mR_nE_m-R_m.
\]

Insert the common global target \(|A|\). The triangle inequality gives

\[
\begin{aligned}
\|E_mR_nE_m-R_m\|
&\le
\|E_m(R_n-E_n|A|E_n)E_m\|\\
&\quad+
\|E_m|A|E_m-R_m\|.
\end{aligned}
\]

Therefore

\[
\boxed{
\|E_mR_nE_m-R_m\|
\le
3\delta_n+3\delta_m.
}
\]

The finite residuals are asymptotically compatible under packet restriction.

## Strong convergence

Since

\[
E_n|A|E_n
\longrightarrow
|A|
\]

strongly and

\[
\|R_n-E_n|A|E_n\|
\longrightarrow0,
\]

one obtains

\[
\boxed{
R_nE_n
\longrightarrow
|A|
}
\]

strongly on the phase-energy completion.

For every core vector \(u\),

\[
\langle E_nu,R_nE_nu\rangle
\longrightarrow
\langle u,|A|u\rangle.
\]

## Categorical meaning

The pairs

\[
(E_n,R_n)
\]

form an asymptotically coherent positive pro-system. Its transition defect is

\[
\epsilon_{m,n}
=
E_mR_nE_m-R_m
\]

with

\[
\|\epsilon_{m,n}\|
\le3\delta_n+3\delta_m.
\]

Passing to the norm-zero asymptotic quotient makes the transition cells exact. The resulting pro-object realizes the positive boundary \(|A|\) on the cofinal diagonal.

## Scope

This construction uses the established finite-packet absolute-Gram theorem and the spectrally adapted target filtration. It supplies:

- a cofinal positive residual system;
- asymptotic packet naturality;
- strong convergence to \(|A|\);
- an exact object after quotienting norm-null transition defects.

A global physical residual feature before packet compression requires the stronger regulator-uniform compression estimate. Mosco convergence of the raw full-domain physical forms requires the corresponding liminf and recovery statements.

## Consequence for the program

The positive boundary now has an intermediate realization between isolated finite packets and a global physical residual operator:

\[
\boxed{
\text{spectrally adapted cofinal pro-system}
\longrightarrow
|\mathcal A_S|.
}
\]

This is sufficient for a positive asymptotic categorical lift on the countable observer core. The global closed-form lift remains governed by the regulator-uniform graph estimate.
