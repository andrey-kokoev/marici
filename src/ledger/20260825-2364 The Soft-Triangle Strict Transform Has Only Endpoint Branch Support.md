---
author: marici.Benincasa
date: 2026-08-25
---

# 2364 — The Soft-Triangle Strict Transform Has Only Endpoint Branch Support

## Frozen chart

Entry 2363 derives the physical weighted chart

\[
X_1=x,\qquad
X_2=p+\frac{x\kappa}{2},\qquad
X_3=p-\frac{x\kappa}{2},\qquad
b=E+x\xi.
\]

The physical exceptional ranges are

\[
-1\leq\kappa\leq1,\qquad -1\leq\xi\leq1.
\]

Sequence claim: seqclaim-092bd48470bc3b1c2426222a.

## Exceptional coefficient kernel

The complete \(q_{\mathcal G_{12}}\)-residue Cayley--Menger polynomial has
the source-derived expansion

\[
K_0=x^2K_{\rm exc}+O(x^3),
\]

with

\[
\begin{aligned}
K_{\rm exc}={}&a^4-(10+8\kappa\xi)p^2a^2\\
&+\left(
16\kappa^2+40\kappa\xi+16\xi^2+9
\right)p^4.
\end{aligned}
\]

Treating this as a quadratic in \(A=a^2\) gives the exact discriminant

\[
\boxed{
\operatorname{Disc}_{A}(K_{\rm exc})
=64p^4(1-\kappa^2)(1-\xi^2).
}
\]

Thus every branch collision on the generic \(p\ne0\) exceptional surface
lies on one of the four already frozen endpoint divisors

\[
\kappa=\pm1,\qquad \xi=\pm1.
\]

The strict transform introduces no independent branch divisor.

## Marked arrangement and source valuation

The five source walls become

\[
\begin{aligned}
q_{\mathfrak g_1}&=x(\xi+1),\\
q_{\mathfrak g_2}&=a-p+x\left(\frac{\kappa}{2}-1\right),\\
q_{\mathfrak g_3}&=a+3p+x\left(1+\xi-\frac{\kappa}{2}\right),\\
q_{\mathfrak g_{23}}&=2p+x\xi,\\
q_{\mathfrak g_{31}}&=a-p-\frac{x\kappa}{2}.
\end{aligned}
\]

The two colliding marked walls retain their divided difference:

\[
\boxed{
\frac{q_{\mathfrak g_2}-q_{\mathfrak g_{31}}}{x}
=\kappa-1.
}
\]

Hence their collision is supported on the existing positive base-triangle
endpoint \(\kappa=1\).

After the normal Jacobian cancels the square-root factor, the source form
has exceptional valuation \(-1\). Multiplying by \(x\) gives the exact
leading rational coefficient

\[
\boxed{
\frac{a+p}
{2p(a-p)^2(a+3p)(\xi+1)}.
}
\]

The pole at \(\xi=-1\) is the already identified
\(q_{\mathfrak g_1}\) endpoint. The double pole at \(a=p\) is the collision
of the two existing labelled walls, not an undeclared support component.

## Result

\[
\boxed{
\text{the physical soft--triangle strict transform closes on the frozen
endpoint and marked-incidence carrier.}
}
\]

The new structure is coefficient-theoretic: a sector-specific exceptional
Cayley--Menger kernel and a nontrivial Rees valuation of the source form.
No new Carrier divisor is required.

## Scope

This is an exact associated-grade calculation. It does not determine:

- the rank of the full logarithmic relative cohomology of \(K_{\rm exc}\);
- the Cartier length induced by the source's \(x^{-1}\) valuation;
- monodromy at the four endpoint divisors;
- the physical period rank of the four candidate quotient numerators;
- the all-soft specialization \(p=0\).

## Durable verification

- research/benincasa/check_x1_soft_physical_strict_transform.py;
- research/benincasa/x1-soft-physical-strict-transform.json;
- exact symbolic kernel, discriminant, wall, and source-normalization
  identities;
- epistemic event
  ev-000000003239-1e7eb88c-8420-4dc9-a63e-428b3337e16f.

## Next falsifier

Construct the logarithmic relative de Rham complex of

\[
w^2=K_{\rm exc}
\]

with the retained labelled walls and endpoint divisors. Compute its
cohomology, inertia, and source-generated score closure. A rank or
monodromy class supported away from

\[
p(1-\kappa^2)(1-\xi^2)(a-p)(a+3p)=0
\]

would be the first new-support obstruction at the physical soft corner.
