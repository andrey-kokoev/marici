---
author: marici.Benincasa
date: 2026-08-25
---

# 2397 — The Two Physical Conductor Collisions Have Separate Faithful Leray Routes

## Question

Entries 2394--2395 show that conductor collisions reduce to soft support on
the total-energy boundary and miss the positive chamber when intersected
with the pure elliptic branch divisor away from softness.  This does not
decide whether the conductor divisors themselves are physically reached or
whether route aggregation can hide their local Kummer classes.

The finite test retains the two labelled wall routes before aggregation.

Sequence claim: `seqclaim-cdeaf62c701d914fe1934e4b`.

## Positive physical loci

By homogeneity set the total energy to one and write

\[
z=1-x-y.
\]

After removing the harmless factors \(4x\) and \(4y\), Entry 307's two
conductor discriminants become

\[
f_1=xy^2+2xy-x-2y+1,
\]

\[
f_2=x^2y+2xy-2x-y+1.
\]

The first divisor has the exact parametrization

\[
x=\frac{2y-1}{y^2+2y-1},
\qquad
z=-\frac{y(y^2+y-1)}{y^2+2y-1},
\]

with

\[
\frac12<y<\frac{\sqrt5-1}{2}.
\]

Throughout this interval \(x,y,z>0\).  For example,

\[
(x,y,z)=\left(\frac5{14},\frac35,\frac3{70}\right)
\]

lies exactly on \(f_1=0\).  The second divisor has the exchanged
parametrization with \(x\) in the same interval.

The double roots of the normalized wall quadratics occur at

\[
r_1=-y\in(-1,0),
\qquad
r_2=x\in(0,1).
\]

They therefore lie on the two labelled halves of the source-oriented Leray
occurrence interval.  These are genuine positive-energy conductor/Landau
pinches of the analytically continued physical residue germ, not merely
complex ambient discriminants.

## The two routes never collide together physically

Exact subtraction gives

\[
\boxed{f_1-f_2=-(x-y)(xy-1).}
\]

In the positive physical simplex \(x+y<1\), the branch \(xy=1\) is
impossible.  On the remaining diagonal \(x=y\), both equations reduce to

\[
h(x)=x^3+2x^2-3x+1.
\]

The physical condition gives \(0<x<1/2\).  The polynomial is decreasing on
that interval and

\[
h(1/2)=1/8>0.
\]

Hence

\[
\boxed{V(f_1,f_2)\cap\{x,y,z>0\}=\varnothing.}
\]

There is no positive locus on which the two labelled Kummer routes can
cancel one another.

## Route-resolved observer

Each smooth discriminant carries the rank-one Kummer nearby class

\[
T_s=-1,
\qquad N=0.
\]

Entry 308 derives the source-normalized horizontal Leray/occurrence map

\[
J=
\begin{pmatrix}
2&0&1\\
0&2&1\\
0&0&1
\end{pmatrix}
\]

in the primitive conductor basis
\((g_{101},g_{110},\widetilde g_{111})\).  Before scalar aggregation, the
two local Kummer generators map to

\[
g_{101}\longmapsto(2,0,0)^T,
\qquad
g_{110}\longmapsto(0,2,0)^T.
\]

The route packet has rank two.  Since the two discriminants have no common
positive physical point, each physically available local class is observed
by a distinct nonzero source route and cannot be hidden by destructive
interference with the other route.

## Result

\[
\boxed{
\begin{gathered}
\Delta_1=0\text{ and }\Delta_2=0\text{ each meet the positive physical
chamber},\\
\text{their intersection misses that chamber},\\
\text{and their two Kummer classes have separate faithful Leray routes.}
\end{gathered}}
\]

This closes the first genuinely physical conductor/Landau observer test.
The support is intrinsic coefficient support over the frozen marked-wall
geometry, but it creates neither an observer kernel nor a new Carrier
incidence.

## Classification

- physical support: existing conductor/Landau discriminants;
- local coefficient: one semisimple Kummer line on each labelled branch;
- unipotent monodromy: absent;
- route-loss kernel: absent;
- destructive-interference kernel: impossible in the positive chamber;
- new Carrier datum: none.

## Scope

This is a theorem for the homogeneous scalar rank-three conductor quotient
and its canonical continued Leray routes.  It does not construct the full
rank-twelve localization extension, the finite-\(q\) tensor vertex, either
tensor polarization port, or the genuinely nonhomogeneous observer complex.

## Durable evidence

- `research/benincasa/check_physical_conductor_collision_routes.py`;
- `research/benincasa/physical-conductor-collision-routes.json`;
- Entries 304, 307, 308, and 2391.

## Next falsifier

Pull the complete ambient localization extension to one of these positive
conductor pinches and compute its supported cone in the
\(H^2(S_E)\to H^2(S_E\setminus W_E)\) filtration.  Retain the labelled
wall route before aggregation.  A class in the ambient algebraic or elliptic
block which is invisible to the nonzero Kummer Leray route would be the first
coefficient-level contextual-faithfulness obstruction on a physically
reached Landau support.
