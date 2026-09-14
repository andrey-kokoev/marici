# The quarter-twisted relative residue matches combined but not separate wall monodromy

## Question

What conductor monodromy is represented by the equal-order relative normal residue after choosing the smallest exponent that turns its two nonzero eigenvalues into Kummer sign changes?

## Claim boundary

This is a conditional monodromy comparison. The relative exponent \(\varepsilon=\pm1/4\) is not yet derived from the conductor integral or contour.

## Relative involution

The equal-order residue has eigenvalues \((2,2,0)\). Choosing a quarter twist makes the two nonzero monodromy eigenvalues equal to \(-1\), while the flat eigenvalue gives \(+1\). Orientation reversal gives the inverse monodromy, which is the same involution.

Using the primitive eigenlattice matrix

\[
W=
\begin{pmatrix}
-1&1&0\\
1&0&-1\\
0&1&1
\end{pmatrix},
\]

the resulting integral relative monodromy is

\[
M_{\rm rel}=W\operatorname{diag}(-1,-1,1)W^{-1}
=
\begin{pmatrix}
-1&0&0\\
1&0&-1\\
-1&-1&0
\end{pmatrix}.
\]

It is integral and involutive.

## Conductor comparison

The audited conductor wall monodromies are

\[
M_1=
\begin{pmatrix}-1&0&-1\\0&1&0\\0&0&1\end{pmatrix},
\qquad
M_2=
\begin{pmatrix}1&0&0\\0&-1&-1\\0&0&1\end{pmatrix}.
\]

Their product is

\[
M_{12}=M_1M_2=
\begin{pmatrix}-1&0&-1\\0&-1&-1\\0&0&1\end{pmatrix}.
\]

Define

\[
T=
\begin{pmatrix}
0&-1&0\\
0&0&1\\
1&1&-1
\end{pmatrix}.
\]

Then \(T\) is unimodular and

\[
TM_{\rm rel}=M_{12}T.
\]

Thus the quarter-twisted relative normal monodromy is integrally conjugate to the combined two-wall conductor involution.

## What the combined monodromy forgets

Both \(M_{\rm rel}-I\) and \(M_{12}-I\) have Smith invariants

\[
(1,2,0).
\]

Their simultaneous integral eigenspaces form an index-two lattice. This detects only one diagonal parity obstruction.

The completed conductor enhancement instead has

\[
\operatorname{coker}J\cong(\mathbb Z/2)^2.
\]

Therefore the combined monodromy cannot recover the two independent wall parities. Multiplying \(M_1\) and \(M_2\) loses the factorization data required by the integral conductor lattice.

## Consequence

A single relative nearby-cycle object can model the product monodromy but not the full wall-separated integral defect. The two wall-labelled lifts must retain separate monodromy operators before gluing. Their ordered pair, not merely their product, is the datum capable of supporting the two commuting index-two enhancements.

## Disposition

Conditional on a quarter twist, the relative normal monodromy has an exact integral conjugacy to the combined conductor monodromy. This simultaneously proves a match and a limitation: separate wall-labelled nearby cycles remain necessary, and the quarter-twist exponent still lacks contour authority.
