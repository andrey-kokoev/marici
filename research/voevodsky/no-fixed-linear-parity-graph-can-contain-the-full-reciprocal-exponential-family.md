# No fixed linear parity graph can contain the full reciprocal exponential family

## Proposed graph condition

Suppose a fixed linear operator

\[
T:\mathcal H_e\to\mathcal H_o
\]

had a graph containing every bilateral physical exponential

\[
e_s(u)=e^{-su}.
\]

Its parity components are

\[
(e_s)_e=
\cosh(su),
\qquad
(e_s)_o=
-
\sinh(su).
\]

The graph condition would require

\[
T\cosh(su)
=
-
\sinh(su)
\]

for every \(s\).

## Reciprocal contradiction

Replacing \(s\) by \(-s\) leaves the even component unchanged and reverses the odd component:

\[
\cosh(-su)=
\cosh(su),
\]

\[
-
\sinh(-su)
=
+
\sinh(su).
\]

Linearity would therefore force simultaneously

\[
T\cosh(su)
=-
\sinh(su)
\]

and

\[
T\cosh(su)
=+
\sinh(su).
\]

For nonzero \(s\), this is impossible.

## Infinitesimal contradiction

The same obstruction appears at the origin. Differentiating

\[
T\cosh(su)
=-
\sinh(su)
\]

at \(s=0\) gives

\[
T(0)=-u,
\]

which contradicts linearity.

Thus the problem is not boundedness, locality, or choice of operator class. No single-valued linear graph over the even sector can contain the full reciprocal family.

## Consequence for positive polarization

A maximal uniformly positive subspace is ordinarily representable as a contractive graph over one fundamental sector. Such a subspace cannot contain both \(e_s\) and \(e_{-s}\), because those states have the same even projection and opposite odd projections.

Therefore the desired physical admission cannot mean placing the complete reciprocal family into one fixed positive graph.

At least one of the following is necessary:

1. retain \(s\) and \(-s\) as distinct input-labelled fibers rather than vectors in one graph;
2. pass to an oriented quotient that identifies only the physical Clark combination;
3. use a linear relation with nontrivial multivalued part instead of an operator graph;
4. admit only one Hardy orientation and reconstruct the other by adjoint boundary values;
5. enlarge the state by a spectral/input coordinate so that the projection becomes injective.

## Control interpretation

The reciprocal branches are two different trajectories with the same even state observation. No deterministic static controller can recover which odd branch occurred from that observation alone.

The missing datum is branch orientation or input history. This is exactly what the Hardy half-plane orientation, stopped transport history, or boundary incidence must retain.

## Correction to the prior candidate

A Toeplitz or Hankel operator may encode the relation after choosing one Hardy orientation. It cannot define a graph containing both reciprocal exponential branches simultaneously over the raw even sector.

The universal constructor must therefore be an oriented colligation or relation, not a fixed parity graph.

## Disposition

The bilateral carrier makes reflection unitary, but the full physical reciprocal family is not the graph of any linear even-to-odd operator. Positive admission must preserve branch orientation as additional state data.
