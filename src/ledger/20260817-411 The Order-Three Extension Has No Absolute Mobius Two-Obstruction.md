---
id: 411
date: 2026-08-17
title: The Order-Three Extension Has No Absolute Mobius Two-Obstruction
---

# The Order-Three Extension Has No Absolute Möbius Two-Obstruction

Entry 410 produced a local extension class in \(\mathbb Z/3\). Its global
Čech obstruction must be computed with the selected orientation local
system, not with constant coefficients.

The exact twelve-face carrier of Entries 88 and 408 collapses through
unimodular face and tree pivots to the universal rank-one complex
\[
R\xrightarrow{u-1}R.
\]
For the orientation character \(u=-1\) over \(\mathbb F_3\),
\[
u-1=-2=1\pmod3,
\]
which is a unit. Thus the twisted Möbius complex is acyclic:
\[
\boxed{H^i(M;\mathbb F_{3,\rm or})=0\quad\text{for all }i.}
\]
In particular,
\[
\boxed{\check H^2(M;\mathbb F_{3,\rm or})=0.}
\]
Every transported local order-three extension therefore admits a global
filtered descent on the open Möbius carrier. There is no absolute Čech
two-obstruction and hence no higher associator supported solely on its
twelve local faces.

The cap changes the answer. The residual octagonal cell adds the universal
top differential \(u+1\). At \(u=-1\),
\[
u+1=0,
\]
so the capped complex has
\[
\boxed{H^2(X;\mathbb F_{3,\rm or})\cong\mathbb F_3.}
\]
Equivalently, the relative top group for the cap is one-dimensional. Thus
the local extension class can survive only as a capped/relative top class,
not as an obstruction to gluing the filtered atlas over \(M\).

## Consequence

The filtered atlas exists on the twelve-chart Möbius carrier. The remaining
question is a single scalar in \(\mathbb F_3\): evaluate the transported
order-three extension on the oriented Jordan cap. Values \(0\), \(+1\), and
\(-1\) are the complete candidate space. A zero value extends the filtered
atlas across the cap; a unit is the genuine order-three Jordan associator.

The executable audit is
\`research/voevodsky/check_global_mod3_filtered_atlas.py\`.
