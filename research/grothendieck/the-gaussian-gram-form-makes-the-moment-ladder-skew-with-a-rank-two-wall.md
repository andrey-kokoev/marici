# The Gaussian Gram form makes the moment ladder skew with a rank-two wall

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact source Green identity and scope correction

## Carrier Gram matrix

Let

\[
g_k(x)=(\pi x^2)^ke^{-\pi x^2},
\qquad k\ge0.
\]

Their real Gaussian Gram matrix is

\[
G_{jk}=\langle g_j,g_k\rangle
=\frac{\Gamma(j+k+1/2)}{2^{j+k+1/2}\sqrt\pi}.
\]

It is strictly positive on every finite coefficient packet because the
functions (g_k) are linearly independent.

The dilation generator

\[
K=x\partial_x+\frac12
\]

acts by

\[
Kg_k=\left(2k+\frac12\right)g_k-2g_{k+1}.
\]

Integration by parts gives the exact Green identity

\[
\langle Kg_j,g_k\rangle+\langle g_j,Kg_k\rangle=0.
\]

Equivalently,

\[
\left(2j+2k+1\right)G_{jk}-2G_{j+1,k}-2G_{j,k+1}=0.
\]

This also follows from

\[
G_{r+1}=\frac{r+1/2}{2}G_r,
\qquad r=j+k.
\]

Thus the infinite moment ladder is skew with respect to a canonical positive
source metric; no fitted Lyapunov matrix is required.

## Finite-wall anomaly

Let (A_N) be the ladder matrix truncated after grade (N), and let (G_N)
be the corresponding principal Gram matrix. Then

\[
A_N^TG_N+G_NA_N=B_N,
\]

where

\[
(B_N)_{jk}
=2\delta_{jN}G_{N+1,k}+2\delta_{kN}G_{j,N+1}.
\]

Hence the failure of a finite cutoff to be skew has rank at most two and is
supported entirely on its top-grade wall. This is the quadratic counterpart
of the outward current (-2c_NM_{N+1}) from ledger 3052.

## Scope correction

This positive Green form governs dilation of the archimedean carrier. The
Riemann zeros are zeros of the spectral transform of the scalar matrix
coefficient produced after pairing that carrier with the arithmetic comb.
Those are different levels.

A unitary or skew flow can have a vanishing matrix coefficient between two
nonzero states. Therefore the identity above does not confine zeros. It
supplies the correct source metric and finite-wall current, but the missing
theorem must couple this carrier energy to the spectral tail transform and the
arithmetic boundary before scalar compression.

## Remaining obstacle

The next admissible object is not another positive form on the moment ladder.
It is an intertwiner from the carrier Green form to the spectral-tail Green
form, retaining the comb, reciprocal sheet, and endpoint currents. Without
that bridge, carrier norm conservation and spectral zero confinement are
logically independent.

## Scope

The Gram formula, skew identity, strict finite positivity, and rank-two cutoff
anomaly are exact. Completion of the unbounded ladder and the carrier-to-tail
intertwiner remain unproved. No zero confinement or RH claim is made.

