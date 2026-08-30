# Complete Positive Prime Sieving Still Allows an Off-Seam Primitive Zero

## Arithmetic completion of an arbitrary primitive seed

Let \(g(u)>0\) be any sufficiently decaying primitive source and define

\[
\Psi(u)=\sum_{n\ge1}n^{-1/2}g(u+\log n).
\]

This source has exactly the same integer-label grammar as the theta sum. For
every prime \(p\),

\[
D_p\Psi
=
\left(I-p^{-1/2}T_{\log p}\right)\Psi
=
\sum_{p\nmid n}n^{-1/2}g(u+\log n)>0.
\]

All finite products of the \(D_p\) are positive and their exhaustion isolates
\(g\). Thus complete positive prime sieving does not determine the primitive
cell.

## Closed-form hostile primitive

Choose

\[
g=\phi_2+\phi_1,
\]

where \(\phi_a\) is the normalized Gaussian whose Fourier transform is
\(e^{-az^2}\). Then

\[
\widehat g(z)=e^{-2z^2}+e^{-z^2}.
\]

Take

\[
z_0=\sqrt\pi\,e^{-i\pi/4}.
\]

Since \(z_0^2=-i\pi\), one has \(\widehat g(z_0)=0\). Moreover,

\[
\operatorname{Im}z_0=-\sqrt{\pi/2}<-rac12.
\]

Therefore

\[
s_0=\frac12+iz_0
\]

lies in the absolute Euler chamber \(\operatorname{Re}s_0>1\).

## Transform factorization

Absolute convergence permits termwise transformation at \(z_0\):

\[
\widehat\Psi(z)
=
\widehat g(z)
\sum_{n\ge1}n^{-1/2-iz}
=
\widehat g(z)\zeta\left(\frac12+iz\right).
\]

The zeta factor is finite and nonzero for \(\operatorname{Re}s>1\). Hence

\[
\widehat\Psi(z_0)=0.
\]

This zero is off the imaginary seam because \(\operatorname{Re}z_0\ne0\).

## What the hostile preserves and omits

The source preserves:

- positivity;
- every integer label and its exact weight;
- the complete commuting positive prime-sieve hierarchy;
- absolute Euler factorization at the hostile zero.

It omits the completed reciprocal Poisson sewing that relates the two scale
tails and fixes the primitive theta cell.

## Consequence

Positive prime sieving has no zero-orientation force by itself. Its genuine
role is arithmetic provenance: it resolves the source into primitive-label
strata. The RH-bearing mechanism, if present, must couple that sieve tower to
the reciprocal archimedean sewing and moving endpoint.

## Next falsifier

The next hostile target must satisfy both the complete positive sieve and the
full reciprocal Poisson boundary law. If such a source retains off-seam zeros,
the current arithmetic-sewing programme closes.
