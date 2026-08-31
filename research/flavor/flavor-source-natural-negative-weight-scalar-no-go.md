# Source-natural negative-weight scalar no-go: WP1091

## Question

Can any source-natural scalar function of \(A,x\) supply the required
ray-phase weight \(-3\) for \(\rho\)?

## Regular-polynomial gate

Under ray scaling \(x\mapsto\zeta x\), the conditional Wilson operator \(A\)
is fixed. A regular polynomial in \(x\) of total degree \(d\) therefore has
weight \(d\). Since every regular polynomial degree is nonnegative, no nonzero
regular polynomial can have weight \(-3\).

## Bounded meromorphic scan

A meromorphic candidate with determinant denominator \(D^m\) has weight

\[
\deg(f)-3m.
\]

Requiring weight \(-3\) gives

\[
\deg(f)=3(m-1).
\]

For bounded denominator powers \(m=1,2,3,4\), the only degree pairs are
\((0,1),(3,2),(6,3),(9,4)\). With the only admitted positive-weight alternating
scalar \(D\), these reduce to

\[
\frac1D,\qquad \frac{D}{D^2}=\frac1D,\qquad
\frac{D^2}{D^3}=\frac1D,\qquad \frac{D^3}{D^4}=\frac1D.
\]

They therefore inherit the WP1090 failure: a tautological meromorphic inverse,
not an independent source-authorized section.

## Singularity witness

For spectrum \((2,3,5)\) and eigenline \(x=(1,0,0)\),

\[
D(x)=0.
\]

Every \(D\)-denominator reduction is singular there and cannot be a global
nonsingular reference over rays.

## Classification

Negative gate. No source-natural scalar of \(A,x\) supplies an independent
weight-\((-3)\) \(\rho\) in the stated authority class. The remaining gate is a
source-authorized line-bundle section or coorientation independent of \(D\),
with descent law, temporal scope, and comparison node.

Checker: `research/flavor/checkers/wp1091_source_natural_negative_weight_scalar_no_go.py`

Result: `results/wp1091_source_natural_negative_weight_scalar_no_go.json`
