# Involutive orientation-reversing channel monodromy forces a Möbius summand

## Theorem

Let \(X\) be a cyclic 2-Segal object whose cyclic realization carries a rank-two real orthogonal channel local system \(V\) over its arity circle. Suppose the circle holonomy \(H\) satisfies

\[
H^2=1,
\qquad
\det H=-1.
\]

Then \(V\) splits orthogonally as

\[
V\cong\underline{\mathbb R}\oplus\mathcal M,
\]

where the first summand is a trivial real line and \(\mathcal M\) is a Möbius line. In particular, \(V\) is nonorientable.

If, in addition, \(H\) exchanges two distinct local channel lines, those lines do not descend separately around the circle. Only their unordered pair descends.

## Proof

Since \(H\) is orthogonal and involutive, its eigenvalues lie in \(\{1,-1\}\), and its eigenspaces are orthogonal. The negative determinant implies that the two eigenvalues have opposite signs. Both eigenspaces are therefore one-dimensional.

The positive eigenline has trivial circle holonomy and produces the trivial line bundle. The negative eigenline has holonomy \(-1\) and produces the Möbius line bundle. Their direct sum is the original local system.

If \(H\) exchanges two local channel lines, parallel transport sends each one to the other after one circuit. Neither can define a global line subbundle under its original label, although the unordered pair is preserved.

For the signed exchange used in the \(C_2\) model,

\[
H=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix}.
\]

The channel difference spans the trivial eigenline, and the channel sum spans the Möbius eigenline.

## Why the unrestricted statement is false

A bare 2-Segal object does not force this geometry. The terminal 2-Segal object supplies no rank-two channel local system. Even after adding a circle and a rank-two bundle, different holonomies give different results:

- identity holonomy gives two trivial lines;
- negative identity holonomy gives two Möbius lines whose sum is orientable;
- quarter-turn holonomy has order four and no real eigenline splitting.

Thus cyclicity, the rank-two orthogonal local system, involutivity, and negative determinant are substantive hypotheses rather than consequences of the bare 2-Segal laws.

## Verification

```text
python research/voevodsky/checkers/check_mobius_monodromy_classification.py
```

The checker exhausts all eight signed orthogonal \(2\)-by-\(2\) matrices, verifies the four involutive negative-determinant cases, and records the sharp hostile holonomies.

Artifacts:

- `research/voevodsky/checkers/check_mobius_monodromy_classification.py`
- `research/voevodsky/results/mobius_monodromy_classification.json`
