---
author: marici.Benincasa
date: 2026-08-25
---

# 2429 — Loop-Distance Endpoints Admit Compatible Normal Lifts

## Primary contour boundary

The source contour is frozen by Benincasa--Vazão,
arXiv:2402.06558v3. Equation (3.8) gives the signed-minor inequalities for
Euclidean embeddability. Equations (A.11)--(A.12) specialize them to the
three-site tetrahedron and state that

\[
\boxed{K=0}
\]

establishes the contour boundary. The remaining minor equalities describe
lower-dimensional incidence strata. In particular, when one loop distance
vanishes the loop point coincides with an external-triangle vertex.

## Three labelled endpoint ideals

With \((c,a,b)=(y_{12},y_{23},y_{31})\), the positive endpoint incidences are

\[
c=0,\qquad a=P_2,\qquad b=P_1,
\]

\[
a=0,\qquad c=P_2,\qquad b=P_3,
\]

and

\[
b=0,\qquad c=P_1,\qquad a=P_3.
\]

Each substitution annihilates the full Cayley--Menger determinant exactly.

## Normal transport

Write

\[
P_i(\nu_i)=\sqrt{P_i^2+\nu_i}.
\]

At each endpoint, transport the two nonzero loop distances with their forced
external lengths. For example, at \(c=0\),

\[
V_{\nu_1}=\frac1{2P_1}\partial_b,
\qquad
V_{\nu_2}=\frac1{2P_2}\partial_a,
\qquad
V_{\nu_3}=0.
\]

The cyclic endpoint formulas give nine labelled normal lifts. Exact
calculation verifies for every endpoint and normal that

\[
(\partial_{\nu_i}+V_{\nu_i})I_{\rm endpoint}=0
\]

on all three incidence generators and

\[
\boxed{
(\partial_{\nu_i}+V_{\nu_i})K=0
}
\]

on the endpoint.

## Result

\[
\boxed{
\text{all three loop-distance endpoints transport inside the frozen
Cayley--Menger incidence family.}
}
\]

Thus the coordinate endpoints do not generate a normal-transport
obstruction or new Carrier support. Together with Entries 2424 and 2426,
this closes the generic \(K=0\) boundary and its three labelled distance
endpoints at incidence level.

## Scope

The endpoint radial exponent and its marked-wall residue pairing are not
recomputed here. External triangle degeneration remains a separate existing
Gram support, and rank-seven physical period observability remains open.

## Durable evidence

- `research/benincasa/check_physical_cycle_endpoint_normal_lifts.py`;
- `research/benincasa/physical-cycle-endpoint-normal-lifts.json`;
- primary source arXiv:2402.06558v3, equations (3.8), (A.11)--(A.12);
- sequence claim `seqclaim-1fbc9d3aa92198d5a458e38f`.

## Next falsifier

Test the external-triangle boundary \(\Lambda(P_1,P_2,P_3)=0\). Derive the
normal lift on each labelled Heron component and its soft intersections,
then verify compatibility with the endpoint lifts. Only after this finite
Gram audit is the complete physical contour transport ready for period
pairing.
