# The primitive top kernel has unit e6 incidence

The remaining integral divisibility question can be answered at the level of the specialization graph and normalized components.

The generic marked quotient basis is

\[
(g_{101},g_{110},g_{111}^{\rm top}),
\]

and its specialization matrix is

\[
\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}.
\]

Hence the disappearing class is the primitive vector

\[
(0,0,1)=g_{111}^{\rm top}.
\]

The specialization cokernel is torsion-free. Independently, the global Bunch--Davies construction represents this kernel by the primitive Cech half-boundary

\[
(1,-1,1,-1),
\]

whose coefficients have greatest common divisor one.

In the normalization of the double-conic central fiber, the two components \(S_+\) and \(S_-\) meet transversely along the conductor. The cellular connecting map sends an oriented primitive crossing to the component difference

\[
e_{6,\mathrm B}=[C_+]-[C_-]
\]

with incidence \(+1\) (or \(-1\) after reversing all orientations). There is no factor two: such a factor would make the rank-one image nonsaturated, contradicting both the primitive half-boundary and the torsion-free specialization graph.

Therefore

\[
\left\langle2m,e_6^\vee\right\rangle
=\pm1
\]

in the primitive integral normalization, and hence

\[
a=1.
\]

The marked extension composition already showed that the same primitive top generator has zero projection to \(v_{\rm alg}\), so

\[
b=0.
\]

Thus the ordered ambient cusp parity is

\[
\boxed{(a,b)=(1,0)}.
\]

The rational coefficient \(1/[8(x+y)]\) in the de Rham frame is now understood as a period normalization of the primitive component-difference class; it is not its integral index.

Certificates:

- `research/voevodsky/checkers/primitive_top_to_e6_incidence.py`;
- `research/voevodsky/results/primitive_top_to_e6_incidence.json`;
- `research/voevodsky/checkers/compose_top_kernel_with_marked_extension.py`;
- `research/voevodsky/results/top_kernel_marked_extension_composition.json`.
