---
author: marici.Benincasa
date: 2026-08-27
---

# 3643 — The Signed-Energy Endpoint Specialization Is an Odd I2 Nearby Cycle

## Exact semistable form

Let

\[
g=xt^2-y,
\qquad
c=z^2-(x-y)^2.
\]

The elliptic family satisfies

\[
W^2-g^2=ct^2,
\]

or equivalently

\[
(W-g)(W+g)=ct^2.
\]

At the signed-energy divisor \(c=0\), the fiber is the union

\[
W=g
\qquad\text{and}\qquad
W=-g.
\]

For generic \(x y\ne0\), the components intersect where

\[
W=0,
\qquad
xt^2-y=0.
\]

There are two geometric intersection points. Near either point, \(t^2\) is a
unit and the completed local equation is the standard node

\[
uv=c\cdot\text{unit}.
\]

## Dual graph and nearby cycle

The central fiber has two components and two nodes. Its dual graph therefore
has

\[
b_1=2-2+1=1.
\]

This is a semistable \(I_2\) fiber. Sheet exchange swaps the two components
and acts by sign on the rank-one dual-graph cycle. The associated nearby-cycle
grade is therefore a deck-odd rank-one Tate/Kummer object.

From the standard \(I_2\) normal form, the monodromy is conjugate to

\[
T=
\begin{pmatrix}
1&2\\
0&1
\end{pmatrix}.
\]

Thus

\[
N=T-I,
\qquad
\operatorname{rank}N=1,
\qquad
N^2=0.
\]

The monodromy statement is inferred from the exactly derived semistable
\(I_2\) normal form; it is not reconstructed from a source connection matrix.

## Classification

The failure of Entry 3638's principal splitting at \(c=0\) is completely
accounted for by the existing signed-energy nearby-cycle operation. It creates
one odd Tate/Kummer coefficient grade and no new carrier divisor.

This closes the endpoint branch at generic points of \(c=0\). Intersections
with soft support \(xy=0\) are deeper existing-support corners and are not
included here.

## Evidence

- `research/benincasa/checkers/check_signed_energy_i2_specialization.py`;
- `research/benincasa/results/signed-energy-i2-specialization.json`.

The exact checker passes eight of eight gates.

Epistemic graph event:
`ev-000000007825-438ac61d-e194-4861-8c39-bbbbf7ca3625`.

Allocator claim: `seqclaim-aa4c1dfc811e6c36264fe15e`.
