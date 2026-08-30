# The Minimum Zero Packet Has an A3 Control Lattice

## Question

What is the exact integral structure of the three defect-period modes in a
minimum four-zero spin-two packet?

## Fixed attachment and redistribution

For four positive simple zeros, the fixed Euler attachment is

\[
\mathbf 1=(1,1,1,1).
\]

Any integral redistribution preserving total degree four has the form

\[
n=\mathbf 1+\delta,
\qquad
\delta_1+\delta_2+\delta_3+\delta_4=0.
\]

The redistribution lattice is therefore the root lattice \(A_3\). A simple
root basis is

\[
e_1-e_2,
\qquad
e_2-e_3,
\qquad
e_3-e_4.
\]

Its Cartan matrix is

\[
\begin{pmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{pmatrix}.
\]

Thus the three period modes are not three unrelated scalars. They are the
three simple directions of one rank-three integral control lattice.

## Symmetry and integral residue

Permuting the four zeros preserves the fixed attachment direction and acts as
the Weyl group \(S_4\) on the redistribution lattice. The orbit of one simple
root contains all twelve \(A_3\) roots.

The Cartan determinant is four and its Smith type is

\[
(1,1,4).
\]

Equivalently, the lattice generated inside \(\mathbb Z^4\) by the diagonal
attachment and three simple redistributions has index four.

This integral fourfold residue is a lattice discriminant. It is not yet a
physical four-state sector or a selector observable; such an interpretation
would require a source-derived readout of the weight-lattice quotient.

## Prediction

A minimum generic selector attachment should organize as

```text
one fixed diagonal degree-four attachment
plus
three A3 redistribution controls
with
S4 relabeling coherence
```

Any compiler that treats the three defect modes independently and ignores the
Cartan pairing will miss their integral composition law.

## Disposition

The finite defect sector is classified as an affine \(A_3\) torsor based at
the Euler attachment. Its rank, symmetry, Cartan form, and discriminant are
forced by the minimum four-zero geometry.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/a3_zero_defect_redistribution_checks.py
```
