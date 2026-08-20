---
author: marici.Benincasa
---

# 1109 — The Rational Tangency Is a Doubled Conic with One Labelled Marked Face

## Question

At the exceptional parameter center

\[
(u,v)=\left(\frac23,0\right),
\]

what is the source-labelled Cayley--Menger degeneration, and does its first
smoothing require a new carrier wall?

## Frozen source

Use the same homogeneous rank-twelve Cayley--Menger polynomial \(K\), residue
coefficient \(K_1\), and marked planes

\[
L_1=b+1-u,
\qquad
L_2=a+\frac{v-2-u}{2}
\]

as in Entries 1098--1108. No wall, quotient, or support summand is added after
the calculation.

## The naive marked intersection is not the critical point

Simultaneously imposing \(L_1=L_2=0\) gives
\((a,b)=(4/3,-1/3)\), but direct substitution yields

\[
K=\frac{256}{81},
\qquad
K_1=\frac{128}{81}.
\]

That point is therefore rejected.

At fixed \((u,v)=(2/3,0)\), the complete fiber polynomial instead factors as

\[
\boxed{
K
=
\frac1{729}
\left(27a^2-18b^2+2\right)^2.
}
\]

The labelled plane \(L_1=b+1/3\) is tangent to this doubled conic at

\[
\boxed{(a,b)=\left(0,-\frac13\right),}
\]

while \(L_2=-4/3\) is a unit there.

## Joint Newton audit

Set

\[
p=u-\frac23,
\qquad q=v,
\qquad A=a,
\qquad B=b+\frac13.
\]

The exact Symbolica expansion gives

\[
\nu K=2,
\qquad
\operatorname{in}K
=
\frac{16}{81}(p+q-B)^2,
\]

and

\[
\nu K_1=1,
\qquad
\operatorname{in}K_1
=
-\frac{32}{81}(p+q-B).
\]

Writing \(T=p+q-B\), the next coefficient on the doubled plane is

\[
\boxed{
K_3|_{T=0}
=
-\frac49 q(3p+q-2A)(3p+q+2A).
}
\]

Moreover,

\[
L_1|_{T=0}=q,
\qquad
L_2|_{T=0}=-\frac43.
\]

## Narrow conclusion

The first smoothing contains the already-labelled \(L_1\) occurrence. The two
additional linear factors

\[
3p+q-2A,
\qquad
3p+q+2A
\]

are branches of the coefficient smoothing polynomial. This calculation does
not type them as new carrier walls.

Thus the surviving statement is

\[
\boxed{
\text{doubled conic}
+
\text{exceptional normal}
+
\text{one existing labelled }L_1\text{ face},
}
\]

with no new carrier datum found.

This entry does not yet claim that the resulting support complex is exact.

## Verification

The durable checker is

research/benincasa/marici-gm/src/bin/rank12_u2over3v0_newton.rs.

Its machine-readable packet is

research/benincasa/rank12-u2over3-v0-rational-tangency.json.

Ledger claim: seqclaim-d727929531ddbd13dfba88a8.

Epistemic event:

ev-000000000808-40cf5c73-4a73-48c8-b70b-565d588bcb45.

## Next finite falsifier

Normalize the doubled conic and construct the occurrence-resolved support
complex for the exceptional normal and \(L_1\). Retain the two coefficient
branches separately, and test whether their intersection creates Tor or a
nontrivial nearby-cycle extension. Only such surviving cohomology could
justify new coefficient complexity; it would still not by itself define a new
carrier wall.
