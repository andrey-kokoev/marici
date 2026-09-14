# The finite Euler modification has an explicit almost-periodic Fourier expansion whose nonzero modes are suppressed in high gamma moments

## Relative semilocal weight

For a finite prime set `S`, the semilocal cyclic measure is

\[
dm_S(t)
=w_S(t)dm_\infty(t),
\]

where

\[
w_S(t)
=
\prod_{p\in S}
|L_p(1/2-it)|^2
=
\prod_{p\in S}
\frac1{|1-p^{-1/2+it}|^2}.
\]

Each factor is positive, bounded above and below on the real line, and periodic with period `2pi/log p`.

## Exact Poisson expansion

Put `r_p=p^(-1/2)`. The Poisson identity gives

\[
|L_p(1/2-it)|^2
=
\frac1{1-r_p^2}
P_{r_p}(t\log p)
\]

and hence

\[
\boxed{
|L_p(1/2-it)|^2
=
\frac1{1-p^{-1}}
\sum_{k\in\mathbb Z}
p^{-|k|/2}
e^{ikt\log p}.
}
\]

Therefore

\[
\boxed{
w_S(t)
=
C_S
\sum_{\mathbf k\in\mathbb Z^S}
\left(
\prod_{p\in S}p^{-|k_p|/2}
\right)
 e^{it\omega_{\mathbf k}},
}
\]

where

\[
C_S=
\prod_{p\in S}(1-p^{-1})^{-1},
\]

\[
\omega_{\mathbf k}
=
\sum_{p\in S}k_p\log p
=
\log
\left(
\prod_{p\in S}p^{k_p}
\right).
\]

Unique factorization implies

\[
\omega_{\mathbf k}=0
\quad\Longleftrightarrow\quad
\mathbf k=0.
\]

Thus the constant Fourier coefficient is isolated algebraically, although nonzero frequencies can approach zero for multi-prime integer combinations.

## Gamma moment transform

Let the archimedean density be

\[
dm_\infty(t)=\rho_\infty(t)dt.
\]

Its gamma factor has exponential decay

\[
\rho_\infty(t)
=
O
\left(
(1+|t|)^a
e^{-b|t|}
\right)
\]

for a positive constant `b` fixed by normalization.

Define its Fourier transform

\[
\Phi_\infty(x)
=
\int_\mathbb R
e^{itx}dm_\infty(t).
\]

The perturbed moments satisfy

\[
\mu_n(S)
=
\int t^n w_S(t)dm_\infty(t)
=
C_S
\sum_{\mathbf k}
c_{\mathbf k}
 i^{-n}
\Phi_\infty^{(n)}
(\omega_{\mathbf k}),
\]

where

\[
c_{\mathbf k}
=
\prod_{p\in S}p^{-|k_p|/2}.
\]

The zero-frequency term is

\[
C_Si^{-n}
\Phi_\infty^{(n)}(0)
=
C_S\mu_n(\infty).
\]

All arithmetic deformation is carried by derivatives of the gamma Fourier transform at nonzero logarithmic frequencies.

## One-prime suppression

For `S={p}`, every nonzero frequency satisfies

\[
|\omega_k|

\ge
\log p.
\]

For model two-sided exponential density `e^(-b|t|)`, the even moments obey

\[
\int t^{2n}e^{-b|t|}e^{i\omega t}dt
=
2(2n)!\operatorname{Re}
(b-i\omega)^{-(2n+1)}.
\]

Relative to the zero mode, its magnitude is bounded by

\[
\left(
\frac{b}{\sqrt{b^2+\omega^2}}
\right)^{2n+1}.
\]

Thus every fixed nonzero prime frequency is exponentially suppressed in high moments. The true gamma density has the same qualitative analytic-strip mechanism, with polynomial prefactors.

This strongly suggests exponentially decaying moment deformation for one prime.

## Several primes and small frequencies

For several primes, quantities

\[
\omega_{\mathbf k}
=
\log(a/b)
\]

with `a,b` supported on `S` can approach zero. However their Fourier coefficients satisfy

\[
|c_{\mathbf k}|
=
\exp
\left(
-\frac12
\sum_p|k_p|\log p
\right).
\]

