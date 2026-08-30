---
author: marici.Benincasa
date: 2026-08-25
---

# 2374 — The Physical Soft Nodes Share One Projective Picard–Lefschetz Orientation

## Question

Entry 2373 fixes the deck character but leaves the relative signs of the four
physical node lines open. Are those signs source-derived, or must they be
chosen independently at each node?

Sequence claim: seqclaim-8f3a81ff2fd3793f6ddf80a8.

## Exact conifold coordinates

Write

\[
F=t^2-5-4\kappa\xi,qquad
Y_+=w+F,qquad Y_-=w-F,
\]

\[
U=4(1-\kappa^2),qquad V=4(1-\xi^2).
\]

The exceptional hypersurface identity is exactly

\[
\boxed{
w^2-K_{\rm exc}=Y_+Y_-+UV.
}
\]

Thus every endpoint node is the same labelled conifold singularity. The two
boundary normals (U,V), the signed-face fold (F), and the square-root deck
coordinate remain distinct.

## Inward orientation

In the source coordinate order ((w,t,\kappa,\xi)), the coordinate Jacobian is

\[
\det\frac{\partial(Y_+,Y_-,U,V)}
{\partial(w,t,\kappa,\xi)}
=-256\kappa t\xi.
\]

At an endpoint write

\[
\kappa=\epsilon(1-r_\kappa),qquad
\xi=\delta(1-r_\xi),qquad r_\kappa,r_\xi\ge0.
\]

In the inward coordinate order ((w,t,r_\kappa,r_\xi)), the Jacobian becomes

\[
\boxed{-256t.}
\]

All four physically incident nodes have (t>0), so this sign is common.

## Second-normal smoothing

Entry 2372 gives the four smoothing coefficients

\[
9p^2,quad9p^2,quad p^2,quad81p^2.
\]

They are all positive for real nonsoft (p\ne0). In the standard conifold
model the physical second-normal deformation therefore approaches the same
side of the smoothing parameter at every node.

Combining the common inward Jacobian sign with the common smoothing side gives
the projective Picard--Lefschetz ray

\[
\boxed{[1:1:1:1].}
\]

Only one overall orientation remains conventional; there is no independent
four-sign freedom.

## Classification

- local geometry: standard conifold (Y_+Y_-+UV=0);
- boundary data: the existing triangle and loop-endpoint normals (U,V);
- coefficient data: four anti-invariant vanishing lines with common relative
  orientation;
- first activation: second ordinary/Rees normal grade;
- new Carrier datum: none.

## Scope

This is an exact normal-form and projective-orientation theorem. It does not
fix an affine period normalization, prove nonzero intersection with the full
physical relative cycle, compute global relations among the four vanishing
cycles, or identify their image in the observer complex.

## Durable verification

- `research/benincasa/check_soft_triangle_conifold_orientation.py`;
- `research/benincasa/soft-triangle-conifold-orientation.json`;
- exact conifold identity, all four inward Jacobians, and all four
  second-normal coefficients;
- epistemic event
  `ev-000000003252-b2a553ad-2180-4386-931d-e2c7416db0be`.

## Next falsifier

Build the endpoint/Gysin cone using the two labelled boundary normals (U,V)
and the occurrence quotient of Entry 2371. Test whether the common ray maps to
a nonzero primitive anti-trace of the physical relative current or becomes
exact after the endpoint restrictions are sewn.
