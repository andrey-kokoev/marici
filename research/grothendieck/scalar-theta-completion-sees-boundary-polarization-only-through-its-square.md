# Scalar theta completion sees boundary polarization only through its square

## Question

The completed continuation boundary has symmetric coordinate \(1/2\) and
antisymmetric coordinate \(z=s-1/2\).  Does the scalar theta tail retain the
orientation of that antisymmetric coordinate?

## Cosh form of the reciprocal tail

Start from the entire reciprocal tail

\[
I(s)
=
\int_1^\infty
\psi(x)
\left(
x^{s/2}+x^{(1-s)/2}
\right)
\frac{dx}{x}.
\]

Put

\[
s=\frac12+z,
\qquad
x=e^{2u}.
\]

Then

\[
K(z)
:=
I\left(\frac12+z\right)
=
4\int_0^\infty
\psi(e^{2u})e^{u/2}\cosh(zu)\,du.
\]

Consequently,

\[
K(-z)=K(z).
\]

The completed scalar becomes

\[
\xi\left(\frac12+z\right)
=
\frac12
+\frac12
\left(z^2-\frac14\right)K(z).
\]

It depends on the antisymmetric boundary coordinate only through reciprocal
even combinations.

## Exact information loss

The two boundary orientations \(z\) and \(-z\) are distinct before scalar
aggregation, but

\[
\xi\left(\frac12+z\right)
=
\xi\left(\frac12-z\right).
\]

Thus the scalar readout cannot distinguish which reciprocal sector supplied
the state.  The half-planes are not merely mapped to one another by an
external symmetry; their orientation label has been erased by the scalar
compression.

This gives a precise version of the two-sectors-pretending-to-be-one
intuition:

- the boundary packet retains the sign of \(z\);
- the scalar theta completion retains only \(z^2\);
- a scalar zero is therefore a cancellation in the orientation-forgetting
  quotient.

## Canonical odd companion

The first source-derived channel that restores reciprocal orientation is the
derivative of the tail:

\[
K'(z)
=
4\int_0^\infty
u\psi(e^{2u})e^{u/2}\sinh(zu)\,du.
\]

It satisfies

\[
K'(-z)=-K'(z).
\]

On the critical seam,

\[
K'(it)
=
4i\int_0^\infty
u\psi(e^{2u})e^{u/2}\sin(tu)\,du,
\]

so the missing orientation channel becomes precisely an oscillatory tangent
readout.  This reconnects the completed-boundary calculation to the earlier
value--tangent collision and seam-matched score residual.

The smallest reciprocal representation is therefore not the scalar \(K\),
but the parity pair

\[
\mathcal K(z)=\left(K(z),K'(z)\right),
\]

with reflection acting by

\[
\mathcal K(-z)=\left(K(z),-K'(z)\right).
\]

## Collision condition in the lifted coordinates

A scalar zero satisfies

\[
1+\left(z^2-\frac14\right)K(z)=0.
\]

This equation constrains only the even channel.  It places no direct condition
on \(K'(z)\).  Therefore scalar vanishing need not mean disappearance of the
full reciprocal relationship.

The next hard theorem must show that an admissible off-seam scalar-null state
is incompatible with the odd channel and its source boundary conditions.  It
cannot be obtained from the scalar functional equation, because that equation
has already forgotten the relevant sign.

## Hostile boundary

Multiplying by a reciprocal-even hostile factor preserves the even scalar
architecture and can insert off-seam zero quartets.  Hence the parity lift is
useful only if the odd companion is derived before multiplication and obeys a
source coherence law that the hostile factor cannot lift.

The immediate falsifier is a hostile source that reproduces both \(K\) and an
admissible odd companion with the same boundary law while retaining off-seam
zeros.  Until that test is passed, the parity pair explains information loss
but does not prove divisor confinement.

## Result

Scalar theta completion sees the antisymmetric completed boundary coordinate
only through its square.  The canonical missing orientation port is the odd
sinh-transform \(K'(z)\).  RH must be a theorem about the full even--odd
relationship, not the reciprocal-even scalar alone.
