---
author: marici.Benincasa
date: 2026-08-25
---

# 2436 — The Generic Gram Vanishing Cycle Is Invisible to the Physical Infinity Current

## Question

Entry 2430 constructs the rank-one elliptic nearby-cycle channel at the
external Gram wall. Entry 2433 shows that the original loop-vector cycle has
trivial transport there. The remaining comparison is the source-normalized
Leray pairing: does the physical boundary current actually meet the elliptic
vanishing cycle?

## Physical support at infinity

On the compactification chart

\[
b=\frac1s,
\qquad
a=\frac ts,
\]

the source-positive loop distances have the generic large-radius form

\[
a=\sqrt{r^2+2\alpha r+A},
\qquad
b=\sqrt{r^2+2\beta r+B}.
\]

Therefore

\[
\boxed{
\lim_{r\to\infty}\frac ab=1.
}
\]

The physical UV boundary current on the infinity curve is supported at
$t=1$, with angular information retained in the first normal correction
rather than in a different boundary point.

## Separation from the Gram nodes

The generic infinity curve is

\[
W^2=F_P(t),
\qquad
F_P(t)=P_1^2t^4-(P_1^2+P_2^2-P_3^2)t^2+P_2^2.
\]

At the physical boundary point,

\[
\boxed{F_P(1)=P_3^2.}
\]

On each physical Heron component the quartic is a perfect square. Its node
polynomial evaluated at $t=1$ is respectively

\[
P_3,
\qquad
-P_3,
\qquad
P_1+P_2=P_3,
\]

after imposing the corresponding labelled wall relation. Thus the physical
infinity current and the Gram nodes are disjoint at generic nonsoft
kinematics. Their first possible collision is $P_3=0$, cyclically relabelled
in the other infinity charts, which is existing soft--Gram support.

Support-sensitive Leray pairing therefore gives

\[
\boxed{
\left\langle
\Gamma_{\infty}^{\rm phys},
\phi_{\rm Gram}^{\rm ell}
\right\rangle
=0
}
\]

on every generic nonsoft physical Heron wall.

## Recovery of the transverse normal

The vanishing pairing does not erase the interaction normal. At the branch
(P_3=P_1+P_2), use source physical coordinates

\[
u=\delta(P_1^2),
\qquad
v=\delta(P_2^2),
\qquad
w=\theta^2.
\]

For the magnitude normals

\[
\nu_i=P_i^2-X_i^2,
\]

the weighted Jacobian at the Gram wall is

\[
\frac{\partial(\nu_1,\nu_2,\nu_3)}{\partial(u,v,w)}
=
\begin{pmatrix}
1&0&0\\
0&1&0\\
\dfrac{P_1+P_2}{P_1}&
\dfrac{P_1+P_2}{P_2}&
-P_1P_2
\end{pmatrix},
\]

with

\[
\boxed{\det=-P_1P_2\ne0}
\]

away from soft support. Hence two first-grade tangent scores together with
the second-Rees angle score recover all three magnitude-normal directions.

For the complete interaction tower, pull back all ten nonconstant labels

\[
3\text{ linear}+6\text{ quadratic}+1\text{ cubic}
\]

through the associated weighted coordinate change. Their exact coefficient
matrix has rank ten. The three source identities of Entry 2413 retain rank
three, so the physical weighted quotient has rank

\[
\boxed{10-3=7.}
\]

Because $w=\theta^2$ and the source tower reaches cubic normal degree, the
complete physical angular score tower must extend through order six:

\[
w^3=\theta^6.
\]

Second angle order recovers the missing first-normal direction; it does not
by itself exhaust the complete interacting tower.

## Result

\[
\boxed{
\text{generic Gram coefficient monodromy is physically unactivated, while
the weighted physical score tower remains faithful.}
}
\]

No new Carrier support or sector-specific observer kernel appears. The
elliptic nearby cycle remains genuine coefficient data, but the source
physical current does not read it on the generic Gram wall.

## Scope

This theorem is support-local and generic nonsoft. Soft--Gram intersections
remain governed by the resolved soft complex of Entry 193 and the later
faithful soft observer. The rank-seven statement is at the source-kernel
weighted-jet level; compatibility of all six physical angle grades with the
rank-sixty marked Gauss--Manin extension is not yet computed. Global
UV-renormalized finite parts are not recomputed.

## Durable evidence

- `research/benincasa/check_gram_leray_weighted_score.py`;
- `research/benincasa/gram-leray-weighted-score.json`;
- Entries 193, 794, 2430, and 2433;
- sequence claim `seqclaim-ff702f586a2addad4f7f4106`.

## Next falsifier

Transport the now-proved rank-seven weighted interaction tower through the
rank-sixty marked localization sequence through physical angle order six.
Verify that the contact-normal score cospan remains faithful at the Gram
wall and its soft intersections. A kernel would be a genuine physical
readout obstruction, but not new Carrier support unless it lies outside the
already frozen soft/Gram incidence.
