# Theta boundary-control system gives an exact Evans bridge but leaves forcing bulk

## Bounded question

Can the constant channel excluded by the relative-Haar form be retained as an
independent boundary coordinate, and does the resulting source system connect
scalar zeros to admissible states?

## Source tail system

Let (f) be the completed logarithmic theta source and define

\[
F(z)=\int_0^\infty f(v)e^{zv}\,dv.
\]

For each (z), set

\[
G_z(q)=\int_q^\infty f(v)e^{z(v-q)}\,dv.
\]

Then

\[
G_z'(q)+zG_z(q)+f(q)=0,
\qquad
G_z(0)=F(z),
\qquad
G_z(\infty)=0.
\]

Introduce an independent scalar boundary-control coordinate (c) and the
closed system node

\[
\mathcal D_z(G,c)=G'+zG+cf.
\]

The scalar is not represented by a constant function in the Haar carrier.
Instead, the bounded control map sends (c) to (cf). This avoids the domain
obstruction of packet 229 without renormalizing an infinite constant norm.

## Exact Evans bridge

For (c\ne0), every solution of \(\mathcal D_z(G,c)=0\) that decays at
infinity is (G=cG_z). Impose the two-endpoint domain

\[
G(0)=0,
\qquad
G(\infty)=0.
\]

Then

\[
\ker\left(\mathcal D_z\big|_{0,\infty}\right)\ne0
\quad\Longleftrightarrow\quad
F(z)=0.
\]

This is a source-derived zero-to-state theorem. The differential system and
its endpoint domain are defined directly from (f), without division by
(F) or use of zero locations.

## Green identity

For a homogeneous state \(\mathcal D_z(G,c)=0\),

\[
\partial_q|G|^2
=-2\Re z\,|G|^2
-2\Re\left(cf\overline G\right).
\]

After integration,

\[
2\Re z\int_0^\infty|G|^2\,dq
=|G(0)|^2-|G(\infty)|^2
-2\Re\int_0^\infty cf\overline G\,dq.
\]

For a zero-state both endpoint terms vanish, but the forcing bulk remains:

\[
2\Re z\int_0^\infty|G|^2\,dq
=-2\Re\int_0^\infty cf\overline G\,dq.
\]

Therefore the Evans bridge alone does not force \(\Re z=0\).

## Reciprocal doubling

Pair the direct state at (z) with the reciprocal state at \(-\overline z\).
Adding their correctly oriented Green identities produces

\[
2\Re z
\left(
\|G_+\|^2+\|G_-\|^2
\right)
=2\Re
\left(
c_-\langle f,G_-\rangle
-c_+\langle f,G_+\rangle
\right)
\]

when all endpoint values vanish. The right-hand side is the exact mixed-sheet
forcing difference.

It is not eliminated by the scalar zero condition. It must be identified with
a source-derived modular boundary current or cancelled by the primitive,
prime-square, seam, and archimedean channels.

## What is now solved

The boundary-control formulation resolves two previous gates:

- the affine constant has a legitimate finite-dimensional type;
- scalar vanishing is exactly equivalent to a nonzero two-endpoint kernel
  state.

The remaining RH content is no longer the Evans bridge. It is the typed
conversion of the doubled forcing difference into completed boundary flux.

## Finite falsifier

At any source cutoff, compute

\[
R_X
=2\Re
\left(
c_-\langle f_X,G_{-,X}\rangle
-c_+\langle f_X,G_{+,X}\rangle
\right)
-J_{\mathrm{declared},X}.
\]

Here (J_{\mathrm{declared},X}) is the sum of independently constructed source
currents. A nonzero typed residual closes the conservation route. Defining the
current as an antiderivative of the displayed forcing is circular.

## Scope

This packet constructs a source-derived boundary-control Evans system and
proves its exact zero-to-state equivalence. It also derives the surviving
doubled forcing bulk. It does not identify that bulk with modular boundary
currents, prove completion stability of the full block system, or prove RH.
