# The four boundary traces share a weighted second-order relative graph domain

## Question

Do reciprocal endpoints, seam value, and seam flux belong to one completed trace domain, rather than existing only as separate finite-source coordinates?

## Claim boundary

A weighted second-order relative Sobolev graph supplies a common continuous four-trace map and is reached continuously by one derivative-regular Volterra source. Existing finite-order Euler summability transports the source-generated packets into this domain. This proves trace continuity and source-side provenance, not membership of unrelated arithmetic rows in an external analytic transpose range.

## Problem

The first-order relative history graph controls endpoint traces and seam values, but point evaluation of the derivative is not continuous in an \(H^1\)-type norm. Treating seam flux as another first-order trace would be an unproved promotion.

## Bold conjecture

The existing first-order relative graph already carries all four traces continuously.

## Named rivals

1. Seam flux requires one additional graph derivative.
2. Flux exists only on the theta-generated finite-dimensional packet and has no completed trace extension.
3. A second-order graph supplies flux but destroys reciprocal reflection or moving-seam covariance.

## Second-order relative graph

Fix \(\epsilon>0\) and

\[
w_a(u)=(1+|u-a|)^{1+\epsilon}.
\]

Define \(\mathcal H_{{\rm rel},a}^2\) to consist of functions \(f\) such that:

- \(f\) and \(f'\) are locally absolutely continuous;
- \(f',f''\in L^2(\mathbb R,w_a\,du)\);
- \(f(-\infty)\) and \(f(+\infty)\) exist.

Use the graph norm

\[
\|f\|_{{\rm rel},a,2}^2
=
|f(-\infty)|^2+|f(+\infty)|^2
+
\int_{\mathbb R}w_a(u)
\bigl(|f'(u)|^2+|f''(u)|^2\bigr)\,du.
\]

This is a Hilbert graph completion of the smooth source core.

## Trace theorem

Since \(w_a\ge1\), one has \(f'\in H^1(\mathbb R)\). The one-dimensional Sobolev trace theorem gives

\[
|f'(a)|
\le C\bigl(\|f'\|_2+\|f''\|_2\bigr)
\le C\|f\|_{{\rm rel},a,2},
\]

with \(C\) independent of \(a\) because the weights are translated together with the seam.

Also \(w_a^{-1}\in L^1\), so

\[
|f(a)-f(-\infty)|
\le
\|w_a^{-1/2}\|_2\|w_a^{1/2}f'\|_2.
\]

Therefore the complete trace

\[
\Gamma_a f
=
\bigl(P(f),Q(f),M_a(f),J_a(f)\bigr)
=
\bigl(f(-\infty),f(+\infty),f(a),f'(a)\bigr)
\]

is continuous

\[
\Gamma_a:\mathcal H_{{\rm rel},a}^2\longrightarrow\mathbb C^4.
\]

This rejects the bold conjecture at its exact boundary: the endpoint and value coordinates extend at first order, while flux requires the second-order graph.

## Volterra source

Let

\[
\mathcal E_{w,a}^1
=
\{g:g,g'\in L^2(\mathbb R,w_a\,du),\ g\in L^1(\mathbb R)\}
\]

with its graph norm. For causal Volterra history

\[
(H_ag)(u)=\int_{-\infty}^u g(v)\,dv,
\]

one has

\[
(H_ag)'=g,
\qquad
(H_ag)''=g'.
\]

Hence

\[
H_a:\mathcal E_{w,a}^1\longrightarrow\mathcal H_{{\rm rel},a}^2
\]

is continuous. Its traces are

\[
P(H_ag)=0,
\qquad
Q(H_ag)=\int g,
\qquad
M_a(H_ag)=\int_{-\infty}^ag,
\qquad
J_a(H_ag)=g(a).
\]

Thus seam flux is source-reached by evaluation of the pre-history density, not added as an independent fitted coordinate.

## Reflection and seam transport

Reflection about the seam,

\[
(R_af)(u)=f(2a-u),
\]

preserves the graph norm, exchanges \(P\) and \(Q\), fixes \(M_a\), and reverses \(J_a\). Translation of both the function and weight gives an isometry

\[
T_{b\leftarrow a}:\mathcal H_{{\rm rel},a}^2
\longrightarrow
\mathcal H_{{\rm rel},b}^2
\]

satisfying

\[
\Gamma_bT_{b\leftarrow a}
=
T_{b\leftarrow a}^{\partial}\Gamma_a.
\]

The four-port reciprocal and moving-seam signs therefore persist on the completed trace domain.

## Arithmetic assembly

Prior Euler-weighted estimates show that source-generated local packets and their finite graph derivatives grow at most polynomially in \(\log p\), while the mixed weight is \(p^{-3/2-\sigma}/2\). Consequently their prime assembly is absolutely summable in this fixed second-order Green rung. This supplies cutoff-compatible source packets in \(\mathcal H_{{\rm rel},a}^2\).

## Boundary form

The joint value--flux trace on each reciprocal deficiency channel has the canonical Green form

\[
\omega((M,J),(\widetilde M,\widetilde J))
=
J\widetilde M-M\widetilde J.
\]

For two reciprocal channels, the direct sum gives the four-dimensional joint trace space. Reflection reverses each oriented flux and exchanges the endpoint channels, preserving the declared total pseudoscalar up to its source orientation convention.

## Disposition

All four boundary ports have one completed source-reached trace domain: the weighted second-order relative graph. The seam-flux provenance gap was a derivative-order mismatch, not a missing primitive observer. The remaining transpose-range problem concerns whether externally declared arithmetic currents arise from functionals on the same analytic Green graph; it no longer concerns existence or continuity of the four trace coordinates themselves.
