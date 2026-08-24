# Exceptional magnetic coefficients are primitive path-block minors

Companion to `checkers/magnetic_path_block_checks.py` (8/8, exit 0) and
`results/magnetic_path_blocks.json`. This packet remains wholly
combinatorial: no potential, residue, logarithmic, or physical interpretation
is used.

## Canonical path polynomial

For datum vertex \((a,m)\), the folded numerator after \(g\) steps has
coefficients

\[
C_j=\binom gj(-1)^{g-j}(a)^{\overline{g-j}}
(4-a)^{\overline j},\qquad0\le j\le g.
\]

After the magnetic derivative combines adjacent targets, define

\[
\begin{aligned}
B_0&=mC_0,\\
B_j&=(m+j)C_j+(m+j-1-g)C_{j-1},\qquad1\le j\le g,\\
B_{g+1}&=mC_g.
\end{aligned}
\]

Let \(c=1-g\), \(n=a+m\), and \(q=|n-c|\). On the canonical target side
with exponent difference \(+q\), the sparse column is the Laurent polynomial

\[
K_{g,a,m}(x)=
\begin{cases}
x^{-a-g}\sum_{j=0}^{g+1}B_jx^j,&n<c,\\
-x^{-a-g+q}\sum_{j=0}^{g+1}B_jx^j,&n>c,\\
0,&n=c.
\end{cases}
\]

This is not a new model: it is an exact one-dimensional coordinate for the
cleared-denominator lattice column. Direct sparse columns and the polynomial
agree in 315 checked cases.

## Grade-2 cubic law

At \(g=2\), the path coefficients reduce to

\[
\begin{aligned}
B_0&=ma(a+1),\\
B_1&=a\big((3a-7)m-10\big),\\
B_2&=(a-4)\big((3a-5)m-10\big),\\
B_3&=m(a-4)(a-5).
\end{aligned}
\]

The factors explain the unusually short exceptional columns. At \(a=0\),
the first two entries vanish. At \(a=4\), the last two vanish. Other special
integer pole depths shorten the opposite endpoints. Exceptional syzygies
occur when these shortened, shifted paths occupy the same canonical rows.

## The first collision

For \((a,m)=(0,-2),(0,0)\), the canonical component block is

\[
\begin{pmatrix}-40&-40\end{pmatrix}.
\]

The two columns are identical, so its primitive incidence flow is
\((-1,1)\), giving

\[
1-\bar z^{-2}.
\]

## Why the second coefficients are 1, -3, 2

For the ordered source vertices

\[
(0,-8),\qquad(4,2),\qquad(6,0),
\]

the canonical \(q=7\) block is exactly

\[
A=
\begin{pmatrix}
-120&0&60\\
-160&-40&20
\end{pmatrix}.
\]

A rank-two \(2\times3\) integer matrix has a canonical null vector formed by
its signed maximal minors. Here they are

\[
\big(\det A_{23},-\det A_{13},\det A_{12}\big)
=(2400,-7200,4800).
\]

Dividing by their gcd \(2400\) gives the primitive integral flow

\[
\boxed{(1,-3,2).}
\]

Therefore the exceptional datum

\[
\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}
\]

is not fitted and its coefficients are not imported arithmetic. They are the
primitive Plucker coordinates of the local weighted path block. The block
entries themselves come from binomial move interleavings, rising-factorial
edge weights, and the final derivative weights.

## Singular-block census and scope

Across

\[
2\le g\le20,\qquad0\le a\le20,\qquad1\le q\le30,
\]

all 570 complete reflected blocks were reduced exactly. Only

\[
(g,q)=(2,1),\qquad(2,7)
\]

are singular, each with nullity one. This supplies a local theorem for both
exceptional coefficient vectors and a larger finite-range singular-block
classification.

It does not prove that every other block is injective for unbounded
\(g,a,q\). That remaining theorem is now sharply formulated: show that the
shifted path polynomials \(K_{g,a,m}\) are independent except for the two
displayed grade-2 minor degeneracies.

## Verification

`uv run --with sympy python -u research/strominger/checkers/magnetic_path_block_checks.py`
passes 8/8. Coverage: 315 path identities, 231 grade-2 cubic evaluations,
the exact E1 and E2 blocks, the raw and primitive E2 minors, and 570 reflected
component ranks.

