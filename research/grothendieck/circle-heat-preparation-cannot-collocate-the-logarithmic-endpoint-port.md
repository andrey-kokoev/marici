# Circle heat preparation cannot collocate the logarithmic endpoint port

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact cross-carrier intertwining obstruction

## Tempting repair

The theta source is constructed from heat evolution of the arithmetic-circle
seam state. This suggests using the positive heat semigroup to identify the
endpoint delta with the smooth theta forcing.

That suggestion conflates two different carrier spaces.

## Two generators with incompatible spectral type

On the mean-zero arithmetic circle, the winding Laplacian has

\[
A_{\mathrm{circ}}e_n=n^2e_n.
\]

It has a complete discrete eigenbasis. The heat family

\[
e^{-\pi tA_{\mathrm{circ}}/2}\delta_0
\]

lives on this circle carrier.

The tail resolvent instead uses logarithmic translation on the full line,

\[
A_{\mathrm{log}}=-i\partial_q.
\]

This operator has no nonzero \(L^2(\mathbb R)\) eigenvectors. A formal
eigenfunction at real eigenvalue \(\lambda\) is \(e^{i\lambda q}\), whose
truncated squared norm on \([-R,R]\) equals \(2R\) and diverges.

## Intertwiner theorem

Suppose a bounded operator \(J\) obeys

\[
J A_{\mathrm{circ}}=A_{\mathrm{log}}J
\]

on the circle eigenbasis. Then \(Je_n\) would be an \(L^2\) eigenvector of
\(A_{\mathrm{log}}\) with eigenvalue \(n^2\). Therefore \(Je_n=0\) for every
\(n\). Density of the eigenbasis gives \(J=0\).

Hence no nonzero bounded generator-intertwiner turns the circle heat seam
state into the logarithmic source or endpoint port.

## Meaning

The circle delta and logarithmic endpoint delta share notation but not type.
The theta construction passes from the circle heat state through an operator
differential and a winding trace to scalar forcing on the logarithmic line.

The trace is a cross-carrier readout, not a unitary or boundedly invertible
state transport. It cannot be reversed to identify the two ports.

## Surviving construction

Any useful bridge must be a correspondence rather than an intertwining
isomorphism. It must retain both carriers and specify:

- the circle winding state;
- the logarithmic tail state;
- the heat-and-trace incidence between them;
- its adjoint boundary incidence;
- and the topology in which the distributional endpoint is continuous.

The previously derived Epstein coherence matrix is one such uncompressed
cross-carrier object. Its scalar trace is not yet the required determinant or
positive colligation.

## Falsifier

Any claimed bounded port identification must state which generators it
intertwines. If it preserves the circle Laplacian and log translation, the
point-spectrum argument forces it to vanish. A rigged correspondence may
survive, but it must expose its distributional domain and cannot claim
ordinary Hilbert equivalence.

## Scope

The bounded-intertwiner no-go is exact. It does not rule out an unbounded
rigged correspondence, a trace correspondence, or an enlarged two-carrier
colligation.

## Verification

The checker verifies the non-square-integrability of every formal real
translation eigenfunction, which supplies the point-spectrum obstruction.
