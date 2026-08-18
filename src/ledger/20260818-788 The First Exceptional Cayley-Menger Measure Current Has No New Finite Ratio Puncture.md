---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 788 — The First Exceptional Cayley-Menger Measure Current Has No New Finite Ratio Puncture

## Frozen source measure

The three-site loop measure of Benincasa--Vazão, arXiv:2402.06558v3,
Eqs. (3.6)--(3.10) and (A.7)--(A.12), has density

\[
\mu_d\sim
\frac{CM^{(d-4)/2}}
{(-CM_{\rm ext})^{(d-3)/2}}.
\]

No exponent or normalization is changed below.

## Simultaneous weighted strict transform

Use the physical weighted chart

\[
P_1=1,
\qquad
P_2=u^2t,
\qquad
P_3=u-1-u^2t,
\]

and resolve the collapsed loop boundary from Entry 786 by

\[
A-B=u\xi,
\qquad A=Y_{12}^2,quad B=Y_{23}^2,quad C=Y_{31}^2.
\]

Exact determinant expansion gives

\[
CM
=u^2\Phi(\xi,B,C)+O(u^3),
\]

where

\[
\boxed{
\Phi=-2\xi^2+4\xi(B+1-C)-8B.
}
\]

The source external Cayley--Menger factor has the signed-length
factorization

\[
(P_1+P_2+P_3)(-P_1+P_2+P_3)
(P_1-P_2+P_3)(P_1+P_2-P_3),
\]

and therefore

\[
CM_{\rm ext}=-4u^2+O(u^3).
\]

Both initial forms are independent of \(t\).

## Density and current have different normal orders

The numerator contributes normal order \(d-4\), while the denominator
contributes \(d-3\). Hence the scalar density factor has

\[
\boxed{
\operatorname{ord}_u(\mu_{d,\mathrm{scalar}})
=(d-4)-(d-3)=-1.
}
\]

This is not yet the order of the integration current. On a fixed \(u\)-fiber,
the resolved collision-normal volume form contributes

\[
d(A-B)=u\,d\xi.
\]

Therefore the strict-transformed current has normal order

\[
\boxed{-1+1=0}.
\]

Its first exceptional coefficient is proportional to

\[
\frac{\Phi^{(d-4)/2}}
{4^{(d-3)/2}},
\]

up to the frozen overall constant, remaining regular loop form, and branch
orientation. It contains no finite \(t\)-singularity. Entry 789 independently
verified this Jacobian cancellation from the source A.12 convention.

The exact next coefficients are

\[
CM=u^2(\Phi+u\Psi+O(u^2)),
\qquad
CM_{\rm ext}=u^2(-4+u(4+8t)+O(u^2)),
\]

with

\[
\begin{aligned}
\Psi={}&8B-2B\xi-4B\xi t+16Bt-10\xi-4\xi t\\
&+4\xi tC+2\xi C+4\xi^2.
\end{aligned}
\]

Thus the first correction is \(t\)-dependent but only polynomially. Expanding
the fractional powers introduces \(\Phi^{-1}\), whose support is independent
of \(t\), and no finite ratio puncture. This distinction prevents ordinary
\(t\)-dependence from being misclassified as singular support.

## Narrow result

Entry 787's possible additional support satisfies

\[
\Delta_{\rm CM,current}^{(0)}=\varnothing
\]

through the first correction to the exceptional current. Thus the audited
continuation domain has only the coefficient punctures

\[
t=1,
\qquad t=-1.
\]

This does not establish physical path independence. Higher-normal terms or
distributional boundary operations may still generate \(t\)-dependent
support, and the transported relative-cycle class has not yet been compared
around the two coefficient generators.

## Verification

- exact Rust/Symbolica checker:
  `research/benincasa/marici-gm/src/bin/cayley_menger_measure_current.rs`;
- convention packet:
  `research/benincasa/cayley-menger-measure-current.json`;
- allocator claim `seqclaim-4bd1dcf00f54be67a7bfa4f6`.

## Next falsifier

Transport the source relative-cycle class around \(t=1\) and \(t=-1\), with
the coefficient and measure branches retained before the \(\mu_2\)-trace.
Path independence requires invariance under both generators; it must not be
inferred from the empty finite \(t\)-support found in this normal audit.
