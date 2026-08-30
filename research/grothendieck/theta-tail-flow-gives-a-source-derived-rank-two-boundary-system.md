# The theta tail flow gives a source-derived rank-two boundary system

## Bounded construction

The combined Deutsch--Sommerfeld brief asks for a source operator and boundary
problem from which a scalar zero produces an admissible state.  The previously
derived source-tail feature supplies a minimal candidate without beginning
from a prescribed zero set.

Let `f(q)` be the completed one-sided theta forcing and define

\[
 G_s(q)=e^{-sq}\int_q^\infty f(v)e^{sv}\,dv
\]

where the integral converges. Then

\[
 (\partial_q+s)G_s(q)+f(q)=0.
\]

Moreover,

\[
 G_s(0)=\int_0^\infty f(v)e^{sv}\,dv,
 \qquad
 G_s(\infty)=0.
\]

Thus a zero of the one-sided transform is exactly a two-ended boundary
condition on a source-derived tail state:

\[
 G_s(0)=G_s(\infty)=0.
\]

## Homogeneous augmentation

The tail equation is inhomogeneous only because the source channel has been
suppressed. Adjoin the constant channel and put

\[
 \Psi_s(q)=\binom{G_s(q)}{1},
 \qquad
 \mathcal D_s=
 \begin{pmatrix}
 \partial_q+s&f(q)\\
 0&\partial_q
 \end{pmatrix}.
\]

Then

\[
 \mathcal D_s\Psi_s=0.
\]

This operator is derived from the source-tail flow. It is not manufactured by
declaring a one-dimensional differential equal to the completed scalar.

The constant component is essential: deleting it converts a forced transport
problem into a false eigenvalue problem. It is the smallest analogue of the
primitive boundary channel in the three-level Tate filtration.

## Zero-to-state bridge

For this augmented system, a scalar transform zero supplies a nonzero
solution with the first component satisfying Dirichlet conditions at both
ends. The state itself is not zero because its source component equals one.

This gives a genuine but still local bridge:

\[
 \text{scalar pairing null}
 \longrightarrow
 \text{admissible two-ended solution of a source-derived system}.
\]

It does **not** yet identify zeros of the completed Xi function. The exact
bilateral modular sewing, constant carrier, Mellin units, and endpoint terms
must be included before that identification is made.

## Green identity frontier

The adjoint pairing of the first row gives

\[
 \partial_q|G_s|^2
 =-2\Re(s)|G_s|^2-2\Re\bigl(f\overline{G_s}\bigr).
\]

For a two-ended zero state, integration yields

\[
 \Re(s)\int_0^\infty|G_s|^2\,dq
 =-\Re\int_0^\infty f\overline{G_s}\,dq.
\]

The right side is indefinite. Therefore the one-sided rank-two system alone
does not force `Re(s)=0` in centered coordinates. This exactly locates what
the full boundary-bearing construction must add: the Fourier--Tate dual
system and its primitive, square, and archimedean boundary currents must turn
the forcing cross-term into a cancelling boundary flux or a source norm.

## Why this route is noncircular

The construction order is

\[
 f\longrightarrow G_s\longrightarrow\mathcal D_s
 \longrightarrow\text{boundary evaluation}.
\]

A hostile scalar multiplier `H(s)` cannot be attached to the boundary
evaluation while keeping this operator fixed. To reproduce `H(s)F(s)`, it
must change the forcing, add source channels, or alter the boundary map. The
first altered source datum is therefore observable before examining the new
divisor.

## Immediate next calculation

Construct the doubled operator

\[
 \mathcal D_s^+\oplus\mathcal D_{1-s}^-
\]

on the two valuation orientations, retain all moving-seam cross terms, and
derive its exact Green/Clifford current. The decisive question is whether
bilateral modular sewing converts

\[
 \Re\int f\overline G
\]

into the complete `k=1`, `k=2`, and archimedean boundary flux with no residual
indefinite bulk channel.

The falsifier is any uncancelled bulk polarization after the exact doubled
identity is formed. Local positivity is neither assumed nor required.

