# A self-adjoint Green return cannot be strictly one-way triangular

## Question

Can source-grade filtration preservation of the coupling alone force reverse triangularity of the positive Green Schur return?

## Structural no-go

The normalized Green return has the form

\[
K=A^{-1/2}CD^\dagger C^*A^{-1/2}
\]

and is positive self-adjoint on its reduced support. For complementary grade projectors \(P_+,P_-\),

\[
(P_-KP_+)^*=P_+KP_-.
\]

Therefore a one-way condition

\[
P_-KP_+=0
\]

automatically kills the opposite block as well. On a self-adjoint return, “reverse triangularity” is not a directional condition; it means the grade splitting reduces \(K\), so \(K\) is block diagonal.

## Coupling hostile

Even if the raw coupling preserves a one-step flag, Schur return can recreate both directions. Take

\[
C=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad D=I,
\qquad A=I.
\]

For the flag \(F^1=\operatorname{span}(e_1)\), \(C F^1\subseteq F^1\). But

\[
K=CC^*
=\begin{pmatrix}2&1\\1&1\end{pmatrix}
\]

is positive definite and has

\[
P_-KP_+\ne0.
\]

The adjoint factor \(C^*\) restores the reverse-grade path. Thus filtration preservation of \(C\) alone does not survive elimination.

## Consequence

The handoff target must be strengthened. It is insufficient to prove that the physical coupling or history map is triangular. One must prove one of:

1. the grade subspaces reduce the complete normalized return;
2. \(C^*A^{-1/2}\) and \(D^\dagger\) preserve compatible orthogonal grade splittings;
3. the off-diagonal return blocks cancel by an independently sourced orthogonality law.

If the physical tail/PV sector genuinely mixes primitive and square grades, exact reverse triangularity of positive \(K\) is impossible. The viable target is then a strict norm bound \(\|K\|<1\), not one-way triangularity.

## Verification

`research/aspect/checkers/check_selfadjoint_return_filtration.py` verifies flag preservation by \(C\), positivity of \(CC^*\), recreation of the reverse block, and adjoint pairing of both off-diagonal blocks using exact rationals.

## Disposition

Reject raw-coupling filtration preservation as sufficient. The next discriminating test is whether the physical grade decomposition reduces the full normalized return. If not, abandon reverse triangularity for the Green energy return and test the quantitative strict-return margin directly.
