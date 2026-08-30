# The Fifth Channel Splits Tail-Area and Wall Duals

## Operator stimulus

After the determinant-dual fourth channel repaired the relative spectrum but
failed to give a common stepwise metric, the operator asked whether another
comparison channel was required.

Yes. The invariant coflag shows that the full determinant dual had collapsed
two independently typed comparison channels.

## Source splitting

The three-dimensional carrier has an invariant tail plane \(T\) and a wall
quotient \(W\):

\[
0\longrightarrow T\longrightarrow V\longrightarrow W\longrightarrow0.
\]

The tail determinant scales by

\[
b_j=\frac32\left(j+\frac54\right),
\]

while the wall quotient scales by \(c\). The full determinant is \(b_jc\).
Its inverse therefore tensors together two distinct dual responses:

\[
(b_jc)^{-1}=b_j^{-1}c^{-1}.
\]

The comparison carrier should retain \(b_j^{-1}\) and \(c^{-1}\) separately.

## Five-channel lift

Define

\[
\widetilde M_j=
\operatorname{diag}(M_j,b_j^{-1},c^{-1}).
\]

The relative map between degrees zero and one is

\[
\widetilde R=
\begin{pmatrix}
9/5&-14/5&-4/(5c)&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&5/9&0\\
0&0&0&0&1
\end{pmatrix}.
\]

Its spectrum is

\[
\{1,1,1,9/5,5/9\}.
\]

The tail expansion \(9/5\) now has its reciprocal contraction \(5/9\), while
the wall comparison supplies the central fixed mode required in odd
dimension.

## Relative quadratic form

Solving

\[
\widetilde R^TQ\widetilde R=Q
\]

produces a family whose determinant is

\[
-c^2u^2
\left(
-r^2a+2rbd+sae-sb^2-d^2e
\right).
\]

Here \(a,b,d,e,r,s,u\) are free real parameters in the invariant symmetric
form. The polynomial is not identically zero, so nondegenerate invariant
forms exist.

## Meaning

The fifth coordinate is not another physical wall. It is the second
comparison channel required by the source coflag:

- one comparison channel dualizes oriented tail area;
- one comparison channel dualizes the wall quotient.

The earlier inverse-determinant coordinate was their scalar product after
type erasure. Splitting it restores the incidence information needed to see
why the relative spectrum closes.

This is a concrete instance of the programme's durable rule: a scalar product
of typed channels can be faithful to total weight while erasing how that
weight is distributed among source strata.

## Remaining boundary

The result establishes a five-dimensional relative orthogonalization for the
first degree comparison. It does not yet prove that all relative degree maps
preserve one common form, nor that the two comparison channels arise as
continuous operators on the completed Mellin strip.

The next test is the all-degree relative family

\[
\widetilde M_{j+1}\widetilde M_j^{-1}.
\]

If one source-derived form works for every \(j\), the five-channel geometry is
global along the degree direction. If not, its metric still moves and a
second transport direction or larger dual module is required.

## Verification

The checker
`research/grothendieck/checkers/fifth_channel_split_comparison.py` verifies
the split lift, reciprocal spectrum, invariant-form family, and existence of
a nondegenerate specialization exactly.
