# Perron–Schur Multipliers Optimize Absolute-Incidence Certificates

Let \(M=|R|\) be the entrywise absolute normalized incidence matrix and form
the symmetric bipartite matrix

\[
K=\begin{pmatrix}0&M\\M^T&0\end{pmatrix}.
\]

For positive vectors \(p,q\), the inequalities

\[
Mq\le\rho p,
\qquad
M^Tp\le\rho q
\]

are equivalent to

\[
K\binom pq\le\rho\binom pq.
\]

The Perron–Frobenius/Collatz bound then gives

\[
\|R\|\le\|M\|=\rho(K)\le\rho.
\]

Conversely, in finite dimension, if \(\|M\|<1\), then for every
\(\rho\) strictly between \(\|M\|\) and one there are strictly positive
multipliers satisfying the inequalities. For example, one may take

\[
w=(\rho I-K)^{-1}\mathbf1>0.
\]

Thus positive multipliers are a complete finite certificate for the
absolute-incidence operator bound. They optimize the unweighted row/column
test without changing the incidence matrix.

## Strict typing of the multipliers

These multipliers are dual proof witnesses, not new observations, source
constructors, or physical frame choices. Cutoff-dependent multipliers are
legitimate if they certify the same uniform \(\rho<1\) on the native Gram
matrices. No condition-number bound is needed for that inference because the
conclusion is already an operator-norm bound in the native Hilbert norm.

If instead the weighted coordinates are declared to be the completed source
norm, then uniform equivalence to the frozen source topology is a separate
mandatory theorem. Confusing these two uses either rejects valid certificates
or silently changes the problem.

## Exact improvement over crude loads

For

\[
M=\begin{pmatrix}0&0&1/10\\0&2/5&4/5\end{pmatrix},
\]

the unweighted row/column product is \(27/25>1\), so the crude test fails.
Nevertheless

\[
\|M\|^2=\frac{81+\sqrt{6497}}{200}<\frac{81}{100}.
\]

At \(\rho=9/10\), the exact positive multiplier

\[
(p,q)=left(445/4,1100;10/9,490,3965/4\right)
\]

satisfies \(K(p,q)^T=\rho(p,q)^T-\mathbf1\), giving a strict certificate.

## Irreducible loss from absolute values

Multiplier optimization does not recover phase cancellation. For the signed
Hadamard coupling \(R=H_4/4\), \(\|R\|=1/2\), but
\(|R|\) is the all-ones matrix divided by four and has norm one. No positive
absolute-incidence multiplier can certify a strict gap. The next improvement,
if needed, must retain source-derived phases rather than optimize positive
weights further.

## Falsifiers

- The certified \(\rho_N\) approaches one with the cutoff.
- The multiplier inequalities use a matrix different from the frozen native
  absolute-incidence matrix.
- A proof multiplier is claimed to be a physical or source-authorized port.
- A multiplier-defined topology is used without uniform equivalence to the
  source topology.
- Failure of the absolute-incidence certificate is reported as failure of the
  phase-sensitive operator Schur gap.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to optimize the local incidence compiler and type its
weights correctly.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Positive multipliers are complete for the finite absolute-incidence
problem, the crude-load false negative is repaired, and the remaining loss is
located exactly at phase erasure.
