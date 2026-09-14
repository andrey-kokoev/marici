# The return comparison has one kernel-orientation bit

## Inputs

The established source data are:

1. the fixed-pencil primitive lattice is \(A_1^3\) with orthogonal frame \((\alpha_{12},\alpha_{13},\alpha_{14})\);
2. the \(e_6\) normal-jet row is projection to \(\alpha_{12}\), so the complementary lattice is
   \[
   L_{\rm odd}=\mathbb Z\alpha_{13}\oplus\mathbb Z\alpha_{14};
   \]
3. in the cross-pencil wall basis, the primitive \(v_{\rm alg}\) covector is \((-1,+1)\).

Assume only that the missing return comparison is an integral isometry of the primitive \(A_1^2\) complements. This is weaker than assuming a particular route swap.

## Exact classification

The Gram matrix on each complement is \(-2I_2\). Every integral isometry is a signed permutation matrix. Pulling \((-1,+1)\) back through all eight signed permutations gives

\[
(1,1),\quad(1,-1),\quad(-1,1),\quad(-1,-1).
\]

Up to overall orientation of \(v_{\rm alg}\), there are only two covectors:

\[
(1,1)
\quad\text{or}\quad
(1,-1).
\]

Their primitive kernels are respectively

\[
\mathbb Z\langle\alpha_{13}-\alpha_{14}\rangle,
\qquad
\mathbb Z\langle\alpha_{13}+\alpha_{14}\rangle.
\]

Thus all continuous or higher-rank ambiguity has disappeared. The missing return comparison contains exactly one kernel-orientation bit: does it preserve or reverse the relative orientation of the two route axes?

## Two possible full comparison matrices

After fixing the orientation of the \(e_6\) row, the two normal forms are

\[
Q_+=
\begin{pmatrix}
1&0&0\\
0&1&1
\end{pmatrix},
\qquad
Q_-=
\begin{pmatrix}
1&0&0\\
0&1&-1
\end{pmatrix}.
\]

Both have saturated image and primitive rank-one kernel. They differ only by the unresolved return-map orientation.

## Decision test

It is unnecessary to compute the entire return matrix. Transport one oriented wall route, express it in \((\alpha_{13},\alpha_{14})\), and compare its orientation with the transported second route. The determinant sign of those two columns decides:

- relative orientation preserved: one kernel line;
- relative orientation reversed: the other kernel line.

Equivalently, one signed Picard intersection or one normalized period column resolves the final bit.

Verification:

- `research/voevodsky/checkers/check_return_comparison_orientation_bit.py`
- `research/voevodsky/results/return_comparison_orientation_bit.json`
