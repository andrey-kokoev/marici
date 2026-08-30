---
title: "The Five-Site Focus Labels Are Corrected Without Changing the Landau Closure"
date: 2026-08-20
entry: 1271
status: active-provenance-correction
author: marici.Benincasa
---

# 1271 — The Five-Site Focus Labels Are Corrected Without Changing the Landau Closure

Sequence claim: `seqclaim-d26689966f16135837e939bb`.

## Defect

Entry 1217 fixes the labelled routing

\[
r_1=0,
\quad r_2=q_1,
\quad r_3=q_2,
\quad r_4=q_3,
\quad r_5=q_4.
\]

The first asymmetric Landau checkers instead used the cyclically shifted list

\[
(q_1,q_2,q_3,q_4,0).
\]

That shift was invisible on the superseded cyclic slice but is not an
admissible relabelling of Entry 1257's asymmetric kinematics. The original
evidence packets for Entries 1261, 1262, and 1266 therefore had incorrect
focus-label provenance.

## Repair

All three engines now use

\[
\operatorname{focus}(e)=
\begin{cases}
0,&e=1,\\
P_1+\cdots+P_{e-1},&e=2,\ldots,5,
\end{cases}
\]

in one-based source labels. Every squared distance is regenerated from this
ordered list.

## Exact verification

The complete corrected rerun gives

\[
105/105
\]

shared-cut proper pairs with unit direct resultant,

\[
35/35
\]

disjoint-cut proper pairs with a unit staged resultant, and

\[
30/30
\]

disjoint one-cut/proper pairs with unit direct resultant.

Thus the numerical closures in Entries 1261, 1262, 1266, and the inherited
higher-wall conclusion in Entry 1267 remain unchanged.

## Epistemic status

\[
\boxed{
\text{the routing provenance is corrected;}
\quad
\text{the complete Landau closure survives independently.}
}
\]

This entry supersedes the focus-coordinate fields in the earlier JSON packets;
the regenerated packets are authoritative.
