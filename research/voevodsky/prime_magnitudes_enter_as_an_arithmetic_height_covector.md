# Prime magnitudes enter as an arithmetic height covector

## Question

Can the Cartan--Hankel generalized spectrum predict the numerical cube-completion grades?

## Claim boundary

The index metric and probe metric determine directional and observational geometry but contain no prime magnitudes. Numerical completion grades require an additional arithmetic-height covector. The combined structure recovers every canonical grade exactly; the generalized spectrum alone cannot.

## Effective-divisor coordinates

Let \(F\) have prime-valuation basis \(f_i\), and represent a natural number by

\[
D(N)=\sum_i\nu_{p_i}(N)f_i.
\]

Multiplication becomes addition in the effective cone. Define the arithmetic-height covector

\[
\ell_p(f_i)=\log p_i.
\]

Then

\[
\ell_p(D(N))=\log N.
\]

An adjacent-prime transfer is the root

\[
\alpha_i=f_{i+1}-f_i,
\]

and its height increment is

\[
\ell_p(\alpha_i)=\log\frac{p_{i+1}}{p_i}.
\]

Thus the ordering and adjacency of primes determine the root geometry, while their magnitudes determine a linear height on that geometry.

## Canonical completion divisor

The canonical \(n\)-cube begins at

\[
D(B_n)=f_1+\cdots+f_n.
\]

Immediately before its final direction-\(n\) edge, directions one through \(n-1\) have all been applied:

\[
D_{\mathrm{source}}
=
\sum_{i=1}^{n}f_i+
\sum_{i=1}^{n-1}\alpha_i
=
f_2+\cdots+f_{n-1}+2f_n.
\]

The edge grade multiplies its source by \(p_{n+1}\), so its grade divisor is

\[
h_n=f_2+\cdots+f_{n-1}+2f_n+f_{n+1}.
\]

Therefore

\[
L_n=
\exp\ell_p(h_n)
=
p_2p_3\cdots p_{n-1}p_n^2p_{n+1}.
\]

The recurrence is

\[
\frac{L_{n+1}}{L_n}
=
\frac{p_{n+1}p_{n+2}}{p_n}.
\]

## Why the spectrum cannot supply the grade

The Cartan matrix depends only on index adjacency. The Hankel matrix depends only on shell exponents and selected character settings. Replace the numerical prime labels by any other increasing positive weights while retaining the same ordered index path. Both \(C\) and \(Q_T\) remain unchanged, but

\[
\exp\ell(h_n)
\]

changes. Hence no invariant constructed solely from the Cartan--Hankel pencil can recover \(L_n\).

The correct object is the triple

\[
(W_n,C,Q_T;\ell_p).
\]

Here \(C\) is composition geometry, \(Q_T\) is distinguishability geometry, and \(\ell_p\) is arithmetic height.

## Geometric meaning

The root metric measures how adjacent valuation transfers overlap. The probe metric measures whether a combination is resolved. The height covector assigns multiplicative cost to the effective divisor supporting a move. Cube completion is therefore a height threshold at which a new metric-null root combination acquires an admissible route realization.

This is closer to a metric-affine geometry than to a single metric space: two quadratic forms govern overlap and observation, while one linear functional governs arithmetic scale.

## Strongest falsification attempt

Verify in exact exponent vectors that the base plus the first \(n-1\) roots and the grade prime equals \(h_n\). Evaluate the resulting monomial for dimensions two through eight and compare with the closed formula and recurrence. Construct two different increasing weight sequences on the same index path and verify that their Cartan and probe matrices agree while all nontrivial completion heights differ.

## Disposition

The generalized spectrum cannot predict numerical prime grades by itself. It predicts unresolved index dimension. Prime magnitudes enter through the independent, source-derived covector \(\ell_p\), which converts the completion divisor into the observed cutoff.
