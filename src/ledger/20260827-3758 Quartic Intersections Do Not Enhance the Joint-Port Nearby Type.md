---
author: marici.Benincasa
date: 2026-08-27
---

# 3758 — Quartic Intersections Do Not Enhance the Joint-Port Nearby Type

## Question

Entry 3754 proves that the horizontal infinity joint port is regular across
generic \(\mathcal Q=0\). The remaining authorized test is its restriction to
proper intersections with the five existing transport divisors.

## Exact intersection census

In the \((u,v)\) chart, restriction of \(\mathcal Q\) gives

\[
\begin{aligned}
\mathcal Q|_{u=0}&=-4(v-2)^2,\\
\mathcal Q|_{u=2}&=-4(v-2)^2,\\
\mathcal Q|_{v=0}&=-(u^2+2u-4)^2,\\
\mathcal Q|_{v=2}&=-u^2(u-2)^2,\\
\mathcal Q|_{u+v-2=0}&=-u^3(5u-8).
\end{aligned}
\]

Thus the proper intersections are:

- the already resolved deeper corners \((0,2)\) and \((2,2)\);
- two quadratic points \(u=-1\pm\sqrt5\) on \(v=0\);
- one rational point \((u,v)=(8/5,2/5)\) on the signed-energy wall.

## Nearby type

At either quadratic point, the residue along \(v=0\) remains rank-one
nilpotent. At the rational signed-energy point, the residue is

\[
\begin{pmatrix}
0&-25/16\\
0&0
\end{pmatrix},
\]

again rank-one nilpotent. In both cases the square is zero and no residue-rank
jump occurs.

The quartic therefore selects distinguished points on existing support but
does not enhance the local nearby-cycle type of the infinity joint port.

## Classification

For this coefficient object, every proper quartic intersection is either:

- an already existing deeper soft/energy corner; or
- an ordinary point of an existing rank-one nodal nearby system.

No new carrier stratum and no new joint-port coefficient grade appears.
Whether the physical horizontal section has zero or nonzero value at one of
the generic points is a period-evaluation question, not a new support class.

## Consequence

The infinity joint-port branch is closed as a home for \(\mathcal Q\), both
generically and at its proper intersections. Reopening it would require new
source data that changes the coefficient object or physical relative cycle.

## Evidence

- `research/benincasa/checkers/check_infinity_joint_port_quartic_intersections.py`;
- `research/benincasa/results/infinity-joint-port-quartic-intersections.json`;
- Entries 863, 3754, and the existing soft-corner nearby calculations.

Allocator claim: `seqclaim-ad0ed4283113f324c86230db`.
