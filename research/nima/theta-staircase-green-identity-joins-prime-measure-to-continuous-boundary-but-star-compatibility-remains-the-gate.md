# Theta staircase Green identity joins prime measure to continuous boundary, but star compatibility remains the gate

## Status

Exact distributional Green identity and noncircularity boundary. The
distributional derivative of the cumulative arithmetic staircase is exactly
the typed prime-power incidence measure. Integration by parts joins its
discrete sampled current to the continuous centered boundary port.

Reciprocal transport and Hilbert adjunction agree on the complete continuous
interval family exactly on the critical seam. This gives a perfect seam
detector, but not yet a zero-confinement theorem: star compatibility must be
forced by source-derived zero-state boundary conditions rather than imposed.

## Arithmetic staircase and its derivative

Let

\[
W(v)=\sum_{p,k:\,k\log p\leq v}w_{p,k}.
\]

As a distribution or locally finite measure,

\[
dW
=\sum_{p,k}w_{p,k}\delta_{k\log p}.
\]

Thus the staircase is a primitive of the exact typed prime-power incidence
measure. Restriction to (k=1\), (k=2\), and (k\geq3\) recovers the primitive,
square, and higher channels without type erasure.

## Discrete sampled current

For a smooth rapidly decaying source (A\), define

\[
P_W[A](z)
=\int_0^\infty A(v)e^{izv}\,dW(v).
\]

By the atomic form of (dW\),

\[
P_W[A](z)
=\sum_{p,k}
w_{p,k}A(k\log p)p^{izk}.
\]

This is the exact prime-power sample current.

## Continuous staircase bulk

Define the centered continuous port

\[
C_W[A](z)
=-\int_0^\infty W(v)A(v)e^{izv}\,dv
\]

and its differentiated companion

\[
D_W[A](z)
=-\int_0^\infty W(v)A'(v)e^{izv}\,dv.
\]

The theta tail removes the boundary at infinity, and (W\) vanishes before the
first prime-power jump. Distributional integration by parts gives

\[
P_W[A](z)
=D_W[A](z)+izC_W[A](z).
\]

This is the source-derived Green identity joining the discrete arithmetic
measure to the continuous staircase boundary state.

It is not a fitted relation: every term is constructed from (A\) and (W\)
before scalar zero inspection.

## Interval-family derivative

For

\[
B_\ell^+(z)=\int_0^\ell A(v)e^{izv}\,dv,
\]

we have

\[
\partial_\ell B_\ell^+(z)
=A(\ell)e^{iz\ell}.
\]

The complete continuous interval family therefore recovers the source pointwise
where (A\) is nonzero. The staircase current samples this family precisely at
the arithmetic jump locations.

## Reciprocal transport versus adjunction

Reciprocal transport gives

\[
B_\ell^-(z)=B_\ell^+(-z).
\]

For real (A\), Hilbert adjunction gives

\[
\overline{B_\ell^+(z)}
=B_\ell^+(-\overline z).
\]

Star compatibility of reciprocal transport requires

\[
B_\ell^+(-z)
=B_\ell^+(-\overline z)
\]

for the complete continuous family.

Differentiating in \(\ell\) yields

\[
A(\ell)e^{-iz\ell}
=A(\ell)e^{-i\overline z\ell}.
\]

On any interval where (A(\ell)\neq0\), this forces

\[
z=\overline z.
\]

In the centered Fourier coordinate, this is exactly the critical seam.

## Why this is not yet RH

The implication just proved starts from star compatibility of the continuous
boundary family. It does not prove that a scalar zero supplies that
compatibility.

The currently established zero-state facts provide:

- convergence or summability of exceptional discrete arithmetic currents;
- a well-defined centered staircase output;
- reciprocal typing of the discrete packets;
- source construction of the ambient continuous interval family.

They do not yet identify the zero-state reciprocal action with Hilbert
adjunction on that family.

Assuming this identification would insert the seam conclusion as a boundary
axiom.

## Discrete-to-continuous extension gate

Let the completed zero-state arithmetic packet provide values at the discrete
lengths

\[
\ell_{p,k}=k\log p.
\]

The missing theorem must show that these values extend through the
source-derived cocycle to the continuous family (B_\ell\) and that the
extension is star-compatible.

The required data are:

1. continuity or closed-graph control in \(\ell\);
2. the interval cocycle under addition of lengths;
3. agreement with the discrete primitive and square packets;
4. compatibility with the staircase Green identity;
5. adjoint compatibility derived from the zero-state domain.

Only the fifth item contains seam-confining force.

## Finite and local falsifiers

For a proposed continuous extension, compute the star defect

\[
\mathfrak S_\ell(z)
=B_\ell^+(-z)-B_\ell^+(-\overline z).
\]

Its derivative is

\[
\partial_\ell\mathfrak S_\ell(z)
=A(\ell)
\left[e^{-iz\ell}-e^{-i\overline z\ell}\right].
\]

At any off-seam (z\) and any source-positive interval, this derivative is
nonzero except at isolated lengths. Thus a continuous star-compatible extension
is locally impossible off seam.

For the Green identity, the finite falsifier is failure of

\[
P_W=D_W+izC_W
\]

at a finite prime-power cutoff, including all endpoint contributions.

## Consequence

The arithmetic staircase has now acquired its exact discrete–continuous Green
identity and an exact seam detector. The remaining RH problem is concentrated
in one bridge:

Does a scalar zero, together with the completed primitive/square boundary
conditions, force the discrete staircase state to extend as the
star-compatible continuous interval cocycle?

If yes, the seam conclusion follows immediately. If not, the staircase port
remains a genuinely independent observer but not an orientation mechanism.