Small logarithmic frequencies require large integer vectors. Quantitative lower bounds for nonzero linear forms in logarithms of algebraic numbers give inequalities of the schematic form

\[
|\omega_{\mathbf k}|
\ge
C_S(1+\|\mathbf k\|)^{-A_S}.
\]

Combining this with exponential coefficient decay suggests a stretched-exponential upper bound after optimizing frequency size against coefficient size:

\[
|\mu_n(S)-C_S\mu_n(\infty)|
\lesssim
\exp(-c_S n^{\alpha_S})
\times
\text{archimedean moment scale}
\]

for some `alpha_S>0`.

This estimate has not been proved here; it identifies the required analytic-number-theory input.

## From moments to Jacobi coefficients

Let

\[
a_n(S),

b_n(S)
\]

be the recurrence coefficients of the orthonormal polynomials for `dm_S`. The transported degree curvature

\[
\widetilde N_S-N_\infty
\]

is controlled not directly by individual moments but by the change-of-basis matrix between the two orthogonal-polynomial systems.

Moment convergence alone is insufficient because Hankel determinants and Gram--Schmidt can be ill-conditioned at high degree. To deduce trace-ideal behavior one needs uniform bounds on the inverse moment Gram matrices or a Riemann--Hilbert/strong-asymptotic theorem for the exponentially decaying weight multiplied by `w_S`.

The desired estimate is of the form

\[
|a_n(S)-a_n(\infty)|
+
|b_n(S)-b_n(\infty)|
\le
C_S e^{-c_Sn^{\alpha_S}}.
\]

Such an estimate would imply summability of the Jacobi coefficient differences and make the Jacobi perturbation trace class.

## Important distinction: Jacobi versus degree curvature

A trace-class difference of Jacobi matrices

\[
\mathcal J_S-\mathcal J_\infty
\in
\mathcal L^1
\]

would provide scattering theory for the scaling Jacobi operators. The exact Euler scattering phase is already known there.

The prolate perturbation involves

\[
\widetilde N_S-N_\infty,
\]

which is the degree operator transported by the scaling intertwiner. Trace-class recurrence-coefficient differences do not automatically imply that this unbounded degree curvature is trace class. One still needs weighted off-diagonal decay of the connection matrix between polynomial bases.

Thus two estimates are required:

1. trace-ideal control of the Jacobi recurrence perturbation;
2. relative trace-ideal control of the transported number operator.

## Candidate connection matrix

Let

\[
C_S=(c_{mn}^{(S)}),
\qquad
c_{mn}^{(S)}
=
\langle
P_m^S,
\Omega_S^-P_n^\infty
\rangle_{H_S}.
\]

Then `C_S` is unitary and

\[
\widetilde N_S
=C_S^*NC_S.
\]

Therefore

\[
\boxed{
\widetilde N_S-N
=C_S^*[N,C_S].
}
\]

The relative prolate bridge reduces to decay of the off-diagonal matrix entries:

\[
[N,C_S]_{mn}
=(m-n)c_{mn}^{(S)}.
\]

A sufficient condition for trace class is

\[
\sum_{m,n}
|m-n||c_{mn}^{(S)}|
<
\infty,
\]

which is strong but concrete. Relative Schatten conditions allow weaker weighted sums.

## Source data still missing

The 2023 paper states that the coefficients of the general semilocal Jacobi matrix are deferred to future work. It proves Hilbertian stability of Sonin spaces but gives no asymptotic estimate for

\[
c_{mn}^{(S)},
\qquad
a_n(S)-a_n(\infty),
\qquad
b_n(S)-b_n(\infty).
\]

Therefore the trace-ideal bridge cannot be concluded from the cited theorem alone.

## Disposition

The finite Euler modification has a highly structured Fourier expansion with exponentially decaying arithmetic coefficients. Nonzero frequencies are suppressed by the analytic gamma moment transform, exponentially for one prime and plausibly stretched-exponentially for every fixed finite set of primes.

This provides a concrete route to the missing relative perturbation theorem. The decisive next result is a stable orthogonal-polynomial asymptotic converting Fourier/moment suppression into weighted off-diagonal decay of the connection matrix `C_S`, sufficient to control

\[
C_S^*[N,C_S]
(W_{\lambda,\infty}-i)^{-m}.
\]
