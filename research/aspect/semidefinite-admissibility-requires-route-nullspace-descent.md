# Semidefinite admissibility requires route-nullspace descent

## Question

What additional gate is required when the q_G12 admissibility form is semidefinite rather than positive definite?

## Unbounded cylinder

Let \(H\ge0\) define admissible displacements by

\[
w^*Hw\le1.
\]

Every vector in \(\ker H\) generates an unconstrained affine direction. For the route family

\[
b+Rw,
\]

a finite uniform bound exists only if

\[
\ker H\subseteq\ker R.
\]

Indeed, if \(v\in\ker H\) and \(Rv\ne0\), then every \(w+tv\) remains admissible while

\[
\|b+R(w+tv)\|
\]

grows without bound as \(|t|\) grows.

## Reduced S-lemma

If \(R\) kills \(\ker H\), the affine route descends to the quotient by that nullspace. The induced admissibility form is positive definite on its support, and the ordinary S-lemma block applies there. This order is mandatory:

1. identify the exact nullspace of \(H\);
2. prove \(R\) annihilates it;
3. form the reduced support;
4. certify the augmented block.

Using a pseudoinverse before the nullspace test silently discards route-visible directions.

## Exact model

Take

\[
H=\operatorname{diag}(1,0),
\qquad
b=\frac12.
\]

For route \(R=(1/4,0)\), the null direction is killed and the exact reduced maximum squared norm is \(9/16\). For route \(R=(0,1/10)\), the admissible sequence \((0,y)\) has unbounded route image and exceeds unit norm by \(y=20\).

## Relation to the current blocker

Nima reports that the current q_G12 branch lacks the complete physical target form, base route \(b_p\), omitted route \(R_p\), and common target pairing. Therefore neither the nullspace condition nor the augmented S-lemma block is currently formable. A local soft positive-cut normalization does not define these missing global objects.

## Verification

`research/aspect/checkers/check_semidefinite_affine_route.py` verifies the reduced finite bound and route-visible null growth with exact rational arithmetic.

## Disposition

The first physical object is not a multiplier or eigenvalue estimate. It is the complete common target pairing together with maps \(b_p\) and \(R_p\). Once those exist, the admissibility nullspace must be tested before any reduced-support confinement certificate.
