# Source projective completion supersedes the synthetic edge weight

## Question

Does prior research already provide a source topology and cutoff-natural completed cycle observer, making the geometric Hilbert edge budget unnecessary?

## Claim boundary

Yes for the source edge and cycle topology. The greedy-global-forest packet constructs a projective exponential completion and continuous cutoff-natural cycle port. The remaining comparison to half-line \(L^2\) reduces to one explicit edge-length-versus-grade bound. This does not identify a physical covariance or a Hilbert norm intrinsic to the source.

## Existing source completion

For a source-fixed edge order and proper grade \(W(e)\), prior research defines

\[
q_\delta(c)=\sum_e |c_e|e^{\delta W(e)},
\qquad
\mathcal C_{D,\exp}=\bigcap_{\delta>0}\ell^1(E_D,e^{\delta W}).
\]

The greedy forest is inherited exactly by every initial cutoff. Its chord projection satisfies

\[
z_\delta(Z_Dc)\leq q_\delta(c),
\]

and \((B_D,Z_D)\) is injective on the completed source. This already supplies the cutoff transition and completed cycle topology sought in the recent synthetic-weight construction.

## Hilbert comparison

For every \(\delta>0\), there is a continuous inclusion

\[
\mathcal C_{D,\exp}\longrightarrow
H_\delta:=\ell^2(E_D,e^{2\delta W}),
\]

because

\[
\left(\sum_e|c_e|^2e^{2\delta W(e)}\right)^{1/2}
\leq q_\delta(c).
\]

This gives a source-indexed family of Hilbert comparison targets without choosing the geometric budget \(2^{-(n+1)}\).

For the history columns \(b_e=B_D\mathbf e_e\), the earlier half-line estimate gives

\[
\|b_e\|_{L^2(\mathbb R_+)}
\leq
\ell_e\,\|\Phi_1\|_\infty\|\Phi_1\|_2.
\]

If there exist \(\delta>0\) and \(C_\delta<\infty\) such that

\[
\ell_e\leq C_\delta e^{\delta W(e)}
\quad\text{for every edge }e,
\]

then

\[
\|B_Dc\|_2
\leq
C_\delta\|\Phi_1\|_\infty\|\Phi_1\|_2 q_\delta(c).
\]

Thus \(B_D\) is continuous from the projective source to half-line \(L^2\). No summability count for the edge set is needed because the source norm is weighted \(\ell^1\).

## Exact remaining source datum

For interval edges with endpoints \(A_e=\log(np)\) and \(B_e=\log(nq)\),

\[
\ell_e=|\log(q/p)|.
\]

The recorded projective packet does not state how its proper grade \(W(e)\) bounds this interval length. Establishing a single exponential-order inequality above would complete continuity of the source history into the existing half-line Hilbert carrier.

The arithmetic-loading majorant is relevant but not identical: it controls prime-weighted feature sums, not the unweighted operator norm of every edge-history column.

## Correction to the synthetic branch

The geometric edge budget in `weighted-common-history-cycle-completion.v1.json` remains a valid synthetic Hilbert model, but it is not the preferred source topology. The source projective Fréchet topology and greedy forest already solve completion and cutoff naturality. Only the half-line comparison bound and source authority for the edge order/grade remain.

## Disposition

Use \(\mathcal C_{D,\exp}\), not the synthetic weighted \(\ell^2\), as the source completion. The next executable test is to recover the exact definition of \(W(e)\) and prove or refute exponential domination of \(|\log(q/p)|\).
