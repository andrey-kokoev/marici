# The physical marked-relative rank is 26, not 21

## Exact geometric census

At the frozen generic point \((X_1,X_2,X_3)=(2,3,4)\), the residue-chart
Cayley--Menger curve is

\[
K=4a^4+3a^2b^2-975a^2+9b^4-1800b^2+109440.
\]

Its projective closure is a smooth plane quartic, hence has genus three.  It
meets the line at infinity in four distinct points, so its affine Euler
characteristic is \(-8\).  The five marked affine lines have eight distinct
finite crossings (two pairs are parallel), hence their union has Euler
characteristic \(5-8=-3\).

The restrictions of \(K\) to the marked lines factor with respectively

\[
2,2,2,4,4
\]

distinct zeros.  None lies at a line--line crossing.  Thus the quartic meets
the line union in 14 distinct points and

\[
\chi\!\left(\mathbb A^2\setminus(K\cup L_1\cup\cdots\cup L_5)\right)
=1-\bigl((-8)+(-3)-14\bigr)=26.
\]

This reproduces the already known generic restriction rank 26 without a large
linear solve.

## Stabilization and correction

The product-pole reducer was extended from cutoff five to cutoff seven with
ambient degree 14.  Independently over

\[
\mathbf F_{32003},\quad\mathbf F_{32009},\quad\mathbf F_{65521},
\]

both the quotient dimension and the horizontal saturation of the literal
physical numerator are 26.  The observed sequence is therefore a truncation
approach to the geometric value (including the earlier values 21 and 25), not
a stable rank-21 coefficient object.

Accordingly, the earlier rank-21 language is superseded:

\[
\boxed{
\text{rank 21 = cutoff-five plateau},\qquad
\text{rank 26 = exact geometric and stabilized rank}.
}
\]

The characteristic-zero equivariant-horizontality result remains valid; its
correct target is the rank-26 marked-relative object.  No new carrier divisor
or \(\mathcal Q\)-support follows from this correction.
