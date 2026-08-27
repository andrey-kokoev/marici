# RH unit-preserving completion has a relative Fredholm compiler

## Result

Preservation of the Schur–Evans comparison unit can be reduced to operator estimates when the relative comparison is represented by a Fredholm determinant

\[
u_X(z)=\det\bigl(I+K_X(z)\bigr).
\]

Three conditions provide the relevant compact-local compiler:

1. (K_X(z)) is trace class with uniformly bounded trace norm;
2. (I+K_X(z)) has a uniformly bounded inverse;
3. (K_X) converges locally uniformly in trace norm.

The first condition bounds the determinant above. Applied to the inverse relative operator, the second and first conditions bound its reciprocal. The third identifies a completed Fredholm determinant rather than only a bounded family of unrelated finite determinants.

## Two independent hostiles

Trace-class boundedness alone does not suffice. For a rank-one projection (P), let

\[
K_N=-\left(1-\frac1N\right)P.
\]

Then the trace norm stays below one, but

\[
\det(I+K_N)=\frac1N
\]

and the inverse norm grows like (N). The relative operator approaches the forbidden eigenvalue (-1).

Uniform invertibility alone also does not suffice. Let (K_N) have (N) eigenvalues equal to (-1/2). Then

\[
\left\|(I+K_N)^{-1}\right\|=2,
\qquad
\det(I+K_N)=2^{-N}.
\]

Here no individual mode approaches (-1), but unbounded trace-class mass kills the determinant collectively.

The two failure modes are therefore distinct:

- one mode becomes singular;
- infinitely many safe modes accumulate a vanishing determinant.

## Categorical meaning

The determinant functor preserves invertibility only on a restricted operator category. Its morphisms must carry both nuclear-size control and inverse control. Completion outside that subcategory forgets whether an infinite product remains a unit.

This is not the missing RH orientation law. It is a compiler for deciding whether a proposed source-derived Schur–Evans comparison survives completion. The arithmetic work remains to construct (K_X) without dividing by the completed scalar section.

## Source-local target

The admissible construction must obtain (K_X) from the difference between two independently built objects:

- the full reciprocal colligation and its determinant section;
- the endpoint Evans section with all typed boundary currents retained.

Defining (K_X) from the quotient (S_X/F_X) is forbidden because it assumes the divisor comparison being tested.

For the theta/Tate system, the immediate questions are:

1. Do the (k\ge3) currents form the trace-class part of (K_X)?
2. Do the (k=1), (k=2), seam, and archimedean currents supply a finite-rank or renormalized boundary block?
3. Is the resulting relative operator uniformly separated from (-1) on compact subsets of each open half-plane?
4. Does the relative operator converge in trace norm after the declared boundary renormalization?

A negative answer to either the trace-mass or inverse-control gate closes unit-preserving completion for this colligation.
