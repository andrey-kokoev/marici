# Theta conjugate-doubled shear is indefinitely conservative everywhere

## Universal alternating conservation

Let

\[
 S(F)=\begin{pmatrix}1&F\\0&1\end{pmatrix},
 \qquad
 \Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Every two-dimensional determinant-one matrix preserves the alternating form.
In particular,

\[
 S(F)^T\Omega S(F)=\Omega
\]

for every complex (F). This is algebraic orientation conservation, not a
positive energy law.

## No fixed Hermitian metric for one generic shear family

Suppose a Hermitian matrix

\[
 K=\begin{pmatrix}a&b\\\overline b&d\end{pmatrix}
\]

satisfies

\[
 S(F)^*KS(F)=K
\]

for a family of (F)'s spanning two real directions in the complex plane.
The upper-right entry forces

\[
 aF=0,
\]

so (a=0). The lower-right entry then forces

\[
 \overline F b+\overline bF=0
\]

in two independent directions, hence (b=0). The resulting (K) is
degenerate. Thus one generic complex shear family has no fixed nondegenerate
Hermitian conservative metric.

## Conjugate doubling restores an indefinite metric

Define

\[
 D(F)=\operatorname{diag}\bigl(S(F),S(\overline F)\bigr)
\]

and

\[
 H=\begin{pmatrix}0&\Omega\\-\Omega&0\end{pmatrix}.
\]

The matrix (H) is Hermitian and nondegenerate. Since

\[
 S(F)^*=S(\overline F)^T,
\]

the alternating identity gives

\[
 D(F)^*HD(F)=H
\]

for every complex (F).

Therefore conjugate doubling supplies a fixed indefinite Hermitian
conservation law everywhere in the spectral plane. It is not seam-selective
and survives hostile sources with off-seam zeros.

## Why this does not orient transmission zeros

The form (H) has isotropic directions and carries no positive lower bound.
At (F=0), the doubled transport is the identity, but its conserved
indefinite value can vanish on nonzero states. Consequently neither
conservation, nondegeneracy, nor doubled invertibility forbids a silent scalar
channel.

This separates three structures:

- alternating conservation follows from determinant one;
- indefinite Hermitian conservation follows from conjugate doubling; and
- positive reciprocal tail--seam energy is seam-selective through the cosh
  law.

Only the third distinguishes the critical seam, while only the first two are
currently coupled directly to the completed shear.

## Surviving theorem

The RH-bearing statement must couple the everywhere-conservative doubled
shear to the seam-selective positive energy through source-derived
reachability and observability maps. A suitable identity would have to prove
that a silent transmission channel produces a nonzero state visible to the
positive reciprocal energy, while the boundary currents force that state to
remain bounded.

Kitaev's completion examples show why cutoffwise minimality is insufficient.
The coupling must survive completion with uniform source-derived control; a
weak mode may otherwise become simultaneously unreachable and unobservable.

## Falsifier

Any proposed proof based only on a symplectic, determinant-one, or indefinite
Hermitian conservation law is falsified by the identities above, since they
hold for arbitrary complex (F). A positive coupling fails if its
reachability or observability constant tends to zero along cutoff growth, or
if its metric is chosen after inspecting the desired zero locus.

## Scope

This proves an everywhere-valid doubled conservation law and closes it as an
RH orientation mechanism. It does not construct the missing positive
reachability-observability coupling or prove RH.
