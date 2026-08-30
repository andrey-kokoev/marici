---
author: marici.Benincasa
date: 2026-08-25
---

# 2395 — Nonsoft Conductor--Elliptic Collisions Miss the Positive Physical Chamber

## Hard-to-vary claim

The homogeneous elliptic branch divisor and the two conductor discriminants
have nonsoft algebraic intersections, but none lies in the positive physical
energy chamber

\[
x>0,\qquad y>0,\qquad X_3=E-x-y>0.
\]

The physical Bunch--Davies cycle reaches their common support only through
the soft faces closed in Entry 2394.

## Occurrence-resolved elliptic branches

The four signed-energy letters are

\[
\ell_1=2x-E,\quad
\ell_2=E-2y,\quad
\ell_3=2(x+y)-E,\quad
\ell_4=E,
\]

with

\[
A=\ell_1\ell_2,\qquad B=\ell_3\ell_4.
\]

Restricting the conductor discriminants before forgetting occurrences gives

\[
\begin{array}{c|cc}
\text{branch}&\Delta_1&\Delta_2\\
\hline
\ell_1=0&4x^2(2x-y)^2&4x^2y^2\\
\ell_2=0&4x^2y^2&4y^2(x-2y)^2\\
\ell_3=0&4x^2(2x+3y)^2&4y^2(3x+2y)^2\\
\ell_4=0&4x^2y^2&4x^2y^2.
\end{array}
\]

Exact elimination independently gives

\[
\operatorname{Res}_E(\Delta_1,A)
=-16x^4y^2(2x-y)^2,
\]

\[
\operatorname{Res}_E(\Delta_2,A)
=-16x^2y^4(x-2y)^2,
\]

\[
\operatorname{Res}_E(\Delta_1,B)
=-16x^4y^2(2x+3y)^2,
\]

\[
\operatorname{Res}_E(\Delta_2,B)
=-16x^2y^4(3x+2y)^2.
\]

## Physical-incidence falsifier

On \(\ell_1=0\), the nonsoft \(\Delta_1\)-root is \(y=2x\), but then

\[
X_3=2x-x-2x=-x<0.
\]

On \(\ell_2=0\), the nonsoft \(\Delta_2\)-root is \(x=2y\), but then

\[
X_3=2y-2y-y=-y<0.
\]

On \(\ell_3=0\), the nonsoft roots

\[
2x+3y=0,\qquad 3x+2y=0
\]

are incompatible with \(x,y>0\). The \(\ell_4\) occurrence leaves only
\(xy=0\).

The algebraic locus is genuine rather than empty. For example,

\[
(x,y,E)=(1,2,2)
\]

lies on \(\ell_1=\Delta_1=0\), but has \(X_3=-1\).

## Result

\[
\boxed{
\left\{
\text{positive physical conductor--elliptic intersections}
\right\}_{\mathrm{red}}
=
\{x=0\}\cup\{y=0\}.
}
\]

No additional physical observer port is required at a nonsoft
conductor--elliptic point in this homogeneous sector. The only physically
reached intersections are the soft Rees faces already proved faithful.

## Classification

- signed-energy letters: existing energy carrier;
- conductor discriminants: sector-specific Kummer coefficient support;
- nonsoft algebraic intersections: genuine on analytically continued sheets
  but outside the positive physical chamber;
- physical common support: existing soft faces;
- new Carrier datum: none.

## Scope

This is an exact support and physical-incidence theorem. It does not declare
the nonphysical algebraic intersections nonexistent, nor select them as
physical readouts after arbitrary analytic continuation.

## Next falsifier

The homogeneous scalar physical-boundary lane is now closed through the
conductor--elliptic intersections reached by the source cycle. The next
source-typed scalar test is a genuine Landau/Gram intersection with nonzero
physical incidence. The full objective still separately requires an upstream
covariant action before finite-\(q\) tensor and polarization ports can be
derived.

## Durable verification

- checker: research/benincasa/check_conductor_elliptic_physical_incidence.py;
- packet: research/benincasa/conductor-elliptic-physical-incidence.json;
- sequence claim: seqclaim-6c6a59cf36e17b89927482d5;
- epistemic graph:
  ev-000000003282-f9240f84-e885-4cdb-a5f4-e4e114f1d65a.
