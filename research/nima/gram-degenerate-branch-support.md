# Gram Degeneracy Changes the Branch-Support Mechanism

The adjugate formulas for fourfold and fivefold Kummer-branch support were
derived only on the chart \(\det G\ne0\). On \(\det G=0\), clearing the
denominator is not enough: the geometric problem changes type.

Translate one external point to the origin and put the remaining relative
vectors into the rows of \(A\). Their common branch equations are

\[
A\ell=\frac12d,
\qquad
\ell^2=0,
\qquad
d_i=v_i^2.
\]

This gives the intrinsic rank-aware test:

1. the affine circumcenter locus exists iff
   \(\operatorname{rank}A=\operatorname{rank}[A\mid d]\);
2. if it exists, restrict \(\ell^2\) to that affine locus;
3. the common branch support is the zero locus of that restricted quadratic.

For rank three this recovers the earlier unique-center discriminant. For a
generic consistent rank-two degeneration, however, the affine locus is a
line and its restricted quadratic has two roots over the complex numbers.
Thus the Gram divisor is not merely an exceptional chart on which the old
numerator should be continued: it can itself support fourfold branching by a
different mechanism.

The exact control

\[
a=(1,0,0),\quad b=(0,1,0),\quad c=(1,1,0)
\]

has affine locus

\[
\ell=(1/2,1/2,z),
\qquad
\ell^2=z^2+1/2,
\]

and hence two complex fourfold branch points. Adding a transverse fifth point
\(p=(0,0,s)\) fixes \(z=s/2\); fivefold support then requires

\[
s^2+2=0.
\]

Rank loss alone is not sufficient. A distinct collinear control has

\[
\operatorname{rank}A=1,
\qquad
\operatorname{rank}[A\mid d]=2,
\]

so no affine circumcenter and no common branch locus exist.

Therefore the geometric realization of the formal Loewy tower has two typed
lanes:

- on \(\det G\ne0\), bordered-Gram/cosphericity discriminants constrain the
  unique center;
- on \(\det G=0\), rank consistency and the quadratic on the affine center
  locus determine support.

The formal Boolean deck algebra remains valid, but its degree-four and
degree-five monomials cannot be assigned geometric support from the cleared
adjugate numerators alone.

Artifacts:

- `research/nima/check_gram_degenerate_branch_support.py`
- `research/nima/results/gram-degenerate-branch-support.json`
