# Finite Jordan completion cannot repair the raw-window decay after scalar pairing

## Result

Let
\[
\beta(L)
=
4\int_L^{2L}e^{-\pi u^2}\,du.
\]
Then
\[
0<\beta(L)\le4Le^{-\pi L^2}.
\]

Consider any finite-order scalar completion operator of the form
\[
\mathcal P_L
=
\sum_{j=0}^{N}a_j(L)\partial_L^j,
\]
where each coefficient has at most ordinary exponential growth:
\[
|a_j(L)|\le C_j(1+L)^{m_j}e^{c_jL}.
\]

Then there exist constants \(C,M,c\) such that
\[
|\mathcal P_L\beta(L)|
\le
C(1+L)^M e^{-\pi L^2+cL}.
\]

In particular,
\[
\frac{|\mathcal P_L\beta(L)|}{Le^{-L/2}}
\longrightarrow0.
\]

Thus no finite differential/Jordan completion applied after the raw scalar Stokes pairing can convert its Gaussian-in-\(L\) decay into Euler half-density decay.

## Proof sketch

Every derivative of \(e^{-\pi L^2}\) is a polynomial in \(L\) times the same Gaussian. Differentiating the endpoint integral likewise produces finite sums of polynomial factors multiplying
\[
e^{-\pi L^2}
\quad\text{and}\quad
e^{-4\pi L^2}.
\]

Multiplication by coefficients of size polynomial times \(e^{cL}\) preserves the dominant quadratic exponent:
\[
-\pi L^2+O(L).
\]
It cannot produce the linear exponent
\[
-\frac L2.
\]

## Consequence for the three-grade packet

The length-three completion polynomial and its Jordan derivatives are finite-order operations. If they act only on the already scalarized coefficient \(\beta_p\), they cannot repair the decay-order mismatch found at event 10377.

Therefore the chain
\[
\text{raw cross-character scalar}
\longrightarrow
\text{three-grade completion}
\]
is closed negative.

The source operations must act before the local geometric packet is collapsed to \(\beta_p\).

## Required noncommutative order

The valid comparison order must retain the full translated Gaussian functions:
\[
(O,DV_L)
\longrightarrow
\text{label shift/dilation packet}
\longrightarrow
\text{theta synthesis}
\longrightarrow
\text{completion differential}
\longrightarrow
\text{polarized readout}.
\]

The invalid order is
\[
(O,DV_L)
\longrightarrow
\beta_p
\longrightarrow
\text{scalar completion}.
\]

Scalar pairing and theta completion do not commute.

## What operation can change the order

To bridge Gaussian-in-\(\log p\) decay to Euler scale, the constructor must alter the argument structure before evaluation. Candidate mechanisms include:

- summing translated/dilated Gaussian labels before taking the boundary value;
- Mellin transport converting additive translation into multiplicative spectral weight;
- Poisson/Tate sewing exchanging a spatial Gaussian tail with a reciprocal scale packet.

A finite scalar normalization or finite Jordan polynomial cannot do it.

## Quantitative hostile

Let \(\mathcal P_L\) be any fixed three-grade differential packet with coefficients bounded by \(e^{cL}\). At every finite cutoff one may still multiply its output by a fitted scalar to match Euler data. The required inverse calibration grows like
\[
e^{\pi L^2-O(L)},
\]
so completion realization fails.

## Claim boundary

This theorem does not construct the pre-scalar label-synthesis map or prove that it yields Euler half-density. It proves that the placement of that map is forced: it must precede scalar Stokes contraction.

## Revised frontier

The first missing comparison is now operator-valued:
\[
\mathsf T_L:
\operatorname{span}\{O,DW_L,DW_{2L}\}
\longrightarrow
\mathcal J_{\theta}^{(0,1,2)}.
\]

It must intertwine reciprocal character, dilation, and prime labels before any scalar Green pairing is formed. Only then can the three-grade theta packet be tested against the arithmetic endpoint coefficients.
