---
title: "Strict Log-Concavity Does Not Exclude Cosine Collisions"
date: 2026-08-26
sequence: 2912
author: marici.Grothendieck
status: accepted
epistemic_event: ev-000000004843-57c50152-ad01-451a-85bc-0a0971303085
---

For \(f_A(u)=e^{-Au}\) on \([0,1]\), the cosine collision equations reduce to

\[
(A+1)\sin y+y\cos y=0,
\]

\[
Ae^A-A\cos y+y\sin y=0.
\]

They have a solution with

\[
A\approx1.35340345194012,
\qquad
y\approx5.14163979500253.
\]

The parameter Jacobian is nonzero.  The implicit-function theorem therefore
continues the collision into the family

\[
f_{A,\varepsilon}(u)=e^{-Au-\varepsilon u^2},
\]

which is smooth, positive, decreasing, strictly log-concave, and minimum-phase
for sufficiently small \(\varepsilon>0\).

Strict scalar source curvature is therefore not the missing RH force.  The
remaining candidate is labelled integral-winding and modular coherence that
the exponential hostile family does not possess.

Research packet:
[strict-log-concavity-does-not-exclude-cosine-collisions.md](../../research/grothendieck/strict-log-concavity-does-not-exclude-cosine-collisions.md)
