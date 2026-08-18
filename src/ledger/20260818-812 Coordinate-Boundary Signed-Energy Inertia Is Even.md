---
authors:
  - marici.Nima
date: 2026-08-18
---
# 812 — Coordinate-Boundary Signed-Energy Inertia Is Even

## Purpose

Entry 811 closes the universal interior higher-specialization packet.  The
next possible excess lies on Entry 807's coordinate boundaries.  Before
computing their local Milnor or Kato ranks, the exact critical values already
determine their coefficient inertia.

## Exact boundary discriminants

On (A=a^2=0), after eliminating the remaining critical coordinate,

\[
\Delta_A
=-
\frac{(E-P_2)^2(E+P_2)^2\Lambda}{4P_2^2}.
\]

On (B=b^2=0),

\[
\Delta_B
=-
\frac{(E-P_1)^2(E+P_1)^2\Lambda}{4P_1^2}.
\]

Away from the displayed unit denominators, every signed-energy factor has
valuation two and the triangle factor has valuation one.  Therefore the
anti-invariant Kummer line has

\[
\boxed{
M_{E\pm P_i}=+1,
\qquad
M_\Lambda=-1.
}
\]

At a signed-energy/triangle intersection the commuting character pair is
((+1,-1)).  Each signed-energy normal retains a length-two Cartier/Rees
layer, exactly as the total-energy normal did in Entries 809–810.

## Consequence

The coordinate-boundary branches can still create a new reduced class
through their local singularity, support map, or an intersection extension.
They cannot create a new Kummer character merely from signed-energy
ramification: that ramification is even.  Thus any rank excess found by the
local calculation must be geometrically sourced, rather than inferred from
the discriminant alone.

Cyclic transport permutes the source-labelled coordinate boundaries and
preserves this parity packet.  The result therefore supplies a rigid
coefficient constraint for the local calculations without pre-assigning
their ranks.

## Scope

This is a coefficient-inertia and Cartier-length statement only.  It does
not infer local Milnor/Kato ranks, surjectivity of specialization, or excess
Tor at the boundary intersections.

## Verification

- checker: `research/nima/audit_coordinate_boundary_kummer_inertia.py`;
- packet: `research/nima/coordinate-boundary-kummer-inertia.json`;
- allocator claim: `seqclaim-fd68d3f4141a6822ee53e2a4`.
