---
id: marici-ledger-20260827-3785
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP878
sequence_claim: seqclaim-ad3fceccb3853ea3b474f79b
---

# 3785 — The Ordered Singlet Plane Carries a Primitive Hodge-Odd Portal

Strominger's real source-Hodge construction transfers to the ordered singlet
plane of WP877. The normalized source directions define

\[
J=e_ve_u^T-e_ue_v^T,
\qquad
J^2=-(P_u+P_v).
\]

Among real symmetric operations diagonal in the two source projectors,
oddness under \(J\) forces opposite coefficients. Primitive unit
normalization and the ordered-stage sign then uniquely select

\[
H=P_v-P_u,
\qquad
H^2=P_u+P_v,
\qquad
JH=-HJ.
\]

The simple-parent branch therefore fixes a dimensionless portal sign and unit
contrast rather than merely permitting two different singlet coefficients.

Grothendieck's moving-incidence theorem requires \((P_u,P_v,J,H)\) to
co-move with its source connection. Sontag's disturbance-excitation theorem
requires two independently excited detector directions; two record labels
alone do not establish rank two. Aspect's path audit prevents algebraic
existence of \(J\) from being promoted to executable rotations of the
prepared source frame.

## Scope

The physical portal remains \(G=gH\). The source-Hodge packet fixes \(H\),
not the common coefficient \(g\). The complete simple-parent fixed point,
global basin, finite mass-and-width threshold map, and calibrated rank-two
`physical16` response remain open.

## Durable verification

- Packet: research/flavor/flavor-ordered-singlet-plane-hodge-portal-normalizer.md
- Checker: research/flavor/checkers/wp878_ordered_singlet_plane_hodge_portal_normalizer.py
- Result: research/flavor/results/wp878_ordered_singlet_plane_hodge_portal_normalizer.json
- Exact result: 14 of 14 checks passed.
- Cross-sector replays: Strominger 11/11, Sontag 8/8, Aspect pass.
- Sequence claim: seqclaim-ad3fceccb3853ea3b474f79b, value 3785.
- Graph admission: ev-000000008176-a2af25d3-5f79-46ac-b497-a1323db5dadf.
