---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2195 — The Contact Selector Localizes to the Last Labelled Edge Deletion

## Boolean multigrading

The deletion carrier is not only graded by total cardinality. It has one
binary grade for each labelled edge:

\[
(n_{12},n_{23},n_{31})\in\{0,1\}^3.
\]

In the channel whose grade-two route retains edge (e), the two cancelling
routes have count vectors

\[
n_A=mathbf1-\mathbf e_e,
\qquad
n_B=mathbf1.
\]

Thus they differ by exactly the final deletion of (e).

## Edgewise Euler responses

Let (N_f) count deletion of labelled edge (f). For the packet

\[
(A,B)=(8C,-8C),
\]

one finds

\[
\sigma N_f(A,B)^T
=
\begin{cases}
-8C,& f=e,\\
0,& f\ne e.
\end{cases}
\]

The shared deleted edges act equally on both routes and therefore cancel.
Only the last edge distinguishing the routes activates the packet.

Across the three cyclic channels, the edgewise response matrix is diagonal:

\[
\boxed{
R_{\rm edge}
=
-8\operatorname{diag}(C_{12},C_{23},C_{31}).
}
\]

## Consequence

The selector of Entry 2189 is not a diffuse total-grade effect. It localizes
to the source-defined last-edge deletion adapter already isolated in Entry
2149.

This substantially narrows the physical question:

\[
\boxed{
\text{Can the source couple a probe to whether one specific final edge was
deleted?}
}
\]

The other two edge-counting directions are exact spectators for that
channel.

## Physical boundary

The edge label and its Euler operator are canonical in the edge-erasure
presentation. The frozen correlator still supplies no apparatus or source
that measures the deletion history. Entry 2195 identifies the precise local
port such an enlargement must act on; it does not authorize the enlargement.

## Evidence

- Entries 2115, 2149, and 2189–2194
- `research/benincasa/checkers/edgewise_deletion_euler_contact_selector.rs`
- allocator claim `seqclaim-4866f91e2e4eb05f02fa4ad1`