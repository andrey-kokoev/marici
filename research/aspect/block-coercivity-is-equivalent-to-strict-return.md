# Block coercivity is equivalent to strict return

## Question

What source inequality on the complete coupled physical form is exactly equivalent to a strict Green-return margin?

## Normalized block

On source-derived reduced supports, define

\[
T=A^{-1/2}CD^{-1/2},
\qquad
B=
\begin{pmatrix}
I&T\\
T^*&I
\end{pmatrix}.
\]

The normalized Green return is \(K=TT^*\). The spectrum of \(B\) consists of \(1\pm s_j(T)\), so

\[
B\ge\eta I
\quad\Longleftrightarrow\quad
\|T\|\le1-\eta.
\]

Consequently

\[
\|K\|\le(1-\eta)^2
\]

and the return margin obeys the exact relation

\[
1-\|K\|\ge 2\eta-\eta^2.
\]

Conversely, a return margin \(1-\|K\|\ge\delta\) yields block coercivity

\[
\eta\ge1-\sqrt{1-\delta}.
\]

Thus uniform strict return is equivalent to uniform coercivity of the fully normalized coupled block, not merely positivity of its diagonal sectors.

## Determinant consequence

In rank \(r\), every singular value satisfies \(s_j(T)\le1-\eta\), hence

\[
\det(I-K)
=
\prod_{j=1}^r(1-s_j(T)^2)
\ge
[\eta(2-\eta)]^r.
\]

For the primitive-square plane, \(r=2\). This derives the Fredholm determinant bound from one coercivity estimate and simultaneously supplies the trace gate.

## Terminal boundary

A unit singular value of \(T\) gives a null vector of \(B\), zero block coercivity, and eigenvalue one of \(K\). This is exactly terminal scalar cancellation. Positivity \(B\ge0\) permits this boundary; strict confinement needs a source-uniform positive coercivity constant.

## Source formulation

Because

\[
B=
\operatorname{diag}(A^{-1/2},D^{-1/2})
G
\operatorname{diag}(A^{-1/2},D^{-1/2}),
\]

the required theorem can be stated without a Green constructor: prove

\[
G\ge\eta\,\operatorname{diag}(A,D)
\]

on the physical reduced support, uniformly over primes. This is a relative coercivity estimate for the complete wall–history–tail/PV form. Diagonal positivity of \(A,D\) alone does not imply it.

## Verification

`research/aspect/checkers/check_block_coercivity_return.py` checks the exact margin identity, determinant lower bound, and terminal unit-singular-value boundary with rational singular values.

## Disposition

The highest-value physical target is now one relative block inequality. If the source constructor proves it, scalar-null confinement follows with an explicit margin. If it supplies only semidefinite positivity, terminal cancellation remains admissible.
