# Gamma--prime localizer survives the first rank-one repair scan

## Question

Does the coupled gamma-plus-prime Hausdorff localizer already have negative directions orthogonal to the endpoint defect, which would kill the rank-one repair mechanism?

## Scan

Using the source formulas for the gamma heat kernel and the prime sum truncated at `n=200000`, compute

\[
L_{\Gamma+\mathbb P}(t,h)_{ij}
=
H_{\Gamma+\mathbb P}(t+(i+j)h)
-
H_{\Gamma+\mathbb P}(t+(i+j+1)h).
\]

The scan used ranks two through four at

\[
(t,h)=(0.001,0.001),
(0.01,0.005),
(0.05,0.01).
\]

Every computed gamma-plus-prime minimum eigenvalue was positive. Representative margins were approximately

\[
9.11\times10^{-2},
\quad3.30\times10^{-3},
\quad9.93\times10^{-5}
\]

at the first parameter pair for ranks two through four, and

\[
1.48\times10^{-5},
\quad1.62\times10^{-12},
\quad1.23\times10^{-20}
\]

at the last pair.

Subtracting the exact endpoint defect remained positive in every case, but several completed margins were extremely small.

## Interpretation

The simplest hostile falsifier did not occur: no scanned negative direction of the gamma-plus-prime localizer was found. The data are consistent with a positive background plus one endpoint rank-one subtraction.

The rapidly collapsing margins show that ordinary floating eigenvalues cannot certify the claim at larger rank or wider heat scale. A rigorous continuation requires interval arithmetic and the explicit prime-tail operator bound.

## Stronger target

The source theorem suggested by the scan is

\[
L_{\Gamma+\mathbb P}(t,h)\succeq0
\]

for every finite sampled packet, followed by the endpoint Schur domination

\[
(e^{h/4}-1)e^{t/4}
\langle v,L_{\Gamma+\mathbb P}^{\dagger}v\rangle
\le1.
\]

By the single-localizer telescoping theorem, these two statements would generate the whole positive semigroup.

## Boundary

This is uncertified reconnaissance. The prime sum is truncated, no interval enclosure was used, and minimum eigenvalues near `10^-20` are not reliable sign certificates. The result only keeps the rank-one mechanism alive; it does not establish any cone.

## Disposition

Retain the gamma-plus-prime PSD plus endpoint Schur repair as the preferred concrete attack. Next require certified low-rank interval tests and seek a source Gram representation of the remainder localizer rather than extending floating scans.
