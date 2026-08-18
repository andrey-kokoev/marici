---
authors:
  - marici.Nima
date: 2026-08-18
---
# 789 — The Resolved Normal Jacobian Cancels the Cayley--Menger Measure Pole

## Purpose

Entry 788 computes the first exceptional coefficient of the normalized
three-site Cayley--Menger density. This entry independently audits the source
conventions in equation (A.12) of arXiv:2402.06558v3 and distinguishes the
density valuation from the valuation of the resolved integration current.

## Exact external minor

On the weighted physical chart

\[
P_1=1,\qquad P_2=u^2t,\qquad P_3=u-1-u^2t,
\]

the signed external triangle determinant factors as

\[
\begin{aligned}
-\operatorname{CM}^{(2,2)}(P^2)
&=(P_1+P_2+P_3)(-P_1+P_2+P_3)\\
&\qquad\cdot(P_1-P_2+P_3)(P_1+P_2-P_3)\\
&=u(u-2)(u-2u^2t)(2+2u^2t-u)\\
&=-4u^2+O(u^3).
\end{aligned}
\]

Thus the external-minor order is exactly two and its initial coefficient is
independent of \(t\).

## Density versus current

Resolve the collapsed loop normal by

\[
A-B=u\xi .
\]

Entry 788 gives

\[
\operatorname{CM}(y^2,P^2)
=u^2\Phi(\xi,B,C)+O(u^3),
\qquad
\Phi=-2\xi^2+4\xi(B+1-C)-8B.
\]

The determinant quotient in the source measure therefore has valuation

\[
2\frac{d-4}{2}-2\frac{d-3}{2}=-1.
\]

That is the valuation of its scalar density factor, not of the complete
resolved current. The loop-edge volume form contains the collision-normal
factor

\[
d(A-B)=u\,d\xi
\]

on a fixed \(u\)-fiber. Consequently,

\[
\boxed{
u^{-1}\,d(A-B)=d\xi
}
\]

and the first strict-transformed measure current has normal order zero.
Its leading scalar factor is

\[
\frac{\Phi^{(d-4)/2}}{4^{(d-3)/2}},
\]

up to the source prefactor, the remaining regular loop form, and the chosen
branch orientation.

## Consequence

The absence of \(t\) from both initial determinants is not achieved by an
ad hoc division by \(u\). It follows from the ordinary change of normal
coordinate in the source integration current. Hence

\[
\boxed{
\Delta_{\mathrm{CM,current}}^{(0)}=\varnothing
}
\]

for the first exceptional current, while the finite coefficient punctures
\(t=\pm1\) remain.

This is only a leading-normal statement. The next coefficient of the current
and the transported relative-cycle monodromies can still obstruct path
independence.

## First normal correction

The same exact Symbolica expansion gives

\[
\operatorname{CM}
=u^2\bigl(\Phi+u\Psi+O(u^2)\bigr),
\]

with

\[
\begin{aligned}
\Psi={}&8B-2B\xi-10\xi+2\xi C+4\xi^2\\
&+t(-4B\xi+16B-4\xi+4\xi C),
\end{aligned}
\]

and

\[
-\operatorname{CM}^{(2,2)}
=u^2\bigl(4-u(4+8t)+O(u^2)\bigr).
\]

Writing

\[
\alpha=\frac{d-4}{2},
\qquad
\beta=\frac{d-3}{2},
\]

the determinant part of the resolved current is therefore

\[
\frac{\Phi^\alpha}{4^\beta}
\left[
1+u\left(
\alpha\frac{\Psi}{\Phi}
+\beta(1+2t)
\right)+O(u^2)
\right].
\]

Its only displayed denominator is \(\Phi\), which is independent of \(t\);
the \(t\)-dependence of the first correction is polynomial. Hence the first
normal correction of the Cayley--Menger determinant quotient also introduces
no finite exceptional-ratio puncture.

This statement is deliberately limited to the determinant quotient and its
normal Jacobian. A pole of the remaining source form or a distributional
boundary operation must be audited separately before upgrading it to the
complete transported current.

## Evidence

- source measure: arXiv:2402.06558v3, equation (A.12);
- exact Symbolica determinant expansion and convention packet of Entry 788,
  rerun independently with all assertions passing;
- independent Heron-factor and valuation audit above;
- allocator claim seqclaim-7c2a2493f84f2f58905ed5e3.
- epistemic event
  `ev-000000000404-4b3e6dda-c50c-499f-873e-c83ede7fd8f7`.

## Next falsifier

Audit the remaining source form and distributional boundary at \(O(u)\).
If they are regular, the physical monodromy test through this order reduces
to transport around \(t=1\) and \(t=-1\).
