# Newman Heat Transports the Full Divisor Current Without Bulk Creation

## Source current

For a holomorphic Newman family \(H_\lambda(z)\), define its divisor current

\[
\mathcal D_\lambda
=\frac{1}{2\pi}\Delta_z\log|H_\lambda(z)|.
\]

By the Poincare--Lelong formula, this is the positive atomic current of zeros
with their multiplicities. It is constructed from the theta-derived entire
function and does not require a prior zero census.

The Newman family obeys

\[
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]

## Simple-zero transport law

Let \(z_j(\lambda)\) be a simple zero. Differentiating
\(H_\lambda(z_j(\lambda))=0\) gives

\[
z_j'(\lambda)
=\frac{H_\lambda''(z_j)}{H_\lambda'(z_j)}.
\]

Therefore, on every region where the divisor is simple and no zero crosses
the region boundary, the current obeys the weak continuity equation

\[
\frac{d}{d\lambda}
\langle\mathcal D_\lambda,\varphi\rangle
=
\sum_j
\nabla\varphi(z_j)\mathbin{\cdot}z_j'.
\]

Equivalently, divisor charge is advected by the source-derived zero velocity.
There is no bulk creation term.

## The only transition loci

The velocity becomes singular exactly when \(H'=0\) at a zero. That is the
cubic collision already identified. Across such a collision, multiplicity is
conserved although the support can change from two seam points to an off-seam
conjugate pair.

For a finite-degree polynomial family, total divisor charge is fixed and
cannot enter from infinity. Hence off-seam charge can arise only through a
multiple-zero collision on the seam.

For the entire Xi family, a second mechanism remains: zeros can cross the
boundary of every compact spectral window. After Aspect's correction, this is
not disappearance but incidence through the marked all-scale infinity germ.

Thus the exact mechanism trichotomy is:

1. smooth advection of simple divisor points;
2. cubic redistribution at the collision locus;
3. boundary incidence through spectral infinity.

There is no fourth bulk-production mechanism.

## Minimal exact model

The family

\[
H_\lambda(z)=z^2-2\lambda

\]

obeys the Newman equation. Its roots are real for \(\lambda>0\), collide at
zero, and become imaginary for \(\lambda<0\). Their velocity is exactly

\[
z'=\frac1z=\frac{H''}{H'}.
\]

The divisor mass remains two, its center remains zero, and its algebraic
second moment is \(4\lambda\). The collision changes support type without
creating charge.

## Revised RH attack

De Bruijn gives a heat time at which the complete divisor is seam-supported.
Transporting backward toward physical time zero, RH can fail only if:

1. a seam collision emits an off-seam pair at nonnegative heat time; or
2. off-seam divisor charge enters through the all-scale infinity germ.

The proof target is therefore no longer an unspecified positivity theorem. It
is a two-boundary exclusion theorem for a conserved source current:

> On the nonnegative Newman interval, the completed theta divisor current has
> neither outward cubic collision flux from the seam nor incoming off-seam
> incidence from infinity.

This formulation is still equivalent in difficulty to the missing support
theorem unless an independent theta current or orientation law controls those
two channels. Its value is explanatory and falsifiable: every failure has a
typed location and mechanism.

## Next source-specific gate

The universal continuity law does not orient collisions. The next calculation
must derive the collision crossing form from the theta source. At a double
zero \((\lambda_0,z_0)\), the local unfolding coefficient is determined by

\[
H_\lambda(z)
\simeq
\frac12H_{zz}(z_0)(z-z_0)^2
+H_\lambda(z_0)(\lambda-\lambda_0).
\]

Using \(H_\lambda=-H_{zz}\), the two coefficients are not independent. The
universal heat equation fixes their ratio and hence which side of the
collision is real-rooted. What remains source-specific is whether such a
double-zero state is reachable at nonnegative heat time and whether one can
arrive from infinity.

## Scope

The continuity equation and mechanism trichotomy are exact. They do not
exclude either permitted transition channel and therefore do not prove RH.

