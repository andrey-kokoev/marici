# Reassembly conjugation closes the resolved graph under moving-seam transport

## Status

Exact local reconciliation. This closes moving-seam covariance of the resolved analytic graph, not endpoint/bulk attachment, full-pushout closed range, G1.1, or RH.

## Reassembly transport

The moving-seam bundle has unitary reassembly maps

\[
R_a:E_a\to L^2(0,\infty),
\qquad
T_{b\leftarrow a}=R_b^{-1}R_a.
\]

The completed causal history on the common reassembled logarithmic carrier is

\[
(H_\Phi f)(u)=\int_0^\infty\Phi(r)f(u+r)\,dr.
\]

Define the seam-indexed history and output-wall operators by conjugation from this common carrier:

\[
H_{\Phi,a}=R_a^{-1}H_\Phi R_a,
\qquad
W_a=R_a^{-1}(M_\Phi I)R_a=M_\Phi I_{E_a}.
\]

No new operator is fitted here; these are the forced pullbacks along the already declared reassembly maps.

## Exact intertwiners

Associativity immediately gives

\[
\begin{aligned}
H_{\Phi,b}T_{b\leftarrow a}
&=R_b^{-1}H_\Phi R_bR_b^{-1}R_a\\
&=R_b^{-1}H_\Phi R_a\\
&=T_{b\leftarrow a}H_{\Phi,a},
\end{aligned}
\]

and, because the wall is scalar multiplication,

\[
W_bT_{b\leftarrow a}=T_{b\leftarrow a}W_a.
\]

For the resolved tail operator

\[
B_a=H_{\Phi,a}-M_\Phi I,
\]

one therefore has

\[
B_bT_{b\leftarrow a}=T_{b\leftarrow a}B_a.
\]

This is also consistent with the separately proved logarithmic translation covariance

\[
H_\Phi V_c=V_cH_\Phi.
\]

## Three-port graph covariance

Set

\[
\mathcal R_a f=(f,B_af,W_af)
\in E_a\oplus E_a\oplus E_a.
\]

Then

\[
\mathcal R_bT_{b\leftarrow a}
=
T_{b\leftarrow a}^{\oplus3}\mathcal R_a.
\]

Since \(T_{b\leftarrow a}\) is unitary,

\[
\|\mathcal R_bT_{b\leftarrow a}f\|^2
=
\|\mathcal R_af\|^2.
\]

Equivalently, in quadratic-form notation,

\[
T_{b\leftarrow a}^*
\bigl((1+M_\Phi^2)I+B_b^*B_b\bigr)
T_{b\leftarrow a}
=
(1+M_\Phi^2)I+B_a^*B_a
\]

on the transported graph domain, and hence after closure.

## Radical descent

The resolved graph form contains the identity-port norm, so its radical is already trivial on each analytic fiber. More generally, the exact isometry carries any prequotient zero-norm vector to a zero-norm vector. Thus moving-seam transport descends through any compatible source radical and extends unitarily to the resolved graph completion.

## Remaining endpoint issue

This does not identify the rank-two endpoint Mellin metric with the three-port graph metric. No such identification is needed. The existing endpoint theorem supplies

\[
\Phi_{\partial,b}T_{b\leftarrow a}
=
\widetilde T^\partial_{b\leftarrow a}\Phi_{\partial,a}.
\]

Both the endpoint observer and resolved graph are now separately natural under the same seam transport. What remains is their common Green trace mate: the source-defined identity coupling the resolved bulk/history graph to the wall--jump endpoint trace, including external boundary flux. That is exactly the bulk-plus-external-port/anti-diagonal Green gate named by the existing seam theorem.

## Verdict

Moving-seam preservation of the resolved saturated graph is closed by forced reassembly conjugation. The frontier advances from graph covariance to the Green compatibility of endpoint attachment with the resolved bulk/history form. Full analytic--arithmetic pushout closed range and global coercivity remain open.
