# Modular reflection classifies but does not select the cross-storage

## Natural reflection operator

Let

\[
\mathcal H_+
=
L^2(\mathbb R_+,\Phi(u)\,du),
\qquad
\mathcal H_-
=
L^2(\mathbb R_-,\Phi(u)\,du).
\]

Modular evenness defines the unitary reflection

\[
(Rf)(u)=f(-u).
\]

After identifying \(\mathcal H_-\) with \(\mathcal H_+\) through \(R\), the simplest source-covariant cross-storage family is

\[
K=\rho R,
\qquad
\rho\in\mathbb R.
\]

The doubled storage is

\[
P_\rho
=
\begin{pmatrix}
I&\rho R^*\\
\rho R&I
\end{pmatrix}.
\]

## Even and odd channels

In the Hadamard even/odd basis, this becomes

\[
P_\rho
\sim
\begin{pmatrix}
(1+\rho)I&0\\
0&(1-\rho)I
\end{pmatrix}.
\]

Therefore

\[
P_\rho\ge0
\]

exactly when

\[
-1\le\rho\le1.
\]

Strict positivity requires

\[
-1<\rho<1.
\]

The endpoint cases have a radical:

- \(\rho=1\) removes the odd channel;
- \(\rho=-1\) removes the even channel.

The uncoupled value \(\rho=0\) retains both channels but contains no reciprocal interference.

## Consequence

Pure modular reflection does not determine the physical cross-storage. It leaves a full interval of positive candidates.

The extremal reflection graph \(K=R\) cannot be the Xi storage because it makes the odd derivative channel radical. The opposite graph makes the even Xi channel radical. Both \(X\) and \(X'\) must survive in the Clark transfer.

Thus the missing operator is not reflection alone. It must include a nontrivial source-derived contraction on the reflection-identified fiber:

\[
K=CR,
\qquad
\|C\|\le1,
\]

with \(C\) determined by the Green boundary coupling rather than by symmetry.

## Exact checker

Checker:

`research/voevodsky/checkers/check_modular_reflection_cross_storage_family.py`

Result:

`research/voevodsky/results/modular-reflection-cross-storage-family.json`

The checker diagonalizes the family exactly.

## Control interpretation

Reflection determines the wiring diagram but not the feedback gain. Positivity bounds the gain but does not select it.

The physical gain must be fixed by matching the doubled KYP boundary form to the Clark ports

\[
E=X+iX',
\qquad
E^*=X-iX'.
\]

This matching is the same missing wall-tail or reciprocal Green cross term encountered in the prime-cell formulation.

## Next calculation

Let \(C\) act on the theta-tail fiber. Insert

\[
K=CR
\]

into the doubled KYP identity and polarize it between exponential sections \(e_s,e_t\). The boundary equations determine the matrix elements

\[
\langle e_s,Ce_t\rangle_\Phi.
\]

The acceptance test is whether these matrix elements define one bounded contraction on the dense exponential span. If they do, \(C\) extends uniquely and supplies the common storage. If the resulting Gram matrices have a negative defect or unbounded norm, this storage ansatz fails.

## Disposition

A canonical reflection exists, but it is only the carrier identification. The sought cross-storage is a reflection followed by an independently derived contraction. Symmetry and positivity alone cannot recover that contraction.
