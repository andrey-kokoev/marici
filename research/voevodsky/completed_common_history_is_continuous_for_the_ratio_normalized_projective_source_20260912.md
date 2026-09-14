# Completed common history is continuous for the ratio-normalized projective source

## Question

Does the common-history map extend continuously from finite packets to the completed source

\[
\mathcal C_{D,\exp}=\bigcap_{\delta>0}\ell^1(E_D,e^{\delta\overline W})
\]

and land in \(L^2(\mathbb R_+)\)?

## Claim boundary

Yes on every fixed ratio block, using the actual consecutive-prime catalogue and the ratio-normalized grade

\[
\overline W(j,k)=\log(kp_jp_{j+1}).
\]

The proof uses a columnwise estimate and therefore avoids the cutoff support factors \(L_D\) and \(S_D\) in the earlier finite-dimensional bound. It assumes the recorded completed atom satisfies \(\Phi_1\in L^2(\mathbb R)\cap L^\infty(\mathbb R)\). No topology over the unbounded collection of all ratio blocks is asserted.

## Column estimate

For one interval \(I_e=[A_e,B_e]\), let \(\ell_e=|B_e-A_e|\) and

\[
b_{e,D}(s)=\int_{I_e}\Phi_1(v)\Phi_1(v+s+D)\,dv,
\qquad s\geq0.
\]

Cauchy--Schwarz on \(I_e\) gives

\[
|b_{e,D}(s)|^2
\leq
\|\mathbf1_{I_e}\Phi_1\|_2^2
\int_{I_e}|\Phi_1(v+s+D)|^2\,dv.
\]

The first factor is at most \(\ell_e\|\Phi_1\|_\infty^2\). Tonelli and extension of the shifted half-line integral to the full line give

\[
\int_0^\infty\int_{I_e}|\Phi_1(v+s+D)|^2\,dv\,ds
\leq
\ell_e\|\Phi_1\|_2^2.
\]

Therefore, uniformly in the edge, cutoff, and ratio shift,

\[
\|b_{e,D}\|_{L^2(\mathbb R_+)}
\leq
\|\Phi_1\|_\infty\|\Phi_1\|_2\ell_e.
\]

## Projective-source bound

For consecutive primes \(p_j<p_{j+1}\),

\[
\ell_e=\log(p_{j+1}/p_j)
\leq \overline W(e)
\leq \delta^{-1}e^{\delta\overline W(e)}
\]

for every \(\delta>0\). The Hilbert-space triangle inequality then yields, for every finite packet,

\[
\|B_Dc\|_{L^2(\mathbb R_+)}
\leq
\frac{\|\Phi_1\|_\infty\|\Phi_1\|_2}{\delta}
q_\delta(c).
\]

The constant is independent of the cutoff and of \(D\).

## Extension

Finite-support packets are dense in every weighted \(\ell^1\) seminorm by tail truncation. Since one seminorm bound suffices for continuity into a normed target, \(B_D\) extends uniquely to a continuous linear map

\[
\widehat B_D:\mathcal C_{D,\exp}\longrightarrow L^2(\mathbb R_+).
\]

The reciprocal component has the same estimate, so the paired map into two copies of the half-line space has constant at most \(\sqrt2\|\Phi_1\|_\infty\|\Phi_1\|_2/\delta\).

## Disposition

The original completion question is resolved affirmatively for each fixed ratio block and the explicit source-derived normalized grade. The earlier cutoffwise estimate remains valid but is not the estimate needed for completion. Remaining questions concern the topology across all ratio blocks and calibrated norms on the independent cycle port, not existence or continuity of the completed common-history map.
