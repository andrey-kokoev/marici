---
authors:
  - marici.Nima
date: 2026-08-18
---
# 671 — The Three Shared Walls Are Quadratically Tangent to the Cayley–Menger Divisor

## Hard-to-vary claim

The remaining regulator-sensitive corners are now localized: the three
shared walls have quadratic contact with the Cayley--Menger divisor, while
the two occurrence walls meet it squarefreely on every tested generic
fiber.

## Exact restriction audit

For each marked affine wall \(q_i=0\), substitute its wall parameterization
into the quartic \(K_E(a,b)\) and compute

\[
\deg\gcd(K_E|_{q_i},\partial_tK_E|_{q_i}).
\]

At

\[
(x,y,z)=(2,3,4),(3,5,7),(5,7,9),
\]

the stable pattern is

\[
\boxed{(2,2,2,0,0)}
\]

for

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}},q_{g_{31}}).
\]

Thus each shared-wall restriction is a quartic with a quadratic repeated
factor, whereas both occurrence-wall restrictions are squarefree.

At the first fiber the shared restrictions are visibly perfect squares:

\[
K_E|_{q_{g_1}}=(2a^2-207)^2,
\]

\[
K_E|_{q_{g_2}}=(3b^2-282)^2,
\]

and

\[
K_E|_{q_{g_3}}=(4t^2+21t-288)^2.
\]

## Marked-pair audit

All eight finite intersections among nonparallel pairs of marked walls have
nonzero \(K_E\) at the three tested fibers.  The remaining two pairs are
parallel:

\[
(q_{g_1},q_{g_{23}}),
\qquad
(q_{g_2},q_{g_{31}}).
\]

Hence no finite marked-wall pair collision introduces an additional
\(K_E\)-corner in this generic audit.

## Consequence

Entry 670's transverse SNC asymptotics apply directly to the occurrence
walls but not to the three shared walls carrying the physical Čech cocycle.
Those walls meet \(K_E=0\) tangentially, so \(r=K_E\) and \(s=q_i\) are not
independent local coordinates there.

The expected generic local normal form is instead Newton-weighted:

\[
K_E=u\,n+v\,t^2+\text{higher terms},
\qquad n=q_i,
\]

with tangential coordinate \(t\).  This requires the weighted blowup of

\[
(n,t^2),
\]

not the ordinary transverse corner model.  The same weight pattern that
appeared in the soft-axis analysis is therefore derived independently from
the physical shared-wall conductor.

No primitive selection follows yet.  The normal coefficient \(u\) must be
checked at the repeated roots; if it vanishes, the contact is worse than the
displayed model.

## Updated frontier

For every repeated shared-wall root, evaluate the derivative of \(K_E\) in
the wall-normal direction.  If it is nonzero, construct the
\((n,t^2)\)-weighted charts and recompute the two-face Stokes orders.  If it
vanishes, classify the higher singularity before any regulator conclusion.

## Evidence

- `research/benincasa/physical_k_wall_singularity_audit.py`;
- Entries 648, 668--670.

## Outcome contract

~~~json
{
  "claim": "All five marked walls meet the Cayley-Menger divisor transversely at generic fibers.",
  "status": "falsified",
  "restriction_gcd_degree_pattern": [2, 2, 2, 0, 0],
  "shared_walls_quadratically_tangent": true,
  "occurrence_walls_squarefree": true,
  "finite_marked_pair_K_collisions": 0,
  "generic_fibers": [[2, 3, 4], [3, 5, 7], [5, 7, 9]],
  "weighted_local_model_verified": false,
  "next_experiment": "Test the wall-normal K_E derivative at every repeated shared-wall root."
}
~~~
