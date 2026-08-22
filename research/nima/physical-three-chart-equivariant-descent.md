# The three physical residue charts assemble by equivariant descent, not Cech gluing

The triangle source has three labelled cut sectors

\[
G_{12},\qquad G_{23},\qquad G_{31}.
\]

Each calibrated marked-relative sector has rank \(21\).  Exact labelled chart
transport preserves the quotient relations, residue orientation, and physical
numerator.  However, the source contains no product of two distinct cut poles.
Consequently there is no source-supported double-cut overlap on which to define
a Cech differential between these sectors.

The canonical assembly is instead

\[
V_{12}\oplus V_{23}\oplus V_{31},
\qquad \dim V_{ij}=21,
\]

with the cyclic group \(C_3\) permuting the three labelled summands.  The full
printed triangle integrand uses the cyclic sum of the three occurrences, so its
coefficient object lies in the diagonal invariant subspace

\[
(V_{12}\oplus V_{23}\oplus V_{31})^{C_3}
=\{(v,\rho v,\rho^2v):v\in V_{12}\}.
\]

The two vector equations identifying consecutive summands have total rank
\(42\) in the labelled rank-\(63\) direct sum.  Hence

\[
\boxed{
\dim (V_{12}\oplus V_{23}\oplus V_{31})^{C_3}=63-42=21.
}
\]

Cyclic organization therefore does not create a rank-63 physical system, and
it does not isolate a smaller line or quotient.  It descends the full rank-21
marked packet over the cyclic quotient of the labelled kinematic base.

This is the correct finite replacement for the proposed global Cech sewing.
The remaining theorem gate is characteristic-zero horizontality of this
equivariant descent, not construction of unsupported overlap maps.
