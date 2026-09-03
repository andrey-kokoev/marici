# The divisor root does not select an extension shear

In the standard A2 basis, the sourced divisor
`dlog(X3/X2)` has coordinates `(0,-1)`. Cyclic extension shears are
\[
M(x,y)=\begin{pmatrix}x&y\\-y&x+y\end{pmatrix}.
\]
A vector does not determine such an endomorphism. Choosing the first primitive
basis root as domain anchor gives `M(0,1)`, while choosing the second gives
`M(-1,0)`; both commute with the cyclic action and send their chosen anchor to
the same divisor root.

This ambiguity is typed, not numerical. Constructing a shear from the root
requires an independently sourced covector or domain anchor. Moreover, the
existing A2 audit proves there is no nonzero equivariant linear map from A2 to
the trivially acted centralizer parameter lattice. The root alone therefore
selects no `(x,y)`.
