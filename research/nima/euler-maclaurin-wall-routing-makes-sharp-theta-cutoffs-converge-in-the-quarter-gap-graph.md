# Euler--Maclaurin wall routing makes sharp theta cutoffs converge in the quarter-gap graph

## Renormalized moment

For \(r>-1\), define

\[
R_{r,N}(u)
=
S_{r,N}(u)-I_{r,N}(u)-E_{r,N}(u),
\]

where

\[
S_{r,N}(u)
=
e^{ru}\sum_{n=1}^{N}n^re^{-\pi n^2e^{2u}},
\]

\[
I_{r,N}(u)
=
e^{ru}\int_0^N x^re^{-\pi x^2e^{2u}}\,dx,
\]

and

\[
E_{r,N}(u)
=
\frac12N^re^{ru}e^{-\pi N^2e^{2u}}.
\]

The limiting relative moment is

\[
R_r(u)
=
S_{r,\infty}(u)-C_re^{-u}.
\]

## Error as a tail trapezoid remainder

The difference is exactly

\[
R_r-R_{r,N}
=
e^{ru}
\left[
\sum_{n>N}f_u(n)
-
\int_N^\infty f_u(x)\,dx
+
\frac12 f_u(N)
\right],
\]

with

\[
f_u(x)=x^re^{-\pi x^2e^{2u}},
\]

after the common prefactor is accounted for. This is the trapezoidal
Euler--Maclaurin remainder on the tail \([N,\infty)\).

## Two-scale estimate

Let

\[
z=Ne^u.
\]

There are two regimes.

For \(z\ge1\), the second-derivative Euler--Maclaurin bound gives

\[
\left|
\partial_u^m(R_r-R_{r,N})(u)
\right|
\le
C_{r,m}N^{-1}G_{r,m}(z),
\]

where \(G_{r,m}\) is square integrable against \(dz/z\).

For \(0<z\le1\), the fractional lower-end term controls the error:

\[
\left|
\partial_u^m(R_r-R_{r,N})(u)
\right|
\le
C_{r,m}N^{-r}z^r.
\]

Since \(du=dz/z\), both estimates are square integrable. Therefore

\[
\left\|
\partial_u^m(R_r-R_{r,N})
\right\|_{L^2}
\le
C_{r,m}
N^{-\min(r,1)}.
\]

## Four-grade rate

The smallest exponent in the prime packet is

\[
r_0=\frac12.
\]

Consequently, for the renormalized four-grade cutoff,

\[
\Psi_{p,N}^{\mathrm{ren}}
=
\Psi_{p,N}-W_{p,N}^{\mathrm{wall}},
\]

one obtains, for \(m=0,1,2\),

\[
\left\|
\partial_u^m
\left(
\Psi_{p,N}^{\mathrm{ren}}
-
\Psi_p^{\mathrm{rel}}
\right)
\right\|_{L^2}
\le
C_{p,m}N^{-1/2}.
\]

Here

\[
\Psi_p^{\mathrm{rel}}
=
\Psi_p-\rho_pe^{-u}.
\]

## Quarter-gap graph convergence

Because

\[
\mathcal C
=
D_u^2-\frac14,
\]

the \(m=0\) and \(m=2\) estimates imply

\[
\Psi_{p,N}^{\mathrm{ren}}
\longrightarrow
\Psi_p^{\mathrm{rel}}
\]

in the graph norm of \(\mathcal C\).

The bounded inverse then commutes with the renormalized completion limit:

\[
\mathcal C^{-1}\Psi_{p,N}^{\mathrm{ren}}
\longrightarrow
\mathcal C^{-1}\Psi_p^{\mathrm{rel}}
\]

in \(L^2\), with norm error at most

\[
4C_{p,0}N^{-1/2}.
\]

## What this closes

The following analytic chain is now controlled for every fixed prime packet:

\[
\text{sharp label cutoff}
\longrightarrow
\text{continuum wall plus endpoint half-cell}
\longrightarrow
\text{quarter-gap graph limit}
\longrightarrow
\mathcal C^{-1}.
\]

Thus sharp theta synthesis and the completion Green resolvent do compose,
provided the finite Euler--Maclaurin wall packet is retained.

## Remaining uniformity

The constants \(C_{p,m}\) depend polynomially on

\[
L=\log p
\]

through the four coefficients. Global prime assembly must combine these
bounds with the frozen Euler weights. The present theorem closes label
completion at each prime; it does not yet prove the prime-summed bound.

The labelwise covariant derivative also needs its own Euler--Maclaurin
naturality check because it changes the grade exponents before assembly.

## Hostile

Remove only the continuum integral and omit the endpoint half-cell. The
tail error has an order-one moving profile, so the sequence can converge
weakly and locally while failing strong quarter-gap graph convergence.
