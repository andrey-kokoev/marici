---
author: marici.Benincasa
---

# 1494 — One Loop Pushes the Cubic Initial Packet into an Independent Quadratic Statistical Block

## Status

Primary-source coefficient-mixing result from Collins--Holman--Vardanyan,
arXiv:1408.4801v1, Eqs. (5.5)--(5.9).

## Source one-loop mechanism

The finite-time one-loop two-point function contains two insertions drawn
from the bulk cubic Hamiltonian and Entry 1492's cubic initial action. To
cancel the displayed quadratic divergence in the initial time, the source
introduces a new quadratic initial action

\[
\begin{aligned}
S_0^{(2)}=\frac12\bigl[
&\langle\zeta_+,A\zeta_+\rangle
-\langle\zeta_-,A^*\zeta_-\rangle\\
&+2i\langle\zeta_+,B\zeta_-\rangle
\bigr].
\end{aligned}
\]

Here \(A=A_R+iA_I\), while \(B\) is the cross-branch density kernel. The
matching condition gives, at the calculated divergent order,

\[
\boxed{A_R=0,}
\]

and fixes nontrivial \(A_I\) and \(B\) separately by the source loop
integrals.

## Exact Keldysh decomposition

For self-adjoint translation-invariant kernels and

\[
\zeta_\pm=\zeta_c\pm\frac12\zeta_q,
\]

one obtains

\[
\boxed{
S_0^{(2)}
=
\langle\zeta_c,A_R\zeta_q\rangle
+i\langle\zeta_c,(A_I+B)\zeta_c\rangle
+\frac{i}{4}
\langle\zeta_q,(A_I-B)\zeta_q\rangle.
}
\]

The three terms have contour-conormal grades \(1,0,2\), respectively.

Since the source matching sets \(A_R=0\) at this order, the generated
quadratic correction is deck even:

\[
\boxed{
\operatorname{gr}_\Delta S_{0,\mathrm{generated}}^{(2)}
=
\operatorname{gr}_\Delta^0
\oplus
\operatorname{gr}_\Delta^2.
}
\]

It is statistical/density-matrix data, not a causal action difference.

## Failure of cubic closure

Entry 1492's four-grade cubic packet is not closed under the one-loop
two-point pushforward. The loop lowers boundary field degree and generates an
independent quadratic coefficient object:

\[
\boxed{
\mathcal C_{S_0^{(3)}}
\longrightarrow
\mathcal C_{S_0^{(2)},\mathrm{stat}}^{(0,2)}.
}
\]

The map is source-defined by the finite-time matching calculation. It must
not be replaced by an endomorphism of the cubic kernel \(C\).

## Trace interpretation

The grade-zero term survives diagonal restriction:

\[
\Delta^*S_0^{(2)}
=i\langle\zeta_c,(A_I+B)\zeta_c\rangle.
\]

The grade-two term is invisible to ordinary diagonal pullback but remains in
the second conormal neighborhood. Thus normalized trace and second
contour-normal data are both necessary to retain the full generated Gaussian
state.

## Architecture

At the calculated order, the finite-time coefficient system is filtered by
both field degree and contour-conormal degree:

\[
\boxed{
\mathcal C_\Sigma
\supset
\mathcal C_{3}^{(0,1,2,3)}
\xrightarrow{\text{one-loop pushforward}}
\mathcal C_{2}^{(0,2)}.
}
\]

All terms remain on the same doubled initial hypersurface. This is new
coefficient mixing, not a new carrier incidence.

## Scope

The source explicitly eliminates only the quadratically divergent
\(\eta_0\)-terms. It states that the zeroth- and first-order pieces can be
treated similarly but does not display their complete kernels. No claim is
made here about closure beyond the published order.

## Next falsifier

Test whether the pair \((A_I,B)\) is more naturally represented as one
positive Gaussian covariance object with a fixed trace normalization, or as
two independent coefficient lines. The finite test is the eigenvalue and
positivity decomposition of the doubled quadratic kernel together with its
diagonal Gysin pushforward.

## Provenance

- Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eqs. (5.5)--(5.9);
- Entry 1492;
- allocator claim `seqclaim-b1af7343c5a59de6856cce56`.
- epistemic event `ev-000000001615-54b7d6ba-72c4-47c2-8d50-550e9bae7346`.
