# The infinity--seam budget needs a rectangular defect port

Author: `marici.Nima`

## Typing question

The completed prime--seam comparison now has a trace-class relative Schur
return. Grothendieck's divisor accounting adds two finite-height carriers:

- \(I_T\), the projective-infinity divisor carrier, of dimension
  \(N_{\rm tot}(T)\);
- \(S_T\), the multiplicity-sensitive seam-germ carrier, of dimension
  \(N_{\rm seam}(T)\).

Reciprocal symmetry gives

\[
 \dim I_T-\dim S_T=2N_+(T).
\]

The question is whether the missing comparison can be adjoined as one more
square Schur correction.

## Square trace-class corrections cannot carry this defect

For a square Fredholm operator

\[
 F=I-K
\]

with trace-class \(K\), the Fredholm index is zero. Such an operator can carry
a determinant and finite-dimensional kernel/cokernel events, but their
dimensions cancel in the index.

The infinity--seam budget is instead a one-sided dimension defect. It therefore
cannot be represented by the square trace-class return alone. It requires a
rectangular comparison or an independently typed boundary projection.

## Minimum operator object

The minimum candidate is a source-derived partial isometry

\[
 W_T:I_T\longrightarrow S_T
\]

whose final projection is the seam carrier:

\[
 W_TW_T^*=I_{S_T}.
\]

Its initial-space defect is

\[
 D_T=I_{I_T}-W_T^*W_T.
\]

If \(W_T\) is a coisometry, then

\[
 \operatorname{rank}D_T
 =\dim I_T-\dim S_T
 =2N_+(T).
\]

Thus RH is not merely surjectivity of the saturation map. Surjectivity permits
a nonzero initial defect. The required statement is that the source-derived
comparison is unitary at every height:

\[
 D_T=0.
\]

## Finite falsifiers

Take \(I=\mathbb C^4\), \(S=\mathbb C^2\), and

\[
 W=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix}.
\]

Then \(WW^*=I_2\), so every seam state is saturated, but

\[
 \operatorname{rank}(I_4-W^*W)=2.
\]

Surjectivity therefore does not exclude one reciprocal off-seam pair.

Conversely, equal budget dimensions do not construct coherence. The map

\[
 W_0=\begin{pmatrix}1&0\\0&0\end{pmatrix}
\]

has equal source and target dimensions but is not unitary and does not
saturate the seam carrier.

## Categorical form

At every height the desired source construction must provide an exact diagram

\[
 0\longrightarrow D_T
 \longrightarrow I_T
 \mathop{\longrightarrow}^{W_T} S_T
 \longrightarrow0,
\]

with reciprocal structure on \(D_T\). The scalar budget identity computes the
class of the kernel object; it does not construct the arrow \(W_T\), its
coisometry law, or a contraction of \(D_T\).

The completed Schur return and this sequence have different jobs:

- the trace-class Schur return makes the coupled prime--boundary determinant
  well-defined;
- the rectangular comparison exposes any divisor supply not realized as seam
  germs.

They may meet in a determinant-line square, but neither may be substituted for
the other.

## Verdict

The projective-infinity port does not complete the existing square Schur block
by itself. It forces a new rectangular defect port. The exact next gate is to
derive \(W_T\) from theta/Tate boundary operations before inspecting zeros,
prove compatibility as \(T\) varies, and identify its initial defect with the
reciprocal off-seam carrier. Proving \(D_T=0\) without an independent source
law would merely restate RH.

