# Flip-protected kinetic interface: WP667

## Kinetic classification

For two labelled real triplets, the general \(SO(3)\)-invariant quadratic
kinetic term has species Gram

\[
K=\begin{pmatrix}Z_n&Z_x\\Z_x&Z_m\end{pmatrix}.
\]

Requiring invariance under both independent flips \(n\mapsto-n\) and
\(m\mapsto-m\) forces

\[
Z_x=0.
\]

For \(Z_n,Z_m>0\), the label-preserving canonical map is exactly

\[
C=\operatorname{diag}(Z_n^{-1/2},Z_m^{-1/2}),
\qquad C^TKC=I.
\]

Thus a disjoint messenger model whose fermion charges extend both flips has a
well-defined source-to-canonical interface without mixing the two frame axes.

## Hostile unprotected case

Without the flips, the positive Gram

\[
K=\begin{pmatrix}2&1\\1&2\end{pmatrix}
\]

is legal and has determinant three. Canonicalization then mixes the labelled
triplets, so the separate \(J_n,J_m\) word interpretation is not preserved.

## Disposition

WP666's interface can be repaired algebraically, but only after the messenger
source declares charges implementing both flips. The repair diagonalizes and
normalizes the kinetic term; it does not fix either canonical Yukawa. Their
two-coordinate Jacobian remains rank two.

This is a conditional source rigidifier, not a selector. The next gate is an
explicit messenger charge table followed by canonical Yukawa running and
threshold decoupling.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp667_flip_protected_kinetic_interface.py

Generated result: results/wp667_flip_protected_kinetic_interface.json.
