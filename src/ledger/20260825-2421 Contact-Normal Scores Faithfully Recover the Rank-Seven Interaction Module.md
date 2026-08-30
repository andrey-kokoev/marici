---
author: marici.Benincasa
date: 2026-08-25
---

# 2421 — Contact-Normal Scores Faithfully Recover the Rank-Seven Interaction Module

## Frozen object

Entry 2400 derives the generic six-scale Cayley--Menger kernel

\[
K(\nu)=K_0+\sum_{0<|\alpha|\le3}K_\alpha\nu^\alpha,
\qquad \nu_i=P_i^2-X_i^2,
\]

with ten nonconstant labelled coefficients. Entries 2413--2419 prove that
three exact source relations reduce this presentation to a rank-seven
interaction module and that the complete rank-sixty direct image acts
faithfully on it.

The observer tested here is the source contact-normal logarithmic jet

\[
S_\alpha=
\left.\partial_\nu^\alpha\log K(\nu)\right|_{\nu=0},
\qquad 0<|\alpha|\le3,
\]

restricted to the ten monomials actually present in the frozen kernel. This
channel is defined before integration. No physical-cycle covector or fitted
projector is introduced.

## Exact inversion

The normalized kernel is recovered by the finite moment--cumulant identity

\[
\boxed{
\frac{K(\nu)}{K_0}
=
\exp\!\left(
\sum_{0<|\alpha|\le3}
\frac{S_\alpha}{\alpha!}\nu^\alpha
\right)_{\le3}.
}
\]

The truncation is exact because the source normal tower has degree three.
At the zero-interaction point, the Jacobian from normalized kernel
coefficients to logarithmic scores is

\[
\operatorname{diag}(1,1,1,2,2,2,1,1,1,1),
\]

with determinant \(8\). Hence the transformation is generically invertible.
It is also equivariant under the source cyclic permutation of the three
occurrence labels.

In the unnormalized coefficient coordinates the determinant is

\[
\boxed{\det J_{\rm raw}=\frac{8}{K_0^{10}}.}
\]

It has no zero divisor on the regular chart. Its only failure is a pole at
\(K_0=0\), the already frozen Cayley--Menger/Landau branch. Thus contact-score
recovery introduces no new rank-loss support.

The literal three-site measure has exponent \(\gamma=-\tfrac12\). Repeating
the calculation for the normalized source response jets

\[
R_\alpha=
K_0^{-\gamma}
\left.\partial_\nu^\alpha K(\nu)^\gamma\right|_{\nu=0}
\]

gives linearized determinant

\[
\boxed{\det J_R=\frac1{128}},
\qquad
\boxed{\det J_{R,{\rm raw}}=\frac1{128K_0^{10}}}.
\]

Thus the literal source integrand normal jets also recover the complete
interaction packet before integration.

## Result

The complete contact-normal score tower reconstructs all ten presentation
coefficients. Quotienting by the three identities already true in the source
therefore leaves no observer kernel:

\[
\boxed{
\ker\bigl(
\mathcal I_{\rm source}^{(7)}
\longrightarrow
\mathcal O_{\rm contact}
\bigr)=0.
}
\]

Thus the first remaining possible loss is not in contact normalization,
the coefficient direct image, or cyclic transport. It is in the passage from
these algebraic insertions to periods of the physical relative cycle.

## Scope

This theorem is at integrand/coefficient level. Differentiating the physical
period also differentiates its relative cycle and requires Gauss--Manin
covariant boundary terms. The frozen source has not yet been shown to realize
all ten logarithmic insertions as operational ports. Tensor polarization also
remains gated on an independent tensor-interaction source.

Classification:

- contact-normal algebraic kernel: zero;
- generic contact-score rank-loss support: empty;
- score-chart pole: existing Cayley--Menger/Landau support;
- literal \(K^{-1/2}\) response kernel before integration: zero;
- source interaction rank: seven;
- physical period observer: uncomputed;
- new Carrier support: none.

## Durable evidence

- `research/benincasa/check_rank7_contact_normal_score_recovery.py`;
- `research/benincasa/rank7-contact-normal-score-recovery.json`;
- sequence claim `seqclaim-ca0d6b174ac4beafd6430e28`.

## Next falsifier

Derive the Gauss--Manin covariant normal derivatives of the source physical
relative period and separate bulk contact insertions from cycle-boundary
terms. Compute the induced rank on the seven-dimensional source interaction
quotient. A kernel there is a physical readout obstruction; it must not be
retyped as coefficient loss.
