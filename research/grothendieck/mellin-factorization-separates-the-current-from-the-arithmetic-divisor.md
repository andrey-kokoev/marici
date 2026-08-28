# Mellin Factorization Separates the Current from the Arithmetic Divisor

## Mellin transform of the frontier current

Let

\[
F(\rho)
=
\rho^2(2\pi\rho^2-3)e^{-\pi\rho^2}.
\]

For the initial convergence chamber, define

\[
\mathcal M F(s)
=
\int_0^\infty F(\rho)\rho^{s-1}\,d\rho.
\]

Gaussian integration gives

\[
\mathcal M F(s)
=
\pi^{-(s+2)/2}
\left[
\Gamma\left(\frac{s+4}{2}\right)
-
\frac32\Gamma\left(\frac{s+2}{2}\right)
\right].
\]

Using the gamma recurrence,

\[
\mathcal M F(s)
=
\frac{s-1}{2}
\pi^{-(s+2)/2}
\Gamma\left(\frac{s+2}{2}\right),
\]

and hence

\[
2\pi\mathcal M F(s)
=
\frac{s(s-1)}2
\pi^{-s/2}
\Gamma\left(\frac{s}{2}\right).
\]

## Lattice sampling factor

The completed source in multiplicative scale is

\[
2\pi t^{1/2}\sum_{n\geq1}F(nt).
\]

Taking its Mellin transform and changing variables \(\rho=nt\) gives

\[
2\pi
\sum_{n\geq1}n^{-s}
\mathcal M F(s).
\]

Therefore

\[
2\pi\zeta(s)\mathcal M F(s)
=
\frac{s(s-1)}2
\pi^{-s/2}
\Gamma\left(\frac{s}{2}\right)
\zeta(s)
=
\xi(s).
\]

The completed Riemann function is thus derived as the product of two typed
components:

\[
\xi(s)
=
\left(
2\pi\mathcal M F(s)
\right)
\zeta(s).
\]

## Divisor separation

The current factor

\[
2\pi\mathcal M F(s)
=
\frac{s(s-1)}2
\pi^{-s/2}
\Gamma\left(\frac{s}{2}\right)
\]

has no zeros in the open critical strip. Its explicit polynomial zeros are at
the boundary values \(s=0,1\), and the gamma factor has no zeros.

Consequently, every nontrivial zero of \(\xi\) arises from the arithmetic
sampling factor \(\zeta(s)\), while the Fourier-fixed boundary current supplies
the archimedean completion, boundary polynomial, and reciprocal covariance.

## Explanatory consequence

The source mechanism now divides cleanly:

- the exact Fourier-fixed current explains the completed local geometry;
- the integer sampling comb supplies the nontrivial divisor;
- Poisson sewing couples them and produces the functional equation.

This rules out a purely local-current proof of zero confinement. The current
contains no interior divisor to constrain. RH must follow, if this route
closes, from a conservation law governing the interaction between the current
and the arithmetic sampling comb.

## Zero-to-kernel interpretation

An interior zero is not disappearance of the current. It is vanishing of the
sampled multiplicative matrix coefficient after the nonvanishing current unit
has been factored out.

The source-derived impossible task is therefore sharper:

Construct an off-seam Mellin character annihilated by the integer-sampling
correspondence while remaining compatible with Fourier-fixed reciprocal
sewing.

## Falsifier

The typed factorization fails if the Mellin integral does not equal the
displayed gamma factor or if the scaling sum produces a Dirichlet factor other
than \(\zeta(s)\). Both are exact calculations in their common convergence
chamber before analytic continuation.
