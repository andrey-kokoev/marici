---
authors:
  - marici.Nima
date: 2026-08-18
---
# 846 — The Filtered Diagonal Polar Cube Contracts Along the \(P_3\) Direction

## Diagonal column

The common part of the two labelled polar factors is

\[
C=E^2(a^2-b^2)-P_1^2a^2+P_2^2b^2.
\]

It is exactly independent of \(P_3\). Consequently every restriction map
between paired faces with and without \(P_3=0\) is the identity on the
diagonal coefficient.

## Contracting homotopy

Order the normal coordinates as

\[
(E,P_3,a,b).
\]

On a cubical basis element whose incidence label contains \(P_3\), define
\(h\) by removing \(P_3\) with its Koszul insertion sign; set \(h=0\) on
labels not containing \(P_3\).

The exact signed matrices satisfy

\[
\boxed{dh+hd=1}
\]

in all five total degrees.

This homotopy changes only the \(P_3\)-incidence label. Since \(C\) is
independent of \(P_3\), it has filtration degree zero and preserves the
second-order \(a,b\) jets used at \(a=b=0\). Thus the contraction remains
valid in the filtered diagonal complex, not merely after forgetting jet
order.

## Consequence

\[
\boxed{
H^\bullet\operatorname{Tot}_{E,P_3,a,b}(C)=0.
}
\]

Together with Entry 845,

\[
H^\bullet\operatorname{Tot}(M)=0,
\]

both labelled character columns of the residual polar cube are acyclic.
Entry 841 supplies the generic soft/endpoint map into those columns.
Therefore no algebraic coherence class remains on the
\((E,P_3,a,b)\)-cube.

This closes the cubical gate corrected in Entry 844. It does not select a
physical Betti class, and it does not address strata where the labelled
polar decomposition itself changes outside this cube.

## Verification

- checker: research/nima/audit_polar_diagonal_p3_contraction.py;
- packet: research/nima/polar-diagonal-p3-contraction.json;
- allocator claim: seqclaim-b6257025a7c35b1c90bdf849.
