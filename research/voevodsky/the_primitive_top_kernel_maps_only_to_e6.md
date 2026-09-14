# The primitive top kernel maps only to e6

The existing rank-twelve packets contain a typed composition that had not been used in the conductor analysis.

The total-energy conductor specialization has primitive kernel

\[
\ker(\operatorname{Sp})=\mathbb Z\langle g_{111}^{\rm top}\rangle.
\]

The source-normalized marked algebraic extension map has source basis

\[
(g_{101},g_{110},g_{111}^{\rm top})
\]

and target coordinates

\[
(e_2,e_4,e_6,v_0).
\]

Its \(g_{111}^{\rm top}\) column is exactly

\[
\begin{pmatrix}
0\\0\\[2pt]\dfrac{1}{8(x+y)}\\[2pt]0
\end{pmatrix}.
\]

Therefore the quotient generator that actually disappears at the total-energy specialization maps only to the \(e_6\)-line. Its projection to the second algebraic quotient direction \(v_0\), corresponding to the \(v_{\rm alg}\) direction in this marked block, is exactly zero.

This is the correctly typed reason for the vanishing second component. It uses the primitive specialization kernel and the marked extension column themselves; it does not infer an off-diagonal extension from a diagonal dlog residue or an untyped point evaluation.

Thus

\[
b=0.
\]

The integral uncertainty is now one-dimensional. The nonzero rational coefficient

\[
\frac{1}{8(x+y)}e_6
\]

does not by itself determine the divisibility of the corresponding integral Betti class. Hence the remaining question is only

\[
a\in\{0,1\}.
\]

The global Bunch--Davies Cech half-boundary supplies a candidate primitive normalization for this top generator. The next calculation must compare that primitive integral chain directly with the source generator \(g_{111}^{\rm top}\) and determine whether the displayed \(e_6\) image is primitive or twice a primitive class.

Certificate:

- `research/voevodsky/checkers/compose_top_kernel_with_marked_extension.py`;
- `research/voevodsky/results/top_kernel_marked_extension_composition.json`.
