# Fourier--Tate reflection inverts the arithmetic anomaly torsor

## Local reciprocal transition

For a prime (p), write

\[
q=p^{-s},
\qquad
r=p^{s-1}.
\]

The local direct-to-dual Tate transition is

\[
\gamma_p(s)=\frac{1-q}{1-r}.
\]

Reciprocal reflection (s\mapsto1-s) exchanges (q) and (r). Therefore

\[
\gamma_p(1-s)=\gamma_p(s)^{-1}.
\]

This is an exact identity of invertible line transitions. It requires no
choice of logarithm.

## Grade-by-grade action

In a convergent local chart,

\[
\log\gamma_p(s)
=
\sum_{k\ge1}\frac{r^k-q^k}{k}.
\]

Define the valuation-grade coordinate

\[
c_{p,k}(s)=\frac{r^k-q^k}{k}.
\]

Then

\[
c_{p,k}(1-s)=-c_{p,k}(s)
\]

for every (k\ge1). In particular, primitive, square, and connected grades
all reverse together. They are not independent Fourier representations.

## Cutoff line system

For (X\subset Y), let

\[
U_{X,Y}(s)=\prod_{X<p\le Y}\gamma_p(s).
\]

The ordinary cutoff cocycle law is

\[
U_{Y,Z}(s)U_{X,Y}(s)=U_{X,Z}(s).
\]

Reflection gives

\[
U_{X,Y}(1-s)=U_{X,Y}(s)^{-1}.
\]

Because inversion reverses compositions and the transition group is
commutative, the reflected line system obeys the same triangle coherence.

At the affine-coordinate level,

\[
\Delta C_{k;X,Y}(1-s)
=
-\Delta C_{k;X,Y}(s).
\]

Thus Fourier--Tate acts canonically on the relative arithmetic observer
without choosing a global scalar anomaly coordinate.

## Real structure and the critical seam

Under the Real reciprocal involution (s\mapsto1-\overline s),

\[
\gamma_p(1-\overline s)
=
\overline{\gamma_p(s)}^{-1}.
\]

On the fixed locus (operatorname{Re}s=1/2), this becomes

\[
|\gamma_p(s)|=1.
\]

Hence the unitary seam property is exactly the fixed-point condition of the
line-valued Fourier action.

## Fourth-tower consequence

The finite-prime part of the relative observer naturality cell is now exact:

- line transitions invert;
- primitive and square affine coordinates reverse;
- the connected tail reverses grade by grade;
- cutoff triangles remain coherent.

No arithmetic naturality residual survives at this level.

The remaining residual must be sought where the arithmetic torsor attaches to
the additive Poisson four-channel incidence and the archimedean determinant
line. A discrepancy found only after scalar multiplication would be too late;
the attachment must be checked before forming the completed scalar section.

## Next gate

Construct the archimedean/polar line transition in the same relative category
and compare its Fourier action with the arithmetic inversion above. Then form
the mixed attachment cell between:

\[
(A_f(s),A_{\widehat f}(1-s),\widehat f(0)/(s-1),-f(0)/s)
\]

and the arithmetic anomaly line.

The RH-bearing residual, if present, can now live only in this mixed
attachment or in its completion descent—not in the isolated finite-prime
Fourier action.

## Falsifiers

The arithmetic closure fails if any finite cutoff violates inversion, any
valuation grade does not reverse, triangle coherence changes under
reflection, or a logarithm branch is required to define the line action.

