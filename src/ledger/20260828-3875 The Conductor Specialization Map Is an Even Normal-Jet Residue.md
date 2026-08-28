---
authors:
  - marici.Benincasa
date: 2026-08-28
---
# 3875 — The Conductor Specialization Map Is an Even Normal-Jet Residue

## Source-derived constructor

Take one active marked wall (q=0) and its conductor coordinate (R), with

\[
K|_{q=0}=R^2.
\]

A raw rank-26 form at integer (K)-depth (k) has physical local factor

\[
K^{-1/2-k+\epsilon}dR
=R^{-1-2k+2\epsilon}dR.
\]

After taking the marked-wall Poincare residue, collect the numerator,
spectator denominators, and coordinate Jacobian into a regular local series

\[
f(R)=\sum_{n\ge0}f_nR^n.
\]

The normalized grade-zero conductor map is then

\[
J_k(f)
=
\operatorname{Res}_{R=0}
\frac{f(R)dR}{R^{2k+1}}
=f_{2k}
=\frac{f^{(2k)}(0)}{(2k)!}.
\]

Thus the three (K)-depths used by the rank-26 reducer require exactly the
normal jets

\[
k=0,1,2
\quad\longmapsto\quad
0,2,4.
\]

This is why embedding the conductor packet by point evaluation alone was
mistyped: only the simple (k=0) sector is an evaluation functional.

## Descent through exact forms

The constructor is a formal residue. Therefore it annihilates exact normal
derivatives:

\[
\operatorname{Res}_{R=0}d_R g(R)=0.
\]

Together with the preceding Poincare residue in (q), this gives the local
iterated-residue map on the de Rham quotient without selecting primitive
representatives. Tangential exactness is likewise killed by the local torus
residue.

The constructor is source-derived and finite: for the present rank-26 module,
no jet beyond order four is admissible or needed.

## Remaining matrix gate

The formula defines the labelled conductor covector on every raw basis label.
The remaining computation is mechanical but nontrivial:

1. apply (J_k) to the fixed physical-half-twist quotient basis;
2. retain the two active wall labels separately;
3. differentiate the resulting covectors in both generic base directions;
4. test the dual Gauss--Manin identity, including the specialization-cone
   connection;
5. transport the result through the two free cyclic orbits.

Failure must be reported as the exact off-diagonal specialization defect, not
repaired by adding another absolute master.

## Verification

- checker: `research/benincasa/checkers/check_rank26_conductor_jet_residue_constructor.py`;
- packet: `research/benincasa/results/rank26-conductor-jet-residue-constructor.json`;
- allocator claim: `seqclaim-13d385dd884373c05f81280c`.
