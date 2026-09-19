# The quadratic crosswalk must separate Pauli-dilated positive energy from the Wronskian skew orientation

The previous iteration correctly located the source of the odd coordinate but
combined it too quickly with the raw endpoint Gram.  The raw two-window Gram
has

\[
G_p^{\rm win}\to\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad \det G_p^{\rm win}\to0.
\]

It therefore admits no prime-uniform bi-bounded equivalence with a coercive
theta endpoint Gram.  Moreover plain multiplication by real windows has zero
imaginary cross-polarization, so its quadratic map cannot directly represent a
nonzero Wronskian orientation.

The correct target has two separately typed layers.

First, the positive topology is carried by the Pauli-dilated observer

\[
\mathcal O_pv=
\binom{J_pXv}{J_pYv},
\]

for which

\[
\mathcal O_p^*\mathcal O_p
=XG_p^{\rm win}X+YG_p^{\rm win}Y
=2\begin{pmatrix}b_p&0\\0&a_p\end{pmatrix}
\ge2m_\nu^2I.
\]

Second, reciprocal orientation is retained by the independent bounded skew
response

\[
K_{\rm link}=-J_{\rm link}/2.
\]

It is not an off-diagonal entry that must be absorbed into the positive Pauli
Gram.  The completed object is a flagged positive-plus-skew package

\[
(\mathcal O_p^*\mathcal O_p,\ K_{\rm link}),
\]

with the two Pauli outputs kept distinct.

Consequently the previously written single identity

\[
\Gamma_\pi(G_p^{\rm cell})
=G_p^{\rm analytic}\oplus K_{\rm link}
\]

is too compressed and generally ill-typed for the raw multiplication
representation.  It must be replaced by two compatibility laws:

1. a uniformly bounded positive isometry/equivalence for the Pauli-dilated
   observer;
2. an oriented intertwining law for the separate skew Wronskian block.

Only their common flagged refinement may enter the `CG` correspondence.  This
avoids both the collapsing raw disagreement direction and the accidental
erasure of reciprocal phase.
