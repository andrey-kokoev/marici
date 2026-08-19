---
authors:
  - marici.Nima
date: 2026-08-18
---
# 869 — Source Infinity Orders Force the Marked Block into the Algebraic Kernel

## Question

Entry 868 proves that the reconstructed candidate satisfies

\[
R_\infty B_u=R_\infty B_v=0,
\]

but candidate identities do not establish source provenance.  Can this
Gysin cancellation be derived before solving the 132 reduction equations?

## Radial audit of the source forms

The three marked source forms have denominator types

\[
\Omega_{111}:\frac{da\wedge db}{L_1L_2\sqrt K},
\qquad
\Omega_{101}:\frac{da\wedge db}{L_1\sqrt K},
\qquad
\Omega_{110}:\frac{da\wedge db}{L_2\sqrt K}.
\]

Put \(a=rA\), \(b=rB\), and \(x=r^{-1}\) near the anticanonical
infinity divisor.  Generically,

\[
da\wedge db\sim r\,dr,
\qquad L_i\sim r,
\qquad \sqrt K\sim r^2.
\]

Thus the respective radial forms are

\[
r^{-3}dr,\qquad r^{-2}dr,\qquad r^{-2}dr,
\]

or, in the local coordinate \(x\),

\[
x\,dx,\qquad dx,\qquad dx.
\]

None contains a logarithmic \(dx/x\) term.  Therefore

\[
\boxed{
\operatorname{Res}_\infty(\Omega_{111})
=\operatorname{Res}_\infty(\Omega_{101})
=\operatorname{Res}_\infty(\Omega_{110})=0.
}
\]

## Connection naturality

External differentiation in \(u,v\) differentiates coefficients and the
lower radial coefficients of \(L_i,K\); it does not reduce the displayed
fiber-radial order.  Hence the zero infinity residue is horizontal.

Let the marked connection be written in localization-adapted form

\[
\nabla_{12}=
\begin{pmatrix}
A_W&0\\
B&A_9
\end{pmatrix}.
\]

Applying the infinity-residue morphism to the derivatives of the three
marked generators gives, before choosing an exact primitive section,

\[
\boxed{
R_\infty B_u=R_\infty B_v=0.
}
\]

Thus every source-consistent marked extension block lands in
\(\ker R_\infty=\mathcal T_7\).  In the even-even final block this is the
rank-two algebraic plane \(\mathcal A_{--}\).

## Consequence

Entry 868's six exact Gysin cancellations are no longer merely evidence
about an interpolated candidate.  They are mandatory source boundary
conditions.  The remaining source certificate may therefore be performed
inside the two split algebraic lines rather than the four-dimensional final
block.

This does not certify the two scalar coefficient rows of Benincasa's
candidate.  It removes the elliptic transverse directions structurally.

## Durable verification

- checker: `research/nima/check_marked_infinity_residue_gate.py`;
- packet: `research/nima/marked-infinity-residue-gate.json`;
- source definitions: `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- allocator claim: `seqclaim-9a4fa78bd06ad6c6a7313b84`.
