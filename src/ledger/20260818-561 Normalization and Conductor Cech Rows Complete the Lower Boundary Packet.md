---
id: 561
date: 2026-08-18
title: Normalization and Conductor Cech Rows Complete the Lower Boundary Packet
authors:
  - marici.Benincasa
---

# Normalization and Conductor Cech Rows Complete the Lower Boundary Packet

Entry 560 proves that divisor valuations and finite pair residues detect
exactly the rank-three deck-even quotient of the resolved boundary packet. Its
common kernel is

\[
B^-=
\langle D_+-D_-,\gamma\rangle.
\]

This entry derives the two missing functionals from the resolved double-cover
Čech complex rather than choosing arbitrary complementary rows.

## Normalization transition

The normalization separates the two sheets \(D_+\) and \(D_-\). Its Čech
boundary is the difference of their restrictions. In the ordered basis

\[
(D_+,D_-,E_+,E_-,\gamma)
\]

the resulting row is, up to the source orientation unit,

\[
\boxed{r_{\rm norm}=(1,-1,0,0,0).}
\]

It evaluates the sheet-difference line and raises the known comparison rank
from three to four.

## Conductor trace

The resolved dual graph is the oriented cycle \(K_{2,2}\). The augmentation
of its one-dimensional cycle space is the conductor trace. In the same basis,

\[
\boxed{r_{\rm cond}=(0,0,0,0,1).}
\]

It evaluates \(\gamma\) and raises the rank from four to five.

Therefore

\[
\boxed{
\operatorname{rank}
\begin{pmatrix}
V\\R_{\rm pair}\\r_{\rm norm}\\r_{\rm cond}
\end{pmatrix}
=5.
}
\]

No arbitrary splitting is used: Entry 560 identifies the precise kernel, and
normalization difference plus conductor trace are the two native Čech
operations on its two canonical summands.

## Scope

This completes detection of all five **boundary coordinates**. It does not yet
construct a chain map from Entry 558's contiguity residue cone to those
coordinates. Nor does it make the raw packet a physical rank-five deck sector:
Entry 559's character obstruction remains, and the physical anti-invariant
boundary part is generated only by the two newly detected coordinates.

The next finite gate is to apply \(r_{\rm norm}\) and \(r_{\rm cond}\) to
source-defined residue representatives and verify that the resulting five-row
map intertwines Gauss--Manin transport. Failure of either Čech functional to
lift to source cohomology would leave the raw boundary packet larger than the
realized coefficient image.

The executable audit is
`research/benincasa/marici-gm/src/bin/generic_lower_boundary_cech_completion.rs`.
