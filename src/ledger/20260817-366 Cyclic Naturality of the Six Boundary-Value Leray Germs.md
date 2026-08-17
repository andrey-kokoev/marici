---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Cyclic Naturality of the Six Boundary-Value Leray Germs

## Question

Entry 365 showed that the starting positive chain has no literal boundary on
the marked-Cut union. The sector residues instead arise through the
Bunch--Davies boundary-value continuation. The hard-to-vary claim tested
here is

\[
\boxed{
\text{analytic continuation and the six sectorwise Leray residues may fail
to commute with the source }C_3\text{ action}.}
\]

The negative-imaginary tube, positive Cayley--Menger sheet, source volume,
occurrence order, lower denominators, and boundary-value normalization are
frozen.

## Frozen occurrence action

In source order,

\[
(12|23),(12|31),(23|31),(23|12),(31|12),(31|23),
\]

the cyclic relabelling has two orbits:

\[
(12|23)\to(23|31)\to(31|12)\to(12|23),
\]

\[
(12|31)\to(23|12)\to(31|23)\to(12|31).
\]

The all-positive source vector is fixed by this permutation.

## Boundary-value data

Each marked Cut has the form

\[
q_{\mathcal G_{ij}}=E+y_{ij},
\qquad
\frac{\partial q_{\mathcal G_{ij}}}{\partial y_{ij}}=1.
\]

The three sector residue orders are even cyclic permutations of

\[
dy_{12}\wedge dy_{23}\wedge dy_{31}.
\]

Thus every sector has:

\[
\text{Jacobian}=1,
\qquad
\text{orientation}=+1,
\qquad
\text{multiplicity}=1.
\]

The common boundary value supplies

\[
\operatorname{Disc}\frac1{q-i0}=2\pi i\,\delta(q)
\]

with the same factor in all three sectors.

The tube

\[
\operatorname{Im}x_i<0,
\qquad
\operatorname{Im}y_{ij}<0
\]

is convex and invariant under cyclic relabelling. The positive
Cayley--Menger sheet and signed-minor domain are transported by the same
source permutation.

## Naturality square

On the six occurrence-resolved source summands, the labelled first-residue
matrix is

\[
R_{\rm Leray}=I_6.
\]

Let (P_\rho) denote the permutation matrix of the two three-cycles. Exact
matrix multiplication gives

\[
\boxed{
R_{\rm Leray}P_\rho=P_\rho R_{\rm Leray}.}
\]

All pairwise iterated marked-Cut residues vanish because no source summand
contains two marked-Cut poles. Hence no overlap correction is required for
the square.

The tested failure claim is falsified.

## Narrow result

\[
\boxed{
\text{the six source-defined boundary-value Leray germs form a canonical
}C_3\text{-equivariant family}.}
\]

Analytic continuation is therefore the global operation relating the single
degree-zero meromorphic source packet to its three residue sectors. This is
not Čech gluing: there are still no pairwise transition maps or joint Cut
poles.

## Classification

| Datum | Classification |
|---|---|
| convex negative-imaginary tube | source analytic-continuation domain |
| (2\pi i), Jacobian and orientation | boundary-value Leray normalization |
| two three-cycles | occurrence-resolved (C_3) action |
| commuting residue square | shared analytic continuation/residue calculus |
| pairwise iterated residues | zero |
| cross-sector transitions | absent and unnecessary for this square |
| new carrier datum | none |

## Scope

This establishes naturality for the local physical residue germs and their
source occurrence modules. It does not yet prove a conjugacy of the complete
rank-twelve Gauss--Manin connection matrices, integral lattices, or relative
period bases across the three sectors.

## Evidence

- `research/benincasa/marici-gm/src/bin/cyclic_leray_naturality.rs`;
- `research/benincasa/cyclic-leray-naturality-certificate.json`;
- Entries 180, 229, 364, and 365.

## Next falsifier

Lift the occurrence-level naturality square to the complete (9+3)
rank-twelve filtered coefficient systems. Derive the cyclic basis transport
from the source master descriptors—not from fitted connection matrices—and
test

\[
\nabla_{23}=P_\rho\nabla_{12}P_\rho^{-1},
\qquad
\nabla_{31}=P_\rho^2\nabla_{12}P_\rho^{-2}
\]

for the absolute nine-master block, the three marked quotient classes, and
their extension columns. Any mismatch must be classified as basis gauge,
sector-specific coefficient data, support, or a failure of cyclic
naturality. No overlap transition may be inserted to repair it.
