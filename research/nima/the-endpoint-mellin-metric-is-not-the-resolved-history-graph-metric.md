# The endpoint Mellin metric is not the resolved history-graph metric

## Status

Correction to `the-existing-seam-endpoint-theorem-reduces-the-resolved-graph-gate-to-one-metric-identification.md`. No RH claim.

## The typing mismatch

The existing moving-seam theorem defines a two-dimensional endpoint trace

\[
\tau_a f=(t_-(f),t_+(f))^T
\]

and its wall--jump Hadamard frame

\[
\Phi_{\partial,a}=H_\partial\tau_a.
\]

Its object-indexed metric is explicitly

\[
G_L=D_L^{-*}D_L^{-1},\qquad
D_L=\operatorname{diag}(e^{L/2},e^{-L/2}).
\]

Thus \(G_L\) is a metric on the rank-two endpoint plane. The identity

\[
D_{L\to M}^*G_MD_{L\to M}=G_L
\]

proves isometry of endpoint fibers.

By contrast, the resolved G1.1 form

\[
(1+M_\Phi^2)I+B_N^*B_N
\]

is an operator-valued graph metric on the represented incidence Hilbert space, arising from

\[
\mathcal R_Nf=(f,B_Nf,M_\Phi f).
\]

These metrics do not have the same carrier or rank. They cannot be identified merely by comparing formulas or by invoking endpoint faithfulness. The proposed “one metric identification” in the preceding packet was therefore too strong and ill-typed.

## What the existing theorem really supplies

The exact square

\[
\Phi_{\partial,b}T_{b\leftarrow a}
=
\widetilde T^\partial_{b\leftarrow a}\Phi_{\partial,a}
\]

closes the boundary observer functor. It proves that moving the cut and then taking the complete endpoint trace agrees with transporting the rank-two endpoint data. It does not state an intertwining identity for the three operators \(I,B_N,M_\Phi I\).

The statement that moving-seam transport is source-isometric in a transported saturated topology likewise controls norm growth, but does not identify the transported saturation with the newly selected resolved history dilation.

## Correct remaining local gate

One needs a mate between the endpoint square and the operator graph, not equality of their metrics. Concretely, on the common source-generated domain one must define seam-indexed history operators \(B_{N,a}\) and wall maps \(W_a\), and prove

\[
B_{N,b}T_{b\leftarrow a}=T_{b\leftarrow a}B_{N,a},
\qquad
W_bT_{b\leftarrow a}=T_{b\leftarrow a}W_a,
\]

with \(W_a\) identified after reassembly as multiplication by the fixed theta mass \(M_\Phi\). Then

\[
\mathcal R_{N,b}T_{b\leftarrow a}
=
(T_{b\leftarrow a}\oplus T_{b\leftarrow a}\oplus T_{b\leftarrow a})
\mathcal R_{N,a},
\]

and seam transport preserves the resolved Gram by unitarity.

Endpoint attachment must then be compared to the appropriate trace mate of these three ports. Existing rank-two endpoint naturality supplies the endpoint side of that diagram, but the repository evidence inspected here does not supply the two operator intertwiners above.

## Frontier

The linear seam--endpoint word remains closed. The unresolved quadratic compatibility is precisely the lift from its rank-two endpoint naturality square to the resolved three-port history graph. Radical descent follows only after that lifted graph map is shown contractive or isometric. Full-pushout closed range remains separate and open.
