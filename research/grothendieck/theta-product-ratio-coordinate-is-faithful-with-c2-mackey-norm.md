# Product--ratio coordinate is faithful with a C2 Mackey norm

## Bounded question

Does adjoining the unsigned ratio magnitude repair the even blind channel of
the product correspondence without introducing fitted arithmetic data?

## Faithful quotient coordinate

For positive integers `(n,m)`, define

\[
 p=nm,
 \qquad
 \rho=|\log(m/n)|.
\]

Choose the representative with `m>=n`. Then

\[
 m/n=e^\rho
\]

and

\[
 \boxed{
 n=\sqrt{pe^{-\rho}},
 \qquad
 m=\sqrt{pe^\rho}.}
\]

Therefore `(p,rho)` determines the unordered integer pair `{n,m}` uniquely.
No two distinct swap orbits collide.

The product--ratio map is thus faithful on the reciprocal-even quotient.

## Variable C2 fiber norm

Let

\[
 \pi:(n,m)\longmapsto(p,\rho)
\]

forget only the sign of the logarithmic ratio.  Its fibers have size

\[
 |\pi^{-1}(p,\rho)|
 =\begin{cases}
 2,&\rho>0,\\
 1,&\rho=0.
 \end{cases}
\]

Consequently

\[
 \boxed{
 \pi_!\pi^*
 =\begin{cases}
 2I,&\rho>0,\\
 I,&\rho=0.
 \end{cases}}
\]

This is the exact Mackey norm of the swap action, including the diagonal
stabilizer. A uniform factor of two would be wrong at `n=m`.

The normalized pullback

\[
 U=|\pi^{-1}|^{-1/2}\pi^*
\]

is an isometry from quotient coefficients to swap-even ordered-pair
coefficients. Its adjoint is the correspondingly normalized pushforward.

## Compatibility with hyperbolic transport

The hyperbolic center of packet 118 is exactly the signed ratio coordinate

\[
 c_{nm}=\log(m/n).
\]

Reciprocal swap reverses its sign, while continuous common-scale dilation
changes `q=pe^S` and leaves `rho` invariant.  Thus the faithful coordinates
separate the two operations:

\[
 \boxed{
 \begin{array}{c|c}
 p&\text{radial arithmetic scale sampled under }S\\
 \rho&\text{fixed hyperbolic center magnitude}\\
 \operatorname{sgn}c&\text{reciprocal }C_2\text{ sheet}
 \end{array}}
\]

No coordinate is inferred from the final scalar readout.

## Consequence

The even blind vector at product `6` disappears only because the quotient now
has two distinct points:

\[
 (6,\log6),
 \qquad
 (6,\log(3/2)).
\]

Their coefficients remain separately observable. Product aggregation may be
performed later, but it is no longer treated as a faithful source coordinate.

## Remaining gate

The arithmetic quotient problem is solved. The analytic sampling problem from
packet 128 remains: evaluation at radial points `q=pe^S` is not yet a unitary
matrix coefficient. The next construction must retain `(p,rho)` while turning
radial evaluation into a correspondence or reproducing-kernel overlap.

The falsifier is now properly typed: two distinct product--ratio ports whose
radial evaluation functionals become identified under the proposed analytic
completion. Such an identification would reintroduce the blind channel after
the finite arithmetic quotient has repaired it.
