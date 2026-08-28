# Endpoint and fixed-seam rows have explicit graph-dual provenance

## Question

The transpose-range theorem makes every boundary row an interpolation problem.
Which rows already have explicit representatives in the Mellin–de Rham graph
dual?

## Analytic graph domain

Let

\[
\mathcal G_{QD}=\operatorname{Dom}Q\cap\operatorname{Dom}D,
\qquad D=\partial_q,
\]

with its graph norm, and let

\[
Kc=\sum_p c_p\tau_{\log p}\Phi
\]

be smooth prime synthesis. The derivative component places
\(\mathcal G_{QD}\) inside \(H^1(\mathbb R_+)\), so endpoint evaluation is
continuous. The half-line trace estimate gives

\[
|f(0)|^2\leq \lVert f\rVert_2^2+\lVert f'\rVert_2^2.
\]

Thus \(\delta_0\in\mathcal G_{QD}'\), and its transpose row is explicitly

\[
(K'\delta_0)_p=(\tau_{\log p}\Phi)(0).
\]

This proves provenance for the endpoint of the smooth analytic synthesis. It
does not identify that row with a separately declared archimedean completion
current; such an identification still needs a source comparison map.

## Fixed seam intervals

For fixed \(L<\infty\), let \(g_L=\mathbf 1_{[0,L)}\). Since
\(g_L\in L^2\subset\mathcal G_{QD}'\),

\[
\lVert g_L\rVert_{\mathcal G_{QD}'}\leq \sqrt L.
\]

Its arithmetic transpose row is

\[
(K'g_L)_p=\int_0^L(\tau_{\log p}\Phi)(q)\,dq.
\]

Therefore every fixed seam interval has explicit analytic provenance.

## Uniformity does not follow

The bound grows with \(L\). Fixed-seam provenance does not prove continuity
of a seam whose length follows the prime cutoff, nor does it prove convergence
of the complete seam packet. That problem needs an arithmetic weight,
constructor cocycle, or cancellation law supplying a cutoff-independent dual
bound.

The primitive and prime-square rows are also not obtained from these
representatives. They remain independent transpose-range interpolation
problems.

## Finite exact model

On a finite path, let \(K\) be any synthesis matrix. Endpoint evaluation is
the first coordinate covector, and a seam of length \(L\) is the sum of the
first \(L\) coordinate covectors. Their arithmetic rows are exactly the first
row of \(K\) and the sum of its first \(L\) rows. Cauchy–Schwarz gives seam
dual cost at most \(L\).

The hostile is not failure at any fixed \(L\). It is the family of constant
unit vectors on growing intervals: the seam functional has value \(\sqrt L\),
so no cutoff-independent bound exists on the unrestricted moving-seam family.

## DPC verdict

Resolved:

- endpoint provenance for smooth analytic synthesis;
- provenance of every fixed seam interval;
- exact finite transpose identities for both rows.

Withheld:

- identification with the full archimedean completion current;
- uniform moving-seam provenance;
- primitive and prime-square provenance;
- completion of the full boundary packet.

## Verification

The checker `check_endpoint_fixed_seam_transpose_provenance.py` verifies the
finite transpose identities, the fixed-seam Cauchy bound, and the
square-root growth of the moving-seam hostile.
