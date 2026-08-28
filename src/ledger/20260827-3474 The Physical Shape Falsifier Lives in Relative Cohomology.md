---
author: marici.Benincasa
date: 2026-08-27
---

# 3474 — The Physical Shape Falsifier Lives in Relative Cohomology

## Hard-to-vary claim

The nonzero quadratic shape response of the homogeneous elliptic quotient
cannot be promoted to a statement about the complete Bunch--Davies
wavefunction by projecting the physical source into the absolute
nine-master object. The source provides no canonical projection of that
type. The physical falsifier is instead the second shape derivative of the
source-defined relative period.

## Source typing

The primary source places the published elliptic Picard--Fuchs operator in
the final cyclic block

\[
e_7=\varphi_{001},\qquad
e_8=y_{23}^2\varphi_{001},\qquad
e_9=y_{31}^2\varphi_{001}.
\]

The literal three-site top source is the distinct master

\[
e_{15}=\varphi_{1110}.
\]

After the \(q_{\mathcal G_{12}}\) residue, the complete physical source has
the canonical relative class

\[
[\Omega_{\rm phys}]
\in H^2(S_E\setminus W),
\]

with nonzero wall boundary. The absolute elliptic quotient belongs to
\(H^2(S_E)\). Localization supplies a forward map from absolute to open
cohomology, but the frozen source supplies no reverse retraction.

Therefore a decomposition

\[
[\Omega_{\rm phys}]=s([\rho_{\rm phys}])+j(m)
\]

depends on a choice of section \(s\). Its absolute component \(m\), and
hence any elliptic coefficient extracted from it, is not intrinsic.

## Surviving elliptic result

Along

\[
X_1=1+t,\qquad X_2=1-t,\qquad X_3=1,
\]

the published modulus still satisfies

\[
m(t)=-\frac13+\frac43t^2,
\qquad m''(0)=\frac83.
\]

Thus the rank-two elliptic coefficient object genuinely detects the
quadratic shape intervention. This remains a coefficient prediction, not a
complete physical scalar prediction.

## Correct finite falsifier

Let \(\Gamma_t\) be the source-defined relative integration cycle transported
along the physical shape family. Compute

\[
\left.\frac{d^2}{dt^2}
\langle[\Omega_{\rm phys}(t)],[\Gamma_t]\rangle
\right|_{t=0}.
\]

The derivative insertion remains inside the frozen integer/half-integer
integral family by Entry 3461. Therefore this is a finite relative IBP or
direct-period problem and requires no new carrier support.

The outcomes are:

- nonzero: the quadratic intervention reaches the physical readout;
- zero by a source-derived identity: the relative boundary and absolute
  coefficient contributions cancel physically;
- dependence on a chosen localization section: the proposed computation is
  mistyped and must be rejected.

## Classification

- existing carrier: Cayley--Menger surface and marked denominator walls;
- established coefficient datum: nonzero elliptic shape Hessian;
- physical object: source-defined relative period;
- missing operation: relative second-shape reduction or direct pairing;
- new carrier datum: none.

## Verification

Checker:
`research/benincasa/checkers/audit_relative_shape_response_typing.py`.

Primary source: Benincasa et al., arXiv:2408.16386v2, equations (51),
(58)--(60), and the displayed master bases.

Allocator claim: `seqclaim-70d1794435709b3134e593db`.

