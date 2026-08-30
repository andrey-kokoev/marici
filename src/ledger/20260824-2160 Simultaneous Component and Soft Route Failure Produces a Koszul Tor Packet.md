---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2160 — Simultaneous Component and Soft Route Failure Produces a Koszul Tor Packet

## Source-normalized local complex

For one labelled complementary component, Entry 2159 gives the moving
relation \((2q/y,1)\), where \(q\) is its connected component-energy
denominator and \(y\) is its retained-edge soft coordinate. Clearing the
denominator without discarding either route gives

\[
\boxed{
0\to R
\xrightarrow{(2q,y)^T}
R^2
\xrightarrow{(y,-2q)}
R\to0.
}
\]

The composition is identically zero:

\[
(y,-2q)(2q,y)^T=2qy-2qy=0.
\]

This is the Koszul complex of the regular pair \((2q,y)\).

## Fault-tolerance census

Exact fiber ranks give:

\[
\begin{array}{c|c}
\text{locus}&(h^{-1},h^0,h^1)\\
\hline
q\ne0,\ y\ne0&(0,0,0)\\
q=0,\ y\ne0&(0,0,0)\\
q\ne0,\ y=0&(0,0,0)\\
q=0,\ y=0&(1,2,1).
\end{array}
\]

Therefore failure of either route alone is repaired by the other. At their
intersection both differentials vanish, and the derived fiber retains the
canonical Tor profile

\[
\boxed{1\to2\to1.}
\]

## Comparison with Strominger's mechanism

This is the same fault-tolerance pattern at the level of support:

- primary component transport degenerates at \(q=0\);
- inverse-edge/soft transport degenerates at \(y=0\);
- either route separately keeps the local complex acyclic;
- simultaneous failure creates supported homology.

The cosmological output is not yet a single primitive integer circuit. It is
a three-grade Koszul packet: one relation cell, two invisible route
generators, and one supported costalk. A physical scalar class requires a
source-derived pairing with this packet.

## Classification

- support: existing intersection \(\{q=0\}\cap\{y=0\}\);
- generic kernel relation: presentation redundancy;
- single-divisor exceptional homology: zero;
- double-support derived packet: dimensions \((1,2,1)\);
- new Carrier divisor or incidence cell: none;
- physical activation: untested.

## Cyclic continuation

The triangle has three labelled copies:

\[
(q_{23},y_{23}),\qquad(q_{31},y_{31}),\qquad(q_{12},y_{12}).
\]

The next test is their occurrence-resolved cyclic assembly and intersection
with the Bunch--Davies relative chain. No copies may be identified before
that assembly.

## Evidence

- Entry 2159
- research/benincasa/component-soft-koszul-fault-packet.md
- research/benincasa/checkers/component_soft_koszul_fault.rs
- allocator claim seqclaim-57ab760c8db204ba9547310a
