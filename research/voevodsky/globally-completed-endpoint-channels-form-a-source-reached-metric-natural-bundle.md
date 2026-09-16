# Globally completed endpoint channels form a source-reached metric natural bundle

## Objective

Resolve residual channel 4 of the physical seam audit: globally completed
endpoint channels and their successor naturality.

## Endpoint object is intrinsic

On a finite logarithmic interval \(I_L=[-L,L]\), use

\[
P_{end}=\partial_x^2-\frac14.
\]

Its harmonic cokernel is

\[
\ker P_{end}^*
=
\operatorname{span}\{e^{x/2},e^{-x/2}\}.
\]

The quotient map

\[
\beta_Lg=
\left(
\widehat g(i/2),
\widehat g(-i/2)
\right)
\]

has kernel equal to the closure of the minimal shifted-Laplacian range. Thus
the two completed-zeta endpoint coordinates are selected by the bulk
differential complex rather than appended as arbitrary scalars.

Green's identity identifies endpoint evaluation of a bulk exact vector with
its boundary Wronskian. This fixes the endpoint--bulk cross term canonically.

## Correct endpoint polarity

For a convolution square, write

\[
a=\widehat g(i/2),
\qquad b=\widehat g(-i/2).
\]

The endpoint term is

\[
2\operatorname{Re}(a\bar b)
=
\binom ab^*
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\binom ab.
\]

Hence the completed endpoint is a rank-two Krein fiber with one positive even
and one negative odd line. It is not a positive scalar endpoint except after
restriction to reflection-even observers.

The support-dependent evaluation metric is

\[
G_{end}(L)=
\begin{pmatrix}
2\sinh L&2L\\
2L&2\sinh L
\end{pmatrix}.
\]

Its odd signed eigenvalue is \(2(L-\sinh L)<0\). Therefore endpoint exhaustion
cannot be represented in one fixed uniformly equivalent Euclidean metric.

## Common completed four-trace domain

Prior work constructs the weighted second-order relative graph
\(\mathcal H_{{\rm rel},a}^2\), on which

\[
\Gamma_af=
\left(
f(-\infty),
f(+\infty),
f(a),
f'(a)
\right)
\]

is continuous. These are respectively the two reciprocal endpoints, seam
value, and seam flux. Flux genuinely requires the second graph derivative;
first-order completion is insufficient.

The causal Volterra source maps continuously into this graph, so all four
traces are source reached. Euler half-density estimates make the arithmetic
prime assembly absolutely summable in the same second-order rung.

Thus endpoint existence, continuity, and global source provenance are already
constructed.

## Exact seam naturality

Let \(E_a\) be the cut source fiber and let \(R_a\) be unitary reassembly.
Moving-seam transport is

\[
T_{b\leftarrow a}=R_b^{-1}R_a,
\qquad
T_{c\leftarrow b}T_{b\leftarrow a}=T_{c\leftarrow a}.
\]

The complete endpoint trace has the forced mate

\[
\tau_bT_{b\leftarrow a}
=T^\partial_{b\leftarrow a}\tau_a.
\]

After the fixed endpoint Hadamard transform, this becomes the exact wall--jump
square

\[
\boxed{
\Phi_{\partial,b}T_{b\leftarrow a}
=
\widetilde T^\partial_{b\leftarrow a}
\Phi_{\partial,a}.}
\]

This is a source Green-trace mate, not a fitted endpoint matrix.

## Metric transport

Write

\[
D_L=\operatorname{diag}(e^{L/2},e^{-L/2}),
\qquad
G_L=D_L^{-*}D_L^{-1}.
\]

Then

\[
D_{L\to M}=D_MD_L^{-1}
\]

satisfies

\[
\boxed{D_{L\to M}^*G_MD_{L\to M}=G_L.}
\]

Therefore endpoint transport is exactly isometric as a metric bundle. Failure
of uniform equivalence to one fixed metric is not a defect; it is the reason
the endpoint must remain object-indexed.

At prime-power scale \(a_{p,k}=k\log p\), weighted Adams transport adds the
source cocycle

\[
\rho_r(p,k)=\frac1r p^{-(r-1)k/2}.
\]

The endpoint maps obey exact composition and are uniformly contractive on
nonunit grades. Fourier transport commutes with seam movement, and prime-label
cutoffs commute with endpoint pushforward and Fourier-orbit completion.

## Status of residual channel 4

The globally completed endpoint channel itself is closed:

- rank-two harmonic endpoint object: constructed;
- even/odd signed polarization: constructed;
- common endpoint/value/flux graph domain: constructed;
- source provenance and prime assembly: constructed;
- seam and Adams successor naturality: exact;
- object-indexed metric preservation: exact;
- Fourier saturation and cutoff compatibility: exact.

What remains is not endpoint construction. It is coupling this completed
boundary bundle to the even zero-trace bulk Green form. That mixed Green
identity belongs to the unresolved physical prolate-to-Tate and Sonin readout
interfaces from channels 2 and 3.

## Updated four-channel disposition

1. **Moving placement/volume:** exact affine volume cocycle and asymptotically
   natural ordered boundary — closed at asymptotic-quotient strength.
2. **Prolate-to-Tate bulk removal:** open absolute-Gram theorem
   \(R_\Lambda^*R_\Lambda\to|A_S|\).
3. **Sonin atom:** stable outside-Sonin carrier and successor constructed;
   signed Green/logarithmic-derivative map open.
4. **Completed endpoints:** source-reached metric natural bundle constructed;
   only its mixed bulk Green coupling remains open.

## Verdict

\[
\boxed{
\text{Globally completed endpoint channels and their seam naturality are
constructed.}}
\]

The four-iteration audit is complete. The remaining physical seam has two
nonredundant analytic obligations: the absolute-Gram bulk-removal theorem and
the Sonin/endpoint Green coupling.

## Repository dependencies

- `the-endpoint-pair-is-the-harmonic-cokernel-of-the-shifted-laplacian-and-green-identity-fixes-the-cross-term.md`
- `the-completed-endpoint-polarization-is-the-swap-form-with-one-positive-and-one-negative-parity-channel.md`
- `the_four_boundary_traces_share_a_weighted_second_order_relative_graph_domain_20260910.md`
- `research/nima/moving-seam-transport-and-complete-endpoint-pushforward-form-an-exact-metric-natural-transformation.md`
