# Erratum: static torsion does not exclude zero cusp parity

Prior research leaves all four source-supported cusp classes open:

\[
(a,b)\in(\mathbb Z/2)^2.
\]

The regular complement is indeed torsion-free:

\[
H^2(S\setminus D;\mathbb Z)\cong\mathbb Z^9.
\]

However, the parity is not the isomorphism class of this underlying abelian group. It is the second off-diagonal column of the integral monodromy logarithm

\[
N=\begin{pmatrix}0&B\\0&C-I\end{pmatrix},
\qquad C-I=\begin{pmatrix}0&2\\0&0\end{pmatrix},
\]

modulo changes of integral splitting. Such changes alter the relevant column of \(B\) by an even kernel vector. Thus the source-supported invariant lies in

\[
[B]_{\rm source}\in
\langle e_6,v_{\rm alg}\rangle/2
\langle e_6,v_{\rm alg}\rangle
\cong(\mathbb Z/2)^2,
\]

while the middle lattice remains free for every value of \(B\), including \(B=0\).

The presentation

\[
L_{a,b}=
\frac{\mathbb Z\langle e_6,v_{\rm alg},m\rangle}
{\langle2m-ae_6-bv_{\rm alg}\rangle}
\]

cannot be identified with the full regular complement lattice without an additional comparison theorem. Using its torsion to eliminate \((0,0)\) was therefore invalid. The proviso in the earlier torsion packet was not established.

This agrees with the frozen prior results:

- `research/benincasa/results/integral-del-pezzo2-gysin-lattice.json`: static lattice torsion cannot identify the cusp parity;
- `research/benincasa/results/integral-cusp-source-provenance-gate.json`: all four classes remain open;
- `research/nima/integral-rank9-cusp-extension-class.md`: the invariant is a monodromy/splitting class;
- `research/nima/results/integral-rank9-cusp-extension-class.json`: four source-supported classes.

## Correct disposition

\[
(a,b)\in\{(0,0),(1,0),(0,1),(1,1)\}.
\]

The files claiming that ambient torsion-freeness excludes \((0,0)\) are superseded by this erratum. A globally normalized integral thimble or equivalent Picard--Lefschetz/Gysin comparison is still required.
