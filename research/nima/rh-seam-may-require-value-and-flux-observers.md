# The RH Seam May Require Separate Value and Flux Observers

## Proposed correction

The provisional three-port object uses two reciprocal tail channels and one seam
channel:

\[
(P,Q,M).
\]

This may under-type the interface. A boundary normally carries at least two
logically distinct roles: the value retained on the boundary and the directed
flux crossing it. The candidate primitive object is therefore

\[
(P,Q,M,J),
\]

where \(M\) is the seam value channel and \(J\) is the seam flux channel.

Equivalently, the seam may have two directed traces \(M_+\) and \(M_-\), with

\[
M=\frac{M_++M_-}{2},
\qquad
J=\frac{M_+-M_-}{2}.
\]

This is a change of coordinates, not an extra assumption of positivity.

## Symmetry typing

Reciprocal reflection should act by

\[
P\leftrightarrow Q,
\qquad
M\mapsto M,
\qquad
J\mapsto-J.
\]

Thus the four primitive directions split into two even characters and two odd
characters:

- even: \(P+Q\) and \(M\);
- odd: \(P-Q\) and \(J\).

The earlier three-observer model retained the first three primitive coordinates
but erased \(J\). Even after restoring the odd tail direction \(P-Q\), the
seam-flux direction remains invisible. The exact finite kernel witness is the
nonzero state with only \(J\) present.

## DPC

Candidate principle: one seam observer is sufficient.

Required source consequence: the directed traces must either coincide, making
\(J=0\), or a source-derived law must reconstruct \(J\) from \(P,Q,M\) and must
commute with every admitted continuation.

Finite falsifier: two interface states can share \(P,Q,M\) and have opposite
nonzero values of \(J\). Reciprocal reflection exchanges them while preserving
the three recorded ports. Therefore a later crossing-sensitive Task separates
states identified by the three-port quotient.

Verdict: one seam observer is insufficient unless the required flux law is
derived independently.

## Consequence for the RH mechanism

This changes the likely confinement identity. The missing relation may not be a
law forcing the bulk relative current to vanish by itself. It may instead be a
conservation or matching law between the odd bulk channel and the odd seam
flux:

\[
J_{\mathrm{bulk}}+J_{\mathrm{seam}}=0.
\]

The critical seam would then be characterized by a source-derived boundary
condition on \(J_{\mathrm{seam}}\), not merely by equality of two scalar
half-plane readouts.

This is structurally compatible with the doubled Green identity, where bulk
energy and a boundary current already appear together. It is also compatible
with the earlier warning that the primitive and prime-square currents cannot be
discarded during completion: they may be components of the missing directed
seam record.

## Required source audit

The four-port proposal is not yet established for theta/Tate data. Grothendieck
should test whether the existing boundary packet contains two independently
typed traces, such as value and normal derivative, incoming and outgoing
boundary values, or two Clark boundary orientations. The proposal survives
only if both ports are constructed before scalar completion and their reflection
characters are source-derived.

If the two traces collapse source-locally, the model returns to three ports. If
they do not, the correct Ubersector has four function-valued instruments and
the earlier three-observer coalgebra was still one quotient too small.
