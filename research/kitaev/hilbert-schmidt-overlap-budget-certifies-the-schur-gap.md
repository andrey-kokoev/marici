# A Hilbert–Schmidt Overlap Budget Certifies the Schur Gap

For the normalized core–tail coupling

\[
R_N=A_N^{-1/2}B_NC_N^{-1/2},
\]

the exact coercivity gate is \(\|R_N\|<1\). Operator norm may be difficult to
estimate directly from Euler atoms. In any source-authorized orthonormal core
and tail frames, write

\[
r_{ij}^{(N)}=\langle e_i,R_Nf_j\rangle,
\qquad
\beta_N=\sum_{i,j}|r_{ij}^{(N)}|^2.
\]

Then

\[
\|R_N\|\le \|R_N\|_{\mathrm{HS}}=\sqrt{\beta_N}.
\]

Consequently, the single scalar estimate

\[
\sup_N\beta_N\le 1-\varepsilon
\]

certifies a uniform Schur gap. If \(A_N\ge aI\) and \(C_N\ge cI\), then

\[
G_N\ge
\left(1-\sqrt{1-\varepsilon}\right)\min(a,c)I.
\]

More generally, any source-derived majorants \(m_{ij}\) satisfying
\(|r_{ij}^{(N)}|\le m_{ij}\) and

\[
\sum_{i,j}m_{ij}^2<1
\]

uniformly certify completion-stable no-invisibility. This turns the global
operator question into a summable incidence estimate.

## What the budget does not prove

The Hilbert–Schmidt condition is sufficient, not necessary. For
\(R=\frac12I_5\), the operator norm is \(1/2\), so the block Gram is uniformly
coercive, while \(\|R\|_{\mathrm{HS}}=\sqrt5/2>1\). A failed scalar budget is
therefore inconclusive and must not be reported as a kernel.

Nor does termwise smallness suffice. The scalar family

\[
R_N=1-N^{-1}
\]

has every finite overlap below one, but its budget approaches one and the
block Gram lower bound equals \(N^{-1}\).

## Theta/Tate compiler

Grothendieck can use this theorem only after deriving the normalized overlaps
from the frozen source Gram. If the core atoms and tail atoms admit explicit
pairings, it is enough to dominate their squared normalized incidences by one
cutoff-independent summable array with total strictly below one. Seam,
primitive, and square-current rows may contribute only when they belong to
the authorized feature family; they cannot be inserted to improve the budget
after inspecting the desired kernel.

This certificate proves source coercivity. It neither proves target
surjectivity nor constructs the rigged trace correspondence.

## Falsifiers

- The normalized incidence array is computed in incompatible cutoff frames.
- The proposed majorant depends on the cutoff.
- The squared majorants sum to one or more.
- Pointwise decay is substituted for a uniform summable domination theorem.
- Failure of the Hilbert–Schmidt test is misreported as failure of the exact
  operator-norm Schur criterion.
- An unauthorized observation row is included in the overlap budget.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
9/10. The goal was to compile the operator Schur gap into a source-local
summability problem.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. A strict square-sum budget now supplies a finite, cutoff-uniform
certificate, while an exact high-rank hostile prevents mistaking this
sufficient test for a necessary condition.
