# The maximal recovery-dark vertical bundle is the kernel subbundle

## Question

What vertical auxiliary bundle is canonically available from the skew-product incidence and recovery before physical Green elimination is identified?

## Fiberwise splitting

Over the theta source manifold \(S\), let

\[
I_s:E\to H_s,
\qquad
R_s:H_s\to E,
\qquad
R_sI_s=I_E.
\]

Define

\[
P_s=I_sR_s,
\qquad
Q_s=I_{H_s}-P_s.
\]

Then

\[
P_s^2=P_s,
\qquad
Q_s^2=Q_s,
\]

with

\[
\operatorname{ran}P_s=I_s(E),
\qquad
\operatorname{ran}Q_s=\ker R_s.
\]

Thus

\[
H_s=I_s(E)\oplus\ker R_s.
\]

If \(I_s\) and \(R_s\) vary continuously over \(S\), then \(Q_s\) is a continuous projection family and

\[
N_s^{\max}=\ker R_s
\]

is a split closed vertical subbundle. No separate constant-rank assumption is needed because the explicit projections provide the bundle charts.

## Maximality

Any vertical auxiliary bundle \(N_s\) annihilated by recovery obeys

\[
N_s\subseteq N_s^{\max}.
\]

Conversely, \(N_s^{\max}\) is the largest vertical bundle on which recovery vanishes. It is therefore the canonical candidate for a no-dark quotient, not automatically the physical Green auxiliary bundle.

## Uniform quotient bound

The quotient \(H_s/N_s^{\max}\) is isomorphic to \(E\) through the descended recovery. If

\[
\sup_{s\in K}\lVert R_s\rVert<\infty
\]

on a declared source region \(K\), then

\[
\lVert q_sI_sx\rVert
\ge
\frac{1}{\sup_K\lVert R_s\rVert}\lVert x\rVert.
\]

This gives a uniform no-dark bound for the canonical recovery quotient.

## Physical qualification

A source-derived physical auxiliary bundle \(N_s^{\rm phys}\) may be smaller than \(N_s^{\max}\). It is admissible for recovery descent exactly when

\[
N_s^{\rm phys}\subseteq\ker R_s
\]

fiberwise. Declaring equality without reading the Green variational problem would change the Schur short.

## Verification

`research/aspect/checkers/check_vertical_recovery_kernel_bundle.py` verifies the projection identities over three exact rational source parameters.

## Disposition

The corrected skew-product architecture now has a canonical maximal recovery-dark vertical bundle. The next gate is physical: derive the Green auxiliary generators and test their inclusion in this kernel bundle; the bundle itself no longer needs to be guessed.
