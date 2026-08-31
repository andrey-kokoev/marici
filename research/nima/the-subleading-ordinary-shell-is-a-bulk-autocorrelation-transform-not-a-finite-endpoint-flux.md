# The subleading ordinary shell is a bulk autocorrelation transform, not a finite endpoint flux

## Question

Can maximal-isotropic endpoint sewing alone supply the subleading term required
by the prime-shell cancellation law?

## Claim boundary

The ordinary shell is exactly a Laplace transform of a shell autocorrelation
density. Endpoint sewing controls finite boundary traces, whereas this term
retains an integral over the shell interior. Therefore endpoint flux does not
supply it without an additional source identity identifying that bulk density
with a response or linking port. This is a typing separation, not a universal
claim that no nonlocal response constructor can exist.

## Ordinary analytic shell

For \(a<b\), the positive-end Evans history is

\[
 u_z(x)=-\int_x^\infty e^{-z(r-x)}\Phi(r)\,dr.
\]

The analytic-transpose ordinary shell is

\[
 I_{a,b}^{(0)}(z)
 =\int_a^b\Phi(x)u_z(x)\,dx.
\]

Substitution and Fubini give

\[
 I_{a,b}^{(0)}(z)
 =-\int_a^b\int_x^\infty
 \Phi(x)\Phi(r)e^{-z(r-x)}\,dr\,dx.
\]

Set \(t=r-x\). Then

\[
 I_{a,b}^{(0)}(z)
 =-\int_0^\infty e^{-zt}\rho_{a,b}(t)\,dt,
\]

where

\[
 \rho_{a,b}(t)
 =\int_a^b\Phi(x)\Phi(x+t)\,dx.
\]

Thus the ordinary shell is the Laplace transform of a positive shell
cross-correlation density.

## Endpoint lane

A finite endpoint response built from \(u_z(a)\), \(u_z(b)\), and finitely many
parameter derivatives has Laplace densities in the finite span of

\[
 t^k\Phi(a+t),
 \qquad
 t^k\Phi(b+t),
 \qquad 0\le k\le N,
\]

multiplied by source endpoint coefficients.

By contrast, \(\rho_{a,b}\) integrates \(\Phi(x)\Phi(x+t)\) over every
\(x\in[a,b]\). Equality of its transform with a finite endpoint law requires
the explicit density identity

\[
 \rho_{a,b}(t)
 =\sum_{k=0}^N
 \left(
 A_k(a,b)t^k\Phi(a+t)
 +B_k(a,b)t^k\Phi(b+t)
 \right)
\]

in the relevant distribution or test topology. No such identity follows from
maximal isotropy.

## Injectivity of the transform

On any right half-plane where these rapidly decaying densities are integrable,
Laplace transform is injective. Therefore equality of the shell functions for
all \(z\) in an open set forces equality of the underlying densities.

Matching only one Xi zero, or finitely many jets there, does not establish the
global density identity. Conversely, an actual source density identity would
supply all parameter jets at once.

## Candidate-one consequence

The leading endpoint flux may be cancelled by the reciprocal boundary graph.
The remaining ordinary term requires one of:

1. a nonlocal reciprocal response whose density contains
   \(\rho_{a,b}\);
2. an ordered linking port derived from the same shell autocorrelation;
3. a modified Evans history whose lower residual changes by a
   divisor-preserving chain comparison.

A finite endpoint phase or wall coefficient cannot be assumed to contain this
bulk autocorrelation.

## Relation to the two-term asymptotic

The endpoint asymptotic determines the leading
\(\Phi(a)^2/\Lambda(a)^{j+1}\) hierarchy. The autocorrelation transform supplies
the smaller
\(\Phi(a)^2/(2\Lambda(a)^{j+2})\) hierarchy. Their different origins explain
why maximal-isotropic flux cancellation can close the first coefficient while
leaving the second.

## Cheapest exact test

For a proposed reciprocal/linking response:

1. express its shell contribution as a Laplace transform;
2. extract its source density;
3. subtract the endpoint density required by flux cancellation;
4. compare the remainder with \(-\rho_{a,b}\).

One nonzero density residual rejects exact shell divisibility on an open
parameter set. No Xi-zero fitting is required.

## Disposition

The unresolved subleading shell is a bulk autocorrelation object. Candidate one
cannot be completed by endpoint sewing alone; it needs a source-derived nonlocal
response/linking density or a new divisor-preserving history. No such density
identity is currently established. No RH conclusion is authorized.
