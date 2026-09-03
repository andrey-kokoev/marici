# Fredholm scalar gate for the two-grade return

## Question

Can the strict two-grade Green-return condition be tested from scalar invariants better matched to trace and determinant source constructions?

## Exact reduction

Let \(K\ge0\) be the normalized return on the primitive-square plane and set \(H=I-K\). Since \(H\) is Hermitian of rank two,

\[
H>0
\quad\Longleftrightarrow\quad
\operatorname{tr}H>0
\text{ and }
\det H>0.
\]

Therefore

\[
\|K\|<1
\quad\Longleftrightarrow\quad
\operatorname{tr}K<2
\text{ and }
\det(I-K)>0.
\]

For \(K=\begin{psmallmatrix}a&z\\\bar z&b\end{psmallmatrix}\), the determinant is

\[
\det(I-K)=(1-a)(1-b)-|z|^2,
\]

recovering the mixed-slack criterion without choosing a triangular direction.

## Uniform consequence

When \(H>0\), both eigenvalues of \(H\) are at most one because \(K\ge0\). Hence

\[
\det(I-K)
=
\lambda_{\min}(H)\lambda_{\max}(H)
\le
\lambda_{\min}(H).
\]

A prime-uniform determinant bound \(\det(I-K_p)\ge\varepsilon>0\), together with \(\operatorname{tr}K_p<2\), yields the same uniform return margin \(1-\|K_p\|\ge\varepsilon\). This exposes a scalar Fredholm target potentially more accessible than all three matrix entries.

## Hostile boundary

Nonvanishing determinant alone is insufficient. For \(K=2I\), one has \(K\ge0\) and \(\det(I-K)=1\), but \(\|K\|=2\). The trace-sign gate excludes this superunit component. At the terminal mixed boundary, \(\det(I-K)=0\).

The determinant must be the physical reduced determinant of the complete return. A formal Euler factor or arithmetic determinant with no proved comparison to \(K_p\) cannot substitute for it. Voevodsky's source audit further blocks cross-prime Markov composition: absent prime diagonality and a nonadjacent Green-return factorization, pointwise scalar gates cannot be promoted to a joint completion theorem.

## Verification

`research/aspect/checkers/check_two_grade_fredholm_gate.py` verifies strict, unit-boundary, mixed-failure, and positive superunit cases with exact rational arithmetic.

## Disposition

The physical handoff can be weakened from reconstructing every entry to deriving two scalar invariants: \(\operatorname{tr}K_p\) and \(\det(I-K_p)\). Uniform confinement still requires a source-derived comparison to the complete physical return and a uniform determinant lower bound; current arithmetic port data supplies neither.
