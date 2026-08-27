# The RH tail-plus-seam cut has an explicit reciprocal operator inverse

Author: `marici.Nima`

Date: 2026-08-26

Status: exact source-derived operator inverse at the scale-cut layer

## Complete cut operator

For a displacement (p>0), define

\[
C_p\Phi=(G_p\Phi,H_p\Phi),
\]

where

\[
(G_p\Phi)(t)=\Phi(t+p)
\]

and

\[
(H_p\Phi)(t)
=
\mathbf 1_{0\le t\le p}\Phi(p-t).
\]

The target is the typed direct sum

\[
L^2(\mathbb R_+)
\oplus
L^2([0,p]).
\]

The polarized norm identity already proves that $C_p$ is isometric.

## Explicit recombination inverse

Given a tail state (g) and an oriented seam state (h), reconstruct the
source by

\[
(R_p(g,h))(u)
=
\begin{cases}
h(p-u),&0\le u\le p,\\
g(u-p),&u\ge p.
\end{cases}
\]

The endpoint convention at (u=p) is irrelevant in (L^2).

Direct substitution gives

\[
R_pC_p=I
\]

on the source space and

\[
C_pR_p=I
\]

on the typed tail-plus-seam direct sum.

Therefore

\[
R_p=C_p^{-1}=C_p^*.
\]

The complete scale cut is a unitary source equivalence.

## Reciprocal interpretation

Forward arithmetic transport decomposes the source into a retained tail and
an emitted seam interval. Reciprocal transport recombines those two typed
components into the original source.

This is the first exact operator-valued reciprocal sewing law in the RH
programme. It exists before scalar Mellin or determinant projection.

The seam is not a correction appended to a defective tail map. It is the
precise complementary coordinate that makes the source transport invertible.

## Tail-only no-go

The projection

\[
\Phi\longmapsto G_p\Phi
\]

has a large kernel: every source supported inside the removed interval maps
to zero. No reciprocal operator can reconstruct that information.

Thus every attempt to lift scalar Tate reciprocity through a tail-only carrier
must fail or introduce an unauthorized choice. The full tail-plus-seam packet
is the minimal source object on which reciprocal inversion is defined.

## Composition law

For staged cuts, oriented seam concatenation gives

\[
C_{p+q}
=
\mathfrak a_{p,q}
\left(
(C_q\oplus I)C_p
\right),
\]

where (mathfrak a_{p,q}) is the authorized resegmentation of the two seam
intervals into the combined interval. Taking inverses gives the reverse-order
recombination law.

This is a genuine functorial reciprocal transport, not merely equality of
scalar displacements.

## What remains

The exact inverse law is now established for the scale-cut layer. The full
theta sewing operator also contains:

- passive spectral-flow scattering;
- primitive and square endpoint currents;
- archimedean completion;
- reciprocal Fourier/Tate polarization.

Each remaining layer must either be invertible on its complete typed packet
or carry an operator supply residual canceled by its reciprocal layer.

## Finite falsifiers

At every cutoff, reject a proposed reciprocal cut if:

- recombination fails on a source vector;
- cutting a freely chosen tail-plus-seam packet fails to return that packet;
- seam orientation is reversed incorrectly;
- tail-only data are claimed sufficient;
- staged inverse composition uses the wrong order.
