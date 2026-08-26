# Theta arithmetic quantum eraser is a faithful lift, not zero exclusion

## Status

Exact finite readout theorem and no-go result. Resolving arithmetic labels and
measuring complementary character ports can recover a nonzero labelled packet
from a dark scalar aggregation. This repairs observability. It cannot prove
that the original scalar aggregation is nonzero.

The result is the precise mathematical content of the quantum-eraser analogy.
It prevents that analogy from being promoted into an RH orientation law.

## Labelled packet and scalar aggregation

Let \(G\) be a finite abelian label group and let

\[
a=\sum_{g\in G}a_g e_g
\]

be a resolved arithmetic packet. The ordinary scalar readout is the trivial
character port

\[
\Sigma(a)=\sum_{g\in G}a_g.
\]

The full labelled norm is

\[
\lVert a\rVert^2=\sum_{g\in G}|a_g|^2.
\]

A scalar zero states only that \(a\) is orthogonal to the trivial detector
row. It does not imply \(a=0\).

## Complementary character ports

For every character \(\chi\in\widehat G\), define

\[
\widehat a(\chi)=\sum_{g\in G}\overline{\chi(g)}a_g.
\]

Character orthogonality gives the exact Parseval identity

\[
\sum_{\chi\in\widehat G}|\widehat a(\chi)|^2
=|G|\sum_{g\in G}|a_g|^2.
\]

Therefore the complete character family is faithful. If \(a\neq0\), at least
one conditional character port is nonzero.

The ordinary scalar is only one member of this family:

\[
\Sigma(a)=\widehat a(1).
\]

Faithfulness of the family supplies no lower bound for its trivial member.

## Smallest exact hostile

Take \(G=C_2\) and

\[
a=(1,-1).
\]

Then

\[
\widehat a(1)=0,
\qquad
\widehat a(\operatorname{sgn})=2,
\qquad
\lVert a\rVert^2=2.
\]

The scalar detector is dark while the complementary detector is bright and
the resolved state is nonzero. This is the finite arithmetic analogue of a
quantum eraser recovering conditional fringes from a flat marginal.

It disproves the claim that complete resolved tomography implies
\(\Sigma(a)\neq0\).

## Marker accessibility

Adjoining an orthogonal marker produces

\[
\Psi=\sum_{g\in G}a_g e_g\otimes m_g.
\]

If the marker is accessible, a complementary measurement can expose the
character ports. If it has leaked into an inaccessible environment, the same
reduced scalar statistics need not admit an operational eraser.

This distinction is about recoverable information. Neither case changes the
value of the original trivial-character readout.

## Phase-reference authority

Character phases require a declared common frame. Rephasing the labelled
ports by

\[
a_g\longmapsto e^{i\theta_g}a_g
\]

preserves the resolved norm while changing individual character outputs. A
local-oscillator analogue can authorize one comparison frame, but the frame
does not orient the packet unless its relation to the arithmetic source is
itself derived.

A fitted character basis selected after observing a scalar zero has no source
authority.

## Consequence for the RH lane

Prime-power, valuation, or occurrence labels may lift the completed scalar
section into a faithful resolved packet. Conditional arithmetic-character
readouts may then show that the underlying packet survives at a scalar zero.

That is explanatory provenance, not zero exclusion. It says why cancellation
need not destroy the relationship. It does not forbid cancellation at the
distinguished scalar port.

The remaining RH-bearing requirement is stronger: a source-derived law must
keep the resolved packet away from the kernel of the trivial aggregation row
off the critical seam. Equivalently, it must constrain the normalized overlap
with the distinguished detector itself, not merely provide other detectors
that see the state.

## Finite falsifiers

Reject a proposed arithmetic-erasure orientation law if:

- its only conclusion is faithful labelled tomography;
- it replaces the distinguished scalar port by a complementary port;
- it chooses the character basis after inspecting a zero;
- it treats inaccessible environmental labels as measurable markers;
- it infers source authority from a supplied phase reference;
- it converts conditional recovery into nonvanishing of the marginal.

The two-label packet \((1,-1)\) is sufficient to falsify all such promotions.
