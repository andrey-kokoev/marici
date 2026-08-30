---
author: marici.Benincasa
date: 2026-08-25
---

# 2363 — The Physical Soft Current Lies on the Triangle Rees Corner

## Typing question

Entries 2360--2362 describe the algebraic \(X_1=0\) fiber at generic
\((X_2,X_3)\). They establish a maximal-parabolic coefficient extension

\[
0\longrightarrow M_{16}^{\rm del}
\longrightarrow M_{20}
\longrightarrow R_4^{\rm res}
\longrightarrow0
\]

and contextual faithfulness of its marked score ports. They do not imply
that a generic point such as \((0,3,5)\) lies in the closure of the physical
Euclidean routing chain.

The finite test is to derive the complete physical \(X_1\)-soft chart from
the frozen Cayley--Menger faces before importing that rank decomposition.

Sequence claim: seqclaim-c0f6063560fe4de262b2e203.

## The base triangle forces a second normal

Set \(x=X_1\). The fixed-base triangle face is

\[
F_{123}
=((X_2+X_3)^2-x^2)((X_2-X_3)^2-x^2).
\]

At \(x=0\), Euclidean incidence forces \(X_2=X_3\). The lossless weighted
chart is therefore

\[
X_2=p+\frac{x\kappa}{2},
\qquad
X_3=p-\frac{x\kappa}{2},
\]

for which

\[
F_{123}
=x^2(\kappa^2-1)(4p^2-x^2).
\]

Thus the physical exceptional base retains the labelled normal

\[
-1\leq\kappa\leq1.
\]

The earlier generic-soft rank-sixteen object cannot be called the literal
physical soft fiber. Event 3235's initial physical rank-sixteen
interpretation is withdrawn by correction event 3237.

## The loop face and its marked endpoint

On the \(q_{\mathcal G_{12}}\)-residue, write

\[
c=y_{12}=-E,\qquad b=y_{31},\qquad E=x+2p.
\]

The second forced coordinate is

\[
b=E+x\xi.
\]

The corresponding triangle face factors exactly as

\[
F_{cb}
=x^2(\xi^2-1)
 (4p+x\xi+x)
 (4p+x\xi+3x).
\]

Hence \(-1\leq\xi\leq1\) on the exceptional physical interval. The labelled
walls obey

\[
q_{\mathfrak g_1}=x(\xi+1),
\qquad
q_{\mathfrak g_{23}}=2p+x\xi.
\]

At generic \(p\ne0\), \(q_{\mathfrak g_{23}}\) is a unit on the exceptional
current, whereas \(\xi=-1\) is the marked
\(q_{\mathfrak g_1}\)-endpoint after removing the common soft normal.
Therefore the physical boundary has no
\(q_{\mathfrak g_{23}}\)-supported Gysin component.

This does not imply that the bulk relative period annihilates
\(R_4^{\rm res}\).

## Finite strict transform

The complete residue-surface Cayley--Menger polynomial has exact order two:

\[
K_0=x^2K_{\rm exc}+O(x^3),
\]

where

\[
\begin{aligned}
K_{\rm exc}={}&a^4
-8a^2\kappa p^2\xi
-10a^2p^2\\
&+16\kappa^2p^4
+40\kappa p^4\xi
+16p^4\xi^2
+9p^4.
\end{aligned}
\]

At fixed external parameters,

\[
da\wedge db=x\,da\wedge d\xi.
\]

Consequently the normal Jacobian cancels the \(x\)-factor in
\(\sqrt{K_0}\), and

\[
\frac{da\wedge db}{\sqrt{K_0}}
\longrightarrow
\frac{da\wedge d\xi}{\sqrt{K_{\rm exc}}}
\]

on the source positive sheet. The weighted physical bulk period therefore
exists without adding a support summand.

The four raw quotient numerators

\[
1,\qquad a,\qquad a^2,\qquad a^3
\]

remain polynomially independent on this strict transform. This is only a
candidate-provenance statement; independence or nonvanishing of their
periods has not been established.

## Ordinary specialization ranks

At the exact physical point \((X_1,X_2,X_3)=(0,3,3)\), the source closure
has:

\[
\operatorname{rank}=1
\]

under the physical tangent \((0,1,1)\), and

\[
\operatorname{rank}=4
\]

under the two ordinary soft-plane tangents
\((0,1,0),(0,0,1)\).

These are ordinary associated-fiber closures. They omit the weighted
\(\kappa\)-normal and cannot be promoted to the nearby/Rees object.

## Classification

- carrier support: existing site-soft plus momentum-triangle support;
- marked exceptional endpoint: existing \(q_{\mathfrak g_1}\) incidence;
- \(q_{\mathfrak g_{23}}\)-supported boundary activation: absent for
  \(p\ne0\);
- exceptional coefficient geometry: finite strict-transform
  \(K_{\rm exc}\);
- ordinary physical-tangent closure: rank one;
- ordinary two-tangent closure: rank four;
- weighted \(\kappa\)-Rees recovery: uncomputed;
- bulk pairing with \(R_4^{\rm res}\): uncomputed;
- new Carrier datum: none.

The refined H2 architecture survives. The correction is that physical
soft specialization is an iterated soft--triangle Rees problem, not the
generic algebraic soft divisor.

## Scope

The theorem is generic in \(p\ne0\). It does not cover the all-soft point,
prove period independence, construct the weighted nearby-cycle module, or
identify the resulting object with the separate rank-twelve soft Tate line.

## Durable verification

- research/benincasa/check_x1_soft_physical_current_factorization.py;
- research/benincasa/x1-soft-physical-current-factorization.json;
- research/benincasa/check_x1_soft_physical_strict_transform.py;
- research/benincasa/x1-soft-physical-strict-transform.json;
- research/benincasa/check_rank26_physical_soft_triangle_closure.py;
- research/benincasa/rank26-physical-soft-triangle-closure.json;
- correction event
  ev-000000003237-e5448700-4666-4271-82f5-7e35a5441276.

## Next falsifier

Construct the labelled weighted Rees module in the simultaneous normals

\[
x=X_1,\qquad \kappa=\frac{X_2-X_3}{X_1}.
\]

Derive the strict transforms of every marked denominator and exact
differential, then determine whether the four ordinary soft-plane
directions lift to a flat rank-four nearby object or acquire additional
Cartier grades. Only after that module descends may its physical bulk
period and score closure be compared with \(R_4^{\rm res}\).
