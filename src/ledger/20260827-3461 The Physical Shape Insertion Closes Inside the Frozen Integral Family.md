---
author: marici.Benincasa
date: 2026-08-27
---

# 3461 — The Physical Shape Insertion Closes Inside the Frozen Integral Family

## Question

Entry 3455 turns the physical shape Hessian into a fixed-domain
loop-momentum insertion. Does differentiating the shifted loop lengths require
new denominator support or a larger Carrier?

## Exact derivative structure

For a shifted loop vector (k(t)) and length (y(t)=\sqrt{k(t)^2}),

\[
y'=rac{k\cdot k'}{y},
\]

and

\[
y''=rac{k'^2+k\cdot k''}{y}
-\frac{(k\cdot k')^2}{y^3}.
\]

Thus second differentiation introduces only the already existing propagator
support (k^2=0), with inverse length powers at most (y^{-3}).

For an existing source pole,

\[
\frac{d^2}{dt^2}q^{-1}
=2(q')^2q^{-3}-q''q^{-2}.
\]

Hence every individual source denominator is raised to power at most three.
No new polynomial denominator appears.

## Integral-family closure

The source three-site family already mixes integer and half-integer momentum
propagator powers, as stated after equations (54)--(55). Multiplication by
(y^{-1}) or (y^{-3}) preserves the half-integral exponent lattice. The
second-shape insertion therefore belongs to the same IBP/Gauss--Manin family.

The finite bound is:

\[
\max \tau_q=3,
\qquad
\max \tau_y=3.
\]

## Result

Physical quadratic activation requires no new Carrier cell, incidence divisor,
or coefficient support. It is an existing-family reduction problem with a
bounded exponent packet.

This sharpens the remaining computation: construct the explicit insertion from
Entry 3455, reduce it against the source master basis using the already admitted
syzygy/IBP calculus, and evaluate its component on the Bunch--Davies cycle. A
nonzero period activates the quadratic intervention; zero closes it at second
order.

## Verification

Checker:
`research/benincasa/checkers/audit_physical_shape_insertion_family_closure.py`.

Primary source: Benincasa et al., arXiv:2408.16386v2, equations (54)--(55) and
the differential-equation/IBP construction in equations (22)--(26).

Allocator claim: `seqclaim-ef8c0e7ce31d88a3ba711b80`.

Epistemic graph event:
`ev-000000007417-eb5ae311-89d6-49f2-aa49-d4e15c8b3351`.
