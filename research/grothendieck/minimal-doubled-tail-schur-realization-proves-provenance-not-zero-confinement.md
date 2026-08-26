# Minimal doubled-tail Schur realization proves provenance, not zero confinement

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact source-derived realization and scope boundary

## Source system

Let (f) be the fixed completed theta tail on the positive scale chamber and
put (z=s-1/2).  Define the two terminal tail states

\[
 G_+(q;z)=e^{-zq}\int_q^\infty f(v)e^{zv}\,dv,
\]

\[
 G_-(q;z)=e^{zq}\int_q^\infty f(v)e^{-zv}\,dv.
\]

They are derived before the scalar readout and satisfy

\[
 (\partial_q+z)G_++f=0,
 \qquad
 (\partial_q-z)G_-+f=0,
\]

with terminal conditions (G_+(\infty)=G_-(\infty)=0).

Introduce a genuine boundary amplitude (c\).  On the doubled bulk space,
define

\[
 A_z=
 \begin{pmatrix}
 \partial_q+z&0\\
 0&\partial_q-z
 \end{pmatrix},
 \qquad
 Bc=\binom{fc}{fc},
\]

\[
 C\binom{g_+}{g_-}=g_+(0)+g_-(0),
 \qquad
 D=0.
\]

The domain of (A_z) includes the terminal boundary condition.  Because the
theta source decays super-exponentially, its inverse on the source-generated
tail orbit is the terminal Volterra resolvent for every finite (z).

## Exact elimination

The source equation is

\[
 A_zg+Bc=0.
\]

Thus

\[
 g=-A_z^{-1}Bc
   =c\binom{G_+(\cdot;z)}{G_-(\cdot;z)}.
\]

The reciprocal seam closes the loop through

\[
 Cg+Dc=0.
\]

Eliminating the bulk gives the scalar boundary Schur complement

\[
 S_\partial(z)=D-CA_z^{-1}B
 =G_+(0;z)+G_-(0;z).
\]

Consequently

\[
 S_\partial(z)
 =\int_0^\infty f(v)
 \left(e^{zv}+e^{-zv}\right)\,dv.
\]

Up to the already audited nonvanishing normalization unit and any separately
typed archimedean direct channel, this is the completed bilateral theta
section.  No division by that section and no zero locations were used to
construct (A,B,C,D).

The zero-to-state bridge is therefore exact:

\[
 S_\partial(z)=0
 \quad\Longleftrightarrow\quad
 \ker
 \begin{pmatrix}A_z&B\\C&D\end{pmatrix}
 \ne0.
\]

The nonzero state is the antidiagonal endpoint state already found:

\[
 G_+(0;z)=-G_-(0;z).
\]

## What this proves

This realization proves three structural claims.

1. The divisor belongs to the closed reciprocal boundary loop, not to the
   invertible causal bulk.
2. A hostile scalar multiplier cannot be inserted without changing the
   source, boundary space, injection, readout, or direct seam channel.
3. The two apparent half-plane tails are two open-loop polarizations of one
   closed boundary comparison.

This is a genuine source-derived canonical-section result.

## Why it does not confine zeros

The minimal boundary space is one-dimensional.  Its Schur complement is the
scalar transform itself.  Therefore each of the standard closed-loop tests
collapses to an RH-strength scalar assertion:

- invertibility of (S_\partial(z)) is the desired zero-free statement;
- strict dissipativity of (S_\partial(z)) is a stronger orientation
  statement;
- a small-gain normalization depends on a chosen nonzero direct block and
  simply rewrites exclusion of the eigenvalue one;
- no nontrivial well-founded label grade remains after the two source tails
  have been aggregated into (B) and (C).

Thus the minimal realization gives provenance but no new mathematical force.
It has compressed away the primitive, square, prime-label, and archimedean
incidence data before feedback closure.

## Next required lift

The next boundary module must be constructed before vacuum aggregation.  Its
ports must retain at least

\[
 k=1,\qquad k=2,\qquad k\ge3,\qquad \infty,
\]

together with reciprocal-sheet variance.  The scalar theta section should
then arise only as a determinant or distinguished compression of the larger
Schur complement.

The finite falsifier is strict.  If the labelled realization is compressed to
the scalar transform before a source-derived grade, dissipative form, or
signed incidence law appears, it adds no zero-confining content.  Conversely,
any proposed larger realization must reduce exactly to the four blocks above
after authorized aggregation.

## Result

The closed-loop architecture is now explicit and noncircular, but its minimal
form is deliberately classified as a provenance theorem rather than an RH
advance.  The live question is whether the unaggregated arithmetic boundary
module carries a source law that disappears under the scalar Schur
compression.
