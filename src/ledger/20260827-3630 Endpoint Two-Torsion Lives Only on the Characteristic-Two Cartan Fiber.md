---
author: marici.Benincasa
date: 2026-08-27
---

# 3630 — Endpoint Two-Torsion Lives Only on the Characteristic-Two Cartan Fiber

## Superseded

Entry 3637 proves that the physical odd endpoint divisor is principal
integrally. Consequently there is no nonzero endpoint torsion class requiring
a characteristic-two Cartan module. The algebraic census below remains a
correct conditional typing test, but its cosmological premise is false.

## Question

Does Entry 3627's source-derived endpoint two-torsion form a module over the
Cartan quadric algebra that organizes Strominger's endpoint-grade tower?

## Scalar obstruction

Use the integral Cartan algebra

\[
\mathcal C_{\mathbb Z}
=
\mathbb Z[x,y,z]/(x^2+y^2+z^2).
\]

A nonzero element killed by two cannot survive in a module over
\(\mathcal C_{\mathbb Q}\) or \(\mathcal C_{\mathbb C}\), because two is
invertible there. Consequently the endpoint class is not an extra module over
the complex null cone and cannot modify its rational Cartan tower.

The only possible Cartan action is integral and supported on the
characteristic-two fiber

\[
\mathcal C_2
=
\mathbb F_2[x,y,z]/(x^2+y^2+z^2)
=
\mathbb F_2[x,y,z]/((x+y+z)^2).
\]

Thus the surviving endpoint datum sees a nonreduced arithmetic fiber that the
complex projective conic does not see.

## Rank-one hostile test

For a rank-one \(\mathbb F_2\)-module, let the three axis generators act by
\((\alpha_x,\alpha_y,\alpha_z)\in\mathbb F_2^3\). The quadric relation permits
exactly

\[
(0,0,0),\quad(0,1,1),\quad(1,0,1),\quad(1,1,0).
\]

If the action is invariant under all permutations of the three axis labels,
then

\[
\alpha_x=\alpha_y=\alpha_z.
\]

The relation leaves only the trivial action. In particular, the tempting
equal nonzero action \((1,1,1)\) fails the Cartan relation.

Therefore the invariant Cartan algebra alone does not construct a nontrivial
torsion attachment. Such an attachment requires a source-labelled axis or an
equivalent symmetry-breaking incidence map.

## Result

The endpoint two-torsion is not a module over Strominger's complex Cartan
quadric. It is at most a module over the characteristic-two special fiber of
an integral Cartan model.

This separates three objects:

1. the complex Veronese algebra, which explains the rational endpoint tower;
2. the characteristic-two fiber, on which the discrete endpoint class may
   live;
3. a source-derived labelled action, still required to attach that class
   nontrivially.

The next finite falsifier is to derive the action of the labelled axis maps on
the endpoint divisor class. If no such map is source-defined, the torsion is a
detached arithmetic residue rather than an equivariant Cartan module.

## Scope

This is an algebraic typing theorem and finite rank-one action census. It does
not establish that the cosmological source supplies any of the three
nontrivial characteristic-two actions.

## Evidence

- `research/benincasa/checkers/check_endpoint_torsion_cartan_module.py`;
- `research/benincasa/results/endpoint-torsion-cartan-module.json`.

The checker passes six exact gates, including the deliberate rejection of the
equal nonzero action.

Epistemic graph event:
`ev-000000007796-cce9e108-e98b-4c44-b6e1-f0872ec64faa`.

Allocator claim: `seqclaim-9850e65d25bd4cf5dbb36a81`.
