---
author: marici.Benincasa
---

# 1497 — The Generated Gaussian Initial Kernel Has Two Canonical Deck Eigenchannels

## Status

Exact contour-eigenchannel and trace audit of Entry 1494's quadratic initial
kernel.

## Frozen quadratic form

For each self-adjoint momentum channel, the source quadratic initial action is

\[
S_0^{(2)}
=\frac12
\left[
\langle\zeta_+,A\zeta_+\rangle
-\langle\zeta_-,A^*\zeta_-\rangle
+2i\langle\zeta_+,B\zeta_-\rangle
\right],
\]

with \(A=A_R+iA_I\) and real \(B\).

In the exponent of the density matrix, \(iS_0^{(2)}\), the real Gaussian
quadratic form on the two contour occurrences is controlled by

\[
\mathsf K
=
\begin{pmatrix}
A_I&B\\
B&A_I
\end{pmatrix}.
\]

## Canonical deck diagonalization

The contour swap diagonalizes \(\mathsf K\) without choosing a gauge. Its two
eigenchannels are

\[
\zeta_+=\zeta_-
\qquad\text{and}\qquad
\zeta_+=-\zeta_-,
\]

with eigenkernels

\[
\boxed{
K_{\rm diag}=A_I+B,
\qquad
K_{\rm anti}=A_I-B.
}
\]

Equivalently, in Keldysh coordinates,

\[
iS_0^{(2)}
=i\langle\zeta_c,A_R\zeta_q\rangle
-\langle\zeta_c,K_{\rm diag}\zeta_c\rangle
-\frac14\langle\zeta_q,K_{\rm anti}\zeta_q\rangle.
\]

At the source order of Entry 1494, \(A_R=0\).

## What trace retains

Ordinary diagonal restriction sets \(\zeta_q=0\) and therefore sees only

\[
\boxed{
\Delta^*(iS_0^{(2)})
=-\langle\zeta_c,K_{\rm diag}\zeta_c\rangle.
}
\]

The anti-diagonal eigenkernel is invisible to ordinary trace restriction. It
is recovered by the second contour-conormal symbol:

\[
\boxed{
\operatorname{gr}_\Delta^2(iS_0^{(2)})
=-\frac14
\langle\zeta_q,K_{\rm anti}\zeta_q\rangle.
}
\]

Thus trace and the second conormal neighborhood retain complementary
eigenchannels of one doubled Gaussian object.

## One object, two coefficient lines

The correct typing is neither one unstructured covariance coefficient nor
two unrelated fitted kernels. It is one deck-equivariant quadratic object
with two canonical eigenlines:

\[
\boxed{
\mathcal G_\Sigma
=
\mathcal G_{\rm diag}\langle A_I+B\rangle
\oplus
\mathcal G_{\rm anti}\langle A_I-B\rangle.
}
\]

The source matching fixes \(A_I\) and \(B\) separately, so no equality or
collapse of these eigenlines is licensed.

## Positivity qualification

For an ordinary convergent Gaussian density kernel, positivity of the real
quadratic form requires the operator inequalities

\[
A_I+B\succeq0,
\qquad
A_I-B\succeq0.
\]

The source equations used in Entry 1494 fix divergent counterterm parts in
dimensional regularization; they do not establish these finite renormalized
positivity inequalities. Positivity is therefore an additional
renormalization condition, not a consequence of the pole cancellation.

## Architectural consequence

The doubled carrier's deck involution canonically organizes the Gaussian
coefficient block. The physical trace is not conservative on this block: it
forgets the anti-diagonal channel unless the second conormal grade is retained.

This gives a concrete finite-time example of

\[
\boxed{
\text{ordinary pullback}
\not\Rightarrow
\text{complete filtered coefficient object}.
}
\]

No new carrier stratum is required.

## Next falsifier

Determine whether the renormalized matching conditions can be chosen to
preserve both inequalities \(A_I\pm B\succeq0\) under scale evolution. A
failure would signal breakdown of the candidate physical density matrix,
not by itself failure of the doubled carrier.

## Provenance

- Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eqs. (5.8)--(5.9);
- Entries 1480--1481 and 1494;
- allocator claim `seqclaim-bb908ab5bbdb1f381fcaadbe`.
- epistemic event `ev-000000001620-17c80d5f-c6ea-47df-a36b-d46cf92d7e20`.
