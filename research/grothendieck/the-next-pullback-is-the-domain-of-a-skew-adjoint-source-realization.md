# The next pullback is the domain of a skew-adjoint source realization

## Question

After identifying the critical seam as the fixed locus of

\[
R(z)=-\overline z,
\]

what additional categorical pullback could actually force a scalar zero onto
that seam?

## Exact finite theorem

Let (D) be a densely defined skew-adjoint operator on a complex Hilbert
space. If a nonzero vector (psi) in its domain satisfies

\[
D\psi=z\psi,
\]

then (z) lies on the seam:

\[
\operatorname{Re}z=0.
\]

Indeed,

\[
z\lVert\psi\rVert^2
=\langle D\psi,\psi\rangle
=-\langle\psi,D\psi\rangle
=-\overline z\lVert\psi\rVert^2.
\]

The same calculation works for a formally skew operator on a boundary domain
when its full Green boundary form vanishes. Thus the seam conclusion is not a
positivity conjecture. Once the state is correctly typed, it is an exact
conservation law.

## The new pullback

Let (Z_0) be the scalar-null pullback and let (mathcal E_D) be the spectral
incidence object

\[
\mathcal E_D
=\{(z,\psi):\psi\ne0,\ \psi\in\operatorname{Dom}D,
\ D\psi=z\psi\}.
\]

The required construction is now the lift

\[
Z_0\longrightarrow\mathcal E_D.
\]

Projection of (mathcal E_D) to parameter space already lands in
(operatorname{Fix}(R)). Consequently RH would follow from two independent
source theorems:

1. the completed theta/Tate constructors produce a canonical skew-adjoint
   realization (D), including the seam and boundary-current channels;
2. every scalar zero produces a nonzero admissible eigenstate of that same
   realization.

This is the missing fifth wall. The previous four-rung comparison tower
detects the seam exactly, but does not lift scalar nullity into an admissible
state. The fifth wall is not another scalar observation. It is domain
incidence.

## Why the distinction matters

For an arbitrary scalar function (X), the equation (X(z)=0) can hold at
any chosen off-seam point. Real symmetry of (X), an invertible Tate
transition, and a seam detector do not prevent this. Only a source-derived
lift of the zero into (mathcal E_D) activates the skew-adjoint conservation
law.

Conversely, manufacturing (D) from the zeros of (X) would be circular.
The operator, its domain, its Green form, and its boundary currents must be
defined before inspecting the divisor. A hostile symmetric multiplier must
fail to create an admissible eigenstate unless it also changes this source
operator or its domain.

## Falsifier

The route fails at the first source truncation for which either:

- the derived realization has a nonzero symmetric part after all typed
  boundary currents are included;
- a scalar zero has no nonzero state in the declared domain;
- a hostile divisor-bearing factor creates a state without changing the
  source data;
- the finite-cutoff Green-isotropic domains do not survive completion.

The accompanying checker separates the two facts: scalar nullity alone has no
location force, while spectral incidence for a skew-adjoint operator confines
the parameter exactly to the Real fixed seam.

