# The Moving-Seam Prefix Current Gives a Canonical Mixed-Prime Difference Cocycle

## Common source coordinate

The moving-seam current \(\mathcal K_L(z)\) is defined by the completed theta
source for every admissible real cut \(L\), before any cut is labelled by a
prime power. Prime-power points therefore mark positions in one common source
coordinate; they do not carry separate values of the current.

For two marked cuts \(a,b\), define the oriented overlap cell

\[
C_z(a,b)=\mathcal K_b(z)-\mathcal K_a(z).
\]

This definition uses the source prefix current itself, not interpolation
weights fitted to the Green residual.

## Exact cocycle laws

The overlap cells satisfy

\[
C_z(a,a)=0,
\qquad
C_z(b,a)=-C_z(a,b),
\]

and, for every three cuts,

\[
C_z(a,b)+C_z(b,c)=C_z(a,c).
\]

Consequently every closed cycle has zero total increment. The result is
independent of which primes or prime powers supplied the endpoint labels.

## Refinement invariance

Let

\[
0=L_0<L_1<\cdots<L_N=R
\]

be any finite common refinement of prime-power boundaries. Then

\[
\sum_{j=0}^{N-1}C_z(L_j,L_{j+1})
=\mathcal K_R(z)-\mathcal K_0(z).
\]

Inserting or deleting intermediate marked cuts leaves the total unchanged.
Thus all prime charts glue through one refinement without additive
overcounting and without a higher Čech anomaly.

## Relation to the local Green forcing

Because

\[
\partial_L\mathcal K_L(z)
=\Phi(L)\bigl(H_+(L,z)-H_-(L,z)\bigr),
\]

each overlap cell is the exact integrated relative response over its interval:

\[
C_z(a,b)
=\int_a^b
\Phi(L)\bigl(H_+(L,z)-H_-(L,z)\bigr)\,dL.
\]

Mixed-prime cells therefore require no new local density. They are restrictions
of the same source-derived ternary current.

## What has and has not closed

This closes the chart-gluing and continuous-sampling problem for the moving-
seam forcing current, provided all marked cuts are compared in the common
archimedean theta frame. A demand that each prime chart reconstruct the overlap
using prime-local data alone would reintroduce an artificial obstruction: the
overlap is relational data between charts.

The theorem does not yet identify the arithmetic primitive and prime-square
boundary grades with this current, nor prove that a completed scalar zero makes
the total Green endpoint flux vanish. Those remain separate typed gates.

## Source-authority boundary

The cocycle is authorized by the completed theta prefix current. It is not a
theorem that an Euler product without its archimedean source can construct the
same comparison. The correct derivational direction is

```text
completed theta source -> common prefix current -> prime-marked overlap cells
```

and not independent prime currents followed by a fitted reconciliation.

