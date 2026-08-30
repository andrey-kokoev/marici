# Even--odd first jet does not reject hostile divisors

## Question

Scalar theta completion forgets the sign of the antisymmetric boundary
coordinate.  The first natural lift is the parity pair \((K,K')\).  Does that
pair recover enough source provenance to reject reciprocal-even hostile
factors?

## Hostile scalar modification

Write

\[
a(z)=z^2-\frac14
\]

and

\[
\Xi(z)=\frac12+\frac12a(z)K(z).
\]

Let \(H\) be any even entire function, real on the real axis, satisfying

\[
H\left(\frac12\right)
=
H\left(-\frac12\right)
=
1.
\]

Define the hostile scalar

\[
\Xi_H(z)=H(z)\Xi(z).
\]

It retains the same reciprocal symmetry and the same neutral half carrier.
Solving for its tail gives

\[
K_H(z)
=
H(z)K(z)+\frac{H(z)-1}{a(z)}.
\]

Because \(H-1\) vanishes at both zeros of \(a\), the quotient is entire.
It is also even.  Therefore

\[
K_H(-z)=K_H(z),
\qquad
K_H'(-z)=-K_H'(z).
\]

The hostile scalar automatically acquires the same even--odd first-jet
typing.

## Explicit off-seam family

Choose real \(\alpha,\beta>0\) with

\[
P\left(\frac12\right)\ne0,
\]

where

\[
P(z)
=
\left((z-\alpha)^2+\beta^2\right)
\left((z+\alpha)^2+\beta^2\right).
\]

Then

\[
H(z)=\frac{P(z)}{P(1/2)}
\]

is even, real, normalized at both boundary points, and inserts the off-seam
quartet

\[
z=\pm\alpha\pm i\beta.
\]

Nevertheless \((K_H,K_H')\) satisfies the same parity transformation as the
theta pair.  Thus parity covariance and one tangent channel do not protect the
divisor.

## What additional structure the theta source has

The actual theta tail is a bilateral Laplace transform of a positive symmetric
measure.  Equivalently, its cosh representation implies exponential
convexity.  For real points \(x_1,\ldots,x_m\),

\[
\left[K(x_i+x_j)\right]_{i,j=1}^m
\]

is positive semidefinite.  Its derivative jets therefore satisfy the
associated Hankel positivity conditions.

A generic hostile \(K_H\) need not retain this positive-measure lift.  This
gives a finite falsifier: find a real point packet whose exponential-convexity
matrix has a negative eigenvalue.

But positive-measure representability alone is not yet sufficient for RH.
Earlier hostile positive-source constructions show that an oscillatory
transform may still have the wrong orientation.  The source lift must retain
the labelled modular correspondences, not only the aggregated measure.

## Corrected hierarchy

The information hierarchy is now explicit:

1. Scalar \(\Xi\): forgets boundary orientation.
2. Parity pair \((K,K')\): restores orientation typing but is functorial under
   hostile even multiplication.
3. Positive cosh-measure lift: restores continuum source provenance but may
   still admit hostile sources.
4. Labelled modular lift: retains the arithmetic correspondences that remain
   the only plausible divisor-protection mechanism.

Each level is strictly stronger than the preceding scalar presentation, but
only the last remains a candidate for the RH-bearing conservation law.

## Next target

Construct the odd channel before label aggregation.  If

\[
K(z)=\sum_nK_n(z),
\]

retain the packet

\[
\left(K_n(z),K_n'(z)\right)_{n\ge1}
\]

together with its primal--dual sewing and exact modular tail.  The next
question is whether hostile multiplication has any lift to that labelled
packet which preserves the translate law and boundary incidence.

The immediate rejection criterion is source-level: failure to express
\(K_H\) as a sewn positive labelled packet with the authorized translate law.
No zero location may be used in that test.

## Result

The even--odd first jet restores the missing boundary orientation but does not
restore source authority.  Reciprocal-even hostile factors normalized at the
two completion points lift to the same parity pair automatically.  The next
faithful object must be the labelled positive modular packet.
