# The full completion grade operator is a closed quadratic band operator

## Infinite coefficient carrier

Let
\[
\mathcal K=\ell^2(\mathbb N_0)
\]
with orthonormal grade basis \((\varepsilon_k)_{k\ge0}\). Define the number operator
\[
N\varepsilon_k=k\varepsilon_k
\]
and the unilateral grade shift
\[
S\varepsilon_k=\varepsilon_{k+1}.
\]

The exact completion coefficients found in the finite audit define
\[
\mathfrak J\varepsilon_k
=
(4k^2+2k)\varepsilon_k
-
(8k+6)\varepsilon_{k+1}
+
4\varepsilon_{k+2}.
\]

Equivalently,
\[
\mathfrak J
=
4N^2+2N
-
S(8N+6I)
+
4S^2.
\]

This is the full upper-grade operator whose \(3\times3\) front block is \(J_3\).

## Natural graph domain

Take
\[
\operatorname{Dom}\mathfrak J
=
\operatorname{Dom}N^2
=
\left\{
c=(c_k):
\sum_{k\ge0}k^4|c_k|^2<\infty
\right\}.
\]

The shift terms are lower order relative to \(N^2\). Indeed,
\[
\|SNc\|=\|Nc\|,
\qquad
\|S^2c\|=\|c\|,
\]
and for every \(\varepsilon>0\),
\[
\|Nc\|
\le
\varepsilon\|N^2c\|+C_\varepsilon\|c\|.
\]

Therefore
\[
-S(8N+6I)+4S^2
\]
is \(N^2\)-bounded with relative bound zero.

Since \(4N^2+2N\) is closed on \(\operatorname{Dom}N^2\), the standard lower-order perturbation theorem gives:

\[
\mathfrak J
\text{ is closed on }
\operatorname{Dom}N^2.
\]

Thus higher-grade leakage does not force an ad hoc finite truncation. It has a canonical closed graph realization.

## Core

Finite-support sequences form a core for \(N^2\), and hence for \(\mathfrak J\). The finite Jordan packets are therefore legitimate core calculations, provided they are interpreted as front blocks rather than invariant completed objects.

Cutoff restriction in grade converges in the graph norm:
\[
P_{\le K}c\longrightarrow c
\qquad
(c\in\operatorname{Dom}\mathfrak J).
\]

## Compact embedding

The graph domain of \(N^2\) embeds compactly into \(\ell^2\), because the weights \(k^4\) diverge. The graph norms of \(\mathfrak J\) and \(N^2\) are equivalent up to lower-order constants.

Hence
\[
\operatorname{Dom}\mathfrak J
\hookrightarrow
\mathcal K
\]
is compact.

This gives a discrete grade-completion geometry without asserting positivity or normality of \(\mathfrak J\).

## Parity factorization

The same coefficient operator acts on both completion characters:
\[
\mathcal K_{\mathrm{grade}}
\otimes
\left(
\mathbb C_{\mathrm{even}}
\oplus
\mathbb C_{\mathrm{odd}}
\right),
\]
with
\[
\mathfrak J\otimes I_{\mathrm{char}}.
\]

The analytic realization differs by the degree shift between even and odd Gaussian bases, but the completed grade graph is common.

## Grade-zero mode

Since
\[
\mathfrak J\varepsilon_0
=
-6\varepsilon_1+4\varepsilon_2,
\]
the grade-zero basis vector is not in the kernel of the full band operator, even though the diagonal coefficient at \(k=0\) vanishes.

This differs from the separately typed constant wall killed by the completion differential. The coefficient grade \(\varepsilon_0e^{-X}\) is a nonzero Gaussian label, not the zero-label wall. They must not be identified.

## Spectral caution

The matrix is triangular by increasing grade and has formal diagonal values
\[
4k^2+2k.
\]
But \(\mathfrak J\) is nonnormal in the raw coefficient metric. Diagonal entries alone do not prove spectral equality, positivity, or a coercive lower bound.

Any use of its resolvent must be established in the declared graph metric.

## Hostile

Treat \(J_3\) as invariant and iterate it. This suppresses the \(\varepsilon_3,\varepsilon_4,\ldots\) outputs and changes the second iterate already on \(\varepsilon_1\).

Conversely, admit the infinite matrix on bare \(\ell^2\) with full domain. The quadratic diagonal makes it unbounded, so the operator is undefined without the graph domain.

## Frontier

The full grade-completion carrier now exists as a closed operator. The next theorem is to show that theta label synthesis
\[
\bigoplus_{n\ge1}\mathcal M_n
\]
lands continuously in the common graph domain of
\[
\mathfrak J\otimes I_{\mathrm{char}},
\]
with the odd connection's \(n^{-1}\) factor retained.
