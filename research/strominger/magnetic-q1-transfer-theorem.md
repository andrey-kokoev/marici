# The q=1 magnetic component is triangular for every grade

Companion to checkers/magnetic_q1_transfer_checks.py (6/6, exit 0) and
results/magnetic_q1_transfer.json.

## Nested Hall minor

Fix reflection distance \(q=1\). Order source columns by

\[
(0,-),(0,+),(2,-),(2,+),\ldots,(2k,-),(2k,+).
\]

Choose the target rows

\[
1,2;\quad -2-g,-1-g;\quad -4-g,-3-g;\quad\ldots;\quad
-2k-g,-2k-g+1.
\]

When pole depth \(a=2k\) is appended, the two new rows lie strictly below the
support of every old column. The nested minor therefore has block form

\[
H_{g,k}=\begin{pmatrix}H_{g,k-1}&B_{g,k}\\0&Q_{g,k}\end{pmatrix}.
\]

## Boundary determinants

Write \(a=2k\). The two reflected columns begin one row apart. Their boundary
block is triangular, and the path endpoint coefficient

\[
B_0=m(-1)^g a^{\overline g}
\]

gives

\[
\det Q_{g,k}
=-(a+g)(a+g-2)\left(a^{\overline g}\right)^2.
\]

The \(a=0\) endpoint uses the opposite path end and has determinant

\[
\det H_{g,0}
=-g(g-2)\left(4^{\overline g}\right)^2.
\]

Consequently, for every \(g\ge3\) and \(k\ge0\),

\[
\det H_{g,k}
=-g(g-2)\left(4^{\overline g}\right)^2
\prod_{\ell=1}^{k}
\left[
-(2\ell+g)(2\ell+g-2)
\left((2\ell)^{\overline g}\right)^2
\right]\ne0.
\]

This proves full column rank of every \(q=1\) component at arbitrary grade and
arbitrary pole cutoff.

## Exceptional locus

At \(g=2\), the base factor \(g-2\) vanishes. Thus the known grade-two
\(q=1\) collision is not an accidental small matrix: it is exactly the
singular initial transfer step. For \(g\ge3\), every base and transfer factor
is nonzero.

## Verification and scope

The checker proves the endpoint formulas symbolically and cross-checks 110
exact matrices over \(3\le g\le12\), \(0\le k\le10\). It also checks the
lower-left support block vanishes at every tested extension.

This theorem covers all grades and cutoffs at \(q=1\). Reflection distances
\(q>1\) retain nested Hall row sets in the finite scan but generally lose
literal block triangularity, so they require a wider boundary state or Schur
transfer.

