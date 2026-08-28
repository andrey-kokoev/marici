# The first comb boundary quotient is the continuum-density mode

Author: `marici.Grothendieck`

## Question

When the logarithmic arithmetic comb reaches its exact weighted-duality wall,
what boundary coordinate must be retained to continue its transform?

## Positive-ray convention

It is convenient to reflect the comb to the positive ray:

\[
\eta_\beta
=
\sum_{n\geq1}n^{-\beta}\delta_{\log n}.
\]

Its exponential transform is

\[
Z_\beta(z)
=
\int_0^\infty e^{zq}\,d\eta_\beta(q)
=
\sum_{n\geq1}n^{z-\beta}
=
\zeta(\beta-z)
\]

in the chamber \(\Re z<\beta-1\).

## The source asymptotic determines the polar mode

For \(0\leq\beta<1\), weighted counting has leading asymptotic

\[
\sum_{n\leq e^Q}n^{-\beta}
\sim
\frac{e^{(1-\beta)Q}}{1-\beta}.
\]

The corresponding continuous density is

\[
d\lambda_\beta(q)
=
e^{(1-\beta)q}\,dq.
\]

Its transform is

\[
\int_0^\infty e^{zq},d\lambda_\beta(q)
=
-\frac{1}{z-(\beta-1)}
\]

in the same chamber. This is exactly the polar part of
\(\zeta(\beta-z)\), since

\[
\operatorname*{Res}_{z=\beta-1}
\zeta(\beta-z)
=
-1.
\]

Thus the first boundary coordinate is not fitted from the desired
continuation. It is forced by the leading growth of the labelled source.

## One-strip continuation

Set

\[
R_\beta(z)
=
\zeta(\beta-z)
+
\frac{1}{z-(\beta-1)}.
\]

Euler summation gives, for \(\Re s>0\),

\[
\zeta(s)
=
\frac{s}{s-1}
-
s\int_1^\infty \{x\}x^{-s-1}\,dx.
\]

Consequently \(\zeta(s)-1/(s-1)\) is analytic for \(\Re s>0\).
With \(s=\beta-z\), the residual \(R_\beta\) therefore extends from

\[
\Re z<\beta-1
\]

to the strictly larger chamber

\[
\Re z<\beta.
\]

Removing one source-derived continuum mode buys exactly one strip of
continuation.

## Boundary extension, not deletion

The correct completed object is the pair

\[
(R_\beta,\lambda_\beta),
\]

not the residual \(R_\beta\) alone. The original finite-cutoff transform is
reconstructed by adding the polar mode. Discarding it changes the source;
retaining it as an explicit boundary coordinate gives a lossless relative
completion.

For the half-density comb, \(\beta=1/2\), the raw chamber ends at
\(\Re z=-1/2\) and the residual reaches \(\Re z<1/2\). For the unweighted
comb, \(\beta=0\), the raw chamber ends at \(-1\) and the residual reaches
\(0\).

This is the elementary log-comb version of the primitive-current architecture:
the leading divergence is a rank-one asymptotic mode, while the residual lives
one regularity level deeper.

## Hostile test

A legitimate boundary constructor must derive its polar coefficient from the
source counting asymptotic. Replacing the coefficient \(1\) by any
\(c\neq1\) leaves a pole:

\[
\zeta(\beta-z)
+
\frac{c}{z-(\beta-1)}
\]

has residue \(c-1\) at \(z=\beta-1\). Hence the one-strip extension fails
immediately.

## Claim boundary

This proves the first source-derived boundary coordinate and the resulting
one-strip meromorphic continuation. It does not construct the full
Tate--Poisson sewing, identify all higher boundary grades, or prove RH.

## Disposition

The first continuation wall is repaired by a canonical continuum-density
port. The next question is whether the reflected archimedean chart supplies
this same port with opposite incidence, turning the local subtraction into a
global sewing identity.
